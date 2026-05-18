---
layer: adr
domain: none
canonical_object: repo-agents-governance-phase0
artifact_type: adr
formalizes:
- repo-agents-governance-phase0
derived_from:
- agents-governance-drift
---

# repo-agents-governance-phase0 / adr

- Status: accepted
- Date: 2026-04-21

## Context

仓库已经积累了足够多的 `agents-governance-drift` 证据，能够确认两件事：

- repo-level `AGENTS.md` 的治理漂移是真问题
- 当前偏好的框架仍只是 `candidate`，还不能直接当成已接受主线

如果此时直接启动 repo `AGENTS.md` 的压缩或 proxy migration，会把：

- acceptance
- migration
- enforcement

三件事重新绑成同一轮，重复本轮校准里已经暴露过的 overclaim 问题。

同时，仓库本地治理面还存在一个即时矛盾：

- `ADR-0007` 编号冲突

因此，repo-level `AGENTS.md` 的下一步不能是直接迁移，而必须先有一个更窄的 Phase 0 接受门槛。

## Decision

本仓库接受如下稳定默认决策：

- repo-level `AGENTS.md` 的迁移必须先经过一个独立的 `Phase 0` 接受门槛
- 当前被接受的主线是 `narrow repo-level Phase 0 gate`，不是整套候选 v3.1 框架
- root-level `~/.codex/AGENTS.md` 与 `~/.claude/CLAUDE.md` 默认属于后续外轨，不自动并入本轮 repo change
- Phase 0 完成前，repo-level `AGENTS.md` 工作只允许做：
  - 接受边界澄清
  - repo-local 冲突修复
  - gate wording 发布
- Phase 1 `AGENTS.md` 压缩 / proxy migration 继续保持阻塞，直到：
  - repo-visible Phase 0 主线已接受
  - 影响当前治理引用面的 ADR 编号冲突已消除
  - repo-local commit gate 的状态已经被明文决定

关于 repo-local commit gate，本 ADR 只接受一条边界：

- 本轮 `Phase 0` 不把 hook 实现本身作为完成门槛
- 但后续任何 `Phase 1` change 都必须显式决定：
  - gate required before migration
  - 或 gate deferred to that Phase 1 change

也就是说：

`本 ADR 接受的是 Phase 0 的 gate，不是 Phase 1 的实施方案。`

## Consequences

- 仓库现在有了一个更窄、更诚实的 repo-level 主线，避免把 candidate playbook 当 accepted decision
- repo `AGENTS.md` 暂时不会被拿去直接做大压缩
- root dotfiles 是否合流，必须在后续 change 里单独决定
- repo-local commit gate 不再被暗示为“已经存在”或“已经被接受”
- 以后只要有人想直接做 repo `AGENTS.md` migration，仓库都会先把他拉回 `Phase 0`
