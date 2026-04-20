## Context

The repository now has a formal disagreement-management method and a stable ADR-level decision that conclusion promotion must come after disagreement preservation.

What it still lacks is a reusable validation surface.

Right now the method's evidence lives mostly in one formalization thread. That is enough to justify the method, but not enough to show that future contributors can validate new disagreement threads consistently.

The user asked to continue with more replay / harness validation before runtime behavior work.

## Goals / Non-Goals

**Goals**

- Publish a small reusable replay harness for disagreement-management validation.
- Add at least one more replay case that exercises a different disagreement shape.
- Keep the new proof repo-visible and reusable.
- Preserve the boundary that this is validation work, not runtime automation.

**Non-Goals**

- Do not add automatic triggers.
- Do not add a new skill.
- Do not change disagreement-capture runtime behavior.
- Do not claim rollout proof.

## Decisions

### Decision: Use a lightweight harness instead of executable automation first

The next step should be a reusable manual harness, not a scripted test system.

Alternative considered:
- Build an executable harness immediately.
  - Rejected because the method is still proving its behavioral shape, and premature automation would hide the operator judgment that still matters.

### Decision: Replays should cover disagreement shapes, not just repeated topics

Additional validation should target a different disagreement shape from the initial formalization runs.

Alternative considered:
- Replay more samples of the same governance-shaped disagreement.
  - Rejected because it would increase volume without increasing coverage.

### Decision: Replay proof and rollout proof stay separate

The harness should explicitly record that replay validation is stronger than narrative design reasoning, but still weaker than rollout proof.

Alternative considered:
- Treat successful replay validation as sufficient rollout proof.
  - Rejected because automatic triggering correctness and multi-session behavior are still untested.

## Minimal Harness Shape

Each replay should capture:

- thread label
- disagreement shape
- rejected framing
- correction pressure
- redirection moment
- clarity state
- protected target, if visible
- RED baseline
- GREEN result
- residual risk

## Validation Plan

This change should produce:

1. a reusable harness page under `wiki/ops/`
2. an additional replay validation page under `wiki/ops/`
3. change-local `evaluation.md` and `verification.md`

## Risks / Trade-offs

- [Risk] The harness may become too template-heavy. -> Mitigation: keep the fields minimal and subordinate to the preserved material.
- [Risk] A new replay may still resemble the old ones too much. -> Mitigation: choose a disagreement shape centered on stage-boundary or scope-boundary rather than governance symptom routing.
- [Risk] Contributors may overstate what replay proof means. -> Mitigation: explicitly restate that replay validation is not rollout proof.
