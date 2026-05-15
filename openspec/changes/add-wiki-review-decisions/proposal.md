# Proposal: add wiki review decisions

## Summary

Add a repo-local `wiki-review-decisions` workflow that turns `wiki-doctor`
diagnosis output into a repo-visible human review decision record.

## Problem

The repository now has a medical-loop model:

```text
checkup -> doctor -> review -> treatment -> surgery -> recovery -> archive
```

`wiki-doctor` can produce diagnosis records, but the next stage, `review`, is
not executable yet. Without a review-decision artifact, agents can still jump
from diagnosis to repair language without leaving a confirmed decision record.

The repository needs a first-class, review-only workflow that consumes the
adjudication package and produces a draft decision record for human confirmation.

## Scope

In scope:

- Add a `wiki-review-decisions` repo-local skill.
- Add a script that derives a review-decision package from the existing
  adjudication package.
- Add an explicit CLI for writing non-overwriting Markdown decision records
  under `wiki/ops/wiki-review-decisions/`.
- Classify findings into draft buckets: accepted candidates, rejected
  candidates, deferred items, treatment candidates, surgery candidates, and
  OpenSpec-required items.
- Add tests and behavior-asset evaluation evidence.

Out of scope:

- Writing frontmatter, taxonomy config, relation fields, MOC files, ADRs,
  AGENTS, or OpenSpec lifecycle state.
- Implementing `wiki-treatment`, `wiki-surgery`, or `wiki-recovery`.
- Treating draft decisions as human approval.
- Parsing doctor Markdown as the source of truth when the adjudication package
  is available.

## Success Criteria

- `wiki-review-decisions` is available as a repo-local skill.
- The review-decision CLI writes a Markdown record only when explicitly asked.
- The record points to source details and clearly states it is draft review
  routing, not repair approval.
- Focused tests cover classification, non-overwrite writes, CLI behavior, and
  skill markers.
- OpenSpec validation, behavior asset checks, and focused tests pass or record
  bounded pre-existing failures.
