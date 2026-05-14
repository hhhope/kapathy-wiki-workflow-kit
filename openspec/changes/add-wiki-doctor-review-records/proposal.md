# Proposal: wiki-doctor review records

## Summary

Add an explicit repo-visible review-record path for `wiki-doctor` diagnosis.

## Problem

`wiki-doctor` can inspect and summarize the content adjudication review package,
but the diagnosis can disappear into stdout or chat. The repository needs a
durable, review-only artifact that preserves scan scope, summary counts,
taxonomy candidates, drift traces, eval warnings, proof boundary, and next
review actions for later human review.

## Scope

In scope:

- Add `wiki-doctor` review-record requirements.
- Add a non-overwriting Markdown review-record writer under `wiki/ops`.
- Add an explicit CLI flag for review-record generation.
- Update the `wiki-doctor` skill contract and runtime skill tests.
- Preserve behavior replay and skill evaluation evidence.

Out of scope:

- Applying frontmatter writes.
- Mutating `wiki/config/frontmatter-taxonomy.yaml`.
- Writing `wiki/moc` pages.
- Marking OpenSpec tasks complete from doctor output.
- Reopening `rename-wiki-content-adjudication-skill-to-doctor`.

## Success Criteria

- Default adjudication CLI behavior remains stdout-only.
- Explicit review-record generation writes a Markdown diagnosis under
  `wiki/ops/wiki-doctor-runs/`.
- Generated records include proof boundary and next review actions.
- `wiki-doctor` says review records are diagnosis evidence, not repair approval.
- Tests, behavior-asset checks, and OpenSpec validation pass or record bounded
  expected failures in `evaluation.md`.
