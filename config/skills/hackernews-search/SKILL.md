---
name: hackernews-search
version: 2.0.0
description: 搜索 Hacker News 内容（通过 Algolia HN Search API）和获取首页热门（通过 Firebase API）。返回结构化结果（标题、链接、评分、评论数、作者、摘要等）。当用户要求"搜索 Hacker News"、"HN 上有没有"、"Hacker News 最近在讨论什么"、"HN 热帖"时使用。不应触发：通用 web 搜索（用内置 web_search 工具）、仅提及「HN」但无检索意图。
metadata: {"openclaw":{"emoji":"🔍"}}
---

# Hacker News Search Skill

## 概述

两种模式，全部免费，无需注册，无 Rate Limit。

| 模式 | 首选方式 | 说明 |
|------|---------|------|
| **搜索**（按关键词搜 HN） | `read` 工具直接调 Algolia API | 单次 HTTP GET，零依赖。脚本也支持搜索模式，提供摘要清洗和结构化输出 |
| **Feed**（首页热帖/最新/最高分） | Python 脚本 | Firebase 需要多步 API 调用 |


### 搜索方式选择

| 场景 | 使用 | 原因 |
|------|------|------|
| 快速查关键词、看分数/评论数 | `read` 直接调 Algolia API | 零依赖，最快 |
| 需要正文摘要、区分帖子/评论类型 | Python 脚本搜索模式 | 自动清洗 HTML、生成 `hn_url`、区分 story/comment |

> 脚本的搜索模式底层同样调用 Algolia API，但额外做了摘要提取和结构化处理。
---

## 搜索模式（推荐：`read` 工具）

**直接用 `read` 工具请求 Algolia HN Search API**，无需 Python 脚本。

### URL 模板

```
https://hn.algolia.com/api/v1/search?query=<关键词>&tags=<类型>&hitsPerPage=<条数>
```

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `query` | 是 | 搜索关键词，空格分隔多个词 |
| `tags` | 否 | `story`（默认，帖子）、`comment`（评论）、`(story,comment)`（全部） |
| `hitsPerPage` | 否 | 1–30，默认 20 |

### 示例

```
# 搜索 deepseek 帖子，最多 15 条
read "https://hn.algolia.com/api/v1/search?query=deepseek&tags=story&hitsPerPage=15"

# 只搜评论
read "https://hn.algolia.com/api/v1/search?query=rust+async&tags=comment&hitsPerPage=10"

# 帖子+评论全搜
read "https://hn.algolia.com/api/v1/search?query=linux+kernel&tags=(story,comment)&hitsPerPage=10"
```

### 响应解析

`read` 返回 JSON，关键字段：

- `hits[]` — 结果数组，每条包含：
  - `title` — 标题
  - `url` — 链接（可能是 HN 内部链接）
  - `objectID` — HN 帖子 ID，拼成 `https://news.ycombinator.com/item?id=<objectID>`
  - `points` — 分数
  - `num_comments` — 评论数
  - `author` — 作者
  - `created_at` — 发布时间
- `nbHits` — 总命中数
- `nbPages` — 总页数
- `page` — 当前页（0-indexed）

### 翻页

追加 `&page=<页码>`（0 起始）：

```
read "https://hn.algolia.com/api/v1/search?query=deepseek&tags=story&hitsPerPage=15&page=1"
```

---

## Python 脚本模式

脚本统一入口，自动根据参数判断模式：有 `mode` → Feed，有 `query` → 搜索。

### 脚本路径

```
skill://hackernews-search/scripts/hackernews-search.py
```

> 如果该路径无法解析，回退到搜索模式：用 `read` 分别调 Firebase 端点。

### Feed 模式

```bash
# 首页热门
python "<脚本路径>" '{"mode":"top","count":10}'

# 最新
python "<脚本路径>" '{"mode":"new","count":10}'

# 最高分
python "<脚本路径>" '{"mode":"best","count":10}'
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `mode` | 是 | `top` / `new` / `best` |
| `count` | 否 | 1–30，默认 10 |

### 搜索模式

```bash
# 按关键词搜帖子
python "<脚本路径>" '{"query":"rust async","count":5}'

# 只搜评论
python "<脚本路径>" '{"query":"python","count":5,"type":"comment"}'

# 帖子+评论全搜
python "<脚本路径>" '{"query":"linux kernel","count":5,"type":"all"}'
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `query` | 是 | 搜索关键词 |
| `count` | 否 | 1–30，默认 10 |
| `type` | 否 | `story`（默认）/ `comment` / `all`（全部） |

> `type` 映射到底层 Algolia `tags` 参数：`story` → `tags=story`，`comment` → `tags=comment`，`all` → `tags=(story,comment)`。脚本自动完成此转换。

---

## 失败回退

### 搜索模式回退

如果 `read` 返回网络错误：
1. 重试一次（Algolia 极少宕机）
2. 如果仍失败，用 `web_search` 搜索 `site:news.ycombinator.com <关键词>`

### Feed 模式回退

如果 Python 脚本不可用：
1. `read "https://hacker-news.firebaseio.com/v0/<mode>stories.json"` → 得到 ID 列表
2. 取前 N 个 ID，并行 `read "https://hacker-news.firebaseio.com/v0/item/<id>.json"`
3. 手动提取 `title`、`url`、`score`、`descendants`、`by` 等字段

---

## 展示格式

搜索/feed 完成后，按以下格式呈现给用户：

```
### 🔥 HN 上关于"<query>"的讨论

| # | 标题 | 分数 | 评论 | 日期 | HN 链接 |
|---|------|------|------|------|---------|
| 1 | <title> | <points> | <num_comments> | <date> | [HN](<hn_url>) |

共 <total> 条结果。
```
