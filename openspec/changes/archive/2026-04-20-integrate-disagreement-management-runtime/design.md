## Context

The repository now has enough upstream clarity to move from method definition into runtime integration.

Three things are already true:

1. the method is formally published
2. the stable policy is written into `AGENTS.md` and ADR
3. replay / harness validation exists beyond a single thread

The remaining gap is runtime behavior.

At the moment, the repository still relies too much on operator judgment for two critical transitions:

- when live disagreement should become a repo-visible `wiki/ops retro`
- when archive review should stop a change and ask whether disagreement material was lost, flattened, or promoted too early

## Goals / Non-Goals

**Goals**

- Make disagreement-to-`wiki/ops retro` routing explicit as a default runtime behavior.
- Add an archive-review gate for disagreement preservation / promotion.
- Keep the runtime rule minimal and tied to the already formalized method.

**Non-Goals**

- Do not add executable automation or bots.
- Do not redefine the disagreement method itself.
- Do not add a new skill.
- Do not redo replay / harness work already completed.

## Decisions

### Decision: Route live disagreement to `wiki/ops retro` when calibration work is still active

The repository should default to `wiki/ops retro` when a live disagreement is already doing calibration work and has enough shape to be repo-visible, but is not yet stable enough for `ADR`, spec, or skill promotion.

Alternative considered:
- Keep disagreement only in chat until a stable decision emerges.
  - Rejected because that is exactly where high-value process data is lost.

### Decision: Archive review must ask about disagreement preservation and promotion

Archive review should explicitly check whether the active change generated disagreement material that:

- should have remained in method / retro form
- should have been promoted to ADR
- was flattened away without a durable record

Alternative considered:
- Leave this entirely to ad hoc reviewer memory.
  - Rejected because the repository already observed this exact failure pattern.

### Decision: Keep runtime routing minimal

The runtime change should not attempt to solve trigger automation globally.
It should only connect the already formalized method to the two most important durable boundaries.

Alternative considered:
- Add broad automatic triggers across all conversation flows.
  - Rejected because it would reopen scope before the minimal runtime hooks are proven useful.

## Minimal Runtime Shape

The runtime integration should make these boundaries explicit:

1. live disagreement doing active calibration work
   -> preserve method material first
2. disagreement has enough shape for repo-visible durability but not stable decision
   -> `wiki/ops retro`
3. disagreement has finished enough calibration work to become stable cross-change policy
   -> `ADR`
4. change reaches archive review
   -> review must check whether disagreement preservation / promotion was skipped

## Evaluation Plan

Runtime proof for this change should show:

- the new default route to `wiki/ops retro`
- the new archive-review check
- at least one before/after scenario where archive review would have missed disagreement promotion without the new rule

## Risks / Trade-offs

- [Risk] The retro route may become noisy. -> Mitigation: only route disagreements that are actively doing calibration work and have enough shape to preserve.
- [Risk] Archive review may become heavier. -> Mitigation: keep the check narrow: was disagreement material lost, still open, or promotable?
- [Risk] Contributors may misread this as fully automated capture. -> Mitigation: explicitly state that this is still a default human-operated runtime rule.
