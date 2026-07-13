# omp 配置项参考手册

> 所有配置项按 Settings 界面的 UI 分组排列，数据来源：`omp config list --json`（当前版本）。

---

## appearance — 外观

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `theme.dark` | *(主题名)* | 终端深色背景时使用的主题 |
| `theme.light` | `light` | 终端浅色背景时使用的主题 |
| `symbolPreset` | `nerd` | 图标/符号字体集：`unicode` / `nerd` / `ascii` |
| `colorBlindMode` | `false` | 色盲模式：diff 新增行用蓝色代替绿色 |
| `statusLine.preset` | `default` | 状态栏预设布局：`default` / `minimal` / `compact` / `full` / `nerd` / `ascii` / `custom` |
| `statusLine.separator` | `powerline-thin` | 状态栏段间分隔符样式：`powerline` / `powerline-thin` / `slash` / `pipe` / `block` / `none` / `ascii` |
| `statusLine.sessionAccent` | `false` | 用会话名颜色渲染编辑器边框和状态栏间隙 |
| `statusLine.transparent` | `true` | 状态栏使用终端默认背景（而非主题 `statusLineBg`），Powerline 端帽会被丢弃 |
| `statusLine.showHookStatus` | `true` | 在状态栏下方显示 Hook 状态消息 |
| `statusLine.compactThinkingLevel` | `false` | 将思考级别图标化显示在模型名旁，而非独立的 ` · <level>` 后缀 |
| `statusLine.leftSegments` | `[]` | 自定义状态栏左侧段（`custom` 预设时生效） |
| `statusLine.rightSegments` | `[]` | 自定义状态栏右侧段（`custom` 预设时生效） |
| `statusLine.segmentOptions` | `{}` | 自定义状态栏段选项 |
| `terminal.showImages` | `true` | 在终端内嵌渲染图片 |
| `terminal.showProgress` | `false` | agent 或上下文维护运行时，通过 OSC 9;4 协议显示不确定进度条 |
| `images.autoResize` | `true` | 将大图缩放到最大 2000×2000 以兼容模型 |
| `images.blockImages` | `false` | 禁止向 LLM 提供商发送图片 |
| `images.describeForTextModels` | `true` | 将图片附加给不支持视觉的模型时，先用视觉模型生成描述文本代替原图 |
| `tui.textSizing` | `false` | Markdown H1 标题用 Kitty OSC 66 协议渲染为 2 倍大小（仅 Kitty 终端有效） |
| `tui.renderMermaid` | `true` | 将 Mermaid 围栏代码块渲染为 ASCII 图表 |
| `tui.hyperlinks` | `auto` | 路径/URL 包裹为 OSC 8 超链接：`auto` 自动检测 / `off` / `always` |
| `tui.tight` | `true` | 紧凑布局：移除终端左右 1 字符内边距 |
| `tui.maxInlineImageColumns` | `100` | 内嵌图片最大列数 |
| `tui.maxInlineImageRows` | `20` | 内嵌图片最大行数 |
| `tui.maxInlineImages` | `8` | 单次最大内嵌图片数 |
| `display.shimmer` | `classic` | 等待/加载消息的动画风格 |
| `display.smoothStreaming` | `true` | 流式输出时平滑逐字显示 assistant 文本和工具输入 |
| `display.showTokenUsage` | `false` | 在每条 assistant 消息上显示该轮 token 用量 |
| `display.cacheMissMarker` | `true` | 当某轮请求 prompt 缓存失效时，在该轮上方显示分割线 |
| `showHardwareCursor` | `true` | 显示终端硬件光标（用于输入法支持） |
| `task.showResolvedModelBadge` | `true` | 在 task 组件状态栏显示每个子 agent 实际使用的模型 |

---

