---
name: skill-creator
disableModelInvocation: true
description: 创建、修改和优化 skills。当用户想要创建新 skill、改进已有 skill、或优化触发描述时使用。
---

# Skill Creator — 创建与迭代 Skill

## 核心原则

Skill 是写给 AI 看的操作手册——告诉它何时触发、干什么、怎么干、输出什么。写好一个 skill 的本质：意图清晰、步骤可执行、边界明确。

## Skill 结构

```
skill-name/
├── SKILL.md          —— 必填，frontmatter + Markdown 指令
└── Bundled Resources  —— 可选
    ├── scripts/      —— 可执行脚本（确定性/重复性任务）
    ├── references/   —— 按需加载的参考文档
    └── assets/       —— 输出用文件（模板、图标等）
```

### Frontmatter

- `name` —— skill 标识符，必填
- `description` —— 触发条件 + 功能描述，必填。这是 AI 是否调用此 skill 的核心依据
- `disableModelInvocation` —— 设为 `true` 则仅手动触发，不自动匹配

## 工作流

### 一、创建 Skill

#### 1. 捕获意图

先搞清四个问题：
1. 这个 skill 让 AI 完成什么？
2. 什么情况下触发？（用户说了什么）
3. 期望的输出格式是什么？
4. 是否需要测试用例？——输出可客观验证（文件转换、数据提取、代码生成、固定步骤）则需要；输出主观（写作风格、视觉设计）通常不需要。

如果当前对话已包含完整工作流，直接从对话历史提取答案。

#### 2. 调研与访谈

主动询问边界情况、输入输出格式、示例文件、成功标准、依赖项。有可用 MCP 工具则并行调研，带着上下文来降低用户负担。

#### 3. 撰写 SKILL.md

**结构模式：** 核心原则 → 格式/结构 → 工作流 → 反模式。四段足矣，不另立章节。

**容器选择：**
- 禁止表格——用 `- key —— value` 列表代替，紧凑可扫
- 禁止 `---` 分隔线——用标准 Markdown 标题分层
- 禁止 `<Good>`/`<Bad>` 等 XML 标签——用 `✅`/`❌` 行内标记
- 代码块仅用于三类场景：真实命令（bash/shell）、JSON 模板（schema/配置）、目录树（展示文件结构）。ASCII 流程图、示例对比、参数罗列一律用列表

**语言密度：**
- 用中文撰写正文，专业术语除外
- 祈使句直给指令，不说「你应该」「建议你」
- 每行承载独立语义，不写过渡句和铺垫段
- 解释 why 而非堆 MUST——让 AI 理解意图后自主决策

**篇幅控制：**
- 总行数 ≤ 300，超限拆到 references/ 按需加载
- 目标 ≤ 150 行——超过说明有冗余或该拆模块
- 合并重复章节：相同语义的不同说法，只留一处

**模板优先：**
- 输出格式用模板而非描述——一个好模板省掉三段说明
- 参数用 `- param —— 含义，必填/可选，默认值` 一行讲完

#### 4. 保存测试用例

保存到 `evals/evals.json`：

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "用户任务 prompt",
      "expected_output": "期望结果描述",
      "files": []
    }
  ]
}
```

完整 schema 见 `references/schemas.md`。

### 二、评估与测试

在 `<skill-name>-workspace/` 下按迭代组织：`iteration-N/eval-M/`。以下五步连续执行，中途不停。

#### Step 1：并行起跑

每个测试用例同时 spawn 两个 subagent：
- **with_skill** —— 带 skill 执行，输出到 `with_skill/outputs/`
- **baseline** —— 新建 skill 则不带 skill（`without_skill/`）；改进已有 skill 则用旧版快照（`old_skill/`）

为每个用例写 `eval_metadata.json`：
```json
{"eval_id": 0, "eval_name": "描述名", "prompt": "任务 prompt", "assertions": []}
```

#### Step 2：起草断言

subagent 跑起来后，为每个用例起草量化断言，更新 `eval_metadata.json` 和 `evals/evals.json`。

#### Step 3：记录耗时

每个 run 完成后，保存 `total_tokens` 和 `duration_ms` 到 `timing.json`。

#### Step 4：打分、聚合、启动查看器

1. **打分** —— spawn grader subagent（见 `agents/grader.md`），输出 `grading.json`：`{text, passed, evidence}`
2. **聚合**：
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
3. **分析** —— 读 benchmark 发现隐藏模式（见 `agents/analyzer.md`）
4. **启动查看器**：
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   ```
   迭代 2+ 加 `--previous-workspace`。无头模式加 `--static`。

#### Step 5：读取反馈

读 `feedback.json`。空反馈 = 通过。杀掉查看器进程。

### 三、迭代改进

改进原则：
- 从反馈中提炼通用模式，不过拟合具体测试
- 读 transcript 找冗余，删掉没用的部分
- 解释原因（why），让 AI 自主判断而非盲从
- 多处重复的辅助代码 → 提取到 `scripts/`

迭代循环：
1. 应用改进到 skill
2. 全量重跑到新 `iteration-N+1/`
3. 启动查看器，传入 `--previous-workspace`
4. 等用户审阅完成
5. 读反馈，继续改进

停止条件：用户满意 / 反馈全空 / 无明显进展。

### 四、优化触发描述

description 决定 AI 是否调用 skill。创建或改进后，主动提议优化。

#### Step 1：生成触发评估集

生成 20 条查询——should-trigger（8-10 条，不同措辞）和 should-not-trigger（8-10 条，近义词干扰）。保存为 JSON：`{query, should_trigger}`。

#### Step 2：用户审阅

用 `assets/eval_review.html` 模板展示，用户编辑后导出为 `eval_set.json`。

#### Step 3：运行优化

```bash
python -m scripts.run_loop \
  --eval-set <eval_set.json> \
  --skill-path <skill-path> \
  --model <当前模型> \
  --max-iterations 5 \
  --verbose
```

注：简单一步式查询不会触发 skill，即使 description 完美——只有多步骤或专业查询才可靠触发。

#### Step 4：应用结果

取 `best_description`，更新 SKILL.md frontmatter。展示 before/after 和分数。

## 参考文件

- `agents/grader.md` —— 断言评分
- `agents/comparator.md` —— 盲测 A/B 对比
- `agents/analyzer.md` —— 分析输赢原因
- `references/schemas.md` —— evals.json / grading.json 等 JSON 结构

## 反模式

- 把 skill 写成给人类看的文档——目标是 AI 可执行
- description 写「做什么」但不写「何时触发」→ 从不被调用
- 为单个示例过度优化 → 通用场景失效
- 正文塞满参考信息不拆模块 → 超 300 行，context 爆炸
- 不看 transcript 就改——盲改
- description 优化后不验证——改坏了不知道
