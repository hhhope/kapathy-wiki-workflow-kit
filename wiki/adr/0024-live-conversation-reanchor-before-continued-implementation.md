---
canonical_object: live-conversation-reanchor-gate
artifact_type: adr
formalizes:
- live-conversation-reanchor-gate
derived_from:
- disagreement-management
---

# live-conversation-reanchor-gate / adr

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经 formalize 了分歧管理方法，明确了：

- preserve disagreement
- anti-compression
- retro before ADR

这些规则解决了“争议不要太快蒸发或太快压成结论”的问题，但没有解决另一层失败：

- 用户已经明确指出当前工作偏了
- 原始需求已经被重新说清
- agent 仍可能顺着当前技术链继续 implementation
- `continue` 可能错误继承最近的技术链，而不是最后确认过的主线

所以问题不再只是 disagreement preservation，而是 live conversation 缺少 requirement re-anchor gate。

## Decision

本仓库采用 `live conversation re-anchor before continued implementation` 作为稳定默认决策。

也就是：

- 当 live conversation 已经暴露 scope drift 或 goal drift 时，默认动作不是继续 implementation
- 仓库必须先回到最后确认过的原始需求
- 只有 re-anchor 明确后，implementation continuation 才能解锁

触发信号至少包括：

- 用户反复说当前工作已经偏了、不是这个，或要求回到更早确认过的需求
- 同一个 `continue` 已经有两种以上 materially different 的解释
- 当前工作正从 `analysis / documentation / modeling` 跨到 `runtime / automation / execution`
- agent 继续的是最近技术链，而不是最后确认过的产品主目标

触发后的最小动作：

1. 停止 implementation continuation
2. 重述最后确认过的原始需求
3. 写清当前正沿着哪条链继续
4. 判断是否已经偏离
5. 如果偏离仍未在 active change 内收束，先写一条 `wiki/ops retro`

解锁条件至少满足一条：

- 用户明确确认新的主线
- 已为新方向创建新的 OpenSpec change
- retro 或 `archive-review.md` 已明确写出 `keep / freeze / next action`

## Consequences

- 仓库现在把 disagreement management 分成两层：
  - preservation layer
  - interruption and re-anchor layer
- 以后不能再把“争议已经被保留”误当成“争议已经足以打断错误继续”
- repo-local skill 如果后续需要，只能作为辅助执行层；它不能替代这个 gate 本身
