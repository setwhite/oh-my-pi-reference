---
name: commit-style
description: Commit 信息规范——生成符合约定格式的提交信息。当用户要求提交代码、生成 commit message、发起 PR、或提到"提交"、"commit"、"push"时使用。
---

# Commit 信息规范

## 格式

```
<type>(scope): <summary>
```

- `type`：必填，变更类型
- `scope`：可选，影响范围
- `summary`：必填，中文、动词开头、≤ 50 字、不加句号

## Type 选择

| Type | 适用场景 |
|------|---------|
| `feat` | 新功能、新接口、新能力 |
| `fix` | Bug 修复、异常处理 |
| `refactor` | 重构——行为不变、结构调整 |
| `docs` | 文档、注释、README |
| `test` | 测试补充或修改 |
| `chore` | 构建、依赖、配置、杂务 |

选择口诀：**改行为 → `feat`/`fix`，改结构 → `refactor`，改描述 → `docs`，改验证 → `test`，改环境 → `chore`。**

## Scope 选择

`scope` 是可选的。值得加 scope 的场景：
- 项目有明确模块划分
- 一次 PR 涉及多个模块，分批 commit
- 不加 scope 会导致历史回溯困难

没有明确模块则不强行加。

## 示例

<Good>
```
feat(parser): 支持 Markdown 表格解析
fix: 修复用户名为空时 NPE
refactor(api): 提取公共认证中间件
docs: 补充部署流程说明
test(auth): 补充 OAuth2 回调测试
chore: 升级 TypeScript 至 5.4
```
</Good>

<Bad>
```
feat: 加了一些功能                        ← summary 不具体
fix(api): 修复了一个 bug。                 ← 加句号
feat(parser): 支持 Markdown 表格解析、更新依赖、修复一个拼写 ← 混了三种 type
update code                              ← 无 type，非中文
```
</Bad>

## 生成流程

1. 回顾本次改动（`git diff --stat` 或 `git status`）
2. 判断改动主力类型——如果一条 commit 混合了 feat 和 fix，拆成两条
3. 提炼一句 ≤ 50 字的中文摘要，动词开头
4. 输出完整 commit message，让用户确认后再执行 `git commit`

## 反模式

- 一条 commit 混多种 type → 拆
- summary 用英文 → 中文
- summary 以「了」「的」结尾 → 啰嗦，去掉
- scope 强行编造 → 没有明确的就不加
- `fix bug`、`update code` → 无意义摘要，等于没写
