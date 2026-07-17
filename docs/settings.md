# omp 配置项参考手册

> 数据来源：`omp config list --json`（当前版本）。各分组对应 Settings 界面标签页。

---

## appearance — 外观

### 主题

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `theme.dark` | `dark-monokai` | 终端暗色背景时使用的主题 |
| `theme.light` | `light` | 终端亮色背景时使用的主题 |
| `symbolPreset` | `nerd` | 图标和符号的字符集（Unicode、Nerd Font 或 ASCII） |
| `colorBlindMode` | `false` | 差异添加使用蓝色而非绿色 |

### 状态栏

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `statusLine.preset` | `default` | 预构建的状态行配置 |
| `statusLine.separator` | `powerline-thin` | 各段之间的分隔符样式 |
| `statusLine.sessionAccent` | `false` | 使用会话名称颜色作为编辑器边框和状态行间隙颜色 |
| `statusLine.transparent` | `true` | 使用终端默认背景作为状态行背景，替代主题的 `statusLineBg`。Powerline 端帽被丢弃，因需要对比填充连接终端 |
| `statusLine.compactThinkingLevel` | `false` | 将思考级别显示为模型名称上的单个图标，而非单独的 `· <level>` 后缀 |
| `statusLine.showHookStatus` | `true` | 在状态行下方显示钩子状态消息 |
| `statusLine.leftSegments` | `[]` | — |
| `statusLine.rightSegments` | `[]` | — |
| `statusLine.segmentOptions` | `{}` | — |

### 终端与图片

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `terminal.showImages` | `true` | 在终端内联渲染图片 |
| `images.autoResize` | `true` | 将大图片调整为最大2000x2000以提升模型兼容性 |
| `images.blockImages` | `false` | 阻止将图片发送给 LLM 提供商 |
| `images.describeForTextModels` | `true` | 当图片附加到无视觉支持的模型时，保存到 local:// 并从有视觉能力的模型注入描述，避免丢弃 |
| `terminal.showProgress` | `false` | 在代理或上下文维护运行时，发出 OSC 9;4 不确定进度 |
| `showHardwareCursor` | `true` | 显示终端光标以支持 IME |

### TUI 渲染

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `tui.maxInlineImageColumns` | `100` | — |
| `tui.maxInlineImageRows` | `20` | — |
| `tui.maxInlineImages` | `8` | — |
| `tui.textSizing` | `false` | 使用 Kitty 的 OSC 66 文本大小协议，将 Markdown H1 标题放大2倍。仅Kitty终端有效，其他忽略。默认关闭 |
| `tui.renderMermaid` | `true` | 将 Mermaid 围栏代码块渲染为 ASCII 图表 |
| `tui.hyperlinks` | `auto` | 将路径和URL包裹在OSC 8超链接中实现终端原生点击打开（auto: 自动检测支持；off: 从不；always: 无条件） |
| `tui.tight` | `true` | 移除终端输出左右各1字符的水平内边距 |
| `tui.scrollbackRebuild` | `false` | 当块的最终形式替换其实时预览时，擦除并重放终端回滚。关闭时（默认），旧预览副本保留在历史，最终内容追加在下方 |
| `tui.imeSafeCursor` | `false` | 将提示底部边框移至单独行，以防止 macOS IME 预编辑位移 |
| `task.showResolvedModelBadge` | `true` | 在任务小部件状态行中显示每个子代理使用的实际模型 ID |

### 显示

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `display.shimmer` | `classic` | 工作/加载消息的动画样式 |
| `display.smoothStreaming` | `true` | 在数据块到达时平滑显示助手文本和流式工具输入 |
| `display.showTokenUsage` | `false` | 在助手消息中显示每轮 token 用量 |
| `display.cacheMissMarker` | `true` | 在提示缓存未命中的助手轮次上方显示分隔线 |
| `display.collapseCompacted` | `true` | 在实时转录中，将压缩前历史折叠到摘要分隔线后面；禁用则保留完整历史，每个压缩点显示分隔线 |

---

## interaction — 交互与行为

### 通用

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `autoResume` | `false` | 自动恢复当前目录中最新的会话 |
| `power.sleepPrevention` | `idle` | 在活动会话期间阻止 macOS 睡眠。每个级别累加——包含所有较低级别的标志 |
| `git.enabled` | `true` | 在 TUI 中显示 Git 分支、状态和 PR 信息，并监视仓库元数据 |
| `steeringMode` | `one-at-a-time` | 代理工作时如何处理排队消息 |
| `followUpMode` | `one-at-a-time` | 如何在一轮完成后处理后续消息 |
| `interruptMode` | `immediate` | steering 消息何时中断工具执行 |
| `loop.mode` | `prompt` | 在 /loop 迭代之间、重新提交提示之前发生什么 |
| `doubleEscapeAction` | `tree` | 当编辑器空白时按两次 Escape 的操作 |
| `treeFilterMode` | `default` | 打开会话树时的默认过滤模式 |
| `autocompleteMaxVisible` | `5` | 自动补全下拉列表中最多可见项数（3-20） |
| `emojiAutocomplete` | `true` | 从 `:name:` 简码建议 emoji 并展开文本表情符号如 `:D` 或 `:-)` |
| `paste.largeMenuThreshold` | `100` | 当粘贴行数达到此值时，提供菜单包裹为代码块、XML 标签或保存到文件。0 禁用菜单（大粘贴仍折叠为 [Paste] 标记） |
| `title.refreshOnReplan` | `true` | 在 todo init 重新规划后刷新生成的会话标题，除非标题已由用户设置 |

