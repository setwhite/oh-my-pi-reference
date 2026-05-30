# Oh My Pi 安装与配置指南

## 1. 安装

参考官方仓库安装说明：https://github.com/can1357/oh-my-pi

**Windows (PowerShell)：**

```powershell
irm https://omp.sh/install.ps1 | iex
```

安装完成后，在命令行输入 `omp` 验证是否安装成功。

## 2. 配置

### 2.1 放置配置文件

将以下配置文件复制到 OMP 的 agent 配置目录：

| 源文件 | 目标路径 |
|---|---|
| `config/config.yml` | `~/.omp/agent/config.yml` |

**Windows 实际路径：** `C:\Users\<你的用户名>\.omp\agent\config.yml`

### 2.2 配置文件说明

该配置已经预设了以下关键项：

- **模型路由**：全部使用 OpenCode Go 订阅的模型
  - `default`（日常编码）：`opencode-go/deepseek-v4-pro:high`
  - `slow`（深度推理）：`opencode-go/deepseek-v4-pro:xhigh`
  - `smol`（轻量任务）：`opencode-go/deepseek-v4-flash:high`
  - `vision`（视觉）：`opencode-go/kimi-k2.6:medium`
- **工具审批模式**：`write`（写入操作需确认）
- **子任务隔离**：`rcopy` 模式，补丁合并
- **最大并发子任务**：16
- **浏览器**：非 headless 模式（可见窗口）
- **GitHub 集成**：已启用
- **图片识别**：已启用
- **异步模式**：已启用

## 3. 启动与登录

### 3.1 启动 OMP

在终端中输入：

```bash
omp
```

### 3.2 登录 OpenCode Go 订阅

进入 OMP 交互界面后，输入斜杠命令：

```
/login
```

在弹出的提供商列表中选择 **OpenCode Go**，完成订阅绑定。

> **注意**：登录是一次性操作。OMP 会记住登录状态，后续启动无需重复登录。

## 4. 参考

- **[设置项参考](settings.md)** — 完整设置项中文说明，按 UI 标签页归类（外观、模型、交互、工具、任务等）。