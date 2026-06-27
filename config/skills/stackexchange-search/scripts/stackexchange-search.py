#!/usr/bin/env python3
"""Stack Exchange search skill script (Python stdlib only)."""

from __future__ import annotations

import html
import json
import os
import re
import sys
from typing import Any, Dict, NoReturn
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

EXCERPT_MAX_LENGTH = 300
REQUEST_TIMEOUT_SECONDS = 5
DEFAULT_SITE = "stackoverflow"
API_BASE = "https://api.stackexchange.com/2.3"


def print_usage() -> None:
    print(
        "Usage:\n"
        "  python stackexchange-search.py "
        '\'{"query":"python asyncio","count":5}\'\n'
        "  python stackexchange-search.py "
        '\'{"query":"rust borrow checker","count":5,"site":"stackoverflow"}\'\n\n'
        "Environment:\n"
        "  STACKEXCHANGE_API_KEY    Optional, raises quota to 10,000/day\n"
    )


def die(message: str, *, body: Any = None) -> NoReturn:
    payload: Dict[str, Any] = {"error": message, "exit_code": 1}
    if body is not None:
        payload["body"] = str(body)
    print(json.dumps(payload, ensure_ascii=False))
    raise SystemExit(1)


def parse_payload(raw: str) -> Dict[str, Any]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        die(f"Invalid JSON payload: {exc}")
    if not isinstance(data, dict):
        die("Payload must be a JSON object")
    return data


def parse_query(payload: Dict[str, Any]) -> str:
    query = payload.get("query") or payload.get("Query") or ""
    stripped = query.strip()
    if not stripped:
        die("query is required")
    return stripped


def parse_count(payload: Dict[str, Any]) -> int:
    raw = payload.get("count") or payload.get("Count") or 10
    try:
        count = int(raw)
    except (TypeError, ValueError):
        return 10
    return max(1, min(20, count))


def parse_site(payload: Dict[str, Any]) -> str:
    site = payload.get("site") or payload.get("Site") or DEFAULT_SITE
    return str(site).strip()


def _strip_html(text: str) -> str:
    """移除 HTML 标签，生成纯文本摘要。"""
    text = re.sub(r"<pre><code>.*?</code></pre>", "", text, flags=re.DOTALL)
    text = re.sub(r"<code>(.*?)</code>", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _truncate(text: str) -> str:
    if len(text) <= EXCERPT_MAX_LENGTH:
        return text
    return text[:EXCERPT_MAX_LENGTH] + "…"

def build_result(api_resp: Dict[str, Any]) -> Dict[str, Any]:
    items_raw = api_resp.get("items") or []
    items: list[Dict[str, Any]] = []
    for item in items_raw:
        body_raw = item.get("body") or item.get("body_markdown") or ""
        excerpt = _truncate(_strip_html(body_raw)) if body_raw else ""

        items.append({
            "title": html.unescape(item.get("title", "")),
            "url": item.get("link", ""),
            "score": item.get("score", 0),
            "answer_count": item.get("answer_count", 0),
            "is_answered": item.get("is_answered", False),
            "has_accepted_answer": item.get("accepted_answer_id") is not None,
            "tags": item.get("tags", []),
            "excerpt": excerpt,
        })

    return {
        "item_count": len(items),
        "items": items,
        "quota_remaining": api_resp.get("quota_remaining"),
        "quota_max": api_resp.get("quota_max"),
        "backoff": api_resp.get("backoff"),
    }


def request_stackexchange(query: str, count: int, site: str) -> Dict[str, Any]:
    api_key = os.getenv("STACKEXCHANGE_API_KEY", "").strip()
    params: Dict[str, str] = {
        "q": query,
        "site": site,
        "pagesize": str(count),
        "order": "desc",
        "sort": "relevance",
        "filter": "withbody",  # 返回 body（HTML 格式）
    }
    if api_key:
        params["key"] = api_key

    url = f"{API_BASE}/search/advanced?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "stackexchange-search-skill/1.0"})

    try:
        with urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as resp:
            raw = resp.read().decode("utf-8")
            body = json.loads(raw)
    except HTTPError as exc:
        try:
            err_body = exc.read().decode("utf-8")
        except Exception:
            die(f"HTTP {exc.code}: {exc.reason}")
        try:
            err_json = json.loads(err_body)
            msg = err_json.get("error_message", err_body)
        except json.JSONDecodeError:
            msg = err_body[:200]
        die(f"HTTP {exc.code}: {msg}", body=msg)
    except URLError as exc:
        die(f"HTTP request failed (network error): {exc.reason}")
    except json.JSONDecodeError:
        die("Non-JSON response from API")

    if "error_id" in body:
        msg = body.get("error_message", body.get("error_name", str(body.get("error_id"))))
        die(f"API error: {msg}")

    return build_result(body)


def main() -> None:
    if len(sys.argv) >= 2 and sys.argv[1] in {"-h", "--help"}:
        print_usage()
        raise SystemExit(0)

    if len(sys.argv) < 2:
        print_usage()
        die("Missing JSON payload argument")

    payload = parse_payload(sys.argv[1])
    query = parse_query(payload)
    count = parse_count(payload)
    site = parse_site(payload)

    result = request_stackexchange(query, count, site)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
