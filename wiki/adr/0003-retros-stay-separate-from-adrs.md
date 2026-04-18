# ADR-0003 Retros Stay Separate From ADRs

- Status: accepted
- Date: 2026-04-15

## Context

仓库已经有复盘页，例如 [Scope Drift 复盘](../ops/scope-drift-retro.md)。但复盘回答的是“发生了什么、哪里错了”，不是“最终决定是什么”。

## Decision

决策和复盘必须分开可见：

- `ADR`：记录决定、边界、取舍
- `Retro / logs`：记录失败、偏差、证据、后果

## Consequences

- 后续可以分别回答“为什么这么定”和“以前摔过什么坑”
- 不需要重放整段对话才能理解治理历史
