---
title: openspec-explore-trigger-drift / retro
type: retro
canonical_object: openspec-explore-trigger-drift
artifact_type: retro
language: zh-CN
audience: self
domain: personal-ops
status: active
updated_at: 2026-04-21
ai_generated: true
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-drift-explore.md
related_objects:
  - agents-governance-drift
  - conversation-handoff
  - disagreement-management
notes_scope: 复盘为什么用户显式触发 openspec-explore 时，系统仍多次滑向 remediation / routing / wiki 落点判断
---

# openspec-explore-trigger-drift / retro

## Trigger

用户已经显式点名使用 `openspec-explore`，但本轮对话中系统仍多次把任务执行成：

- 先判断该不该落 wiki
- 先判断落 `retro` 还是 `explore`
- 先把 explore 压成 remediation / plan / direction split

而不是先进入 `openspec-explore` 的探索姿态。

## Rejected Framing

被用户持续否掉的 framing 不是：

- “要不要继续治理 AGENTS.md”

而是：

- “你应该先按 `openspec-explore` 的方式看这个对象，而不是先替我决定该输出什么”

一句话：

`显式 skill trigger 被误读成了内容任务，而不是先约束交互姿态。`

## Correction Pressure

这轮纠偏压力主要来自两点：

- 用户显式指定了 `openspec-explore`
- 用户后续又明确指出：我让你用这个 skill 去看，不是让你先做 remediation 判断

这说明问题不是一次普通答偏，而是 trigger interpretation 本身出了偏差。

## Why It Keeps Happening

当前至少有三层力量会把 `openspec-explore` 往错误方向拉：

### 1. 上游 skill 把它定义成“姿态”

repo-local `openspec-explore` skill 本体沿用了更通用的上游说法：

- `This is a stance, not a workflow`
- `There are no fixed steps, no required sequence, no mandatory outputs`
- `Don't auto-capture`

这会让系统在看到显式 trigger 时，优先认为：

- 只是在换一种思考模式
- 不是一个带 repo-specific 强制边界的入口

### 2. repo 又把它正式化成带强制留痕的 workflow 入口

但本仓库同时又要求：

- 每次 `openspec-explore` 都先在 `wiki/ops/` 留 trace
- trace 要复用 `intake`
- 同主题默认更新现有 trace

这会把系统再拉向另一种理解：

- 不是纯 explore stance
- 而是 `explore + repo routing obligation`

### 3. repo 的其他 durable-output 默认会继续把 explore 拉向路由判断

本仓库还叠加了更强的默认：

- repeated north-star pull -> handoff mode
- drift / disagreement / repeated process confusion -> `wiki/ops retro`
- example-driven capture -> 同轮留下 repo-visible record

所以一旦当前对话带有：

- repeated correction
- governance disagreement
- “这件事要记下来”的信号

系统就很容易越过“先 explore”，直接滑向：

- 这是 retro 吗
- 这是 remediation explore 吗
- 这是不是该起 OpenSpec change

## Current Clarity

当前更清楚的问题不是“用户没有说清楚”，而是：

- 同一个显式 `openspec-explore` trigger，在本 repo 里同时被两种语义竞争
- 系统执行时偏向了“repo routing obligation”一侧
- 从而忽略了用户真正要的第一步：先按 explore 姿态读对象、跟对象走，而不是先决定输出层

更直接地说：

`错误发生在 trigger interpretation，不是发生在后续结论质量。`

## What The Correct First Move Should Be

当用户显式点名 `openspec-explore` 时，第一步应该是：

1. 明确进入 explore 姿态
2. 先围绕用户给的对象做对照、发散、重读、拆解
3. 只有在 explore 已经形成稳定判断后，再讨论：
   - 是否需要 repo-visible trace
   - 是否该进 `retro`
   - 是否只是现有 explore 的补充

也就是说：

`routing 是第二步，不是第一步。`

## Residual Risk

即使已经看清这条漂移，残余风险仍然存在：

- 只要 skill 本体和 repo workflow contract 继续并列表达而不分层
- 只要 `openspec-explore` 的 repo-specific override 没被写得足够直白
- 只要 repeated correction 一出现，系统仍可能本能滑向 durable routing

## Next Step

如果后续继续治理这一类误读，下一步更像是：

- 明确 `openspec-explore` 在本 repo 中的两层语义边界
  - 第一层：交互姿态
  - 第二层：repo-required trace / routing obligation
- 明确显式 skill trigger 时，哪一层优先

这条 retro 先保留“为什么总会理解错”的校准材料，不在这里直接决定改 skill、改 AGENTS，还是起新的 OpenSpec change。
