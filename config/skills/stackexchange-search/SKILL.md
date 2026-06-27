---
name: stackexchange-search
version: 2.0.0
description: 搜索 Stack Exchange 站内内容（Stack Overflow 等），返回结构化结果（标题、链接、评分、回答数、标签、摘要等）。当用户要求"搜索 Stack Overflow"、"Stack Exchange 上有没有"、"查一下 SO"、或在 Stack Exchange 平台检索特定技术问题时使用。不应触发：通用 web 搜索（用内置 web_search 工具）、仅提及「Stack Overflow」但无检索意图、搜索其他平台内容。
metadata: {"openclaw":{"emoji":"🔍"}}
---

# Stack Exchange Search Skill

## 概述

两种方式，全部通过 Stack Exchange API v2.3，免费无需注册。

| 需求 | 首选方式 | 说明 |
|------|---------|------|
| **搜问题列表**（标题/分数/标签） | `read` 工具直接调 API | 单次 HTTP GET，零依赖 |
| **需要正文摘要**（HTML 清洗后的 excerpt） | Python 脚本 | 带 `filter=withbody`，自动去标签+截断 |

API 文档：https://api.stackexchange.com/docs

## 配额

- 无 API Key：300 次/天
- 设置 `STACKEXCHANGE_API_KEY` 环境变量：10,000 次/天
- 在 https://stackapps.com 注册应用获取 Key

---

## 搜索模式（推荐：`read` 工具）

**直接用 `read` 请求 Stack Exchange API**，无需 Python 脚本。

### URL 模板

```
https://api.stackexchange.com/2.3/search/advanced?q=<关键词>&site=<站点>&pagesize=<条数>&order=desc&sort=relevance
```

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `q` | 是 | 搜索关键词，空格分隔多个词 |
| `site` | 否 | 站点，默认 `stackoverflow`。完整列表见 https://api.stackexchange.com/docs/sites |
| `pagesize` | 否 | 1–100，建议 ≤20 |
| `sort` | 否 | `relevance`（默认）/ `votes` / `creation` / `activity` |
| `order` | 否 | `desc`（默认）/ `asc` |
| `tagged` | 否 | 限定标签，分号分隔，如 `python;asyncio` |

### 示例

```
# 搜索 Stack Overflow 上关于 python asyncio 的问题
read "https://api.stackexchange.com/2.3/search/advanced?q=python+asyncio&site=stackoverflow&pagesize=10"

# 按分数排序
read "https://api.stackexchange.com/2.3/search/advanced?q=rust+borrow+checker&site=stackoverflow&pagesize=5&sort=votes"

# 限定标签
read "https://api.stackexchange.com/2.3/search/advanced?q=memory+leak&site=stackoverflow&pagesize=10&tagged=python;asyncio"
```

### 响应解析

`read` 返回 JSON，关键字段：

- `items[]` — 结果数组，每条包含：
  - `title` — 标题
  - `link` — 问题链接
  - `score` — 分数
  - `answer_count` — 回答数
  - `is_answered` — 是否有回答
  - `tags` — 标签数组
  - `creation_date` — Unix 时间戳
  - `view_count` — 浏览次数
- `quota_remaining` / `quota_max` — 当日剩余/总配额
- `backoff` — 限流等待秒数（出现时说明请求过快，应等待该秒数后重试）
- `has_more` — 是否有更多结果

### 翻页

追加 `&page=<页码>`（**1 起始**，与 Algolia 的 0 起始不同）：

```
read "https://api.stackexchange.com/2.3/search/advanced?q=deepseek&site=stackoverflow&pagesize=10&page=2"
```

---

## 正文摘要模式（Python 脚本）

当需要问题的正文摘要（HTML 清洗后的纯文本 excerpt）时，用脚本。

### 脚本路径

```
skill://stackexchange-search/scripts/stackexchange-search.py
```

### 用法

```bash
python "<脚本路径>" '{"query":"python asyncio","count":5}'
python "<脚本路径>" '{"query":"rust borrow checker","count":5,"site":"stackoverflow"}'
```

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `query` | 是 | 搜索关键词 |
| `count` | 否 | 1–20，默认 10 |
| `site` | 否 | 默认 `stackoverflow` |

### 输出字段
相比直接 API 调用，脚本额外提供：
- `excerpt` — HTML 清洗后的纯文本摘要（≤300 字符）
- `has_accepted_answer` — 是否有已接受的回答
- `url` — 问题链接（同 `link`）

脚本同时透传 API 原始字段：`quota_remaining`、`quota_max`、`backoff`。

---

## 失败回退

### `read` 工具失败
1. 重试一次（Stack Exchange API 偶尔限流）
2. 如仍失败，用 `web_search` 搜索 `site:stackoverflow.com <关键词>`

### 脚本不可用
直接用 `read` 调 API（仅无正文摘要，其余字段完全相同）

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
