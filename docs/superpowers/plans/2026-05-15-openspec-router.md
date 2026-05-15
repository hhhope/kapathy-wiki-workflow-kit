# OpenSpec Router Implementation Plan

> Supports OpenSpec change: `add-openspec-router-governance`.
> This plan is an execution aid. OpenSpec remains the lifecycle source of truth.

**Goal:** Add a repo-local `openspec-router` skill and governance integration so
Superpowers method gates and OpenSpec lifecycle gates cannot bypass each other.

**Scope:** Governance and workflow assets only. No product code, backend,
frontend, runtime, migration, or report artifact changes.

## Files

Create:

- `.codex/skills/openspec-router/SKILL.md`
- `docs/superpowers/specs/2026-05-15-openspec-router-replay.md`
- `openspec/changes/add-openspec-router-governance/.openspec.yaml`
- `openspec/changes/add-openspec-router-governance/proposal.md`
- `openspec/changes/add-openspec-router-governance/design.md`
- `openspec/changes/add-openspec-router-governance/tasks.md`
- `openspec/changes/add-openspec-router-governance/specs/agent-workflow-routing/spec.md`
- `openspec/changes/add-openspec-router-governance/evaluation.md`

Modify:

- `AGENTS.md`
- `PROJECT.md`

## Tasks

- [x] 1. Inspect the team-knowledge reference implementation and classify what to reuse.
- [x] 2. Write Superpowers design and execution plan for this repo.
- [ ] 3. Create the repo-local `openspec-router` skill.
- [ ] 4. Create the OpenSpec governance change.
- [ ] 5. Update AGENTS.md and PROJECT.md with minimal routing integration.
- [ ] 6. Add replay evidence covering the original incident.
- [ ] 7. Run OpenSpec validation and behavior-asset checks.
- [ ] 8. Commit only task-related governance files.

## Red Baseline

The current incident is the RED baseline:

- Input contained `$superpowers:brainstorming`.
- The agent read the skill but wrote OpenSpec artifacts before the Superpowers
  written-spec review gate.
- `可以继续做` was treated as broad permission instead of advancing only the
  active gate.

## Green Target

For the same input, the expected route is:

```text
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.
```

OpenSpec edits occur only after the Superpowers review gate passes or when the
route is explicitly `write-openspec-change`.
