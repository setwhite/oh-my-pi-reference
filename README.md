# Oh My Pi 参考知识库

[Oh My Pi](https://github.com/can1357/oh-my-pi) 的个人安装、配置与设置项参考。

## 索引

| 文档 | 说明 |
|---|---|
| [安装指南](docs/installation.md) | 安装 OMP、放置配置文件、启动登录 |
| [设置参考](docs/settings.md) | 完整设置项速查（按 UI 标签页归类） |
| [工具定义速查](docs/tools-reference.md) | 内置工具功能、启用开关与默认值 |

## 目录结构

```
.
├── docs/
│   ├── installation.md      # 安装与配置指南
│   ├── settings.md          # 完整设置项参考
│   └── tools-reference.md   # 内置工具定义速查
├── config/
│   ├── config.yml           # 个人 OMP 配置备份
│   ├── AGENTS.md            # 用户级编码规范（Python/TDD 等）
│   └── skills/              # 全局 skills（commit-style, tdd 等 6 个）
├── .omp/
│   └── skills/
│       ├── sync-config/     # 项目 skill：将 OMP 配置同步到仓库
│       └── install-to-omp/  # 项目 skill：将仓库配置安装回 OMP
└── README.md
```

## 快速开始

```bash
git clone https://github.com/setwhite/oh-my-pi-reference.git
cd oh-my-pi-reference
omp
```

进入 OMP 后输入 **“安装配置”** 即可自动将 `config/` 下的配置、指南和 skills 部署到 `~/.omp/agent/`。

## 参考

- [Oh My Pi 官方仓库](https://github.com/can1357/oh-my-pi)