### 启动

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `startup.quiet` | `true` | 跳过欢迎屏幕和启动状态消息 |
| `startup.showSplash` | `false` | 正常交互启动时显示完整动画设置启动画面，无需重新运行设置。静默启动仍会抑制 |
| `startup.setupWizard` | `true` | 每个设置版本显示一次新添加的引导步骤 |
| `startup.checkUpdate` | `true` | 启动时检查 omp 更新 |
| `marketplace.autoUpdate` | `notify` | 启动时检查插件更新 |
| `collapseChangelog` | `true` | 更新后显示精简更新日志 |
| `magicKeywords.enabled` | `false` | 启用独立 ultrathink、orchestrate 和 workflowz 关键字的隐藏通知 |
| `magicKeywords.ultrathink` | `false` | 让独立 ultrathink 请求最大自动思考并附加其隐藏通知 |
| `magicKeywords.orchestrate` | `false` | 让独立 orchestrate 附加其隐藏的多智能体编排通知 |
| `magicKeywords.workflow` | `false` | 让独立 workflowz 附加其隐藏的评估工作流通知 |

### 通知与询问

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `completion.notify` | `on` | 代理完成一轮时通知 |
| `ask.timeout` | `0` | 在指定秒数后自动选择推荐的 ask 选项（0 禁用） |
| `ask.notify` | `on` | ask 工具等待输入时通知 |
| `recap.enabled` | `false` | 终端闲置后生成 LLM 状态简要总结 |
| `recap.idleSeconds` | `240` | 闲置后等待显示总结的秒数 |
| `ask.enabled` | `true` | 启用 ask 工具进行交互式用户提问 |
| `features.unexpectedStopDetection` | `false` | 使用小型模型检测助手表示将继续但未进行工具调用就停止的情况；自动提示其继续。 |