## context — 上下文与压缩

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `contextPromotion.enabled` | `false` | 上下文溢出时升级到更大上下文窗口的模型，而非压缩 |
| `compaction.enabled` | `true` | 上下文过大时自动压缩 |
| `compaction.midTurnEnabled` | `true` | 在安全的工具循环边界间检查阈值，支持中轮压缩 |
| `compaction.strategy` | `handoff` | 压缩策略：`context-full` / `handoff` / `shake` / `snapcompact` / `off` |
| `compaction.thresholdPercent` | `-1` | 百分比阈值；`-1` = 使用基于 reserve 的默认行为 |
| `compaction.thresholdTokens` | `-1` | 固定 token 阈值（>0 覆盖百分比） |
| `compaction.handoffSaveToDisk` | `true` | 将 handoff 文档保存为 markdown 文件 |
| `compaction.remoteEnabled` | `true` | 使用远程压缩端点代替本地摘要 |
| `compaction.remoteStreamingV2Enabled` | `true` | 对兼容的远程压缩模型使用 Responses 流式压缩 |
| `compaction.autoContinue` | `true` | 压缩后自动继续 agent 执行 |
| `compaction.idleEnabled` | `false` | 空闲时 token 超阈值自动压缩 |
| `compaction.idleThresholdTokens` | `200000` | 触发空闲压缩的 token 数 |
| `compaction.idleTimeoutSeconds` | `300` | 空闲等待秒数后压缩 |
| `compaction.supersedeReads` | `true` | 同一文件再次读取时剪除旧 read 结果 |
| `compaction.dropUseless` | `true` | 剪除上下文无用的工具结果（无匹配、超时等待等） |
| `snapcompact.systemPrompt` | `none` | 实验性：将系统提示渲染为 PNG 图像（仅视觉模型，省 token 但失去 prompt 缓存） |
| `snapcompact.toolResults` | `false` | 实验性：将大工具结果渲染为 PNG 图像（仅视觉模型） |
| `snapcompact.shape` | `auto` | snapcompact 文本帧形状；auto 根据当前模型自动选择 |
| `tools.format` | `auto` | 工具暴露方式：`auto` 自动选择 / `native` / `glm` / `hermes` / `kimi` / `xml` / `anthropic` / `deepseek` / `pi` / `qwen3` / `gemini` / `gemma` |
| `branchSummary.enabled` | `true` | 离开分支时提示生成摘要 |
| `ttsr.enabled` | `true` | 启用 TTSR（时间旅行流规则）：输出匹配规则时流内中断 |
| `ttsr.contextMode` | `discard` | TTSR 触发时对部分输出的处理：`discard` / `keep` |
| `ttsr.interruptMode` | `always` | 中断时机：`never` / `prose-only` / `tool-only` / `always` |
| `ttsr.repeatMode` | `once` | 规则重复方式：`once` 每会话一次 / `after-gap` 间隔后再次 |
| `ttsr.repeatGap` | `10` | 规则可再次触发前需经过的消息数 |
| `ttsr.builtinRules` | `true` | 加载内置默认规则（可由 `ttsr.disabledRules` 逐个禁用） |
| `ttsr.disabledRules` | `[]` | 完全忽略的规则名称列表 |
| `model.loopGuard.enabled` | `true` | 启用 Gemini/DeepSeek 模型的自动流循环检测 |
| `model.loopGuard.checkAssistantContent` | `true` | 对 assistant 文本消息也应用循环检测 |
| `model.loopGuard.toolCallReminder` | `true` | Gemini 推理流连续发出规划头但不调用工具时，中断并注入调用提醒 |
| `model.toolCallLoopGuard.enabled` | `true` | 检测跨轮次的连续相同工具调用并注入纠正引导 |
| `model.toolCallLoopGuard.threshold` | `5` | 触发纠正引导前连续相同工具调用的次数 |
| `model.toolCallLoopGuard.exemptTools` | `["job","irc"]` | 可连续重复而不触发跨轮循环检测的工具名列表 |

---

## files — 文件与编辑

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `edit.mode` | `hashline` | edit 工具模式：`apply_patch` / `hashline` / `patch` / `replace` |
| `edit.fuzzyMatch` | `true` | 允许空白差异的高置信度模糊匹配 |
| `edit.fuzzyThreshold` | `0.95` | 模糊匹配相似度阈值（0-1） |
| `edit.streamingAbort` | `false` | 流式 edit 调用时 patch 预览失败即中断 |
| `edit.blockAutoGenerated` | `true` | 禁止编辑自动生成的文件（protoc、sqlc、swagger 等） |
| `readLineNumbers` | `true` | 默认在 read 输出前添加行号 |
| `read.defaultLimit` | `300` | read 工具未指定限制时的默认行数 |
| `read.summarize.enabled` | `true` | read 未指定选择器时返回结构化代码摘要 |
| `read.summarize.prose` | `false` | 对 Markdown 和纯文本也返回结构化摘要 |
| `read.summarize.minBodyLines` | `4` | 多行体/字面量折叠前的最小行数 |
| `read.summarize.minCommentLines` | `6` | 多行块注释折叠前的最小行数 |
| `read.summarize.minTotalLines` | `100` | 总行数低于此值的文件直接原文返回 |
| `read.summarize.unfoldUntil` | `50` | BFS 展开折叠区域直到摘要至少达到此行数（0 = 仅最外层折叠） |
| `read.summarize.unfoldLimit` | `100` | BFS 展开时的硬性上限 |
| `read.toolResultPreview` | `true` | 在 transcript 中内嵌渲染 read 工具结果而非摘要行 |
| `lsp.enabled` | `true` | 启用 LSP 代码智能（定义、引用、诊断、重命名） |
| `lsp.lazy` | `true` | 首次使用时才启动语言服务器 |
| `lsp.formatOnWrite` | `true` | write 后自动格式化 |
| `lsp.diagnosticsOnWrite` | `true` | write 后返回 LSP 诊断 |
| `lsp.diagnosticsOnEdit` | `true` | edit 后返回 LSP 诊断 |
| `lsp.diagnosticsDeduplicate` | `true` | 抑制已显示过的编辑后诊断，仅展示新增/变化的 |

