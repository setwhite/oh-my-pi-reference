---
name: hackernews-search
version: 2.0.0
disableModelInvocation: true
description: 搜索 Hacker News 内容（通过 Algolia HN Search API）和获取首页热门（通过 Firebase API）。返回结构化结果（标题、链接、评分、评论数、作者、摘要等）。
metadata: {"openclaw":{"emoji":"🔍"}}
---

# Hacker News Search Skill
## 概述
两种免费模式，直接调 API 无需注册。
| 模式 | 首选方式 | 说明 |
|------|---------|------|
| **搜索**（关键词搜 HN） | `read` 调 Algolia API | 单次 HTTP GET，零依赖 |
| **Feed**（首页热帖/最新/最高分） | `python` 脚本 | Firebase 需多步调用 |
> 脚本也支持搜索模式，底层同样调 Algolia API，提供摘要清洗和结构化输出。快速查分/评论数用 `read`，需要正文摘要用脚本搜索。
---
## 搜索：`read` 工具调 Algolia API
### URL 模板
`https://hn.algolia.com/api/v1/search?query=<关键词>&tags=<类型>&hitsPerPage=<条数>`
### 参数
| 参数 | 必填 | 说明 |
|------|------|------|
| `query` | 是 | 搜索关键词，空格分隔 |
| `tags` | 否 | `story`（默认）、`comment`、`(story,comment)`（全部） |
| `hitsPerPage` | 否 | 1–30，默认 20 |
### 示例
```
# 搜帖子（默认 tags=story）
read "https://hn.algolia.com/api/v1/search?query=deepseek&tags=story&hitsPerPage=15"
# 只搜评论
read "https://hn.algolia.com/api/v1/search?query=rust+async&tags=comment&hitsPerPage=10"
# 帖子+评论全搜
read "https://hn.algolia.com/api/v1/search?query=linux+kernel&tags=(story,comment)&hitsPerPage=10"
```
### 响应解析
`read` 返回 JSON：
- `hits[]` — 结果数组：`title`、`url`、`objectID`（拼成 HN 链接）、`points`、`num_comments`、`author`、`created_at`
- `nbHits` / `nbPages` / `page` — 总命中数 / 总页数 / 当前页（0-indexed）
### 翻页
追加 `&page=<页码>`（0 起始）：
```
read "https://hn.algolia.com/api/v1/search?query=deepseek&tags=story&hitsPerPage=15&page=1"
```
---
## Feed：Python 脚本
脚本统一入口，`mode` 走 Feed，`query` 走搜索。
### 脚本路径
```
skill://hackernews-search/scripts/hackernews-search.py
```
> 若路径无法解析，用 `read` 调 Firebase 端点回退。
### Feed
```bash
python "<path>" '{"mode":"top","count":10}'   # 首页热门
python "<path>" '{"mode":"new","count":10}'    # 最新
python "<path>" '{"mode":"best","count":10}'   # 最高分
```
| 参数 | 必填 | 说明 |
|------|------|------|
| `mode` | 是 | `top` / `new` / `best` |
| `count` | 否 | 1–30，默认 10 |
### 搜索（脚本）
```bash
python "<path>" '{"query":"rust async","count":5}'         # 搜帖子
python "<path>" '{"query":"python","count":5,"type":"comment"}' # 评论
python "<path>" '{"query":"linux kernel","count":5,"type":"all"}' # 全部
```
| 参数 | 必填 | 说明 |
|------|------|------|
| `query` | 是 | 搜索关键词 |
| `count` | 否 | 1–30，默认 10 |
| `type` | 否 | `story`（默认）/ `comment` / `all`，映射到 Algolia `tags` |
---
## 失败回退
- **搜索**（read 调 Algolia 网络错误）：重试一次，仍失败用 `web_search` 搜 `site:news.ycombinator.com <关键词>`
- **Feed**（Python 脚本不可用）：`read` 调 Firebase 端点拿 ID 列表 → 并行取详情 → 提取字段
---
## 展示格式
```
### 🔥 HN 上关于"<query>"的讨论

| # | 标题 | 分数 | 评论 | 日期 | HN 链接 |
|---|------|------|------|------|---------|
| 1 | <title> | <points> | <num_comments> | <date> | [HN](<hn_url>) |

共 <total> 条结果。
```