### 协作与分享

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `collab.relayUrl` | `wss://my.omp.sh` | /collab 使用的中继 (wss://host[:port]) |
| `collab.webUrl` | *(空)* | /collab 链接使用的浏览器 UI；空则继承自 collab.relayUrl；显式 http:// 仅限 localhost |
| `collab.displayName` | *(空)* | 向其他协作参与者显示的名称（默认：操作系统用户名） |
| `share.serverUrl` | `https://my.omp.sh/s` | /share 使用的分享查看器/上传基础地址（加密 blob 上传 + 查看器；链接为 <base>/<id>#<key>） |
| `share.store` | `blob` | /share 上传加密会话 blob 的位置 |
| `share.redactSecrets` | `true` | 上传前对 /share 快照运行机密混淆器（使用 secrets.* 配置） |

### 语音

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `stt.enabled` | `false` | 启用通过麦克风的语音转文本输入 |
| `stt.language` | `en` | — |
| `stt.modelName` | `parakeet` | 本地设备端语音模型。Parakeet TDT v3 (sherpa-onnx) 是默认的 SOTA；Whisper base/small/large-v3-turbo 层级（transformers.js）在大小和多语言覆盖之间权衡。首次使用时下载。 |
| `stt.submitTrigger` | `never` | 选择语音听写自动提交的时机：从不、释放（2+ 词）、释放并完成句子、或当我说提交。 |

---

## model — 模型与推理

### Advisor

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `advisor.enabled` | `false` | 配对第二个模型（指定为“advisor”角色），被动审核每一轮并注入备注。 |
| `advisor.subagents` | `false` | 同时为生成的 task/eval 子代理启用 advisor。 |
| `advisor.syncBacklog` | `off` | 如果 advisor 落后指定轮数，暂停主代理最多 30 秒。关闭则禁用追赶延迟。 |
| `advisor.immuneTurns` | `3` | 在 advisor 的关切或阻塞中断后，将后续关切/阻塞以非中断方式路由指定的主代理轮数。 |

### Prewalk

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `prewalk.enabled` | `false` | 从活动模型开始，然后在计划提示的待办列表存在后的第一次编辑/写入时切换到快速/便宜模型（默认为“smol”角色）——强模型规划、提交待办并开始实施后移交。可通过 --prewalk / --no-prewalk 在每个会话中覆盖。 |

### 推理与思考

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `defaultThinkingLevel` | `max` | 支持思考模型的推理深度 |
| `hideThinkingBlock` | `true` | 隐藏助手响应中的思考块 |
| `proseOnlyThinking` | `true` | 从思考摘要中省略代码块并用省略号替换 |
| `omitThinking` | `false` | 指示上游提供商完全从响应中省略思考摘要（在支持的情况下） |
| `inlineToolDescriptors` | `auto` | 在系统提示中渲染完整工具描述符，并从提供商工具模式中去除顶层/嵌套描述，以便描述文本仅发送一次。对 Gemini 模型自动启用，其他情况禁用。 |
| `includeModelInPrompt` | `true` | 在系统提示中显示活动模型标识符，以便代理知道当前是哪个模型 |
| `includeWorkspaceTree` | `false` | 在系统提示中渲染工作区目录树。警告：当文件修改时，这可能会破坏跨会话的提示缓存。 |
| `personality` | `none` | 注入到系统提示个性块中的沟通风格 |

### 循环检测

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `model.loopGuard.enabled` | `true` | 启用模型推理和散文的自动流循环检测 |
| `model.loopGuard.checkAssistantContent` | `true` | 除思考日志外，也对助手散文消息应用循环保护 |
| `model.loopGuard.toolCallReminder` | `true` | 当 Gemini 推理流连续发出多个规划头而未调用工具时，中断并注入提醒以发出工具调用（需要 Loop Guard） |
| `model.toolCallLoopGuard.enabled` | `true` | 检测跨轮次的连续相同工具调用并注入纠正引导 |
| `model.toolCallLoopGuard.threshold` | `5` | 注入纠正引导前所需的连续相同工具调用次数 |
| `model.toolCallLoopGuard.exemptTools` | `["hub"]` | 可连续重复而不触发跨轮循环保护的工具名称 |

### 采样参数

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `temperature` | `-1` | 采样温度（0 = 确定性，1 = 创造性，-1 = 提供商默认） |
| `topP` | `-1` | 核采样截止值（0-1，-1 = 提供商默认） |
| `topK` | `-1` | 从 top-K 令牌中采样（-1 = 提供商默认） |
| `minP` | `-1` | 最小概率阈值（0-1，-1 = 提供商默认） |
| `presencePenalty` | `-1` | 引入已存在令牌的惩罚（-1 = 提供商默认） |
| `repetitionPenalty` | `-1` | 重复令牌的惩罚（-1 = 提供商默认） |
| `textVerbosity` | `medium` | OpenAI Responses 和 Codex 响应详细程度（低、中、高） |

### 服务层级

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `tier.openai` | `none` | 用于OpenAI / OpenAI-Codex请求及经OpenRouter路由的OpenAI系列模型的处理层级（无则不发送）。作为`service_tier`发送。 |
| `tier.anthropic` | `none` | 用于Claude请求的处理层级。`priority`在受支持的直连Anthropic模型上实现快速模式（`speed: "fast"`）；在Bedrock/Vertex Claude及通过OpenRouter时忽略。 |
| `tier.google` | `none` | 用于Gemini（Google AI Studio + Vertex）请求及经OpenRouter路由的Google系列模型的处理层级（无则不发送）。作为顶层`serviceTier`字段发送。 |
| `tier.subagent` | `inherit` | 衍生任务/评估子代理的服务层级。Inherit = 匹配主代理的实时各系列层级（tracks /fast）；选择一个值应用于子代理模型所属系列。 |
| `tier.advisor` | `none` | 顾问模型的服务层级。None = 标准处理；Inherit = 匹配主代理的实时各系列层级；选择一个值应用于顾问模型所属系列。 |

### 重试与回退

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `retry.enabled` | `true` | — |
| `retry.maxRetries` | `10` | API错误时的最大重试次数 |
| `retry.baseDelayMs` | `500` | — |
| `retry.maxDelayMs` | `300000` | 重试之间的最大等待时间（毫秒）。当提供方要求等待超过此时间且凭据或模型回退均无效时，请求快速失败而非休眠（例如Anthropic的3小时速率限制窗口）。 |
| `retry.modelFallback` | `true` | 允许重试恢复时切换到配置的回退模型 |
| `retry.fallbackChains` | `{}` | JSON对象，将模型角色、模型选择器（"provider/model-id"）或提供者通配符（"provider/*"）映射到有序回退选择器，例如{"default":["openai/gpt-4o-mini"],"google-antigravity/*":["google/*","google-vertex/*"]}。面向模型的键在模型/提供者激活时应用，无论角色；"provider/*"条目保留失败模型ID并交换提供者；ID前缀通配符（"openrouter/google/*"）重新前缀失败模型裸ID（google-antigravity/gemini-x -> openrouter/google/gemini-x），作为键时仅匹配该提供者在前缀下的ID。 |
| `retry.fallbackRevertPolicy` | `cooldown-expiry` | 回退后何时恢复主模型 |

### 思考预算

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `thinkingBudgets.minimal` | `1024` | — |
| `thinkingBudgets.low` | `2048` | — |
| `thinkingBudgets.medium` | `8192` | — |
| `thinkingBudgets.high` | `16384` | — |
| `thinkingBudgets.xhigh` | `32768` | — |
| `thinkingBudgets.max` | `32768` | — |

---

## context — 上下文与压缩

### 压缩

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `contextPromotion.enabled` | `false` | 上下文溢出时升级到更大上下文模型而非压缩 |
| `compaction.enabled` | `true` | 自动压缩过大的上下文 |
| `compaction.midTurnEnabled` | `true` | 在下次提供者请求前于安全的回合中工具循环边界检查阈值 |
| `compaction.strategy` | `handoff` | 选择原地全上下文维护、自动交接、surgical shake（丢弃重型内容）、snapcompact（归档历史为密集图像）或禁用自动维护（off） |
| `compaction.thresholdPercent` | `-1` | 上下文维护的百分比阈值；设置为Default使用基于预留的旧行为 |
| `compaction.thresholdTokens` | `-1` | 上下文维护的固定token限制；设置后覆盖百分比 |
| `compaction.handoffSaveToDisk` | `true` | 将生成的交接文档保存为markdown文件，用于自动交接流程 |
| `compaction.remoteEnabled` | `true` | 使用远程压缩端点（如可用）代替本地摘要 |
| `compaction.remoteStreamingV2Enabled` | `true` | 对兼容的远程压缩模型使用Responses流式压缩 |
| `compaction.reserveTokens` | *(空)* | — |
| `compaction.keepRecentTokens` | `20000` | — |
| `compaction.autoContinue` | `true` | — |
| `compaction.remoteEndpoint` | *(空)* | — |
| `compaction.v2RetainedMessageBudget` | `64000` | — |
| `compaction.idleEnabled` | `false` | 空闲时压缩上下文（token数超过阈值） |
| `compaction.idleThresholdTokens` | `200000` | 触发空闲压缩的token数阈值 |
| `compaction.idleTimeoutSeconds` | `300` | 空闲后等待压缩的秒数 |
| `compaction.supersedeReads` | `true` | 再次读取相同文件时裁剪旧读取结果（缓存感知，每轮运行） |
| `compaction.dropUseless` | `true` | 消费后裁剪标记为上下文无用的工具结果（无匹配、等待超时）（缓存感知） |
| `branchSummary.enabled` | `true` | 离开分支时提示总结 |
| `branchSummary.reserveTokens` | `16384` | — |

### Snapcompact

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `snapcompact.systemPrompt` | `none` | 实验性：将选定的系统提示文本渲染为密集PNG图像并附加到首条用户消息（仅视觉模型）。节省token；丢失所成像文本的提示缓存。 |
| `snapcompact.toolResults` | `false` | 实验性：将大型历史工具结果渲染为密集PNG图像而非文本（仅视觉模型）。节省累积的读取/搜索输出的token。 |
| `snapcompact.shape` | `auto` | snapcompact打印文本的框架形状（压缩存档和内联成像）。Auto选择适合当前模型的形状。 |

### 工具格式

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `tools.format` | `auto` | 控制工具如何暴露给模型。Auto使用提供者原生工具调用，除非所选模型标记为不支持，则回退到GLM自有方言。Native强制使用提供者原生工具；其他值强制使用指定的自有方言。在会话开始时应用。 |

### TTSR 流规则

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `ttsr.enabled` | `true` | 当输出匹配规则模式时中断代理中间流（Time-Traveling Stream Rules） |
| `ttsr.contextMode` | `discard` | TTSR触发时如何处理部分输出 |
| `ttsr.interruptMode` | `always` | 何时中断中间流 vs 完成后注入警告 |
| `ttsr.repeatMode` | `once` | 规则重复方式：每会话一次或在消息间隔后 |
| `ttsr.repeatGap` | `10` | 规则再次触发前的消息数 |
| `ttsr.builtinRules` | `true` | 加载代理自带的默认规则（可单独通过ttsr.disabledRules覆盖） |
| `ttsr.disabledRules` | `[]` | 完全忽略的规则名称（适用于捆绑默认规则和自定义规则） |

---

## files — 文件与编辑

### 编辑

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `edit.mode` | `hashline` | 选择编辑工具变体（replace, patch, hashline, apply_patch） |
| `edit.fuzzyMatch` | `true` | 接受针对空白差异的高置信度模糊匹配 |
| `edit.fuzzyThreshold` | `0.95` | 接受模糊匹配的相似度阈值（0-1） |
| `edit.streamingAbort` | `false` | 补丁预览失败时中止流式编辑工具调用 |
| `edit.blockAutoGenerated` | `true` | 阻止编辑看似自动生成的文件（protoc, sqlc, swagger等） |
| `edit.enforceSeenLines` | `true` | 拒绝基于先前读取/搜索未完整显示的行进行的编辑 |

### 读取

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `read.defaultLimit` | `300` | 代理调用read时未指定限制时的默认返回行数 |
| `read.summarize.enabled` | `true` | 当read被调用而未指定显式选择器时返回结构代码摘要 |
| `read.summarize.prose` | `false` | 对Markdown和纯文本读取返回结构摘要 |
| `read.summarize.minBodyLines` | `4` | 读取摘要折叠多行正文或字面量的最小长度 |
| `read.summarize.minCommentLines` | `6` | 读取摘要折叠多行块注释的最小长度 |
| `read.summarize.minTotalLines` | `100` | 总行数较少的文件逐字读取而非结构摘要 |
| `read.summarize.unfoldUntil` | `50` | BFS展开可折叠跨度，直到摘要至少达到此可见行数。0仅保留最外层省略。 |
| `read.summarize.unfoldLimit` | `100` | BFS展开时摘要大小的硬上限。若展开后行数超过此值则跳过该跨度（保持折叠），继续展开剩余跨度。 |
| `read.toolResultPreview` | `true` | 在转录中内联显示读取工具结果，而非摘要行 |

### LSP

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `lsp.enabled` | `true` | 启用 lsp 工具以获取代码智能（定义、引用、诊断、重命名） |
| `lsp.lazy` | `true` | 在首次使用时启动语言服务器（lsp 工具或编辑匹配文件类型），而非在会话启动时 |
| `lsp.formatOnWrite` | `true` | 写入后使用 LSP 自动格式化代码文件 |
| `lsp.diagnosticsOnWrite` | `true` | 写入代码文件后返回 LSP 诊断 |
| `lsp.diagnosticsOnEdit` | `true` | 编辑代码文件后返回 LSP 诊断 |
| `lsp.diagnosticsDeduplicate` | `true` | 抑制文件已显示的编辑后 LSP 诊断；仅显示新增或变更的诊断 |

---

## memory — 记忆

### 记忆流水线

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `memories.enabled` | `false` | — |
| `memories.maxRolloutsPerStartup` | `64` | — |
| `memories.maxRolloutAgeDays` | `30` | — |
| `memories.minRolloutIdleHours` | `12` | — |
| `memories.threadScanLimit` | `300` | — |
| `memories.maxRawMemoriesForGlobal` | `200` | — |
| `memories.stage1Concurrency` | `8` | — |
| `memories.stage1LeaseSeconds` | `120` | — |
| `memories.stage1RetryDelaySeconds` | `120` | — |
| `memories.phase2LeaseSeconds` | `180` | — |
| `memories.phase2RetryDelaySeconds` | `180` | — |
| `memories.phase2HeartbeatSeconds` | `30` | — |
| `memories.rolloutPayloadPercent` | `0.7` | — |
| `memories.phase1InputTokenLimit` | `4000` | — |
| `memories.fallbackTokenLimit` | `16000` | — |
| `memories.summaryInjectionTokenLimit` | `5000` | — |

### 通用

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `memory.backend` | `off` | 关闭、本地摘要流水线、Mnemopi SQLite 或 Hindsight 远程记忆 |
| `autolearn.enabled` | `false` | 代理停止后，提示其将经验捕获至记忆并创建/增强隔离的托管技能 |
| `autolearn.autoContinue` | `false` | 启用时，在停止时自动运行一次私有捕获轮次（消耗额外 token）。禁用时，仅保留常驻的自动学习指导。 |
| `autolearn.minToolCalls` | `5` | — |

### Mnemopi

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `mnemopi.dbPath` | *(空)* | 可选的 SQLite 数据库路径。默认为代理记忆目录。 |
| `mnemopi.bank` | *(空)* | 可选的共享银行基名称。按项目模式从中派生出项目本地银行。 |
| `mnemopi.scoping` | `per-project` | global = 一个共享银行；per-project = 每个 cwd 的隔离银行；per-project-tagged = 项目本地写入加上全局召回可见性 |
| `mnemopi.embeddingVariant` | `en` | 本地嵌入模型系列。en = 更强的英文模型；multilingual = 跨语言模型。更改此选项将在下次启动时重建现有记忆嵌入。 |
| `mnemopi.autoRecall` | `true` | 将本地记忆召回至每个会话的首轮 |
| `mnemopi.autoRetain` | `true` | 将完成的对话轮次保留至本地 Mnemopi 记忆 |
| `mnemopi.polyphonicRecall` | `false` | 启用四路召回（向量、图、事实、时间），以 reciprocal rank fusion 融合 |
| `mnemopi.enhancedRecall` | `false` | 启用分层查询结果缓存，用于重复和相似的召回查询 |
| `mnemopi.proactiveLinking` | `false` | 在存储新记忆时将其摄入情景图，并将其链接到相关实体和记忆 |
| `mnemopi.noEmbeddings` | `false` | 强制使用确定性 FTS-only 召回，而非向量嵌入 |
| `mnemopi.embeddingModel` | *(空)* | 高级：显式嵌入模型 ID，覆盖变量。留空以使用 mnemopi.embeddingVariant。 |
| `mnemopi.embeddingApiUrl` | *(空)* | 可选的 OpenAI 兼容嵌入端点，传递给 Mnemopi |
| `mnemopi.embeddingApiKey` | *(空)* | 可选的嵌入 API 密钥，传递给 Mnemopi |
| `mnemopi.llmMode` | `smol` | 不使用 LLM、在线小模型（来自 /models 的 TINY 角色，否则 @smol）或远程 OpenAI 兼容端点 |
| `mnemopi.llmBaseUrl` | *(空)* | Mnemopi 远程模式的可选 OpenAI 兼容 LLM 端点 |
| `mnemopi.llmApiKey` | *(空)* | Mnemopi 远程模式的可选 LLM API 密钥 |
| `mnemopi.llmModel` | *(空)* | Mnemopi 远程模式的可选 LLM 模型名称 |
| `mnemopi.retainEveryNTurns` | `4` | — |
| `mnemopi.recallLimit` | `8` | — |
| `mnemopi.recallContextTurns` | `3` | — |
| `mnemopi.recallMaxQueryChars` | `4000` | — |
| `mnemopi.injectionTokenLimit` | `5000` | — |
| `mnemopi.debug` | `false` | — |

### Hindsight

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `hindsight.apiUrl` | `http://localhost:8888` | Hindsight 服务器 URL（云端或自托管） |
| `hindsight.apiToken` | *(空)* | — |
| `hindsight.bankId` | *(空)* | 记忆银行标识符（默认：项目名称） |
| `hindsight.bankIdPrefix` | *(空)* | — |
| `hindsight.scoping` | `per-project-tagged` | global = 一个共享银行；per-project = 每个 cwd 的隔离银行；per-project-tagged = 带有项目标签的共享银行，以便全局和项目记忆在召回时合并 |
| `hindsight.bankMission` | *(空)* | — |
| `hindsight.retainMission` | *(空)* | — |
| `hindsight.autoRecall` | `true` | 在每个会话的首轮召回记忆 |
| `hindsight.autoRetain` | `true` | 每 N 轮和会话边界处保留转录 |
| `hindsight.retainMode` | `full-session` | full-session = 每个会话更新插入一个文档；last-turn = 分块 |
| `hindsight.retainEveryNTurns` | `3` | — |
| `hindsight.retainOverlapTurns` | `2` | — |
| `hindsight.retainContext` | `omp` | — |
| `hindsight.recallBudget` | `mid` | — |
| `hindsight.recallMaxTokens` | `1024` | — |
| `hindsight.recallContextTurns` | `1` | — |
| `hindsight.recallMaxQueryChars` | `800` | — |
| `hindsight.recallTypes` | `["world", "experience"]` | — |
| `hindsight.debug` | `false` | — |
| `hindsight.mentalModelsEnabled` | `true` | 在启动时将精选的反思摘要（心智模型）读入开发者指令。加载银行上的现有模型——不写入。与 hindsight.mentalModelAutoSeed 搭配以自动创建内置种子集。 |
| `hindsight.mentalModelAutoSeed` | `true` | 在会话开始时，创建银行上尚未存在的任何内置心智模型（项目约定、项目决策、用户偏好）。 |
| `hindsight.mentalModelRefreshIntervalMs` | `300000` | — |
| `hindsight.mentalModelMaxRenderChars` | `16000` | — |

---

## providers — 提供商与服务

### 通用

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `providers.maxInFlightRequests` | `{}` | 每个提供者 ID（例如 "openai" 或 "anthropic"）的最大并发 LLM 请求数，与此配置根的本地 OMP 进程共享。省略的提供者无限制。 |
| `providers.anthropic.serverSideFallback` | `false` | 当 Claude Fable 5 / Mythos 5 请求被 Anthropic 的安全分类器阻止时，在 Claude Opus 4.8 服务器端重试（Anthropic `server-side-fallback-2026-06-01` beta）。选择加入——禁用则对每个请求保留原始行为。 |
| `secrets.enabled` | `false` | 在发送给 AI 提供者之前混淆密钥 |
| `provider.appendOnlyContext` | `auto` | 缓存系统提示+工具规范并保持追加消息日志，以便提供者前缀缓存（DeepSeek、Xiaomi/SGLang、Anthropic）以最大命中率工作。自动为已知前缀缓存提供者启用。 |

### 搜索与图像

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `providers.webSearch` | `auto` | web_search 工具的首选提供者 |
| `providers.webSearchExclude` | `[]` | web_search 永远不应使用的提供者，即使是作为后备 |
| `providers.webSearchGeminiModel` | *(空)* | 用于 Gemini Google Search grounding 的模型 ID。默认为 gemini-2.5-flash。 |
| `providers.image` | `auto` | 图像生成的首选提供者 |
| `providers.fetch` | `auto` | fetch/read URL工具的读取后端优先级。 |

### TTS 与语音

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `providers.tts` | `auto` | tts 工具的后端：本地设备端神经 TTS（Kokoro-82M）或 xAI Grok Voice |
| `tts.localModel` | `kokoro` | 本地 TTS 后端使用的设备端神经 TTS 模型（Kokoro-82M） |
| `tts.localVoice` | `af_heart` | 本地 TTS 后端使用的 Kokoro 语音（美式/英式，女声/男声） |
| `speech.enabled` | `false` | 在流式传输时通过扬声器朗读助手的输出 |
| `speech.mode` | `assistant` | 朗读内容：all = 助手消息 + 思考过程；assistant = 仅消息；yield = 仅在轮次结束时输出最终消息 |
| `speech.enhanced` | `false` | 使用tiny/smol模型在合成前将助手输出重写为自然口语散文（描述代码，丢弃链接和markdown）。失败时回退到机械清理。 |
| `speech.voice` | `af_heart` | 朗读助手输出时使用的Kokoro语音。 |

### 模型路由

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `providers.ollama-cloud.maxConcurrency` | `3` | 每个进程的最大并发 Ollama Cloud 子代理运行数；0 禁用提供者特定限制 |
| `providers.antigravityEndpoint` | `auto` | google-antigravity 提供者的端点路由策略（聊天、搜索、图像、发现） |
| `providers.fireworksTier` | `standard` | Fireworks 请求的服务路径。Priority 发送 `service_tier: "priority"` 以在高峰流量期间获得更高可靠性，但价格更高；Standard 省略它。Fast（`-fast`）模型忽略此选项——Fast 有自己的服务路径。 |
| `providers.tinyModel` | `online` | 会话标题模型：默认在线（来自/models的TINY角色，否则@smol）或本地设备上的模型。 |
| `providers.tinyModelDevice` | `default` | 本地tiny模型（标题+记忆）的ONNX执行提供者。默认使用仅CPU推理。PI_TINY_DEVICE环境变量可覆盖此设置。 |
| `providers.tinyModelDtype` | `default` | 本地tiny模型的ONNX量化/精度。默认使用各模型自带的dtype（q4）；较低精度更快，较高精度更忠实。PI_TINY_DTYPE环境变量可覆盖此设置。 |
| `providers.memoryModel` | `online` | 用于事实提取+整合的Mnemopi LLM：默认在线（来自/models的TINY角色，否则smol/remote）或本地设备上的模型。 |
| `providers.autoThinkingModel` | `online` | 用于`auto`思考级别的难度分类器：默认在线（来自/models的TINY角色，否则smol）或本地设备上的模型。 |
| `providers.unexpectedStopModel` | `online` | 用于意外停止检测的分类器：默认在线（来自/models的TINY角色，否则smol）或本地设备上的模型。 |
| `providers.kimiApiFormat` | `anthropic` | Kimi Code提供者的API格式。 |
| `providers.openaiWebsockets` | `auto` | OpenAI Codex模型的Websocket策略（auto使用模型默认，on强制开启，off禁用）。 |
| `providers.streamFirstEventTimeoutSeconds` | `-1` | 等待第一个模型流事件的秒数；-1使用提供者/环境默认值，0禁用看门狗。 |
| `providers.streamIdleTimeoutSeconds` | `-1` | 模型流在事件之间保持静默的秒数；-1使用提供者/环境默认值，0禁用看门狗。 |
| `providers.openrouterVariant` | `default` | 附加到OpenRouter模型ID的默认路由变体后缀（当选择器已命名变体时被覆盖）。 |

### Codex Resets

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `codexResets.autoRedeem` | `unset` | 当主动账户的Codex每周限制阻止回合且无其他可用账户时，运行保守的已保存重置检查。unset在花费第一个符合条件的重置前询问，yes直接花费符合条件的重置，no完全禁用检查。需要启用重试。 |
| `codexResets.minBlockedMinutes` | `60` | 仅当自然每周重置至少还有这么多分钟时才自动兑换（不要为了节省短暂等待而花费约30天的信用）。 |
| `codexResets.keepCredits` | `0` | 自动花费时保留至少这么多已保存重置（0=最后一个信用可能自动花费）。 |

### Exa

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `exa.enabled` | `true` | 所有Exa搜索工具的主开关。 |
| `exa.enableSearch` | `true` | 启用Exa基础搜索、深度搜索、代码搜索和爬取工具。 |
| `exa.searchDelayMs` | `1000` | Exa网络搜索请求之间的最小延迟（毫秒）；设为0禁用节流。 |
| `exa.enableResearcher` | `true` | 启用Exa研究员工具进行AI驱动的深度研究。 |
| `exa.enableWebsets` | `true` | 启用Exa网络集管理和丰富工具。 |

### SearXNG

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `searxng.endpoint` | *(空)* | 用于网络搜索的自托管SearXNG实例的基础URL。 |
| `searxng.token` | *(空)* | — |
| `searxng.basicUsername` | *(空)* | — |
| `searxng.basicPassword` | *(空)* | — |
| `searxng.categories` | *(空)* | — |
| `searxng.language` | *(空)* | — |

---

## shell — Shell 与 Eval

### Bash

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `bash.enabled` | `true` | 启用bash工具以执行shell命令。 |
| `bash.autoBackground.enabled` | `true` | 自动将长时间运行的bash命令后台化并稍后返回结果。 |
| `bash.autoBackground.thresholdMs` | `60000` | — |

### 拦截与压缩

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `bashInterceptor.enabled` | `false` | 阻止具有专用工具的shell命令。 |
| `bashInterceptor.patterns` | *(预设)* | — |
| `shellMinimizer.enabled` | `true` | 压缩冗长的shell输出（git、npm、cargo等）后再返回给代理。 |
| `shellMinimizer.settingsPath` | *(空)* | — |
| `shellMinimizer.only` | `[]` | — |
| `shellMinimizer.except` | `[]` | — |
| `shellMinimizer.maxCaptureBytes` | `4194304` | — |
| `shellMinimizer.sourceOutlineLevel` | `default` | 用于cat/read源文件的源轮廓模式：default或aggressive。 |
| `shellMinimizer.legacyFilters` | *(空)* | — |

### Eval 语言

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `eval.py` | `true` | 允许eval工具将Python单元分派给IPython内核。 |
| `eval.js` | `true` | 允许eval工具将JavaScript单元分派给进程内运行时。 |
| `eval.rb` | `false` | 允许eval工具将Ruby单元分派给持久化Ruby内核。 |
| `eval.jl` | `false` | 允许eval工具将Julia单元分派给持久化Julia内核。 |
| `python.kernelMode` | `session` | 在eval调用之间保持IPython内核活跃，或每次都重新启动。 |
| `python.interpreter` | *(空)* | 可选的特定Python可执行文件路径。设置后跳过自动Python运行时发现。 |
| `ruby.interpreter` | *(空)* | 可选的特定Ruby可执行文件路径。设置后跳过自动Ruby运行时发现。 |
| `julia.interpreter` | *(空)* | 可选的特定Julia可执行文件路径。设置后跳过自动Julia运行时发现。 |

---

## tasks — 任务与子 Agent

### Todo

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `todo.enabled` | `true` | 启用待办事项工具进行任务跟踪。 |
| `todo.reminders` | `true` | 提醒代理在停止前完成待办事项。 |
| `todo.remindersMax` | `3` | 放弃前待办事项提醒的最大次数。 |
| `todo.eager` | `default` | 在第一条消息后推送自动待办列表创建的强度。 |

### Plan & Goal

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `plan.enabled` | `true` | 启用计划模式以在执行前进行只读探索和规划。 |
| `plan.defaultOnStartup` | `false` | 在每个新会话开始时自动进入计划模式。 |
| `goal.enabled` | `true` | 启用每会话目标模式和隐藏的目标工具。 |
| `goal.statusInFooter` | `true` | 在状态行中显示目标指示器旁边的令牌预算。 |
| `goal.continuationModes` | `["interactive"]` | 运行模式，其中活动目标可以在回合之间自动继续。 |

### Task 隔离与并发

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `task.isolation.mode` | `rcopy` | 子代理的隔离后端。"auto"让原生PAL选择最佳可用后端（CoW感知文件系统，然后overlayfs/ProjFS，最后是git worktree/递归复制回退）。 |
| `task.isolation.merge` | `patch` | 隔离任务更改如何集成（补丁应用或分支合并）。 |
| `task.isolation.commits` | `generic` | 嵌套仓库更改的提交消息风格（通用或AI生成）。 |
| `worktree.base` | *(空)* | 代理管理工作树的基础目录——任务隔离副本、`github` PR检出和`omp worktree`清理都在此进行。未设置时使用~/.omp/wt。必须是绝对路径或~相对路径；相对路径被忽略。OMP_WORKTREE_DIR环境变量可覆盖此设置。 |
| `task.eager` | `default` | 控制将工作委托给subagents的强度 |
| `task.batch` | `true` | 将task工具切换为批处理模式：一次调用携带{agent, context, tasks[]}，每项一个subagent（隔离），共享context前置。async.enabled=true时每个spawn独立后台运行（正常idle/parked生命周期）；否则阻塞等待合并结果。禁用恢复为平面单spawn模式。 |
| `task.maxConcurrency` | `32` | 最大并发运行subagents数 |
| `task.enableLsp` | `true` | 允许task tool产生的subagents使用lsp tool。默认关闭以保持subagents轻量；当LSP感知的委托值得额外token时启用。 |
| `task.maxRecursionDepth` | `2` | subagents递归产生自身subagents的最大深度 |
| `task.maxRuntimeMs` | `0` | 每个subagent的硬壁钟时间限制（毫秒）。0禁用。深度防御提供商侧流挂起超出推理层watchdog的情况；触发正常subagent中止（原因'timed out'）。 |
| `task.agentIdleTtlMs` | `420000` | 空闲subagent内存驻留时间（毫秒），到期后存储到磁盘。存储的agent在收到消息或恢复时自动复活。0保持空闲agent活跃直到退出。 |
| `task.softRequestBudget` | `200` | 每个subagent的软请求预算（每次运行的assistant请求数）。超出时注入收尾引导通知（参见task.softRequestBudgetNotice）；达到1.5倍预算时强制停止运行，agent必须提交部分结果。0禁用此防护。内置的scout/sonic agents使用更低的固有预算。 |
| `task.softRequestBudgetNotice` | `true` | 当subagent超出软请求预算时注入一次引导通知，要求它在1.5倍强制让出停止前收尾。 |
| `task.disabledAgents` | `[]` | — |
| `task.agentModelOverrides` | `{}` | — |
| `task.agentPrewalk` | `{}` | — |
| `task.prewalk` | `false` | 为内置通用`task` subagent启用prewalk：它从解析的模型开始，规划并开始实施，然后在首次编辑/写入时移交给'smol'角色。Per-agent覆盖设置（task.agentPrewalk，在/agents中用P切换）以及用户agent的`prewalk`前置元数据无论此开关如何均生效。 |

### Skills

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `skills.enabled` | `true` | — |
| `skills.enableSkillCommands` | `true` | 将技能注册为/skill:name命令 |
| `skills.enableCodexUser` | `true` | — |
| `skills.enableClaudeUser` | `true` | — |
| `skills.enableClaudeProject` | `true` | — |
| `skills.enablePiUser` | `true` | — |
| `skills.enablePiProject` | `true` | — |
| `skills.enableAgentsUser` | `true` | — |
| `skills.enableAgentsProject` | `true` | — |
| `skills.customDirectories` | `[]` | — |
| `skills.ignoredSkills` | `[]` | — |
| `skills.includeSkills` | `[]` | — |

### Commands

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `commands.enableClaudeUser` | `false` | 从~/.claude/commands/加载命令 |
| `commands.enableClaudeProject` | `false` | 从.claude/commands/加载命令 |
| `commands.enableOpencodeUser` | `false` | 从~/.config/opencode/commands/加载命令 |
| `commands.enableOpencodeProject` | `false` | 从.opencode/commands/加载命令 |

---

## tools — 工具配置

### 通用

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `tools.artifactSpillThreshold` | `50` | 工具输出超过此大小时保存为artifact；内联保留尾部 |
| `tools.artifactTailBytes` | `20` | 输出溢出到artifact时内联保留的尾部内容字节数 |
| `tools.artifactHeadBytes` | `20` | 输出溢出到artifact时内联保留的头部内容字节数（中间省略）。0禁用——仅保留尾部 |
| `tools.outputMaxColumns` | `768` | 流式工具输出（bash, python, js eval）和`read`的每行字节上限。超出此宽度的行被省略号截断；剩余字节直至换行符被丢弃。0禁用 |
| `tools.artifactTailLines` | `500` | 输出溢出到artifact时内联保留的最大尾部行数 |
| `tools.intentTracing` | `true` | 要求agent在每次工具调用前描述意图 |
| `tools.abortOnFabricatedResult` | `true` | 对于带内工具调用，当模型在回合中开始幻觉一个工具结果时立即停止。禁用则让模型完成生成并丢弃伪造的续文。 |
| `tools.maxTimeout` | `0` | agent可以为任何工具设置的最大超时秒数（0=无限制） |
| `tools.xdev` | `false` | 将不常用的（可发现的）工具挂载到xd://设备URL下，通过read/write驱动，而不是每次请求都发送其schema。禁用则将所有启用的工具暴露在顶层。 |

### 审批

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `tools.approval` | `{}` | 每个工具的审批策略。设置为'allow'自动批准，'prompt'要求确认，'deny'阻止。所有审批模式下均遵循覆盖设置。 |
| `tools.approvalMode` | `yolo` | 工具调用的默认审批行为。'Always ask'仅自动批准只读工具。'Write'自动批准读和工作区写工具。'Yolo'自动批准所有层级；用户策略仍可能提示或阻止。 |

### 文件与搜索

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `glob.enabled` | `true` | 启用glob tool进行基于glob模式的文件查找 |
| `grep.enabled` | `true` | 启用grep tool进行正则表达式内容搜索 |
| `grep.contextBefore` | `1` | 每个grep匹配前的上下文行数 |
| `grep.contextAfter` | `3` | 每个grep匹配后的上下文行数 |
| `fetch.enabled` | `true` | 允许read tool获取和处理URL |

### 代码智能

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `astGrep.enabled` | `true` | 启用ast_grep tool进行结构化的AST搜索 |
| `astEdit.enabled` | `true` | 启用ast_edit tool进行结构化的AST重写 |
| `debug.enabled` | `true` | 启用debug tool进行基于DAP的调试 |

### 浏览器与网络

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `inspect_image.enabled` | `false` | 启用inspect_image tool，将图像理解委托给具备视觉能力的模型 |
| `web_search.enabled` | `true` | 启用web_search tool获取实时网络结果 |
| `browser.enabled` | `true` | 启用browser tool进行脚本化Chromium自动化（puppeteer） |
| `browser.headless` | `true` | 以无头模式启动浏览器（禁用时显示浏览器UI） |
| `browser.cmux` | `true` | 在cmux socket可用时使用cmux WKWebView表面进行浏览器自动化。设置PI_BROWSER_CMUX=0或1覆盖。 |
| `browser.screenshotDir` | `~/Desktop` | 截图保存目录。未设置时截图保存到临时文件。支持~。示例：~/Downloads, ~/Desktop, /sdcard/Download (Android) |

### GitHub

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `github.enabled` | `true` | 启用github tool（基于op的分发：仓库, issue, pull request, diff, 搜索, checkout, push和Actions watch工作流） |
| `github.cache.enabled` | `true` | 在~/.omp/cache/github-cache.db中缓存渲染后的issue/PR视图输出，以便重复读取免费 |
| `github.cache.softTtlSec` | `300` | 在此窗口内（秒），直接返回缓存的issue/PR视图行（默认5分钟） |
| `github.cache.hardTtlSec` | `604800` | 超过软TTL后返回缓存行并在后台刷新；超过硬TTL后丢弃（秒；默认7天） |

### 异步与作业

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `async.enabled` | `true` | 启用异步bash命令和后台任务执行 |
| `async.maxJobs` | `100` | — |
| `async.pollWaitDuration` | `smart` | `hub` wait在返回当前状态前监视后台作业的时长。固定值每次等待相同长度。`smart`自适应：从5秒开始，每次连续等待后增加（最长5分钟），约一分钟无等待后重置为5秒。 |
| `irc.timeoutMs` | `120000` | hub消息等待（和send await:true）的默认超时毫秒数；0禁用超时 |

### MCP

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `mcp.enableProjectConfig` | `true` | 从项目根加载.mcp.json/mcp.json |
| `mcp.notifications` | `false` | 向代理对话注入MCP资源更新 |
| `mcp.notificationDebounceMs` | `500` | MCP资源更新注入对话前的防抖时间（毫秒） |

### 其他

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `speechgen.enabled` | `false` | 启用tts tool进行设备端（Kokoro）或xAI Grok Voice语音文件合成 |
| `checkpoint.enabled` | `false` | 启用checkpoint和rewind tools进行上下文检查点记录 |
| `vault.enabled` | `false` | 启用vault://内部URL通过Obsidian CLI读取编辑Obsidian vault内容。禁用时拒绝解析vault://，并从系统提示中省略vault://条目 |

---

## commit — 提交生成

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `commit.mapReduceEnabled` | `true` | — |
| `commit.mapReduceMinFiles` | `4` | — |
| `commit.mapReduceMaxFileTokens` | `50000` | — |
| `commit.mapReduceTimeoutMs` | `120000` | — |
| `commit.mapReduceMaxConcurrency` | `5` | — |
| `commit.changelogMaxDiffChars` | `120000` | — |

---

## gc — 自动清理

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `gc.blobs` | `true` | — |
| `gc.archive` | `true` | — |
| `gc.wal` | `true` | — |
| `gc.coldArchiveAfterDays` | `30` | — |
| `gc.retainNewestGlobal` | `20` | — |
| `gc.retainNewestPerCwd` | `10` | — |

---

## dev — 开发者选项

| 参数 | 默认值 | 含义 |
|------|--------|------|
| `dev.autoqa` | `false` | 为所有代理启用自动工具问题报告（report_tool_issue） |
| `dev.autoqaPush.endpoint` | `https://qa.omp.sh/v1/grievan…` | 接收Auto QA JSON报告的完整URL（默认https://qa.omp.sh/v1/grievances） |
| `dev.autoqaPush.token` | *(空)* | — |
| `dev.autoqaConsent` | `unset` | — |