---

## interaction — 交互与行为

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `autoResume` | `false` | 自动恢复当前目录最近一次会话 |
| `power.sleepPrevention` | `idle` | macOS 会话期间防休眠级别：`off` / `idle` / `display` / `system` |
| `git.enabled` | `true` | 在 TUI 中显示 git 分支、状态和 PR 信息 |
| `steeringMode` | `one-at-a-time` | agent 工作时排队消息的处理方式：`all` / `one-at-a-time` |
| `followUpMode` | `one-at-a-time` | 一个 turn 完成后后续消息的排空方式 |
| `interruptMode` | `immediate` | 引导消息何时中断工具执行：`immediate` / `wait` |
| `loop.mode` | `prompt` | `/loop` 迭代之间在重新提交提示前做什么：`prompt` / `compact` / `reset` |
| `doubleEscapeAction` | `tree` | 编辑区为空时按两次 Esc：`branch` / `tree` / `none` |
| `treeFilterMode` | `default` | 打开会话树时的默认过滤器 |
| `autocompleteMaxVisible` | `5` | 自动补全下拉最多可见项数（3-20） |
| `emojiAutocomplete` | `true` | `:name:` 表情补全和文本表情符号扩展 |
| `paste.largeMenuThreshold` | `100` | 粘贴超过此行数时弹出菜单（代码块/XML标签/保存为文件），0 禁用 |
| `startup.quiet` | `true` | 跳过欢迎屏幕和启动状态消息 |
| `startup.showSplash` | `false` | 正常启动时显示完整动画启动画面 |
| `startup.setupWizard` | `true` | 每个 setup 版本显示新增的引导步骤 |
| `startup.checkUpdate` | `true` | 启动时检查 omp 更新 |
| `marketplace.autoUpdate` | `notify` | 启动时检查插件更新：`off` / `notify` / `auto` |
| `collapseChangelog` | `true` | 更新后显示精简 changelog |
| `magicKeywords.enabled` | `false` | 启用 ultrathink / orchestrate / workflowz 隐藏提示 |
| `magicKeywords.ultrathink` | `false` | 允许 ultrathink 请求最大推理并附加隐藏提示 |
| `magicKeywords.orchestrate` | `false` | 允许 orchestrate 附加多 agent 编排提示 |
| `magicKeywords.workflow` | `false` | 允许 workflowz 附加 eval 工作流提示 |
| `completion.notify` | `on` | agent 完成一个 turn 时通知 |
| `ask.enabled` | `true` | 启用 ask 工具（向用户提问） |
| `ask.timeout` | `0` | ask 提示超时秒数后自动选择推荐项（0 禁用） |
| `ask.notify` | `on` | ask 工具等待输入时通知 |
| `recap.enabled` | `false` | 终端空闲后生成 LLM 摘要回顾当前状态 |
| `recap.idleSeconds` | `240` | 空闲多少秒后显示回顾摘要 |
| `collab.relayUrl` | `wss://my.omp.sh` | `/collab` 中继地址 |
| `collab.webUrl` | *(空)* | `/collab` 浏览器 UI 地址 |
| `collab.displayName` | *(空)* | 协作中显示的名称（默认 OS 用户名） |
| `share.serverUrl` | `https://my.omp.sh/s` | `/share` 上传/查看服务地址 |
| `share.store` | `blob` | `/share` 上传目标：`blob` / `gist` |
| `share.redactSecrets` | `true` | 上传前对 `/share` 快照运行密钥混淆器 |
| `title.refreshOnReplan` | `true` | todo 重新规划后自动刷新生成的会话标题 |
| `stt.enabled` | `false` | 启用麦克风语音输入 |
| `stt.language` | `en` | 语音识别语言 |
| `stt.modelName` | `parakeet` | 本地设备端语音模型：`parakeet` / `fast` / `balanced` / `turbo` |
| `stt.submitTrigger` | `never` | 语音输入自动提交时机：`never` / Release (≥2词) / Release with complete sentence / When I Say Submit |
| `tools.approval` | `{}` | 按工具审批策略：`allow` / `prompt` / `deny` |
| `tools.approvalMode` | `yolo` | 默认审批行为：`always-ask` / `write` / `yolo` |
| `features.unexpectedStopDetection` | `false` | 用小模型检测 assistant 说会继续但无工具调用即停止的情况 |

---

