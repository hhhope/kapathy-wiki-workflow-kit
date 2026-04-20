# ADR-0013 Agent-Readable Wiki Naming Before Graph Growth

- Status: accepted
- Date: 2026-04-20

## Context

当前仓库已经积累了真实的分歧、决策和验证材料，尤其集中在：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

问题不在于材料不存在，而在于对象身份还不够稳定。

同一个对象在不同层里仍可能被不同叫法表达，标题里也经常混入：

- 对象本身
- artifact type
- 日期
- 状态
- 表层症状词

这会让页面对人类勉强可读，但对 agent 不够低成本。它更像一堆 markdown 文件，而不是一张稳定的对象网络。

在这种状态下直接推进图谱、relation analysis 或更强的检索层，会把弱对象身份固化到更高层，而不是先解决基础问题。

## Decision

本仓库采用 `agent-readable wiki naming before graph growth` 作为稳定默认决策。

也就是：

- 在演变型页面上，先稳定对象命名，再推进 metadata、图谱或关系分析
- 覆盖范围第一版只限于：
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- 新页面默认采用两段式命名：
  - `canonical object / artifact type`
- 标题主位只表达：
  - canonical object
  - artifact type
- 日期、状态、验证轮次、change 标识、表层症状词不进入标题主位
- canonical object 只有在它：
  - 不是一次性事件
  - 已跨至少两种容器或 artifact layer 存在
  - 能统一一条真实演变链
  时才成立
- 第一批 canonical object 为：
  - `disagreement-management`
  - `conversation-handoff`
  - `example-driven-capture`
- 同一对象在覆盖范围内必须保持同一个 canonical object 名
- rollout 采用：
  - 新页强约束
  - 旧页弱约束

## Consequences

- 仓库默认不会因为“标题有点乱”就直接跳到大规模目录重构。
- 图谱和关系分析后续必须建立在稳定对象名之上，而不是反过来替对象命名。
- 覆盖范围内的新页命名会更强约束，旧页则按触碰时逐步收敛。
- `readme-learning` 是否独立为 canonical object，继续保留为后续判断，而不是在第一版过早固定。
