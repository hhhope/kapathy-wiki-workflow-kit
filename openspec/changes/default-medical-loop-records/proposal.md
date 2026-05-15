# Proposal: default medical loop records

## Summary

Make `wiki-doctor` and `wiki-confirm` create complete repo-visible medical-loop
records by default.

The current CLI behavior preserves stdout JSON unless the user explicitly asks
to write a record. That matched the older implementation-shaped
`wiki-review-decisions` workflow, but it now conflicts with the user-facing
medical-loop model: diagnosis and confirmation should leave a durable chart
entry.

## Problem

The repository now presents the wiki self-evolution workflow as:

```text
wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery
诊断 -> 确诊 -> 治疗 -> 手术 -> 复查
```

In a medical loop, diagnosis and confirmation are not transient console views.
They should record what was examined, which standards were applied, what was
abnormal, and what next-stage advice was given.

The current scripts already can write records, but only with explicit flags:

- `scripts/build_wiki_content_adjudication.py --write-review-record`
- `scripts/build_wiki_review_decisions.py --write-decision-record`

This makes it easy for an agent to run diagnosis or confirmation, summarize
truncated stdout, and leave no durable record for treatment, surgery, recovery,
or later audit.

## Scope

In scope:

- Change doctor and confirm CLIs so default execution writes complete records.
- Keep explicit stdout-only mode for debugging.
- Ensure default written records are not truncated by preview limits.
- Update record Markdown sections so they read like diagnosis and confirmation
  reports, not just bucket dumps.
- Update `wiki-doctor`, `wiki-confirm`, and the legacy
  `wiki-review-decisions` skill contracts.
- Add regression tests for default writing, stdout-only mode, full record
  writing, and skill markers.
- Preserve that generated records are excluded from later adjudication scans.

Out of scope:

- Applying frontmatter, taxonomy, relation, MOC, ADR, or OpenSpec changes.
- Treating doctor or confirm records as human approval for treatment or
  surgery.
- Changing treatment, surgery, recovery, or archive execution semantics.
- Removing stdout JSON support entirely.

## Success Criteria

- Running `python3 scripts/build_wiki_content_adjudication.py` writes a complete
  diagnosis record under `wiki/ops/wiki-doctor-runs/` and prints a compact
  summary containing the record path.
- Running `python3 scripts/build_wiki_review_decisions.py` writes a complete
  confirmation record under `wiki/ops/wiki-review-decisions/` and prints a
  compact summary containing the record path.
- `--stdout-json-only` preserves the old non-writing JSON inspection mode.
- `--limit` applies only to stdout preview or explicit preview behavior, not to
  the full written record.
- Doctor records include exam items, reference standards, abnormal findings,
  proof boundary, and recommended next stage.
- Confirm records include decision rules, fixed buckets, abnormal findings,
  medical advice, and proof boundary.
- Focused unit tests and OpenSpec validation pass or record bounded existing
  failures.