## model — 模型与推理

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `advisor.enabled` | `false` | 启用第二个模型（advisor 角色）被动审查每个 turn 并注入建议 |
| `advisor.subagents` | `false` | 也对 task/eval 子 agent 启用 advisor |
| `advisor.syncBacklog` | `off` | advisor 落后 N 轮时暂停主 agent 最多 30 秒：`off` / `1` / `3` / `5` |
| `advisor.immuneTurns` | `3` | advisor 中断后，后续 N 轮不再中断 |
| `defaultThinkingLevel` | `max` | 推理深度：`minimal` / `low` / `medium` / `high` / `xhigh` / `max` / `auto` |
| `hideThinkingBlock` | `true` | 隐藏 assistant 回复中的 thinking 块 |
| `proseOnlyThinking` | `true` | 从 thinking 摘要中省略代码块，替换为省略号 |
| `omitThinking` | `false` | 指示上游提供商完全省略 thinking 摘要 |
| `textVerbosity` | `high` | OpenAI Responses 和 Codex 回复详细程度：`low` / `medium` / `high` |
| `tier.openai` | `none` | OpenAI / Codex 请求的处理优先级：`none` / `auto` / `default` / `flex` / `scale` / `priority` |
| `tier.anthropic` | `none` | Claude 请求的处理优先级；`priority` 在直接 Anthropic 模型上实现 fast mode |
| `tier.google` | `none` | Gemini（Google AI Studio + Vertex）请求的处理优先级 |
| `tier.subagent` | `inherit` | 子 agent 服务级别：`inherit` 跟随主 agent / 其他具体值 |
| `tier.advisor` | `none` | advisor 模型服务级别 |
| `inlineToolDescriptors` | `auto` | 在系统提示中渲染完整工具描述并从 provider schema 剥离描述文本；`auto` 仅对 Gemini 模型启用 |
| `includeModelInPrompt` | `true` | 在系统提示中暴露当前模型标识 |
| `includeWorkspaceTree` | `false` | 在系统提示中渲染工作区目录树（⚠ 会破坏跨会话 prompt 缓存） |
| `personality` | `none` | 系统提示个性块的沟通风格：`default` / `friendly` / `pragmatic` / `none` |
| `temperature` | `-1` | 采样温度（0=确定，1=创意，-1=提供商默认） |
| `topP` | `-1` | 核采样截断（0-1，-1=提供商默认） |
| `topK` | `-1` | Top-K 采样（-1=提供商默认） |
| `minP` | `-1` | 最小概率阈值（0-1，-1=提供商默认） |
| `presencePenalty` | `-1` | 引入已存在 token 的惩罚（-1=提供商默认） |
| `repetitionPenalty` | `-1` | 重复 token 的惩罚（-1=提供商默认） |
| `retry.enabled` | `true` | API 错误重试 |
| `retry.maxRetries` | `10` | 最大重试次数 |
| `retry.maxDelayMs` | `300000` | 重试最大等待毫秒（5 分钟） |
| `retry.modelFallback` | `true` | 允许重试时切换到配置的备用模型 |
| `retry.fallbackRevertPolicy` | `cooldown-expiry` | 备用后何时返回主模型：`cooldown-expiry` / `never` |
| `retry.fallbackChains` | `{}` | 按模型角色/选择器映射到有序 fallback 列表的 JSON 对象 |
| `providers.anthropic.serverSideFallback` | `false` | Claude 安全分类器拦截时服务端重试 Opus 4.8（Anthropic beta） |
| `thinkingBudgets.minimal` | `1024` | minimal 级别的 token 预算 |
| `thinkingBudgets.low` | `2048` | low 级别的 token 预算 |
| `thinkingBudgets.medium` | `8192` | medium 级别的 token 预算 |
| `thinkingBudgets.high` | `16384` | high 级别的 token 预算 |
| `thinkingBudgets.xhigh` | `32768` | xhigh 级别的 token 预算 |
| `thinkingBudgets.max` | `32768` | max 级别的 token 预算 |

---

