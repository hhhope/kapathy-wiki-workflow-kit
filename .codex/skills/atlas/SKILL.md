---
name: atlas
description: Use when continuing, repairing, or completing stateful learning/report collaboration with confirmed anchors, rejected framings, evidence boundaries, visual decisions, H5/share drafts, reports, presentations, wiki/Feishu drafts, or repeated drift.
---

# Atlas

## Purpose

Control stateful learning/report collaboration before worker skills act. Atlas
preserves confirmed anchors, chooses the allowed next action, routes worker
skills, and blocks completion claims when the artifact has drifted.

Atlas is a controller, not a writer, source reader, visual worker, OpenSpec
router, or publishing tool.

## Trigger

Use Atlas when both are true:

- The user wants to continue, confirm, repair, implement, review, complete, or
  re-anchor work.
- The current task is a stateful learning/report collaboration.

Stateful learning/report collaboration includes reports, H5/share drafts,
presentations,演讲稿, wiki/Feishu drafts, material processing, or visual report
work with any confirmed anchor, rejected framing, evidence boundary, selected
output shape, or drift history.

Do not use Atlas for simple one-off work such as a narrow command, lookup,
small grammar edit, isolated code task, or private scratch note with no durable
learning/report artifact.

## Required State Block

Before continuing an Atlas-triggered task, emit this compact block:

```text
- `Using atlas`
- `Current Object`:
- `Current Phase`:
- `Confirmed Anchors`:
- `Allowed Actions`:
- `Blocked Actions`:
- `Open Gaps`:
- `Worker Route`:
- `Next Output`:
```

If `Current Phase` is unclear, set it to `unclear`, allow only clarification or
re-anchor, and block producing or editing the delivery artifact.

## Phases

Use the smallest fitting phase:

- `intent_calibration`
- `structure_lock`
- `evidence_mapping`
- `drafting`
- `visual_binding`
- `implementation`
- `review_or_reanchor`
- `unclear`

## Hard Stops

- Do not continue when phase is unclear; re-anchor first.
- Do not rename, merge, reorder, or compress confirmed chapters, sections,
  talk-track structure, or transitions silently.
- Do not compress approved per-section visuals into one generic visual unless
  the user explicitly approves the compression.
- Do not turn incomplete LinkedIn, JD, profile, or sample evidence into broad
  organization-wide claims.
- Do not claim done, fixed, review-ready, synced, or complete before the Final
  Drift Gate passes.
- Do not use Atlas for simple one-off work.
- Do not use Atlas to replace OpenSpec lifecycle gates or worker skill
  ownership.

## Worker Ownership

Atlas routes workers after the state block:

- `learning-capture`: source roles, learning level, evidence strength,
  proof-boundary, and evidence blocker.
- `public-report-quality-gate`: reader-facing intent, output shape, report
  quality, paragraph drift, judgment ownership, and review/publish boundary.
- `visual-agent`: visual mode, visual task classification, visual proof
  binding, visual worker route, and visual verification.
- `material-collaboration-defaults`: source-first material intake and
  incremental material processing.

Workers must preserve Atlas `Confirmed Anchors`, `Allowed Actions`, and
`Blocked Actions`. If a worker finds a blocker, route back to Atlas for
re-anchor.

## References

Load only the needed reference:

- Continuation state details:
  `references/continuation-state-gate.md`
- Scorecard families:
  `references/scorecard-registry.md`
- Worker routing:
  `references/worker-routing.md`
- Final Drift Gate completion check:
  `references/final-drift-gate.md`
- Replay and pressure scenarios:
  `references/replay-scenarios.md`

## Common Mistakes

- Treating `继续`, `可以`, or `确认` as permission to start a new structure.
- Letting visual work replace the confirmed content model.
- Treating source learning, report quality, or visual routing as Atlas-owned
  work instead of worker-owned work.
- Promoting a Stripe-specific correction into universal skill governance
  without evidence.
