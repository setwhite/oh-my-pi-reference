# Oh My Pi 参考知识库

[Oh My Pi](https://github.com/can1357/oh-my-pi) 的个人安装、配置与设置项参考。

## 目录结构

```
.
├── docs/
│   ├── installation.md      # 安装与配置指南
│   ├── settings.md          # 完整设置项参考（按 UI 标签页归类）
│   └── tools-reference.md   # 内置工具定义速查
├── config/
│   └── config.yml           # 个人配置备份
└── README.md
```

## 快速开始

1. **安装 OMP** → [安装指南](docs/installation.md)
2. **放置配置** → 将 `config/config.yml` 复制到 `~/.omp/agent/config.yml`
3. **启动并登录** → 终端运行 `omp`，输入 `/login` 绑定 OpenCode Go 订阅
4. **查阅设置** → 需要调整某项？查 [设置参考](docs/settings.md)
5. **了解工具** → 不熟悉某个工具？查 [工具定义速查](docs/tools-reference.md)

## 当前配置要点

`config/config.yml` 关键预设（与默认值的差异）：

| 配置项 | 值 | 说明 |
|---|---|---|
| 模型路由 | 全部 OpenCode Go 订阅 | default/slow/smol/vision/plan/designer/task/commit |
| 审批模式 | `yolo` | 工具调用无需确认 |
| 子任务隔离 | `rcopy` | 最大并发 16 |
| 浏览器 | headless 模式 | 后台运行 |
| 异步模式 | 已启用 | 支持后台 bash 和任务 |
| GitHub 集成 | 已启用 | PR/Issue 操作 |
| 图片检查 | 已启用 | `inspect_image` 工具 |
| 思考块 | 隐藏 | `hideThinkingBlock: true` |
| 压缩策略 | `handoff` | 保存 handoff 文档到磁盘 |

## 文档

| 文档 | 适合场景 |
|---|---|
| [安装指南](docs/installation.md) | 首次配置 OMP、放置配置文件、启动登录 |
| [设置参考](docs/settings.md) | 查找某个设置项的类型、默认值、中文说明 |
| [工具定义速查](docs/tools-reference.md) | 快速了解某个工具的功能和关键参数 |

## 参考

- [Oh My Pi 官方仓库](https://github.com/can1357/oh-my-pi)