## memory — 记忆

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `memory.backend` | `off` | 记忆后端：`off` / `local` / `hindsight` / `mnemopi` |
| `autolearn.enabled` | `false` | agent 停止后捕捉经验到记忆并创建/增强技能 |
| `autolearn.autoContinue` | `false` | 自动在停止时运行一次捕捉 turn |
| `mnemopi.scoping` | `per-project` | Mnemopi 作用域：`global` / `per-project` / `per-project-tagged` |
| `mnemopi.embeddingVariant` | `en` | 本地嵌入模型：`en` 英文增强 / `multilingual` 多语言 |
| `mnemopi.autoRecall` | `true` | 每会话首轮自动召回本地记忆 |
| `mnemopi.autoRetain` | `true` | 完成对话 turn 后自动存入 Mnemopi 记忆 |
| `mnemopi.polyphonicRecall` | `false` | 启用四声道召回（向量+图+事实+时序）融合 |
| `mnemopi.enhancedRecall` | `false` | 启用分层查询结果缓存 |
| `mnemopi.proactiveLinking` | `false` | 存入时主动链接相关实体和记忆 |
| `mnemopi.noEmbeddings` | `false` | 强制仅使用全文搜索（不用向量嵌入） |
| `mnemopi.llmMode` | `smol` | Mnemopi LLM：`none` / `smol` / `remote` |
| `mnemopi.llmBaseUrl` | *(空)* | remote 模式的 OpenAI 兼容 LLM 端点 |
| `mnemopi.llmModel` | *(空)* | remote 模式的 LLM 模型名 |
| `mnemopi.llmApiKey` | *(空)* | remote 模式的 LLM API 密钥 |
| `mnemopi.embeddingModel` | *(空)* | 显式指定嵌入模型 ID（覆盖 `embeddingVariant`） |
| `mnemopi.embeddingApiUrl` | *(空)* | OpenAI 兼容嵌入端点 |
| `mnemopi.embeddingApiKey` | *(空)* | 嵌入 API 密钥 |
| `mnemopi.dbPath` | *(空)* | SQLite 数据库路径（默认 agent memories 目录） |
| `mnemopi.bank` | *(空)* | 共享 bank 基础名 |
| `mnemopi.recallLimit` | `8` | 召回结果数量上限 |
| `mnemopi.recallContextTurns` | `3` | 召回上下文轮次 |
| `mnemopi.recallMaxQueryChars` | `4000` | 召回查询最大字符数 |
| `mnemopi.retainEveryNTurns` | `4` | 每 N 轮保留一次 |
| `mnemopi.injectionTokenLimit` | `5000` | 注入摘要 token 上限 |
| `hindsight.apiUrl` | `http://localhost:8888` | Hindsight 服务器 URL |
| `hindsight.scoping` | `per-project-tagged` | Hindsight 作用域 |
| `hindsight.autoRecall` | `true` | 每会话首轮自动召回 |
| `hindsight.autoRetain` | `true` | 每 N 轮和会话边界自动保留 |
| `hindsight.retainMode` | `full-session` | 保留模式：`full-session` / `last-turn` |
| `hindsight.retainEveryNTurns` | `3` | 每 N 轮触发保留 |
| `hindsight.retainOverlapTurns` | `2` | 保留重叠轮数 |
| `hindsight.retainContext` | `omp` | 保留上下文来源 |
| `hindsight.recallContextTurns` | `1` | 召回上下文轮数 |
| `hindsight.recallMaxTokens` | `1024` | 召回最大 token 数 |
| `hindsight.recallMaxQueryChars` | `800` | 召回查询最大字符数 |
| `hindsight.recallBudget` | `mid` | 召回预算级别 |
| `hindsight.recallTypes` | `["world","experience"]` | 召回类型列表 |
| `hindsight.mentalModelsEnabled` | `true` | 启动时读取心智模型到开发者指令 |
| `hindsight.mentalModelAutoSeed` | `true` | 会话启动时自动创建内置心智模型 |
| `hindsight.mentalModelMaxRenderChars` | `16000` | 心智模型渲染最大字符数 |
| `hindsight.mentalModelRefreshIntervalMs` | `300000` | 心智模型刷新间隔（5 分钟） |
| `memories.enabled` | `false` | 启用本地记忆摘要流水线 |
| `memories.maxRolloutsPerStartup` | `64` | 每次启动最大 rollout 数 |
| `memories.maxRolloutAgeDays` | `30` | rollout 最大保留天数 |
| `memories.minRolloutIdleHours` | `12` | rollout 最小空闲小时数 |
| `memories.threadScanLimit` | `300` | 线程扫描上限 |
| `memories.maxRawMemoriesForGlobal` | `200` | 全局原始记忆最大数 |
| `memories.stage1Concurrency` | `8` | 第一阶段并发数 |
| `memories.stage1LeaseSeconds` | `120` | 第一阶段租约秒数 |
| `memories.stage1RetryDelaySeconds` | `120` | 第一阶段重试延迟秒数 |
| `memories.phase2LeaseSeconds` | `180` | 第二阶段租约秒数 |
| `memories.phase2RetryDelaySeconds` | `180` | 第二阶段重试延迟秒数 |
| `memories.phase2HeartbeatSeconds` | `30` | 第二阶段心跳秒数 |
| `memories.rolloutPayloadPercent` | `0.7` | rollout 载荷百分比 |
| `memories.phase1InputTokenLimit` | `4000` | 第一阶段输入 token 上限 |
| `memories.fallbackTokenLimit` | `16000` | fallback token 上限 |
| `memories.summaryInjectionTokenLimit` | `5000` | 摘要注入 token 上限 |

---

