---
name: sync-config
description: 将 ~/.omp/agent/config.yml 同步到仓库 config/config.yml，提交并推送到远端
globs:
  - config/config.yml
---

# Sync Config

将 Oh My Pi 的当前配置同步到本仓库并推送。

## 触发条件

当用户要求"同步配置"、"sync config"、"提交配置"或类似指令时执行。

## 步骤

1. 复制源文件到目标：
   - 源：`~/.omp/agent/config.yml`
   - 目标：`<仓库根目录>/config/config.yml`
2. 检查是否有实际变更（`git diff config/config.yml`）
3. 如果没有变更，报告"配置已是最新，无需提交"并结束
4. 如果有变更：
   - `git add config/config.yml`
   - `git commit -m "sync: 同步 ~/.omp/agent/config.yml"`
   - `git push origin master`

## 注意事项

- 源路径 `~/.omp/agent/config.yml` 在 Windows 下展开为 `C:\Users\<用户名>\.omp\agent\config.yml`
- 使用 `write` 工具以源文件内容覆盖目标文件（而非 shell cp）
- 仅在有实际差异时才提交推送
