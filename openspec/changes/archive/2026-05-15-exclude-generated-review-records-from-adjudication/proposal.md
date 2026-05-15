# Exclude Generated Review Records From Adjudication

## Why

`wiki-doctor` review records and `wiki-review-decisions` records are outputs of
the diagnostic loop. If later adjudication scans include those generated records
as ordinary wiki content, the doctor starts diagnosing its own medical records
and review sheets. That inflates candidate counts and creates false follow-up
work.

## What Changes

- Exclude generated doctor review records under `wiki/ops/wiki-doctor-runs/`
  from adjudication candidates.
- Exclude generated review-decision records under
  `wiki/ops/wiki-review-decisions/` from adjudication candidates.
- Preserve review-only behavior: no frontmatter writes, taxonomy writes,
  relation writes, MOC writes, or repair execution.

## Out Of Scope

- Changing the generated records already committed.
- Changing skill trigger behavior.
- Applying any structural wiki repair.