## providers — 提供商与服务

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `secrets.enabled` | `false` | 发送前混淆密钥 |
| `providers.webSearch` | `auto` | web_search 首选提供商 |
| `providers.webSearchExclude` | `[]` | web_search 永不使用的提供商列表（即使是 fallback） |
| `providers.webSearchGeminiModel` | *(空)* | Gemini Google Search grounding 模型 ID（默认 gemini-2.5-flash） |
| `providers.image` | `auto` | 图像生成首选提供商 |
| `providers.fetch` | `auto` | URL fetch/read 后端优先级 |
| `providers.tinyModel` | `online` | 会话标题模型：`online` 或本地设备端模型 |
| `providers.tinyModelDevice` | `default` | ONNX 执行后端：`default` / `gpu` / `cpu` / `metal` / `webgpu` / `cuda` / `dml` |
| `providers.tinyModelDtype` | `default` | ONNX 量化精度 |
| `providers.autoThinkingModel` | `online` | `auto` 思考级别的难度分类器模型 |
| `providers.memoryModel` | `online` | Mnemopi 事实提取/整合 LLM |
| `providers.unexpectedStopModel` | `online` | unexpected-stop 检测分类器模型 |
| `providers.kimiApiFormat` | `anthropic` | Kimi Code API 格式：`openai` / `anthropic` |
| `providers.openaiWebsockets` | `auto` | OpenAI Codex WebSocket 策略 |
| `providers.openrouterVariant` | `default` | OpenRouter 路由变体后缀 |
| `providers.fireworksTier` | `standard` | Fireworks 服务路径：`standard` / `priority` |
| `providers.antigravityEndpoint` | `auto` | google-antigravity 提供商端点路由策略 |
| `providers.tts` | `auto` | TTS 工具后端：本地 Kokoro-82M 或 xAI Grok Voice |
| `providers.streamFirstEventTimeoutSeconds` | `-1` | 模型流首个事件的等待秒数（-1 = 提供商默认，0 = 禁用） |
| `providers.streamIdleTimeoutSeconds` | `-1` | 模型流事件间静默超时秒数（-1 = 提供商默认，0 = 禁用） |
| `providers.maxInFlightRequests` | `{}` | 按提供商 ID 限制最大并发 LLM 请求数 |
| `providers.ollama-cloud.maxConcurrency` | `3` | Ollama Cloud 每进程最大并发子 agent 数（0 禁用限制） |
| `provider.appendOnlyContext` | `auto` | 缓存系统提示+工具定义并保持追加式消息日志以最大化前缀缓存命中 |
| `exa.enabled` | `true` | Exa 搜索工具总开关 |
| `exa.enableSearch` | `true` | Exa 基本/深度/代码搜索和爬取 |
| `exa.searchDelayMs` | `1000` | Exa 请求最小间隔毫秒 |
| `exa.enableResearcher` | `true` | Exa 深度研究工具 |
| `exa.enableWebsets` | `true` | Exa webset 管理工具 |
| `searxng.endpoint` | *(空)* | 自托管 SearXNG 实例 URL |
| `searxng.token` | *(空)* | SearXNG 令牌 |
| `searxng.basicUsername` | *(空)* | SearXNG Basic Auth 用户名 |
| `searxng.basicPassword` | *(空)* | SearXNG Basic Auth 密码 |
| `searxng.categories` | *(空)* | SearXNG 搜索类别 |
| `searxng.language` | *(空)* | SearXNG 搜索语言 |
| `speech.enabled` | `false` | 流式输出时朗读 assistant 回复 |
| `speech.mode` | `assistant` | 朗读内容：`all` / `assistant` / `yield` |
| `speech.enhanced` | `false` | 用 tiny/smol 模型将输出改写为自然口语化文本后再合成语音 |
| `speech.voice` | `af_heart` | 朗读语音（Kokoro） |
| `tts.localModel` | `kokoro` | 本地 TTS 引擎模型（Kokoro-82M） |
| `tts.localVoice` | `af_heart` | 本地 TTS 语音（美/英，女/男） |
| `codexResets.autoRedeem` | `unset` | Codex 周限制阻塞时自动使用保存的 reset：`unset` / `yes` / `no` |
| `codexResets.minBlockedMinutes` | `60` | 仅在距离自然重置至少 N 分钟时才自动 redeem |
| `codexResets.keepCredits` | `0` | 保留至少 N 个 saved reset 不自动使用 |

---

## shell — Shell 与 Eval

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `bash.enabled` | `true` | 启用 bash 工具 |
| `bash.autoBackground.enabled` | `true` | 自动将长时间命令转为后台运行 |
| `bash.autoBackground.thresholdMs` | `60000` | 自动后台阈值毫秒 |
| `bashInterceptor.enabled` | `false` | 拦截有专用工具替代的 shell 命令 |
| `bashInterceptor.patterns` | *(预设)* | 拦截规则列表：匹配正则 → 提示专用工具 |
| `shellMinimizer.enabled` | `true` | 压缩冗长 shell 输出（git、npm、cargo 等） |
| `shellMinimizer.sourceOutlineLevel` | `default` | 源文件 cat/read 的 outline 模式：`default` / `aggressive` |
| `shellMinimizer.maxCaptureBytes` | `4194304` | shell 输出的最大捕获字节数 |
| `shellMinimizer.except` | `[]` | 不压缩的命令/工具列表 |
| `shellMinimizer.only` | `[]` | 仅压缩的命令/工具列表 |
| `eval.py` | `true` | 允许 eval 工具调度 Python 到 IPython 内核 |
| `eval.js` | `true` | 允许 eval 工具调度 JavaScript 到进程内运行时 |
| `eval.rb` | `false` | 允许 eval 工具调度 Ruby |
| `eval.jl` | `false` | 允许 eval 工具调度 Julia |
| `python.kernelMode` | `session` | Python 内核模式：`session`（持久）/ `per-call`（每次新建） |
| `python.interpreter` | *(空)* | 指定 Python 解释器路径（空=自动检测） |
| `ruby.interpreter` | *(空)* | 指定 Ruby 解释器路径（空=自动检测） |
| `julia.interpreter` | *(空)* | 指定 Julia 解释器路径（空=自动检测） |

