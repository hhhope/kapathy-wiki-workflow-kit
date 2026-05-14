---
layer: adr
domain: none
canonical_object: wiki-runtime-layer-boundary
artifact_type: adr
formalizes:
  - wiki-runtime-layer-boundary
derived_from:
  - wiki-runtime-layer-contract
  - wiki-react-decision-trace
  - brainstorming-drift-wiki-trace
---

# ADR-0033 Wiki React / Eval / Apply / OpenSpec 边界

## 状态

Accepted

## 背景

当前 wiki runtime 已经有几个相邻入口和层级：

- `$wiki-react`：负责显式路由和边界判断
- `eval_wiki_decision_trace.py`：负责验证 agent 产出的 trace
- `/wiki:apply`：负责 bounded self-directed execution 预览
- repair-route labels：负责给诊断修复类别命名
- OpenSpec：负责 runtime 和 workflow 生命周期

在 2026-05-14 的 wiki runtime 讨论中，这些层被反复互相替代。agent 把
eval 当成 repair path，把 `/wiki:apply` 当成 repair executor，又把设计文档里
出现的 repair-route labels 当成已经存在的可执行修复基础设施。

仓库需要一条稳定决策，防止这些层继续被互相替代。

## 决策

wiki runtime 各层不能互相替代。

- `$wiki-react` 负责在模糊或高风险 wiki 请求中产生显式 route 和
  `decision_trace`。
- `eval_wiki_decision_trace.py` 只负责用 replay cases 验证 agent-produced
  traces。它不做自然语言意图分类，不执行 repair，也不批准 OpenSpec 生命周期
  步骤。
- `/wiki:apply` 只预览 bounded self-directed execution 或 context suggestions。
  它不直接修改 runtime files、scripts、skills、AGENTS、command behavior 或
  OpenSpec state。
- Repair-route labels 只给诊断类别命名。它们不证明 executable repair
  infrastructure 已经存在。
- OpenSpec 负责 runtime、workflow、skill、AGENTS、command behavior 和 repair
  capability changes 的生命周期。

## 后果

- trace eval 通过只证明 trace shape 和 boundary checks 通过。
- `/wiki:apply` 输出默认仍是 preview 或 suggestion，除非另有已批准的
  implementation path 授权执行。
- 命名 `runtime-parser-fix` 或 `readable-graph-fix` 这样的 repair route，不等于
  对应实现已经存在。
- runtime 或 workflow behavior changes 不能藏在 status、graph、apply、
  scorecard 或 eval surface 里。
- 后续解释 wiki runtime 时，必须明确 routing、validation、preview、route
  labeling 和 lifecycle approval 分别由哪一层负责。
