# Proposal: add completion bridge gate

## Why

The medical-loop surgery review left `detail-0055` as an OpenSpec candidate:
`wiki/ops/completion-bridge-drift-explore-2026-05-12.md`.

That trace records a recurring AI conversation drift: after a scoped OpenSpec
change completes, the assistant can correctly report delivery details while
failing to reconnect to the user's original north-star or method experiment.
For example, if the user asked to test the Superpowers + OpenSpec dual-track
workflow, a final answer that only says "files changed and tests passed" leaves
the actual experiment unanswered.

Existing specs cover nearby concerns:

- `archive-review-defaults` stops implementation and routes completion toward
  archive review.
- `conversation-north-star-handoff` preserves repeated north-star topics.
- `live-conversation-reanchor-gate` stops continuation when live drift is
  detected.

They do not yet define a completion-time bridge that requires the final report
to answer the original user question when such a question was part of the task.

## What Changes

- Define a completion bridge gate for scoped work completion and archive-ready
  reports.
- Require final reports to distinguish delivery evidence from the original
  user north-star, experiment, or evaluation question.
- Require an explicit answer to that original question when it was present and
  still answerable from completed work.
- Preserve the hard stop boundary: the bridge may report, ask, or propose next
  actions, but it must not continue implementation past completed OpenSpec
  scope.

## Scope

- Applies to repo workflow completion reports for OpenSpec-scoped work and
  similar bounded workflow tasks.
- Covers the reporting behavior after implementation, verification, completion,
  or archive review.
- Adds requirements only; implementation and runtime replay will be handled in
  the task plan for this change.

## Non-Goals

- Do not edit `.codex/skills/*`, `AGENTS.md`, or global rules in the proposal
  step.
- Do not change archive mechanics or allow implementation after `tasks.md` is
  complete.
- Do not require verbose retrospective output for every tiny task.
- Do not treat ordinary file-change summaries as sufficient when the user asked
  a broader evaluation question.

## Evidence

- Source trace:
  `wiki/ops/completion-bridge-drift-explore-2026-05-12.md`
- Medical case:
  `wiki/ops/wiki-medical-cases/2026-05-15-064427-wiki-medical-case.md`
- Related specs:
  `openspec/specs/archive-review-defaults/spec.md`,
  `openspec/specs/conversation-north-star-handoff/spec.md`,
  `openspec/specs/live-conversation-reanchor-gate/spec.md`
