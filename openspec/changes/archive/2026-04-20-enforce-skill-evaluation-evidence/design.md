## Context

The repository has already solved several adjacent governance gaps:

- draft skills cannot masquerade as published skills
- repo health-check can catch structural publication regressions
- principle skills now have a formal publication layer

What is still missing is a hard gate for behavior-proof evidence. Today a skill change can still appear "done" if it has:

- a valid OpenSpec change
- a published `.codex/skills/.../SKILL.md`
- a `verification.md` file with only structure proof

That is insufficient for semantic skill changes. The repository needs a dedicated artifact and an executable check that distinguish:

- structure proof
- behavior proof

## Goals / Non-Goals

**Goals**

- Make behavior-proof evidence explicit and reviewable.
- Require that evidence only when an active change really touches project-local skills.
- Fail the repo health-check when the evidence is missing.

**Non-Goals**

- Automate the actual subagent evaluation runs.
- Require `evaluation.md` for ordinary docs or non-skill workflow changes.
- Rewrite existing archived changes retroactively in this change.

## Decisions

### Decision: Use `evaluation.md` as the dedicated behavior-proof artifact

Behavior-proof evidence should not hide inside `verification.md`, because structure and behavior are different proof types. A separate `evaluation.md` makes the gap visible.

Required sections:

- `## Baseline Scenarios`
- `## Before Results`
- `## After Results`
- `## Residual Risks`

Alternative considered:
- Keep using `verification.md` only.
  - Rejected because it allows structure checks to impersonate behavior checks.

### Decision: Gate only active changes that touch `.codex/skills/`

The repository should not require `evaluation.md` for every change. The rule triggers only when an active change references `.codex/skills/` in its artifacts, which is the repo's formal signal that skill publication or semantic skill work is in scope.

Alternative considered:
- Require `evaluation.md` for all behavior-asset changes.
  - Rejected because that is broader than the immediate failure mode and would add noise.

### Decision: Enforce through repo health-check

The repo already has a health-check entry point. Extending it is the narrowest way to convert the rule from prose into a real gate.

Alternative considered:
- Document the rule in AGENTS only.
  - Rejected because that reproduces the current failure mode.

## Evaluation Plan

### Baseline scenario

- Create a temporary repo with an active change that references `.codex/skills/example/SKILL.md` but lacks `evaluation.md`.
- Before implementation, the repo health-check test fails because the new evidence check does not exist.

### After-change expectation

- The same repo reports a failing `skill-evaluation-evidence` check and points to the missing change.
- A repo with the same skill reference plus a valid `evaluation.md` passes.

## Risks / Trade-offs

- [Risk] The trigger may miss unusual skill changes that avoid `.codex/skills/` references. -> Mitigation: the rule uses the repo's formal publication path, which is the intended change pattern.
- [Risk] Some contributors may add placeholder `evaluation.md` files. -> Mitigation: require named sections so empty stubs are easier to spot and extend later if needed.
