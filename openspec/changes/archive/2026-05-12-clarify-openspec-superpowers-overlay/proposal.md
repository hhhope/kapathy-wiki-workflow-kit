# Clarify OpenSpec / Superpowers Execution Overlay

## Why

The `add-product-status-contract` run showed an artifact-authority drift: OpenSpec
`tasks.md` was the intended lifecycle and progress source, but the Superpowers
`implementation-plan.md` introduced independent `Task 1..6` sections, progress
checkboxes, commit slices, and a final "sync tasks.md" step. That made the
Superpowers plan look like a second task ledger.

The issue is not that Superpowers planning is bad. The useful parts were TDD
strategy, module decomposition, verification commands, commit strategy, and
handoff guidance. The problem is letting those execution tactics compete with
OpenSpec task progress.

## What Changes

- Clarify the repo-local `openspec-apply-change` skill so detailed Superpowers
  planning inside an OpenSpec change is treated as an execution overlay.
- Require `tasks.md` to remain the only progress and completion ledger.
- Forbid execution overlays from defining independent task ids or progress
  checkboxes.
- Keep commit strategy as recovery evidence, not progress truth.
- Add replay evidence using the real `add-product-status-contract` plan shape.

## Non-Goals

- Do not edit the external Superpowers plugin.
- Do not change `add-product-status-contract` implementation.
- Do not require an overlay for every OpenSpec change.
- Do not force every overlay section to mirror each OpenSpec task id.
