# Oh My Pi 安装与配置指南

## 1. 安装 OMP

参考官方仓库安装说明：https://github.com/can1357/oh-my-pi

**Windows (PowerShell)：**

```powershell
irm https://omp.sh/install.ps1 | iex
```

安装完成后，终端输入 `omp` 验证是否成功。

## 2. 项目配置文件

仓库 `config/` 目录下有两个配置文件：

| 文件 | 用途 | 操作 |
|---|---|---|
| `config/config.yml` | OMP 全局设置（模型路由、审批模式、压缩策略等） | 复制到 `~/.omp/agent/config.yml` |
| `config/AGENTS.md` | `config/` 目录的编码规范（Python 规范、TDD 流程、代码维护准则） | 保留在仓库中，OMP 自动发现并加载 |

### 2.1 复制 config.yml

将 OMP 全局设置文件复制到 agent 配置目录：

| 源文件 | 目标路径 |
|---|---|
| `config/config.yml` | `~/.omp/agent/config.yml` |

**Windows 实际路径：** `C:\Users\<用户名>\.omp\agent\config.yml`

### 2.2 AGENTS.md（目录级编码规范）

`config/AGENTS.md` 是 OMP 的目录级上下文文件（Context File）。当 agent 编辑 `config/` 目录下的文件时，OMP 会自动加载其中的编码规范作为指导——包括 Python 编码风格、KISS 原则、TDD 工作流和代码维护准则。

此文件无需手动复制到用户目录，保留在仓库中即可。

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
