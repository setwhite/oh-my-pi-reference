---
name: sync-config
description: 将 ~/.omp/agent/config.yml、~/.omp/agent/AGENTS.md 以及 ~/.omp/agent/skills/ 下的全局 skills 同步到仓库 config/ 目录，提交并推送到远端
globs:
  - config/config.yml
  - config/AGENTS.md
  - config/skills/**
disableModelInvocation: true
---
# Sync Config

将 Oh My Pi 的当前配置、Agent 指南和全局 skills 同步到本仓库并推送。

## 触发条件
本 skill 设置 `disableModelInvocation: true`，不参与自然语言自动匹配。仅当用户显式调用 `/skill:sync-config` 或直接说 "sync-config" 时执行。

## 步骤

1. 创建目标目录并复制单文件：
   - `mkdir -p config/`
   - `cp ~/.omp/agent/config.yml config/config.yml`
   - `cp ~/.omp/agent/AGENTS.md config/AGENTS.md`
2. 安全复制 skills 目录（先拷到临时目录，成功后再替换）：
   - `rm -rf config/skills.new/`
   - `cp -r ~/.omp/agent/skills/ config/skills.new/`
   - `rm -rf config/skills/`
   - `mv config/skills.new/ config/skills/`
3. 检查是否有实际变更（`git status --short config/`——需同时覆盖已跟踪文件的差异和新增文件）
4. 若无变更，报告"配置、指南和 skills 已是最新，无需提交"并结束
5. 若有变更：
   - `git add config/config.yml config/AGENTS.md config/skills/`
   - `git commit -m "sync: 同步 ~/.omp/agent/ 配置和 ~/.omp/agent/skills/ 全局 skills"`
   - `git pull --rebase origin HEAD`
   - `git push origin HEAD`

## 注意事项

- 源路径 `~/.omp/` 在 Windows 下展开为 `C:\Users\<用户名>\.omp\`
- 直接使用 bash `cp` 复制，无需 `write` 工具中转
- 仅在有实际差异时才提交推送
- skills 目录通过临时目录 `config/skills.new/` 中转：先 `cp`，成功后 `rm` 旧目录再 `mv`。若 `cp` 失败则旧目录完好无损
- `git pull --rebase` 确保 push 前已同步远端，避免 conflict reject
- `git push origin HEAD` 推送当前分支，不硬编码分支名
- `git add` 明确列出 `config.yml`、`AGENTS.md`、`skills/`，防止误提交 config/ 下的其他文件
