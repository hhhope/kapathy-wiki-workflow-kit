---
layer: ops
domain: wiki
ops_area: agent-governance
canonical_object: brainstorming-drift-wiki-trace
artifact_type: retro
title: brainstorming-drift-wiki-trace / retro
type: retro
language: zh-CN
status: active
created_at: 2026-05-14
updated_at: 2026-05-14
ai_generated: true
derived_from:
  - chat://2026-05-14/wiki-runtime-brainstorming-drift
  - openspec/changes/add-brainstorming-drift-wiki-trace/design.md
related_objects:
  - wiki-react-decision-trace
  - wiki-runtime-layer-contract
  - live-conversation-reanchor-gate
  - openspec-explore-wiki-trace
notes_scope: 记录用户指出的三次 wiki runtime / brainstorming 漂移，并分析为什么需要 brainstorming drift trace
---

# brainstorming-drift-wiki-trace / retro

## Trigger

用户在 wiki runtime 修复讨论中显式指出：

> 第三次漂移了你看下

随后进一步指出：

> 而且这些ADR都没记录，你把brainstorming也改成和openspec的explore一样。这种漂移要记录wiki

这不是一次普通事实纠正，而是连续三次把 `$wiki-react`、EVAL、
`/wiki:apply`、repair route、OpenSpec、ADR 之间的层级关系混在一起。

## Original Intent

用户要校准的是：

- `$wiki-react` 是否才是 EVAL / decision-trace 的正确入口
- EVAL 层到底负责什么
- `/wiki:apply` 和 repair route 是否真的已经创建成可执行能力
- 当 `$superpowers:brainstorming` 中出现反复漂移时，是否也要像
  `$openspec-explore` 一样写入 `wiki/ops` trace

## Drift Chain

### Drift 1: 把 `/wiki:apply` 当成 repair 执行入口

错误回答把修复链说成：

```text
/wiki:status -> /wiki:apply -> repair route -> 修
```

这把 `/wiki:apply` 的 bounded execution preview 说成了已经可执行的 repair
planning layer，并默认四个 repair route 已经有完整实现。

### Drift 2: 把 EVAL 当成 repair path

后续回答又把 `eval_wiki_decision_trace.py` 作为证明“怎么修”的证据。
但仓库事实是：

- `$wiki-react` 是显式 router 和 `decision_trace` 入口
- `eval_wiki_decision_trace.py` 只验证 agent-produced trace
- Python eval 不做自然语言意图分类
- eval 不替代 OpenSpec review，也不执行 repair

所以 EVAL 能证明的是边界是否守住，不是 repair route 是否已经创建。

### Drift 3: brainstorming 被继续压成 repair-route 讨论

用户显式触发 `$superpowers:brainstorming` 后，正确动作应是停止继续技术链，
重锚设计问题，并提出方案。

实际回答虽然开始重锚，但仍然围绕 `/wiki:apply`、repair route 和 OpenSpec
执行缺口继续展开，没有先把三次漂移作为 wiki-visible 失败证据记录下来。

## Rejected Framing

被用户否掉的 framing 是：

```text
当前问题只是 wiki runtime repair route 该怎么执行
```

更准确的 framing 是：

```text
当前问题是 agent 在高风险 wiki runtime / brainstorming 场景下反复混层，
而这个漂移本身没有被记录为 repo-visible evidence。
```

## Corrected Framing

正确层级应是：

```text
$wiki-react
  -> 产出 decision_trace
  -> EVAL 验证 trace 是否符合边界
  -> 再路由到 /wiki:status / /wiki:graph / /wiki:apply / OpenSpec

/wiki:apply
  -> 预览 bounded self-directed execution/context
  -> 不直接修 runtime

repair routes
  -> 当前主要是 improve-wiki-routing-diagnostics 的设计/文档合同
  -> 不是全部已创建的 executable repair layer

$superpowers:brainstorming drift
  -> 重复漂移时先停下并写 wiki/ops trace
  -> 再继续设计讨论或 OpenSpec 变更
```

## Cause Analysis

### 1. 技术链惯性覆盖了用户的元问题

对话已经处在 wiki graph/status/apply/runtime 这条链上，agent 继续沿着最近的
技术对象回答，而不是识别用户已经切换到“流程为什么漂移”的元问题。

### 2. 把设计合同误读成已落地能力

`improve-wiki-routing-diagnostics` 的设计文档列出了四个 repair route，但这并
不等于 runtime 已经提供了机器可读 route result 或执行器。agent 没有先核对
实现面，就把 contract 当成 capability。

### 3. 混淆了 router、validator、observation、lifecycle

仓库已有 `wiki-runtime-layer-contract`，但回答没有先按这个层级拆开：

- `wiki-react`: router / decision trace
- eval: trace validator
- scorecard/status/graph/apply: observation or preview
- OpenSpec: lifecycle

这导致回答不断把一个层的证据拿去证明另一个层的能力。

### 4. brainstorming 缺少 repo-local drift trace gate

`$openspec-explore` 已有 repo-visible trace gate，live re-anchor 也有 retro gate。
但 `$superpowers:brainstorming` 触发后，如果用户指出连续漂移，当前仓库没有
明确要求先写 `wiki/ops` drift trace。

## Affected Active Change

相关但不应继续塞入的 change：

- `openspec/changes/improve-wiki-routing-diagnostics`

原因：

- 该 change 的 tasks 已经全部完成
- 它的范围是 wiki routing diagnostics runtime / command docs
- brainstorming drift trace 是新的 workflow governance behavior

新的承载 change：

- `openspec/changes/add-brainstorming-drift-wiki-trace`

## ADR Status

不直接创建 ADR。

原因：

- `wiki/adr/0003-retros-stay-separate-from-adrs.md` 已规定 retro 和 ADR 分离
- 当前页面记录失败、漂移、原因和下一步
- 是否稳定为 ADR 应在 OpenSpec change 后续 review 中决定

## Keep

- 保留 `$wiki-react` 作为高风险 wiki runtime 的显式 router。
- 保留 EVAL 作为 decision trace validator，而不是 repair executor。
- 保留 OpenSpec 作为 runtime / workflow behavior change 生命周期。
- 保留 `/wiki:apply` 的 preview / suggest 边界。

## Freeze

- 不再把 repair route 名称说成已经完整创建的 executable layer。
- 不在 completed `improve-wiki-routing-diagnostics` 里追加新范围。
- 不直接写 ADR。
- 不修改 Superpowers upstream skill。

## Next Action

通过 `openspec/changes/add-brainstorming-drift-wiki-trace` 先定义并审查规则：

```text
When $superpowers:brainstorming is active and the user flags repeated drift,
the agent SHALL stop continuation, produce or update a repo-visible wiki/ops
drift trace, and only then resume design discussion.
```

后续再决定是否需要更新 repo guidance、repo-local skill reference，或新增 ADR。
