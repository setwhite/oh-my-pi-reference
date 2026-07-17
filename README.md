# Oh My Pi 参考知识库

[Oh My Pi](https://github.com/can1357/oh-my-pi) 的个人安装、配置与设置项参考。

## 安装

### 安装 OMP

参考官方仓库：https://github.com/can1357/oh-my-pi

**Windows (PowerShell)：**

```powershell
irm https://omp.sh/install.ps1 | iex
```

安装完成后，终端输入 `omp` 验证。

### 克隆仓库

```bash
git clone https://github.com/setwhite/oh-my-pi-reference.git
cd oh-my-pi-reference
omp
```

### 安装配置

在 OMP 对话中输入 **"安装配置"**，触发 `install-to-omp` skill。该 skill 会交互式询问要安装哪些内容（config.yml / AGENTS.md / skills）及安装位置，选择后自动将 `config/` 下的文件复制到 `~/.omp/agent/`。

> 也可以手动复制：
> ```bash
> cp config/config.yml ~/.omp/agent/
> cp config/AGENTS.md  ~/.omp/agent/
> cp -r config/skills/ ~/.omp/agent/skills/
> ```
> Windows 实际路径：`C:\Users\<用户名>\.omp\agent\`

### 登录 OpenCode Go

进入 OMP 交互界面后，输入：

```
/login
```

在弹出的提供商列表中选择 **OpenCode Go**，完成订阅绑定。登录是一次性操作，后续启动无需重复。

## 配置

个人配置文件 `config/config.yml` 包含模型路由、工具行为、审批策略等预设项。配置内容会随需求频繁调整，具体取值请直接查看该文件。

完整配置项含义见 [设置参考](docs/settings.md)。如需修改配置，建议通过 OMP 内置的 `/settings` 命令交互式调整。

## 目录结构

```
.
├── docs/
│   └── settings.md          # 完整设置项参考
├── config/
│   ├── config.yml           # 个人 OMP 配置备份
│   ├── AGENTS.md            # 用户级编码规范
│   └── skills/              # 全局 skills
├── .omp/
│   └── skills/
│       ├── sync-config/     # 项目 skill：将 OMP 配置同步到仓库
│       └── install-to-omp/  # 项目 skill：将仓库配置安装回 OMP
└── README.md
```

## 参考

- [设置参考](docs/settings.md) — 完整配置项速查
- [Oh My Pi 官方仓库](https://github.com/can1357/oh-my-pi)
