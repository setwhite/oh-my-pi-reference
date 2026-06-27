---
name: sync-config
description: 将 ~/.omp/agent/config.yml、~/.omp/agent/AGENTS.md 以及 ~/.omp/agent/skills/ 下的全局 skills 同步到仓库 config/ 目录，提交并推送到远端
globs:
  - config/config.yml
  - config/AGENTS.md
  - config/skills/**
---
# Sync Config

将 Oh My Pi 的当前配置、Agent 指南和全局 skills 同步到本仓库并推送。

## 触发条件

当用户要求"同步配置"、"sync config"、"提交配置"或类似指令时执行。

## 步骤

1. 清理并复制源文件到目标：
   - `mkdir -p config/`
   - `cp ~/.omp/agent/config.yml config/config.yml`
   - `cp ~/.omp/agent/AGENTS.md config/AGENTS.md`
   - `rm -rf config/skills/ && cp -r ~/.omp/agent/skills/ config/skills/`
2. 检查是否有实际变更（`git status --short config/`——需同时覆盖已跟踪文件的差异和新增文件）
3. 若无变更，报告"配置、指南和 skills 已是最新，无需提交"并结束
4. 若有变更：
   - `git add config/`
   - `git commit -m "sync: 同步 ~/.omp/agent/ 配置和 ~/.omp/agent/skills/ 全局 skills"`
   - `git push origin master`

## 注意事项

- 源路径 `~/.omp/` 在 Windows 下展开为 `C:\Users\<用户名>\.omp\`
- 直接使用 bash `cp` 复制，无需 `write` 工具中转
- 仅在有实际差异时才提交推送
- skills 目录先 `rm -rf` 清空目标，再 `cp -r` 复制——防止历史遗留的嵌套目录污染目标路径
