# ADR-0004 Agent Self-Evolution Over Skill Governance

- Status: accepted
- Date: 2026-04-15

## Context

Hermes 的启发如果只被理解成“skill lifecycle”和“skill inventory”，就会偏窄。用户真正要解决的问题不是手工决定是否每次创建 skill，而是 agent 如何从任务中自动提炼、复用、修补经验，而人保留治理权。

## Decision

本仓库将 Hermes 主要视为 `agent self-evolution governance` 参考，而不是单纯的 `skill governance` 参考。

后续关注点应优先放在：

- experience extraction
- candidate memory
- reuse
- failure-driven patching
- human governance

## Consequences

- skill metadata 仍有价值，但不再是顶层框架
- 后续 change 应优先围绕 agent 自进化，而不是只围绕 skill 文件治理
