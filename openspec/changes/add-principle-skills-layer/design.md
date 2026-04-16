## Context

The repository currently has two strong layers:

- governance and lifecycle constraints in `AGENTS.md`, ADRs, and OpenSpec
- scene-specific workflow skills such as meeting-note output and material-collaboration defaults

What is missing is a compact in-the-moment correction layer for common reasoning failures:

- assuming instead of clarifying
- overbuilding instead of using the smallest valid solution
- touching adjacent content instead of making a narrow change
- claiming completion without verification

The external `andrej-karpathy-skills` review showed that these failures can be reduced by a very short principle layer. The repo should adopt that idea without collapsing its richer workflow structure into a single global file.

## Goals / Non-Goals

**Goals**

- Add a dedicated principle layer without replacing current workflow skills.
- Keep each principle skill short enough to act as an immediate behavioral brake.
- Preserve the current distinction between governance, workflow skills, and agent role templates.

**Non-Goals**

- Rewrite existing workflow skills into principle skills.
- Collapse repo behavior into one global instruction file.
- Add more than the minimum principle set needed for the first layer.

## Decisions

### Decision: Add principle skills as a third layer, not as a replacement

The repository should keep:

- `AGENTS.md` for boundaries and routing
- workflow skills for scenario-specific contracts
- principle skills for high-frequency cross-cutting mistakes

Alternative considered:
- Put all principles directly into `AGENTS.md` only.
  - Rejected because discoverable local skills are the repo's formal reusable workflow surface.
- Replace workflow skills with a short principle card.
  - Rejected because principles cannot carry meeting-note or material-processing contracts.

### Decision: Start with four principles only

The first layer should stay small and memorable:

- clarify-before-acting
- simplicity-first
- surgical-changes
- verify-before-claiming

Alternative considered:
- Start with a larger principle catalog.
  - Rejected because too many principles would reduce recall and blur the purpose of the layer.

### Decision: Keep examples outside the AGENTS summary

`AGENTS.md` should only carry the short principle entry section. Longer examples and anti-patterns belong in the individual skill files so the repo entry stays compact.

Alternative considered:
- Expand AGENTS with all anti-pattern examples inline.
  - Rejected because it recreates the long-prose discoverability problem this change is trying to fix.

## Evaluation Plan

### Baseline scenario A: No principle-layer routing exists

- Before change, `AGENTS.md` has no short high-frequency principle section.
- Expected failure: the repo relies on longer governance text and scene-specific skills only.

### Baseline scenario B: No formal principle skills are published

- Before change, `.codex/skills/` contains workflow-oriented skills but no principle skills for clarification, simplicity, surgical edits, or verification claims.
- Expected failure: the missing layer cannot be discovered or reused as a project-local skill.

### After-change expectation

- `AGENTS.md` routes readers to a compact high-frequency principle section.
- The repo formally publishes exactly four principle skills under `.codex/skills/`.
- Workflow skills remain unchanged and distinct from the new principle layer.

## Risks / Trade-offs

- [Risk] The principle layer could duplicate AGENTS wording. -> Mitigation: keep AGENTS short and put detailed guidance in the skills.
- [Risk] Principle skills may become too verbose. -> Mitigation: enforce short files with direct rules and a small anti-pattern section.
- [Risk] Users may expect principle skills to replace workflow contracts. -> Mitigation: explicitly document the layer split in AGENTS and the design.
