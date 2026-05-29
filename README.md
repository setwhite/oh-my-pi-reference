# Oh My Pi Settings Schema

从 `settings-schema.ts` 提取的 Oh My Pi 完整设置项参考，按 UI 标签页归类。

## 分类

| 分类 | 内容 |
|---|---|
| [Appearance](oh-my-pi-settings.md#appearance-外观) | 主题、图标、状态栏、图片渲染 |
| [Model](oh-my-pi-settings.md#model-模型) | 推理深度、采样参数、重试策略 |
| [Interaction](oh-my-pi-settings.md#interaction-交互) | 对话流、通知、语音输入、工具审批 |
| [Context](oh-my-pi-settings.md#context-上下文) | 上下文压缩、分支摘要、TTSR |
| [Memory](oh-my-pi-settings.md#memory-记忆) | 记忆后端（local / hindsight） |
| [Editing](oh-my-pi-settings.md#editing-编辑) | 编辑工具、Read 工具、LSP、Bash 拦截器 |
| [Tools](oh-my-pi-settings.md#tools-工具) | 工具审批策略、输出裁剪、Todo |
| [Tasks](oh-my-pi-settings.md#tasks-任务) | 子代理并发、审批、环境变量 |
| [Providers](oh-my-pi-settings.md#providers-提供商) | 模型提供商密钥与配置 |
| [General / 无 UI](oh-my-pi-settings.md#general--无-ui) | 调试开关、Secret 存储、更新频道等 |

## 字段说明

每条记录包含：

- **设置键** — JSON 路径（如 `edit.mode`）
- **类型** — `string` / `number` / `boolean` / `enum` / `record`
- **默认值** — 出厂值
- **描述** — 中文说明
