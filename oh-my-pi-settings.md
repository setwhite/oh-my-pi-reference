# Oh My Pi — Settings Schema 归类

> 来源: `settings-schema.ts` `SETTINGS_SCHEMA` 对象  
> 按 `ui.tab` 归类；无 UI 的归入 **General / 无 UI**。  
> 格式: `设置键` — 类型, 默认值 — 描述

---

## 目录

1. [Appearance (外观)](#appearance-外观)
2. [Model (模型)](#model-模型)
3. [Interaction (交互)](#interaction-交互)
4. [Context (上下文)](#context-上下文)
5. [Memory (记忆)](#memory-记忆)
6. [Editing (编辑)](#editing-编辑)
7. [Tools (工具)](#tools-工具)
8. [Tasks (任务)](#tasks-任务)
9. [Providers (提供商)](#providers-提供商)
10. [General / 无 UI](#general--无-ui)

---

## Appearance (外观)

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `theme.dark` | string | `"titanium"` | 终端深色背景时使用的主题 |
| `theme.light` | string | `"light"` | 终端浅色背景时使用的主题 |
| `symbolPreset` | enum | `"unicode"` | 图标/符号风格: unicode / nerd / ascii |
| `colorBlindMode` | boolean | `false` | 色盲模式：diff 新增用蓝色代替绿色 |
| `statusLine.preset` | enum | `"default"` | 状态栏预设：default / minimal / compact / full / nerd / ascii / custom |
| `statusLine.separator` | enum | `"powerline-thin"` | 状态栏分隔符样式：powerline / powerline-thin / slash / pipe / block / none / ascii |
| `statusLine.sessionAccent` | boolean | `true` | 使用会话名称颜色渲染编辑器边框和状态栏间隙 |
| `statusLine.showHookStatus` | boolean | `true` | 在状态栏下方显示 hook 状态消息 |
| `terminal.showImages` | boolean | `true` | 在终端内联渲染图片 |
| `images.autoResize` | boolean | `true` | 自动将大图缩放到 2000×2000 以提升模型兼容性 |
| `images.blockImages` | boolean | `false` | 阻止图片发送给 LLM 提供商 |
| `tui.hyperlinks` | enum | `"auto"` | OSC 8 超链接：off / auto / always |
| `display.shimmer` | enum | `"classic"` | 加载/工作中消息的动画风格：classic / kitt / disabled |
| `display.showTokenUsage` | boolean | `false` | 在助手消息上显示每轮 token 用量 |
| `showHardwareCursor` | boolean | `true` | 显示终端硬件光标（IME 支持） |
| `clearOnShrink` | boolean | `false` | 内容收缩时清除空白行（可能导致闪烁） |
| `task.showResolvedModelBadge` | boolean | `false` | 在任务组件状态栏显示子代理实际使用的模型 ID |

---

## Model (模型)

### 推理与提示

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `defaultThinkingLevel` | enum | `"high"` | 支持思考的模型的推理深度 |
| `hideThinkingBlock` | boolean | `false` | 隐藏助手回复中的思考块 |
| `repeatToolDescriptions` | boolean | `false` | 在系统提示中渲染完整工具描述而非工具名称列表 |

### 采样参数

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `temperature` | number | `-1` | 采样温度（0=确定, 1=创意, -1=提供商默认） |
| `topP` | number | `-1` | Nucleus 采样截断（0-1, -1=提供商默认） |
| `topK` | number | `-1` | 从 Top-K token 采样（-1=提供商默认） |
| `minP` | number | `-1` | 最小概率阈值（0-1, -1=提供商默认） |
| `presencePenalty` | number | `-1` | 对已出现 token 的惩罚（-1=提供商默认） |
| `repetitionPenalty` | number | `-1` | 对重复 token 的惩罚（-1=提供商默认） |

### 服务等级

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `serviceTier` | enum | `"none"` | 处理优先级提示：none / auto / default / flex / scale / priority / openai-only / claude-only |

### 重试

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `retry.maxRetries` | number | `3` | API 错误最大重试次数 |
| `retry.maxDelayMs` | number | `300000` | 重试最大等待毫秒数 |
| `retry.fallbackRevertPolicy` | enum | `"cooldown-expiry"` | 回退后何时返回主模型：cooldown-expiry / never |

---

## Interaction (交互)

### 对话流

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `steeringMode` | enum | `"one-at-a-time"` | 代理工作中排队消息的处理方式：all / one-at-a-time |
| `followUpMode` | enum | `"one-at-a-time"` | 本轮结束后跟进消息的排空方式：all / one-at-a-time |
| `interruptMode` | enum | `"immediate"` | 操控消息何时中断工具执行：immediate / wait |
| `loop.mode` | enum | `"prompt"` | /loop 迭代间行为：prompt / compact / reset |
| `autoResume` | boolean | `false` | 自动恢复当前目录最近的会话 |

### 电源（macOS）

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `power.preventIdleSleep` | boolean | `true` | caffeinate -i：会话打开时保持系统唤醒 |
| `power.preventSystemSleep` | boolean | `false` | caffeinate -s：交流电时阻止系统休眠 |
| `power.declareUserActive` | boolean | `false` | caffeinate -u：保持屏幕点亮，视用户为活跃 |
| `power.preventDisplaySleep` | boolean | `false` | caffeinate -d：阻止显示屏空闲休眠 |

### 输入与启动

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `doubleEscapeAction` | enum | `"tree"` | 编辑器为空时双击 Esc 的动作：branch / tree / none |
| `treeFilterMode` | enum | `"default"` | 打开会话树的默认过滤模式 |
| `autocompleteMaxVisible` | number | `5` | 自动补全下拉列表最大可见条目（3-20） |
| `emojiAutocomplete` | boolean | `true` | 建议 `:name:` 短代码的 emoji 并展开文字表情 |
| `startup.quiet` | boolean | `false` | 跳过欢迎画面和启动状态消息 |
| `startup.checkUpdate` | boolean | `true` | 启动时检查更新 |
| `collapseChangelog` | boolean | `false` | 更新后显示精简变更日志 |

### 通知

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `completion.notify` | enum | `"on"` | 代理完成时通知: on / off |
| `ask.timeout` | number | `0` | 超时后自动选择推荐选项（0=禁用） |
| `ask.notify` | enum | `"on"` | ask 工具等待输入时通知: on / off |

### 语音转文字

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `stt.enabled` | boolean | `false` | 启用麦克风语音输入 |
| `stt.modelName` | enum | `"base.en"` | Whisper 模型大小 |

### 工具审批

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tools.approvalMode` | enum | `"yolo"` | 默认审批行为：always-ask / write / yolo |

---

## Context (上下文)

### 上下文提升

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `contextPromotion.enabled` | boolean | `true` | 上下文溢出时自动提升到大上下文模型而非压缩 |

### 压缩

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `compaction.enabled` | boolean | `true` | 上下文过大时自动压缩 |
| `compaction.strategy` | enum | `"context-full"` | 压缩策略：context-full / handoff / off |
| `compaction.thresholdPercent` | number | `-1` | 上下文维护的百分比阈值 |
| `compaction.thresholdTokens` | number | `-1` | 上下文维护的固定 token 限制（覆盖百分比） |
| `compaction.handoffSaveToDisk` | boolean | `false` | 将生成的手顺文档保存为 markdown 文件 |
| `compaction.remoteEnabled` | boolean | `true` | 使用远程压缩端点替代本地摘要 |
| `compaction.idleEnabled` | boolean | `false` | 空闲时当 token 数超过阈值时压缩上下文 |
| `compaction.idleThresholdTokens` | number | `200000` | 触发空闲压缩的 token 数 |
| `compaction.idleTimeoutSeconds` | number | `300` | 空闲后等待的秒数再压缩 |

### 分支摘要

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `branchSummary.enabled` | boolean | `false` | 离开分支时提示生成摘要 |

### TTSR (Time Traveling Stream Rules)

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `ttsr.enabled` | boolean | `true` | 输出匹配模式时中断代理 |
| `ttsr.contextMode` | enum | `"discard"` | TTSR 触发时如何处理部分输出：discard / keep |
| `ttsr.interruptMode` | enum | `"always"` | 何时中断 vs 完成后注入警告 |
| `ttsr.repeatMode` | enum | `"once"` | 规则重复方式：once / after-gap |
| `ttsr.repeatGap` | number | `10` | 规则再次触发前的消息间隔数 |

---

## Memory (记忆)

### 记忆后端

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `memory.backend` | enum | `"off"` | 记忆后端：off / local / hindsight |

### Hindsight

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `hindsight.apiUrl` | string | `"http://localhost:8888"` | Hindsight 服务器 URL |
| `hindsight.bankId` | string | `undefined` | 记忆库标识符（默认=项目名） |
| `hindsight.scoping` | enum | `"per-project-tagged"` | 作用域策略：global / per-project / per-project-tagged |
| `hindsight.autoRecall` | boolean | `true` | 每个会话首轮自动召回记忆 |
| `hindsight.autoRetain` | boolean | `true` | 每 N 轮和会话边界自动保留转录 |
| `hindsight.retainMode` | enum | `"full-session"` | 保留模式：full-session / last-turn |
| `hindsight.mentalModelsEnabled` | boolean | `true` | 启动时将精选反思摘要（心智模型）读入开发者指令 |
| `hindsight.mentalModelAutoSeed` | boolean | `true` | 会话启动时自动创建内置心智模型 |

---

## Editing (编辑)

### 编辑工具

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `edit.mode` | enum | `"hashline"` | 编辑工具变体：replace / patch / hashline / apply_patch |
| `edit.fuzzyMatch` | boolean | `true` | 接受高置信度模糊匹配（空白差异） |
| `edit.fuzzyThreshold` | number | `0.95` | 模糊匹配的相似度阈值 |
| `edit.streamingAbort` | boolean | `false` | 补丁预览失败时中止流式编辑工具调用 |
| `edit.hashlineAutoDropPureInsertDuplicates` | boolean | `false` | 删除与相邻文件上下文重复的载荷行 |
| `edit.blockAutoGenerated` | boolean | `true` | 阻止编辑自动生成的文件 |

### Read 工具

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `readLineNumbers` | boolean | `false` | 默认在 read 输出前加行号 |
| `readHashLines` | boolean | `true` | 包含文件哈希头和行号（hashline 模式） |
| `read.defaultLimit` | number | `300` | 代理调用 read 未指定 limit 时的默认行数 |
| `read.summarize.enabled` | boolean | `true` | 未指定选择器时返回结构化代码摘要 |
| `read.summarize.prose` | boolean | `false` | 对 Markdown/纯文本也返回结构化摘要 |
| `read.summarize.minBodyLines` | number | `4` | 多行体最小长度，超过则折叠 |
| `read.summarize.minCommentLines` | number | `6` | 多行块注释最小长度，超过则折叠 |
| `read.summarize.minTotalLines` | number | `100` | 少于该行数则逐字读取而非摘要 |
| `read.summarize.unfoldUntil` | number | `50` | BFS 展开直到摘要达到该可见行数 |
| `read.summarize.unfoldLimit` | number | `100` | 摘要大小硬上限 |
| `read.toolResultPreview` | boolean | `false` | 在转录中内联渲染 read 结果而非摘要行 |

### LSP

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `lsp.enabled` | boolean | `true` | 启用 lsp 工具 |
| `lsp.formatOnWrite` | boolean | `false` | 写入后使用 LSP 自动格式化 |
| `lsp.diagnosticsOnWrite` | boolean | `true` | 写入代码文件后返回 LSP 诊断 |
| `lsp.diagnosticsOnEdit` | boolean | `false` | 编辑代码文件后返回 LSP 诊断 |

### Bash 拦截器

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `bashInterceptor.enabled` | boolean | `false` | 拦截有专用工具的 shell 命令 |
| `bash.stripTrailingHeadTail` | boolean | `true` | 自动删除单行 bash 命令末尾的 `\| head`/`\| tail` |

### Shell 输出最小化

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `shellMinimizer.enabled` | boolean | `true` | 压缩啰嗦的 shell 输出（git, npm, cargo 等） |

### Eval

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `eval.py` | boolean | `true` | 允许 eval 工具分发到 IPython 内核 |
| `eval.js` | boolean | `true` | 允许 eval 工具分发到 JavaScript 运行时 |

### Python 内核

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `python.kernelMode` | enum | `"session"` | IPython 内核是否跨调用保持存活：session / per-call |

---

## Tools (工具)

### 工具审批策略

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tools.approval` | record | `{}` | 按工具的审批策略：allow / prompt / deny |

### 工具输出

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tools.artifactSpillThreshold` | number | `50` | 工具输出超过此大小（KB）则保存为 artifact |
| `tools.artifactTailBytes` | number | `20` | 溢出时保留在行的尾部大小（KB） |
| `tools.artifactHeadBytes` | number | `20` | 溢出时保留在行的头部大小（KB），0=仅尾部 |
| `tools.outputMaxColumns` | number | `768` | 流式工具输出的每行字节上限 |
| `tools.artifactTailLines` | number | `500` | 溢出到 artifact 时保留的最大尾部行数 |

### 市场

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `marketplace.autoUpdate` | enum | `"notify"` | 启动时检查插件更新：off / notify / auto |

### Todo

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `todo.enabled` | boolean | `true` | 启用 todo_write 工具 |
| `todo.reminders` | boolean | `true` | 停止前提醒代理完成 todo |
| `todo.reminders.max` | number | `3` | 放弃前的最大提醒次数 |
| `todo.eager` | boolean | `false` | 首条消息后自动创建待办列表 |

### Find / Search / AST

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `find.enabled` | boolean | `true` | 启用 find 工具 |
| `search.enabled` | boolean | `true` | 启用 search 工具 |
| `search.contextBefore` | number | `1` | 每个匹配前的上下文行数 |
| `search.contextAfter` | number | `3` | 每个匹配后的上下文行数 |
| `astGrep.enabled` | boolean | `true` | 启用 ast_grep 工具 |
| `astEdit.enabled` | boolean | `true` | 启用 ast_edit 工具 |

### IRC

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `irc.enabled` | boolean | `true` | 启用代理间 IRC 消息 |
| `irc.timeoutMs` | number | `120000` | IRC 超时毫秒（0=禁用） |

### 可选工具开关

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `renderMermaid.enabled` | boolean | `false` | 渲染 Mermaid 图表为 ASCII |
| `debug.enabled` | boolean | `true` | 启用 debug 工具 |
| `calc.enabled` | boolean | `false` | 启用计算器工具 |
| `tts.enabled` | boolean | `false` | 启用文字转语音工具 |
| `recipe.enabled` | boolean | `true` | 检测到构建文件时启用 recipe 工具 |
| `inspect_image.enabled` | boolean | `false` | 启用图片检查工具 |
| `checkpoint.enabled` | boolean | `false` | 启用检查点/回滚工具 |

### 获取与浏览

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `fetch.enabled` | boolean | `true` | 允许 read 工具获取和处理 URL |
| `github.enabled` | boolean | `false` | 启用 github 工具 |
| `github.cache.enabled` | boolean | `true` | 缓存渲染的 issue/PR |
| `github.cache.softTtlSec` | number | `300` | 缓存软 TTL（秒） |
| `github.cache.hardTtlSec` | number | `604800` | 缓存硬 TTL（秒，默认7天） |
| `web_search.enabled` | boolean | `true` | 启用 web_search 工具 |
| `browser.enabled` | boolean | `true` | 启用 browser 工具 |
| `browser.headless` | boolean | `true` | 无头模式启动浏览器 |
| `browser.screenshotDir` | string | `undefined` | 截图保存目录 |

### 工具执行

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tools.intentTracing` | boolean | `true` | 要求代理在执行前描述每次工具调用的意图 |
| `tools.maxTimeout` | number | `0` | 代理可为任何工具设置的最大超时秒数（0=不限） |

### 异步任务

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `async.enabled` | boolean | `false` | 启用异步 bash 命令和后台任务 |
| `async.pollWaitDuration` | enum | `"30s"` | poll 工具等待背景任务更新的时长 |
| `bash.autoBackground.enabled` | boolean | `false` | 自动后台运行长时间 bash 命令 |

### 工具发现

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tools.discoveryMode` | enum | `"off"` | 隐藏工具以节省 token：off / mcp-only / all |
| `tools.essentialOverride` | array | `[]` | 覆盖始终加载的内置工具列表 |

### MCP

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `mcp.enableProjectConfig` | boolean | `true` | 从项目根目录加载 .mcp.json/mcp.json |
| `mcp.discoveryMode` | boolean | `false` | 默认隐藏 MCP 工具，通过发现工具暴露 |
| `mcp.discoveryDefaultServers` | array | `[]` | 发现模式下仍可见的 MCP 服务器 |
| `mcp.notifications` | boolean | `false` | 将 MCP 资源更新注入代理对话 |
| `mcp.notificationDebounceMs` | number | `500` | MCP 通知防抖窗口毫秒数 |

### 开发者 / QA

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `dev.autoqa` | boolean | `false` | 为所有代理启用自动化工具问题报告 |
| `dev.autoqaPush.endpoint` | string | `"https://qa.omp.sh/v1/grievances"` | 自动 QA 推送端点 |

---

## Tasks (任务)

### 规划与目标

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `plan.enabled` | boolean | `true` | 启用规划模式（只读探索和规划） |
| `goal.enabled` | boolean | `true` | 启用每会话目标模式 |
| `goal.statusInFooter` | boolean | `true` | 在状态栏显示 token 预算和目标指示器 |
| `goal.continuationModes` | array | `["interactive"]` | 活跃目标可自动继续的运行模式 |

### 子代理隔离

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `task.isolation.mode` | enum | `"none"` | 子代理隔离后端：none / auto / apfs / btrfs / zfs / reflink / overlayfs / projfs / block-clone / rcopy |
| `task.isolation.merge` | enum | `"patch"` | 隔离任务变更整合方式：patch / branch |
| `task.isolation.commits` | enum | `"generic"` | 隔离提交消息风格：generic / ai |

### 子代理行为

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `task.eager` | boolean | `false` | 鼓励代理将工作委派给子代理 |
| `task.simple` | enum | `"schema-free"` | 任务工具的输入模式：default / schema-free / independent |
| `task.maxConcurrency` | number | `32` | 子代理的最大并发数 |
| `task.enableLsp` | boolean | `false` | 允许子代理使用 lsp 工具 |
| `task.maxRecursionDepth` | number | `2` | 子代理可递归创建子代理的层级深度 |
| `task.maxRuntimeMs` | number | `0` | 子代理的硬墙钟限制（毫秒，0=不限） |

### Todo 与任务管理

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tasks.todoClearDelay` | number | `60` | 完成后从列表中清除已完成/放弃任务的等待秒数 |

### Skills

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `skills.enableSkillCommands` | boolean | `true` | 将技能注册为 `/skill:name` 命令 |

### 命令

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `commands.enableClaudeUser` | boolean | `true` | 从 ~/.claude/commands/ 加载命令 |
| `commands.enableClaudeProject` | boolean | `true` | 从 .claude/commands/ 加载命令 |
| `commands.enableOpencodeUser` | boolean | `true` | 从 ~/.config/opencode/commands/ 加载命令 |
| `commands.enableOpencodeProject` | boolean | `true` | 从 .opencode/commands/ 加载命令 |

---

## Providers (提供商)

### 安全

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `secrets.enabled` | boolean | `false` | 发送到 AI 提供商前混淆秘密 |

### Web 搜索提供商

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `providers.webSearch` | enum | `"auto"` | Web 搜索工具使用的提供商：auto / exa / brave / jina / kimi / zai / perplexity / anthropic / gemini / codex / tavily / kagi / synthetic / parallel / searxng |

### 图片生成提供商

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `providers.image` | enum | `"auto"` | 图片生成工具使用的提供商：auto / openai / antigravity / xai / gemini / openrouter |

### 提供商设置

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `providers.kimiApiFormat` | enum | `"anthropic"` | Kimi Code 提供商的 API 格式：openai / anthropic |
| `providers.openaiWebsockets` | enum | `"auto"` | OpenAI Codex 模型的 WebSocket 策略：auto / off / on |
| `providers.openrouterVariant` | enum | `"default"` | OpenRouter 路由变体后缀：default / nitro / floor / online / exacto |
| `providers.parallelFetch` | boolean | `true` | 凭据可用时使用 Parallel extract API 获取 URL |
| `provider.appendOnlyContext` | enum | `"auto"` | 仅追加上下文缓存策略：auto / on / off |

### Exa

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `exa.enabled` | boolean | `true` | Exa 搜索工具的总体开关 |
| `exa.enableSearch` | boolean | `true` | 基础搜索、深度搜索、代码搜索、爬取 |
| `exa.enableResearcher` | boolean | `false` | AI 驱动深度研究任务 |
| `exa.enableWebsets` | boolean | `false` | Webset 管理及丰富工具 |

### SearXNG

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `searxng.endpoint` | string | `undefined` | 自托管搜索基础 URL |

---

## General / 无 UI

> 这些设置项没有 `ui` 属性，不会出现在设置面板中。

### 认证代理

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `lastChangelogVersion` | string | `undefined` | 上次看到的变更日志版本 |
| `auth.broker.url` | string | `undefined` | 认证代理服务器 URL |
| `auth.broker.token` | string | `undefined` | 认证代理令牌 |

### Shell

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `shellPath` | string | `undefined` | Shell 路径 |

### 扩展与模型

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `extensions` | array | `[]` | 已安装扩展列表 |
| `enabledModels` | array | `[]` | 已启用模型列表 |
| `disabledProviders` | array | `[]` | 已禁用提供商列表 |
| `disabledExtensions` | array | `[]` | 已禁用扩展列表 |
| `modelRoles` | record | `{}` | 模型角色映射 |
| `modelTags` | record | `{}` | 模型标签 |
| `modelProviderOrder` | array | `[]` | 提供商顺序 |
| `cycleOrder` | array | `["smol", "default", "slow"]` | 模型循环顺序 |

### 状态栏

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `statusLine.leftSegments` | array | `[]` | 状态栏左段配置 |
| `statusLine.rightSegments` | array | `[]` | 状态栏右段配置 |
| `statusLine.segmentOptions` | record | `{}` | 状态栏段选项 |

### TUI

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `tui.maxInlineImageColumns` | number | `100` | 内联图片最大宽度（列数） |
| `tui.maxInlineImageRows` | number | `20` | 内联图片最大高度（行数） |

### 显示

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `display.tabWidth` | number | `3` | 制表符宽度 |

### 重试

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `retry.enabled` | boolean | `true` | 启用 API 重试 |
| `retry.baseDelayMs` | number | `2000` | 重试基础延迟毫秒数 |
| `retry.fallbackChains` | record | `{}` | 回退链配置 |

### STT

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `stt.language` | string | `"en"` | 语音识别语言 |

### 压缩

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `compaction.reserveTokens` | number | `16384` | 压缩保留 token 数 |
| `compaction.keepRecentTokens` | number | `20000` | 压缩保留的最近 token 数 |
| `compaction.autoContinue` | boolean | `true` | 压缩后自动继续 |
| `compaction.remoteEndpoint` | string | `undefined` | 远程压缩端点 URL |

### 分支摘要

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `branchSummary.reserveTokens` | number | `16384` | 分支摘要保留 token 数 |

### 记忆（旧版本地管线）

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `memories.enabled` | boolean | `false` | （旧版）启用本地记忆管线 |
| `memories.maxRolloutsPerStartup` | number | `64` | 每次启动最大 rollout 数 |
| `memories.maxRolloutAgeDays` | number | `30` | rollout 最大存活天数 |
| `memories.minRolloutIdleHours` | number | `12` | 最小空闲小时数 |
| `memories.threadScanLimit` | number | `300` | 线程扫描限制 |
| `memories.maxRawMemoriesForGlobal` | number | `200` | 全局记忆最大原始记忆数 |
| `memories.stage1Concurrency` | number | `8` | 阶段 1 并发数 |
| `memories.stage1LeaseSeconds` | number | `120` | 阶段 1 租约秒数 |
| `memories.stage1RetryDelaySeconds` | number | `120` | 阶段 1 重试延迟秒数 |
| `memories.phase2LeaseSeconds` | number | `180` | 阶段 2 租约秒数 |
| `memories.phase2RetryDelaySeconds` | number | `180` | 阶段 2 重试延迟秒数 |
| `memories.phase2HeartbeatSeconds` | number | `30` | 阶段 2 心跳秒数 |
| `memories.rolloutPayloadPercent` | number | `0.7` | Rollout 载荷百分比 |
| `memories.phase1InputTokenLimit` | number | `4000` | 阶段 1 输入 token 限制 |
| `memories.fallbackTokenLimit` | number | `16000` | 回退 token 限制 |
| `memories.summaryInjectionTokenLimit` | number | `5000` | 摘要注入 token 限制 |

### Hindsight（无 UI）

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `hindsight.apiToken` | string | `undefined` | Hindsight API 令牌 |
| `hindsight.bankIdPrefix` | string | `undefined` | Hindsight 银行 ID 前缀 |
| `hindsight.bankMission` | string | `undefined` | 银行使命描述 |
| `hindsight.retainMission` | string | `undefined` | 保留使命描述 |
| `hindsight.recallBudget` | enum | `"mid"` | 召回预算：low / mid / high |
| `hindsight.recallMaxTokens` | number | `1024` | 召回最大 token 数 |
| `hindsight.recallContextTurns` | number | `1` | 召回上下文轮数 |
| `hindsight.recallMaxQueryChars` | number | `800` | 召回查询最大字符数 |
| `hindsight.recallTypes` | array | `["world", "experience"]` | 召回类型 |
| `hindsight.debug` | boolean | `false` | Hindsight 调试开关 |
| `hindsight.retainEveryNTurns` | number | `3` | 每 N 轮保留 |
| `hindsight.retainOverlapTurns` | number | `2` | 保留重叠轮数 |
| `hindsight.retainContext` | string | `"omp"` | 保留上下文 |
| `hindsight.mentalModelRefreshIntervalMs` | number | `300000` | 心智模型刷新间隔（5分钟） |
| `hindsight.mentalModelMaxRenderChars` | number | `16000` | 心智模型最大渲染字符数 |

### Bash 拦截器

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `bashInterceptor.patterns` | array | `(内置规则)` | 拦截规则列表 |

### Shell 最小化

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `shellMinimizer.settingsPath` | string | `undefined` | 自定义 settings 路径 |
| `shellMinimizer.only` | array | `[]` | 仅对这些命令启用最小化 |
| `shellMinimizer.except` | array | `[]` | 排除这些命令不最小化 |
| `shellMinimizer.maxCaptureBytes` | number | `4194304` | 最大捕获字节数（4 MB） |

### 异步

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `async.maxJobs` | number | `100` | 最大异步任务数 |
| `bash.autoBackground.thresholdMs` | number | `60000` | 自动后台阈值（毫秒） |

### 子代理

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `task.disabledAgents` | array | `[]` | 禁用的代理类型列表 |
| `task.agentModelOverrides` | record | `{}` | 代理模型覆盖映射 |

### Skills（无 UI）

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `skills.enabled` | boolean | `true` | 总启用开关 |
| `skills.enableCodexUser` | boolean | `true` | 启用 Codex 用户技能 |
| `skills.enableClaudeUser` | boolean | `true` | 启用 Claude 用户技能 |
| `skills.enableClaudeProject` | boolean | `true` | 启用 Claude 项目技能 |
| `skills.enablePiUser` | boolean | `true` | 启用 Pi 用户技能 |
| `skills.enablePiProject` | boolean | `true` | 启用 Pi 项目技能 |
| `skills.customDirectories` | array | `[]` | 自定义技能目录 |
| `skills.ignoredSkills` | array | `[]` | 忽略的技能列表 |
| `skills.includeSkills` | array | `[]` | 包含的技能列表 |

### SearXNG（无 UI）

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `searxng.token` | string | `undefined` | SearXNG 令牌 |
| `searxng.basicUsername` | string | `undefined` | 基本认证用户名 |
| `searxng.basicPassword` | string | `undefined` | 基本认证密码 |
| `searxng.categories` | string | `undefined` | 搜索分类 |
| `searxng.language` | string | `undefined` | 搜索语言 |

### 提交/变更日志

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `commit.mapReduceEnabled` | boolean | `true` | 提交 MapReduce 开关 |
| `commit.mapReduceMinFiles` | number | `4` | MapReduce 最少文件数 |
| `commit.mapReduceMaxFileTokens` | number | `50000` | MapReduce 每文件最大 token 数 |
| `commit.mapReduceTimeoutMs` | number | `120000` | MapReduce 超时毫秒数 |
| `commit.mapReduceMaxConcurrency` | number | `5` | MapReduce 最大并发数 |
| `commit.changelogMaxDiffChars` | number | `120000` | 变更日志最大差异字符数 |

### 思考预算

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `thinkingBudgets.minimal` | number | `1024` | 最低思考预算 token 数 |
| `thinkingBudgets.low` | number | `2048` | 低思考预算 token 数 |
| `thinkingBudgets.medium` | number | `8192` | 中思考预算 token 数 |
| `thinkingBudgets.high` | number | `16384` | 高思考预算 token 数 |
| `thinkingBudgets.xhigh` | number | `32768` | 极高思考预算 token 数 |

### 开发者

| 设置键 | 类型 | 默认值 | 描述 |
|---|---|---|---|
| `dev.autoqaPush.token` | string | `undefined` | Auto QA 推送令牌 |
| `dev.autoqa.consent` | enum | `"unset"` | 用户同意收集报告：unset / granted / denied |