---

## tasks — 任务与子 Agent

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `plan.enabled` | `true` | 启用 plan 模式（只读探索和规划） |
| `plan.defaultOnStartup` | `false` | 每个新会话启动时自动进入 plan 模式 |
| `goal.enabled` | `true` | 启用每会话 goal 模式 |
| `goal.statusInFooter` | `true` | 在状态栏 goal 指示器旁显示 token 预算 |
| `goal.continuationModes` | `["interactive"]` | goal 可自动在轮次间继续的运行模式 |
| `task.isolation.mode` | `rcopy` | 子 agent 隔离后端：`none` / `auto` / `apfs` / `btrfs` / `overlayfs` / `projfs` / `rcopy` |
| `task.isolation.merge` | `patch` | 隔离任务变更集成方式：`patch` / `branch` |
| `task.isolation.commits` | `generic` | 嵌套仓库提交信息风格：`generic` / `ai` |
| `task.eager` | `default` | 推动委托给子 agent 的强度 |
| `task.batch` | `true` | 批量模式：一次调用带 `{ agent, context, tasks[] }` |
| `task.maxConcurrency` | `32` | 最大并发子 agent 数 |
| `task.enableLsp` | `true` | 允许子 agent 使用 lsp 工具 |
| `task.maxRecursionDepth` | `2` | 子 agent 可递归生子的最大层数 |
| `task.maxRuntimeMs` | `0` | 每子 agent 硬性超时毫秒（0=禁用），防御 provider 侧流挂起 |
| `task.agentIdleTtlMs` | `420000` | 空闲子 agent 驻留内存时间（毫秒，7 分钟）；0 = 永不过期 |
| `task.softRequestBudget` | `200` | 每子 agent 软请求预算（超过则注入收尾提示）；0 禁用 |
| `task.softRequestBudgetNotice` | `true` | 子 agent 超软预算时注入收尾引导消息 |
| `task.agentModelOverrides` | `{}` | 按 agent 类型覆盖模型 |
| `task.disabledAgents` | `[]` | 禁用的 agent 类型列表 |
| `skills.enabled` | `true` | 启用 skills 系统 |
| `skills.enableSkillCommands` | `true` | 将 skills 注册为 `/skill:name` 命令 |
| `skills.enablePiUser` | `true` | 加载 `~/.omp/agent/skills` |
| `skills.enablePiProject` | `true` | 加载 `<cwd>/.omp/skills` |
| `skills.enableClaudeUser` | `true` | 加载 `~/.claude/skills` |
| `skills.enableClaudeProject` | `true` | 加载 `<cwd>/.claude/skills` |
| `skills.enableCodexUser` | `true` | 加载 `~/.codex/skills` |
| `skills.enableAgentsUser` | `true` | 加载 `~/.omp/agent/skills`（agent 专用） |
| `skills.enableAgentsProject` | `true` | 加载 `<cwd>/.omp/agent/skills`（agent 专用） |
| `skills.customDirectories` | `[]` | 额外加载的自定义 skills 目录 |
| `skills.ignoredSkills` | `[]` | 忽略的 skill 名称列表 |
| `skills.includeSkills` | `[]` | 仅加载的 skill 白名单 |
| `commands.enableClaudeUser` | `false` | 加载 `~/.claude/commands/` |
| `commands.enableClaudeProject` | `false` | 加载 `.claude/commands/` |
| `commands.enableOpencodeUser` | `false` | 加载 `~/.config/opencode/commands/` |
| `commands.enableOpencodeProject` | `false` | 加载 `.opencode/commands/` |
| `todo.eager` | `default` | 自动创建 todo 列表的强度 |
| `tasks.todoClearDelay` | `60` | 已完成/放弃的 todo 在组件中延迟显示秒数 |
| `worktree.base` | *(空)* | agent 管理的 worktree 根目录（默认 `~/.omp/wt`） |

---

