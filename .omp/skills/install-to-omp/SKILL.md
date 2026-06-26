---
name: install-to-omp
description: 将仓库 config/ 下的配置文件、Agent 指南和 skills 安装回 ~/.omp/agent/ 目录。当用户要求“安装配置”、“部署到 OMP”、“应用配置”、“install to omp”或类似指令时使用。
globs:
  - config/config.yml
  - config/AGENTS.md
  - config/skills/**
---

# Install to OMP

将本仓库 `config/` 下的配置、指南和 skills 安装到 Oh My Pi 的用户目录，实现“克隆即用”。

## 触发条件

当用户要求“安装配置”、“部署到 OMP”、“应用配置”、“install to omp”、“setup config”或类似指令时执行。

## 步骤

### 1. 询问用户

使用 `ask` 工具依次询问以下三个问题。

**问题一：同步哪些内容？**

```yaml
questions:
  - id: sync_items
    question: 要将仓库 config/ 下的哪些内容安装到 ~/.omp/agent/？
    options:
      - label: config.yml
        description: OMP 全局设置（模型路由、审批模式等）
      - label: AGENTS.md
        description: 用户级编码规范（Python 规范、TDD 流程等）
      - label: skills/
        description: 全局 skills（commit-style、deep-dive、grill-me、prior-art-research、skill-creator、tdd）
    multi: true
    recommended: [0, 1, 2]
```

**问题二（仅当用户选择了 skills/ 时）：skills 安装到哪一级？**

```yaml
questions:
  - id: skill_level
    question: skills 安装到用户级（全局生效）还是项目级（仅当前仓库生效）？
    options:
      - label: 用户级
        description: 复制到 ~/.omp/agent/skills/，所有项目共享
      - label: 项目级
        description: 仅保留在仓库 .omp/skills/ 中，仅本仓库生效
    recommended: 0
```

**问题三（仅当用户选择了 skills/ 时）：同步哪些 skills？**

```yaml
questions:
  - id: which_skills
    question: 要同步 config/skills/ 下的哪些 skills？
    options:
      - label: commit-style
        description: 约定式 commit 信息规范
      - label: deep-dive
        description: 概念深度解析——系统构建知识体系
      - label: grill-me
        description: 需求澄清与消歧——结构化盘问
      - label: prior-art-research
        description: 先验研究——防止重复造轮子
      - label: skill-creator
        description: Skill 创建、修改与评测
      - label: tdd
        description: 测试驱动开发与测试策略分级
    multi: true
    recommended: [0, 1, 2, 3, 4, 5]
```

### 2. 执行复制

根据用户选择执行：

| 选择 | 源 | 目标 |
|---|---|---|
| config.yml | `config/config.yml` | `~/.omp/agent/config.yml` |
| AGENTS.md | `config/AGENTS.md` | `~/.omp/agent/AGENTS.md` |
| skills/ (用户级) | `config/skills/<name>/` | `~/.omp/agent/skills/<name>/` |

- 直接使用 `cp` 复制单文件
- skills 目录使用 `cp -r` 递归复制整个技能目录
- 若目标目录不存在，先 `mkdir -p ~/.omp/agent/skills/`
- 如果用户选择“项目级” skills，则无需操作（skills 已在仓库 `.omp/skills/` 中）

### 3. 报告结果

安装完成后，逐项报告：
- 哪些文件/目录已复制
- 目标路径
- 如有覆盖，明确告知用户

## 注意事项

- 源路径 `~/.omp/` 在 Windows 下展开为 `C:\Users\<用户名>\.omp\`
- 直接使用 bash `cp` 复制，无需 `write` 工具中转
- 覆盖已有文件前无需确认（按用户选择执行）
- 用户级 skills 与项目级 skills 可共存；同名时项目级优先
