## Context

Current repository evidence already separates two truths:

- governance-drift around AGENTS is real and repo-visible
- the currently preferred framework is still only a candidate model

The repository has multiple supporting artifacts:

- `wiki/ops/agents-governance-drift-retro.md`
- `wiki/ops/agents-governance-drift-explore.md`
- `wiki/ops/agents-governance-drift-distill-2026-04-21.md`
- `wiki/ops/agents-governance-drift-distill-calibration-retro.md`
- `wiki/ops/agents-governance-drift-playbook-2026-04-21.md`

Those artifacts already support a repo-level conclusion that Phase 0 is needed
before Phase 1. They do not yet support directly treating the whole playbook or
the whole v3.1 model as an accepted repository-default decision.

This design therefore narrows the change boundary to one question:

`What repo-level governance work must become accepted before repo AGENTS
migration can start?`

## Goals / Non-Goals

**Goals**

- Define a repo-level Phase 0 acceptance boundary for AGENTS-governance work.
- Separate repo-local acceptance from later migration execution.
- Resolve the duplicate `ADR-0007` numbering conflict inside the repo.
- Decide whether the repo requires a repo-local commit gate before any
  `AGENTS.md` migration.
- Leave explicit written deferrals for root dotfiles and other adjacent work.

**Non-Goals**

- Do not execute Phase 1 `AGENTS.md` compression or proxy migration.
- Do not rewrite the repo `AGENTS.md` toward the `<= 50` target in this change.
- Do not modify root-level `~/.codex/AGENTS.md` in this change.
- Do not modify root-level `~/.claude/CLAUDE.md` in this change.
- Do not fold the broader `evaluation.md` field conflict into this change.
- Do not claim that the full v3.1 model is accepted unless the change artifacts
  and resulting ADR explicitly say so.

## Decisions

### Decision: Repo-level Phase 0 is its own change boundary

The repository should formalize Phase 0 as a standalone change before any
repo-level AGENTS migration begins.

Why:

- the current playbook already says Phase 0 must complete before Phase 1
- calibration artifacts show that acceptance and migration were previously
  blended too early
- a standalone change keeps the acceptance question auditable

Alternative considered:
- Start Phase 1 immediately and backfill the acceptance decision later.
  - Rejected because the repo already forbids workflow-level backfill after the
    fact, and the current evidence says `candidate != accepted`.

### Decision: Repo scope comes first; root dotfiles are deferred by default

This change should only govern repository-local behavior and artifacts first.
Root-level dotfiles may be related, but they are not automatic scope for this
change.

Why:

- the user's current direction explicitly prioritizes the repo `AGENTS.md`
- mixing repo and root scope would make the acceptance question unstable again
- dotfile alignment can become a later follow-up once the repo mainline is
  explicit

Alternative considered:
- Include `~/.codex/AGENTS.md` and `~/.claude/CLAUDE.md` immediately.
  - Rejected because that would broaden the change from repo governance into
    personal/global configuration alignment.

### Decision: Duplicate ADR numbering is Phase 0 work, not deferred cleanup

The duplicate `ADR-0007` conflict is already a repo-visible contradiction
inside the governance surface, so it belongs in Phase 0.

Why:

- Phase 0 is the acceptance gate for repo governance
- duplicate ADR numbering weakens the decision surface that Phase 0 depends on
- the conflict is already concrete and local to the repo

Alternative considered:
- Leave the duplicate ADR conflict for a later cleanup pass.
  - Rejected because the repository should not accept a new governance mainline
    while the local ADR identity surface is already contradictory.

### Decision: Commit-gate inclusion must be explicit

The change must decide whether a repo-local commit gate, such as
`.githooks/pre-commit`, is part of the required Phase 0 acceptance set or
whether it stays as a deferred enforcement layer.

Why:

- the candidate playbook treats a commit gate as central
- the repository should not imply that the gate exists unless it is actually
  accepted and implemented
- this is one of the few items that materially changes whether Phase 1 can
  safely begin

Alternative considered:
- Assume the commit gate is required without explicitly deciding it.
  - Rejected because that would repeat the same overclaim pattern seen in the
    distill artifacts.

## Publication Plan

This change is expected to publish, at minimum:

- proposal / design / tasks for the repo-level Phase 0 change
- one new ADR or equivalent repo-visible stable decision that records the
  accepted repo-level mainline
- one ADR-numbering fix that removes the duplicate `ADR-0007` conflict
- repo-visible notes for any deferred items that are intentionally left out

Whether the change also updates `AGENTS.md` with Phase 0 gate wording should be
decided during implementation, not assumed by this design alone.

## Pressure-Test Plan

Validate the change against these cases:

1. A contributor wants to start compressing repo `AGENTS.md` immediately.
   - Expected result: the repository points back to Phase 0 acceptance first.
2. A contributor tries to expand the same change into root dotfiles.
   - Expected result: the repository marks root dotfiles as deferred unless the
     change scope is explicitly widened.
3. A contributor claims the governance mainline is accepted while duplicate
   `ADR-0007` numbering still exists.
   - Expected result: the change remains incomplete.
4. A contributor assumes the commit gate exists without a concrete accepted
   implementation decision.
   - Expected result: the change records that as undecided or incomplete, not
     accepted by implication.

## Risks / Trade-offs

- [Risk] The change may still be read as acceptance of the full v3.1 model.
  - Mitigation: keep the acceptance boundary explicit and narrow.
- [Risk] Phase 0 may grow into Phase 1 by adjacency.
  - Mitigation: keep compression/proxy migration in explicit non-goals and
    separate tasks.
- [Risk] Deferring root dotfiles may leave cross-file drift unresolved.
  - Mitigation: record the deferral explicitly so the gap remains visible.
