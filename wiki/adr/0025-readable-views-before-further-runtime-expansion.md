---
layer: adr
domain: none
canonical_object: wiki-readable-views
artifact_type: adr
formalizes:
  - wiki-readable-views
derived_from:
  - live-conversation-reanchor-gate
---

# wiki-readable-views / adr

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了：

- naming
- frontmatter
- graph extraction
- relation analysis

但在实际使用里，用户仍然读不出来：

- 时间线
- 同类文档
- 当前 graph / relation 到底能怎么读

随后仓库又沿 runtime stack 继续扩展到：

- semantic scoring
- utilization
- runtime context
- source integration
- auto routing
- context injection
- self-directed execution

这条链在技术上连续，但没有先解决最基础的阅读问题。

## Decision

本仓库采用 `readable views before further runtime expansion` 作为稳定决策。

也就是：

- 当当前痛点仍然是 repo legibility 时，优先补阅读视图
- 阅读视图至少包括：
  - 时间线视图
  - 同类文档视图
  - 可读关系视图
- 不应把已有 graph / relation artifact 的存在误当成“用户已经能读懂仓库”

## Consequences

- 以后如果用户主要抱怨的是“看不见、分不清、读不懂”，默认优先级应回到阅读层
- runtime、routing、injection、autonomy 一类下游层不应继续抢占这类问题的优先级
- `openspec-explore` 是否合理可以单独讨论，但不应抢在这三个阅读视图之前
