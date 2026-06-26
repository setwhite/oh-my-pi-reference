# Oh My Pi 安装与配置指南

## 1. 安装 OMP

参考官方仓库安装说明：https://github.com/can1357/oh-my-pi

**Windows (PowerShell)：**

```powershell
irm https://omp.sh/install.ps1 | iex
```

安装完成后，终端输入 `omp` 验证是否成功。

## 2. 放置配置文件
将 `config/` 下的文件复制到 `~/.omp/agent/`：

| 源文件 | 目标路径 | 用途 |
|---|---|---|
| `config/config.yml` | `~/.omp/agent/config.yml` | OMP 全局设置（模型路由、审批模式等） |
| `config/AGENTS.md` | `~/.omp/agent/AGENTS.md` | 用户级编码规范（Python 规范、TDD 流程等） |
| `config/skills/` | `~/.omp/agent/skills/` | 全局 skills（commit 格式、TDD 流程等） |

**Windows 实际路径：** `C:\Users\<用户名>\.omp\agent\`

> 复制 skills 目录时使用递归复制：`cp -r config/skills/ ~/.omp/agent/skills/`

> `config/AGENTS.md` 是用户级全局编码规范。OMP 在每个会话启动时自动加载 `~/.omp/agent/AGENTS.md`。

## 3. 当前配置说明

`config/config.yml` 已预设以下关键项：

- **模型路由**：全部使用 OpenCode Go 订阅模型
  - `default`（日常编码）：`opencode-go/deepseek-v4-pro:high`
  - `slow`（深度推理）：`opencode-go/deepseek-v4-pro:xhigh`
  - `smol`（轻量任务）：`opencode-go/deepseek-v4-flash:high`
  - `vision`（视觉）：`opencode-go/kimi-k2.6:medium`
- **审批模式**：`yolo`（工具调用无需确认）
- **子任务隔离**：`rcopy` 模式，最大并发 16
- **异步模式**：已启用
- **浏览器模式**：headless（后台运行）
- **GitHub 集成**：已启用
- **图片检查**：已启用
- **思考块**：隐藏
- **压缩策略**：`handoff`，保存 handoff 文档到磁盘
- **变更日志**：精简模式

> 完整的配置项说明见 [设置参考](settings.md)。如需修改配置，建议通过 OMP 内置的 `/settings` 命令交互式调整。

## 4. 启动与登录

### 4.1 启动 OMP

终端输入：

```bash
omp
```

### 4.2 登录 OpenCode Go

进入 OMP 交互界面后，输入斜杠命令：

```
/login
```

在弹出的提供商列表中选择 **OpenCode Go**，完成订阅绑定。

> 登录是一次性操作。OMP 会记住登录状态，后续启动无需重复。

## 5. 下一步

→ [返回索引](../README.md)
