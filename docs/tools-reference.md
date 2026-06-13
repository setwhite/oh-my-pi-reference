# 工具定义速查

> 来源: `@oh-my-pi/pi-coding-agent` `src/tools/index.ts` `BUILTIN_TOOLS` + `HIDDEN_TOOLS`  
> 版本: `15.12.3`  
> 每个工具是否启用、行为参数见 [设置参考](settings.md)

---

## 一、内置工具（BUILTIN_TOOLS，25 个）

### 文件与搜索

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `read` | 始终启用 | — | 读取文件、目录、压缩包、SQLite、图片、URL。支持行范围选择器（如 `:50-200`） |
| `write` | 始终启用 | — | 创建或覆盖文件。支持压缩包内写入和 SQLite 行操作 |
| `edit` | 始终启用 | — | 精确文本编辑。支持 replace / delete / insert / replace block |
| `find` | `find.enabled` | `true` | 基于 glob 模式查找文件和目录 |
| `search` | `search.enabled` | `true` | 基于正则表达式搜索文件内容 |

### 代码智能

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `lsp` | `lsp.enabled` | `true` | 语言服务器协议：跳转定义、查找引用、悬停、重命名、诊断、快速修复 |
| `ast_grep` | `astGrep.enabled` | `true` | 基于 AST 的结构化代码搜索 |
| `ast_edit` | `astEdit.enabled` | `true` | 基于 AST 的结构化代码重写（codemod） |

### 执行与调试

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `bash` | `bash.enabled` | `true` | 执行 shell 命令。构建、测试、git、包管理等 |
| `eval` | `eval.py` / `eval.js` | `true` / `true` | 持久化内核执行 Python（IPython）或 JavaScript 代码 |
| `debug` | `debug.enabled` | `true` | 调试器（DAP 协议）：启动、断点、单步、变量检查 |
| `ssh` | —（需 SSH 配置） | — | SSH 远程执行 |

### 浏览器与网络

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `browser` | `browser.enabled` | `true` | 驱动 Chromium 标签页：导航、点击、填表、截图 |
| `web_search` | `web_search.enabled` | `true` | 网络搜索，支持时效过滤（day/week/month/year） |
| `inspect_image` | `inspect_image.enabled` | `false` | 用视觉模型分析图片：OCR、UI 截图调试 |

### 可视化

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `render_mermaid` | `renderMermaid.enabled` | `false` | 将 Mermaid 图表渲染为 ASCII |

### 协作与任务

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `task` | 始终启用 | — | 派生子代理并行工作。支持多种代理类型（task/explore/plan/designer/reviewer/oracle） |
| `job` | 始终启用 | — | 管理异步后台任务：查看、等待、取消 |
| `irc` | `task.maxRecursionDepth` | `2` | 代理间即时消息。无独立启用开关，由任务递归深度控制 |
| `todo` | `todo.enabled` | `true` | 阶段性任务清单：初始化、标记完成/放弃、追加 |
| `ask` | 始终启用 | — | 向用户提问。多条合理方案需用户决策时使用 |

### 外部集成

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `github` | `github.enabled` | `false` | GitHub CLI：仓库信息、PR 创建/检出、搜索、Actions 监控 |

### 版本控制

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `checkpoint` | `checkpoint.enabled` | `false` | 标记当前会话状态为检查点 |
| `rewind` | `checkpoint.enabled` | `false` | 回退到上一个检查点，将探索性上下文折叠为报告 |

### 工具发现

| 工具 | 启用设置 | 默认值 | 说明 |
|---|---|---|---|
| `search_tool_bm25` | `tools.discoveryMode` | `"off"` | BM25 全文搜索工具发现索引 |

---

## 二、系统隐式工具（HIDDEN_TOOLS，5 个）

这些工具不出现在模型可用工具列表中，由系统内部调用或特定条件下自动注入：

| 工具 | 说明 |
|---|---|
| `resolve` | 审批待定操作（如 `ast_edit` 预览确认）。自动注入 |
| `yield` | 子代理回报控制。`requireYieldTool: true` 时注入 |
| `goal` | 目标模式驱动。`goal.enabled` + 目标激活时注入 |
| `report_finding` | `review` 工具的输出通道 |
| `report_tool_issue` | AutoQA 工具问题报告。`dev.autoqa: true` 时注入 |

---

## 三、条件工具（4 个）

仅当 `memory.backend` 设为 `hindsight` 或 `mnemopi` 时启用：

| 工具 | 说明 |
|---|---|
| `recall` | 记忆召回 |
| `retain` | 记忆保留 |
| `reflect` | 记忆反思 |
| `memory_edit` | 记忆编辑 |

---

> 返回仓库首页 → [README](../README.md)
