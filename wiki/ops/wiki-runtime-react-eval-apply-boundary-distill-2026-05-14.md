---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: wiki-runtime-layer-boundary
artifact_type: distill
title: wiki-runtime-layer-boundary / distill
type: distill
language: zh-CN
status: active
created_at: 2026-05-14
updated_at: 2026-05-14
ai_generated: true
derived_from:
  - wiki/ops/wiki-runtime-layer-contract.md
  - wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md
  - openspec/changes/formalize-wiki-runtime-layer-boundary/design.md
related_objects:
  - wiki-react-decision-trace
  - wiki-runtime-layer-contract
  - wiki-self-directed-execution
  - improve-wiki-routing-diagnostics
  - brainstorming-drift-wiki-trace
notes_scope: distill wiki-react、eval、wiki-apply、repair routes、OpenSpec 的职责边界
---

# wiki-runtime-layer-boundary / distill

## 问题

2026-05-14 的 wiki runtime 讨论暴露出一个稳定分层问题：agent 把不同 runtime
层互相当成对方。

被混淆的对象包括：

- `$wiki-react`
- `eval_wiki_decision_trace.py`
- `/wiki:apply`
- repair route labels
- OpenSpec lifecycle

这不是单纯的表达问题。只要边界不稳定，agent 就会把“路由判断”“验证 trace”
“预览 action”“已有 repair 能力”“生命周期批准”混成一件事。

## 正确边界

| 层 | 负责 | 不负责 |
| --- | --- | --- |
| `$wiki-react` | 显式 router 和 `decision_trace` 入口。 | 不做 deterministic eval，不执行 repair，不批准 lifecycle。 |
| `eval_wiki_decision_trace.py` | 验证 agent-produced trace 的结构、动作、边界。 | 不做自然语言意图分类，不修文件，不替代 OpenSpec review。 |
| `/wiki:apply` | 预览 bounded self-directed execution / context suggestions。 | 不是 repair executor，不直接改 runtime、skills、AGENTS、scripts。 |
| repair routes | 给诊断修复分类命名。 | 不证明已经存在 executable repair layer。 |
| OpenSpec | runtime、workflow、skill、AGENTS、command behavior change 生命周期。 | 不应被 eval、scorecard、apply preview 绕过。 |

## 为什么前一个回答错了

错误链条是：

```text
repair route 名字存在
-> 以为 repair layer 已经实现
-> 用 /wiki:apply 解释怎么修
-> 用 eval 证明 route 合法
```

正确链条应该是：

```text
$wiki-react 先决定路由和边界
-> eval 只验证 trace 边界
-> /wiki:apply 只给 preview / suggestion
-> repair route label 只说明问题类别
-> 改 runtime / workflow / behavior 仍走 OpenSpec
```

## Repair Route 当前状态

当前四个 repair route 名称的含义是：

- `page-frontmatter-fix`: 可以在明确页面范围和 precheck hint 下成为 bounded
  page edit。
- `taxonomy-config-fix`: 改 taxonomy 行为，必须走 OpenSpec。
- `runtime-parser-fix`: 改解析行为，必须走 OpenSpec。
- `readable-graph-fix`: 改默认可读输出行为，必须走 OpenSpec。

除非有额外 implementation artifact，否则这些名称只是 route labels / contracts，
不是自动可执行修复器。

## 决策候选

稳定决策应当是：

```text
Wiki runtime layers must not substitute for each other.
Routing, trace validation, preview, repair labels, and lifecycle approval are
separate responsibilities.
```

这条决策进入 ADR-0033。此 distill 保留误读背景和校准材料。

## 边界

本页不新增 runtime 能力，不改变 `$wiki-react`、eval 或 `/wiki:apply` 的代码行为。
它只是把已有事实压成可读边界，并为 ADR 提供上下文。
