# Oh My Pi 参考知识库

[Oh My Pi](https://github.com/can1357/oh-my-pi) 的个人安装、配置与设置项参考。

## 目录结构

```
.
├── docs/
│   ├── installation.md   # 安装与配置指南
│   └── settings.md       # 完整设置项参考（按 UI 标签页归类）
├── config/
│   └── config.yml        # 个人配置备份
└── README.md
```

## 文档

- **[安装指南](docs/installation.md)** — OMP 安装步骤、config.yml 放置、模型路由配置、启动与登录
- **[设置参考](docs/settings.md)** — 从 `settings-schema.ts` 提取的全部设置项，含类型、默认值、中文说明，按 Appearance / Model / Interaction / Context / Memory / Editing / Tools / Tasks / Providers 等分类

## 配置

`config/config.yml` 是个人配置备份，可直接复制到 `~/.omp/agent/config.yml` 使用。

关键预设：
- **模型路由**：全部使用 OpenCode Go 订阅模型
- **审批模式**：`write`（写入操作需确认）
- **子任务隔离**：`rcopy` + `patch` 合并，最大并发 16
- **异步模式**：已启用
- **浏览器**：非 headless 模式

## 参考

- [Oh My Pi 官方仓库](https://github.com/can1357/oh-my-pi)

