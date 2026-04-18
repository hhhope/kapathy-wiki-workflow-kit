# ADR-0002 Stable Decisions Live In Wiki ADR

- Status: accepted
- Date: 2026-04-15

## Context

过去稳定决策有的只在聊天里，有的写在 repo `AGENTS.md`，有的写在单个 change 的 `adr.md`。这样很难统一回顾“项目到底已经决定了什么”。

## Decision

跨 change 仍然成立的稳定决策，统一记录在 `wiki/adr/`。

OpenSpec change 里保留：

- 当前变更范围
- 任务进展
- checkpoint / 中断说明
- 对 wiki ADR 的引用

## Consequences

- 项目级稳定决策有统一入口
- change 历史不会丢，但不再充当长期 ADR 主容器
