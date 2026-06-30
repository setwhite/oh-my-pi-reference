---
name: stackexchange-search
version: 2.0.0
disableModelInvocation: true
description: 搜索 Stack Exchange 站内内容（Stack Overflow 等），返回结构化结果（标题、链接、评分、回答数、标签、摘要等）。
metadata: {"openclaw":{"emoji":"🔍"}}
---
# Stack Exchange Search Skill

## 概述

通过 Stack Exchange API v2.3 免费无需注册。

| 模式 | 使用场景 |
|------|---------|
| `read` 直调 API | 搜问题列表，HTTP GET 零依赖 |
| Python 脚本 | 需要正文摘要（HTML 清洗后的 excerpt） |

API 文档：https://api.stackexchange.com/docs

## 配额

- 无 API Key：300 次/天
- 设置 `STACKEXCHANGE_API_KEY`：10,000 次/天（https://stackapps.com 获取）

---

## 搜索模式（`read` 工具）

URL 模板：`https://api.stackexchange.com/2.3/search/advanced?q=<关键词>&site=<站点>&pagesize=<条数>&order=desc&sort=relevance`

| 参数 | 必填 | 说明 |
|------|------|------|
| `q` | 是 | 搜索关键词，空格分隔 |
| `site` | 否 | 默认 `stackoverflow`，列表见 https://api.stackexchange.com/docs/sites |
| `pagesize` | 否 | 1–100，建议 ≤20 |
| `sort` | 否 | `relevance`/`votes`/`creation`/`activity` |
| `order` | 否 | `desc`/`asc` |
| `tagged` | 否 | 限定标签，分号分隔 |

示例：
```
read "https://api.stackexchange.com/2.3/search/advanced?q=python+asyncio&site=stackoverflow&pagesize=10"
read "https://api.stackexchange.com/2.3/search/advanced?q=rust+borrow+checker&site=stackoverflow&pagesize=5&sort=votes"
read "https://api.stackexchange.com/2.3/search/advanced?q=memory+leak&site=stackoverflow&pagesize=10&tagged=python;asyncio"
```

翻页：`&page=<页码>`（**1 起始**）。例：`read "https://api.stackexchange.com/2.3/search/advanced?q=deepseek&site=stackoverflow&pagesize=10&page=2"`
---

## 正文摘要模式（Python 脚本）

需要正文摘要时使用。脚本路径：`skill://stackexchange-search/scripts/stackexchange-search.py`

用法：
```bash
python "<脚本路径>" '{"query":"python asyncio","count":5}'
python "<脚本路径>" '{"query":"rust borrow checker","count":5,"site":"stackoverflow"}'
```

参数：

| 参数 | 必填 | 说明 |
|------|------|------|
| `query` | 是 | 搜索关键词 |
| `count` | 否 | 1–20，默认 10 |
| `site` | 否 | 默认 `stackoverflow` |

额外输出（相比 `read` 模式）：`excerpt`（HTML 清洗 ≤300 字符）、`has_accepted_answer`。透传 API 字段：`quota_remaining`、`quota_max`、`backoff`。
---

## 失败回退

- `read` 失败：重试一次，仍失败用 `web_search` 搜 `site:stackoverflow.com <关键词>`
- 脚本不可用：直接用 `read` 调 API（仅无正文摘要）
---

## 展示格式

搜索完成后，按以下格式呈现：

```
### Stack Overflow 上关于"<query>"的搜索结果

| # | 标题 | 分数 | 回答 | 标签 | 链接 |
|---|------|------|------|------|------|
| 1 | <title> | <score> | <answer_count> | <tags> | [SO](<link>) |

配额剩余: <quota_remaining>/<quota_max>
```
