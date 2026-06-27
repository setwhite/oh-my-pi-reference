---
name: zhihu-search
version: 1.0.3
description: 搜索知乎站内内容，返回结构化结果（标题、链接、作者、摘要等）。当用户要求"搜索知乎"、"知乎上有没有"、"查一下知乎"、"搜一下知乎"、或在知乎平台检索特定话题/观点/讨论时使用。不应触发：通用 web 搜索（用内置 web_search 工具）、仅提及「知乎」但无检索意图、搜索其他平台内容。
homepage: ../../docs/zhihu_search.md
metadata: {"openclaw":{"emoji":"🔍","requires":{"bins":["python"]}}}
---

# Zhihu Search Skill

## 概述
本 Skill 用于调用知乎开放平台的 `zhihu_search` API。
完整的 API 文档请参考：https://developer.zhihu.com/docs

通过 OpenAPI Platform `GET /api/v1/content/zhihu_search` 检索知乎站内内容，并把响应整理为适合 agent 消费的精简 JSON 结构。

## 认证
使用环境变量 `ZHIHU_ACCESS_SECRET` 进行认证
用户可以在知乎开放平台控制台获取 Access Secret

可选配置：

- `ZHIHU_OPENAPI_BASE_URL`（默认：`https://developer.zhihu.com`）
- `ZHIHU_ZHIHU_SEARCH_URL`（完整 endpoint 覆盖；设置后优先于 `ZHIHU_OPENAPI_BASE_URL` + 默认 path，适用于预发/代理/自定义网关）

## 快速开始

`{baseDir}` 是 agent 框架在运行时自动替换的变量，指向当前 skill 目录的绝对路径（即 `skills/zhihu-search/`）。

```bash
python {baseDir}/scripts/zhihu-search.py '{"query":"如何理解 rave 文化","count":5}'
```

> **跨平台说明**：Unix/macOS 上如果 `python` 不可用，请使用 `python3`。Windows 上使用 `python`。

## 输入约定

传入一个 JSON 参数：

```json
{"query":"...", "count":10}
```

规则：

- `query` 必填，且不能是空字符串（会自动 `strip`）。
- `count` 可选；脚本会自动限制到 1-10。

## 输出约定

### 成功

返回 JSON，包括：

- `code`, `message`
- `item_count`
- `items[]`，包含 `title`, `summary`, `url`, `author_name`, `vote_up_count`, `comment_count`, `edit_time`

### 失败

`error` 字段为动态错误描述，常见情况：

```json
{"error":"query is required","exit_code":1}
{"error":"Invalid JSON payload","exit_code":1}
{"error":"Set ZHIHU_ACCESS_SECRET first (Bearer auth only)","exit_code":1}
{"error":"HTTP request failed (timeout or network error)","exit_code":1}
```

HTTP 非 2xx 时额外携带 `body`：

```json
{"error":"HTTP 403","body":"Forbidden","exit_code":1}
```