## tools — 工具配置

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `tools.artifactSpillThreshold` | `50` | 工具输出超过此 KB 数时溢出到 artifact |
| `tools.artifactHeadBytes` | `20` | 溢出时保留的行首 KB 数 |
| `tools.artifactTailBytes` | `20` | 溢出时保留的行尾 KB 数 |
| `tools.outputMaxColumns` | `768` | 流式输出每行字节上限 |
| `tools.artifactTailLines` | `500` | 溢出时保留的最大 tail 行数 |
| `tools.intentTracing` | `true` | 要求 agent 在每次工具调用前描述意图 |
| `tools.abortOnFabricatedResult` | `true` | 带内工具调用时模型开始幻觉工具结果即停止 |
| `tools.maxTimeout` | `0` | agent 可为工具设置的最大超时秒数（0=无限制） |
| `tools.discoveryMode` | `auto` | 工具隐藏策略：`auto` / `off` / `mcp-only` / `all` |
| `tools.essentialOverride` | `[]` | 覆盖默认内置工具集（默认：read、bash、edit、write、glob、eval） |
| `todo.enabled` | `true` | 启用 todo 工具 |
| `todo.reminders` | `true` | 提醒 agent 在停止前完成 todo |
| `todo.reminders.max` | `3` | 最大提醒次数 |
| `grep.enabled` | `true` | 启用 grep 工具 |
| `grep.contextBefore` | `1` | 每个匹配前的上下文行数 |
| `grep.contextAfter` | `3` | 每个匹配后的上下文行数 |
| `glob.enabled` | `true` | 启用 glob 工具 |
| `astGrep.enabled` | `true` | 启用 ast_grep 工具 |
| `astEdit.enabled` | `true` | 启用 ast_edit 工具 |
| `debug.enabled` | `true` | 启用 debug 工具 |
| `inspect_image.enabled` | `false` | 启用 inspect_image 工具，委托视觉模型理解图片 |
| `fetch.enabled` | `true` | 允许 read 工具获取 URL |
| `github.enabled` | `true` | 启用 github 工具 |
| `github.cache.enabled` | `true` | 缓存 issue/PR 视图输出 |
| `github.cache.softTtlSec` | `300` | 软 TTL：5 分钟内直接返回缓存 |
| `github.cache.hardTtlSec` | `604800` | 硬 TTL：7 天后丢弃缓存 |
| `web_search.enabled` | `true` | 启用 web_search 工具 |
| `browser.enabled` | `true` | 启用 browser 工具（Chromium/Puppeteer） |
| `browser.headless` | `true` | 无头模式启动浏览器 |
| `browser.screenshotDir` | `~/Desktop` | 截图保存目录 |
| `browser.cmux` | `true` | cmux 可用时使用 WKWebView 表面进行浏览器自动化 |
| `async.enabled` | `true` | 启用异步 bash 和后台任务 |
| `async.maxJobs` | `100` | 最大后台任务数 |
| `async.pollWaitDuration` | `smart` | poll 工具等待时长：`smart` 自适应或固定值 |
| `irc.timeoutMs` | `120000` | IRC wait/send await 默认超时毫秒 |
| `mcp.enableProjectConfig` | `true` | 加载项目根目录的 `.mcp.json` / `mcp.json` |
| `mcp.discoveryMode` | `false` | 默认隐藏 MCP 工具，通过工具发现工具暴露 |
| `mcp.discoveryDefaultServers` | `[]` | discovery 模式下始终保持可见的 MCP 服务器列表 |
| `mcp.notifications` | `false` | 将 MCP 资源更新注入 agent 对话 |
| `mcp.notificationDebounceMs` | `500` | MCP 资源更新注入前的防抖窗口（毫秒） |
| `checkpoint.enabled` | `false` | 启用 checkpoint/rewind 工具 |
| `vault.enabled` | `false` | 启用 vault:// Obsidian 保险库读写 |
| `speechgen.enabled` | `false` | 启用 TTS 语音合成工具 |

---

## commit — 提交生成

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `commit.mapReduceEnabled` | `true` | 启用 map-reduce 提交信息生成 |
| `commit.mapReduceMinFiles` | `4` | 触发 map-reduce 的最小文件数 |
| `commit.mapReduceMaxFileTokens` | `50000` | 单文件最大 token 数 |
| `commit.mapReduceTimeoutMs` | `120000` | map-reduce 超时毫秒 |
| `commit.mapReduceMaxConcurrency` | `5` | map-reduce 最大并发数 |
| `commit.changelogMaxDiffChars` | `120000` | changelog 最大 diff 字符数 |

---

## gc — 自动清理

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `gc.blobs` | `true` | 清理过期 blob |
| `gc.archive` | `true` | 清理过期归档 |
| `gc.wal` | `true` | 清理 WAL 文件 |
| `gc.coldArchiveAfterDays` | `30` | 多少天后视为冷归档 |
| `gc.retainNewestGlobal` | `20` | 全局保留的最新会话数 |
| `gc.retainNewestPerCwd` | `10` | 每工作目录保留的最新会话数 |

---

## dev — 开发者选项

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `dev.autoqa` | `false` | 为所有 agent 启用自动工具问题报告 |
| `dev.autoqaPush.endpoint` | `https://qa.omp.sh/v1/grievances` | Auto QA JSON 报告接收地址 |
| `dev.autoqa.consent` | `unset` | Auto QA 同意状态 |

→ [返回索引](../README.md)
