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

使用 `ask` 工具依次询问以下四个问题。其中问题二是 config.yml 专属；问题三、问题四是 skills/ 专属。按用户选择动态出示。

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
        description: 全局 skills（自动扫描 config/skills/ 发现）
    multi: true
    recommended: 0
```


**问题二（仅当用户选择了 config.yml 时）：Nerd Font 与记忆功能**

```yaml
questions:
  - id: nerd_font
    question: 你的终端是否安装了 Nerd Font 字体？（如不确定，选"否"最安全）
    options:
      - label: 是
        description: 保留 symbolPreset: nerd，终端图标正常显示
      - label: 否
        description: 移除 symbolPreset 设置，避免终端出现乱码
    recommended: 0
  - id: enable_memory
    question: 是否开启记忆功能？（开启后 OMP 会记住历史会话中的关键信息）
    options:
      - label: 否（默认关闭）
        description: 保持 memory.backend: "off"
      - label: 是
        description: 设置 memory.backend: local，启用本地记忆
    recommended: 0
```

**问题三（仅当用户选择了 skills/ 时）：skills 安装到哪一级？**

```yaml
questions:
  - id: skill_level
    question: skills 安装到用户级（全局生效）还是项目级（仅当前仓库生效）？
    options:
      - label: 用户级
        description: 复制到 ~/.omp/agent/skills/，所有项目共享
      - label: 项目级
        description: 复制到仓库 .omp/skills/，仅本仓库生效
    recommended: 0
```

**问题四（仅当用户选择了 skills/ 时）：同步哪些 skills？**

先扫描 `config/skills/` 目录，对每个子目录读取其 `SKILL.md` frontmatter 中的 `name` 和 `description`，排除 `install-to-omp` 自身，动态构建选项：

```yaml
questions:
  - id: which_skills
    question: 要同步 config/skills/ 下的哪些 skills？
    options:
      # 动态生成：每个子目录一条，label=目录名，description=SKILL.md frontmatter.description
      # 排除 install-to-omp
    multi: true
    recommended: 0  # 全部推荐
```

**构建方式：**
1. `read config/skills/`（目录路径）获取所有子目录名
2. 对每个子目录 `name`，`read config/skills/<name>/SKILL.md:1-10`，提取 YAML frontmatter 中的 `description` 字段（YAML 块以第二个 `---` 结束）
3. 过滤掉 `name == "install-to-omp"` 的条目
4. 按目录名字母序排列
5. 用提取到的 `name: description` 对填充 options；recommended 为全部索引

### 2. 执行复制

根据用户选择执行。

**通用规则：**

| 选择 | 源 | 目标 |
|---|---|---|
| config.yml | `config/config.yml` | `~/.omp/agent/config.yml` |
| AGENTS.md | `config/AGENTS.md` | `~/.omp/agent/AGENTS.md` |
| skills/ (用户级) | `config/skills/<name>/` | `~/.omp/agent/skills/<name>/` |
| skills/ (项目级) | `config/skills/<name>/` | `.omp/skills/<name>/` |

- 直接使用 `cp` 复制单文件
- skills 目录使用 `cp -r` 递归复制整个技能目录
- 目标目录不存在时，先 `mkdir -p` 创建：
  - 用户级：`~/.omp/agent/skills/`
  - 项目级：`.omp/skills/`

**config.yml 的后处理：**

如果用户选择了 config.yml，先 `cp config/config.yml ~/.omp/agent/config.yml`，然后根据前面 nerd_font 和 enable_memory 的回答修改目标文件。修改操作仅为逐行级简单替换，使用 `grep`/`sed` 即可，不要依赖 `pyyaml` 等第三方库：

- 如果用户选择"否"（没有 Nerd Font）：`sed -i '/^symbolPreset:/d' ~/.omp/agent/config.yml`
- 如果用户选择"是"（开启记忆）：`sed -i 's/backend: "off"/backend: local/' ~/.omp/agent/config.yml`

完成后用 `grep symbolPreset\|backend ~/.omp/agent/config.yml` 验证关键字段是否生效。

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
