# Design

## Model

OpenSpec and Superpowers should remain complementary:

- OpenSpec owns scope, progress, completion, stop conditions, and archive review.
- Superpowers may provide execution tactics: TDD sequencing, module boundaries,
  verification commands, subagent usage, commit strategy, and handoff hints.

The drift appears when a Superpowers plan uses task-like structure:

- independent `Task N` headings
- progress checkboxes
- final `tasks.md` synchronization as a plan step
- ambiguous resume behavior

The replacement shape is an execution overlay:

- no progress checkboxes
- no independent task ids
- authority declaration at the top
- strategy sections instead of task ledger sections
- commit slices treated as recovery evidence
- `tasks.md` updated at OpenSpec task completion boundaries

## Target Artifact

The repo-local `.codex/skills/openspec-apply-change/SKILL.md` is the best
minimal target because it is loaded when applying OpenSpec changes. The skill is
compact today, so this change adds hard rules there and moves the longer real
example to `references/execution-overlay.md`.

## Replay Evidence

`evaluation.md` will include:

- pressure scenarios
- RED baseline from the real `add-product-status-contract/implementation-plan.md`
- GREEN expected overlay for the same change
- residual risks

This is behavior evidence for future agent routing, not proof that every future
session will comply without model variation.
