# 工具定义速查

> OMP 内置工具一览，按用途归类。  
> 每个工具是否启用、行为参数可在 `tools` 相关设置中配置 → [设置参考](settings.md)

## 文件与搜索

### `read`
读取文件、目录、压缩包、SQLite 数据库、图片、文档及 URL。支持行范围选择器（如 `:50-200`）。对代码文件返回结构摘要；对图片返回元数据（视觉分析请用 `inspect_image`）。

### `write`
创建或覆盖文件。支持压缩包内写入和 SQLite 行操作。

### `edit`
精确文本编辑。基于行号 + 快照标签锚定。支持 `replace`（替换）、`delete`（删除）、`insert`（插入）、`replace block`（替换语法块）。

### `find`
基于 glob 模式快速查找文件和目录。默认尊重 `.gitignore`。支持 `hidden` 和 `gitignore` 开关。

### `search`
基于正则表达式搜索文件内容。默认尊重 `.gitignore`。返回带行号的匹配结果和上下文。

## 代码智能

### `lsp`
语言服务器协议接口。支持跳转定义、查找引用、类型悬停、符号重命名、代码诊断、快速修复等。

### `ast_grep`
基于 AST 的结构化代码搜索。用模式匹配语法树。适合找声明、调用、特定语法结构。

### `ast_edit`
基于 AST 的结构化代码重写。适合跨文件重命名、import 改写、模式替换等 codemod。

## 执行与调试

### `bash`
执行 shell 命令。用于构建、测试、git、包管理，或产出计数/校验和等计算型管道。

### `eval`
在持久化内核中执行代码（Python IPython 或 JavaScript VM）。跨 cell 保持状态。Python 支持顶层 `await`。

### `debug`
调试器（DAP 协议）。支持启动调试、设断点、单步执行、查看变量、暂停运行中程序。

## 浏览器与网络

### `browser`
驱动真实 Chromium 标签页。支持页面导航、可访问性快照、点击/填表/截图等交互操作。

### `web_search`
网络搜索。支持时效过滤（day/week/month/year）。

### `inspect_image`
用视觉模型分析图片。用于 OCR、UI 截图调试、场景识别。

## 协作与任务

### `task`
派生子代理并行工作。多种代理类型（task/explore/plan/designer/reviewer/oracle 等），子代理间通过 `irc` 通信。

### `job`
管理异步后台任务。支持查看、等待、取消。

### `irc`
代理间即时消息。支持发送、等待回复、查看未读、列出所有代理。

### `todo`
阶段性任务清单。支持初始化、标记完成/放弃、追加任务。

### `ask`
向用户提问。当存在多条合理方案且需要用户决策时使用。

### `resolve`
审批待定操作。用于确认或丢弃预览中的变更。

## 外部集成

### `github`
GitHub CLI 封装。支持仓库信息、PR 创建/检出、搜索 Issues/PR/代码、监控 Actions 工作流。

---

> 返回仓库首页 → [README](../README.md)
