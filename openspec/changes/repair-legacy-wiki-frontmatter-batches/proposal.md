# Proposal: repair legacy wiki frontmatter batches

## Why

The wiki medical recovery check is still blocked by repository-wide legacy
frontmatter debt. The current recovery evidence reports:

- `frontmatter_precheck`: failed
- `blocking_count`: 916
- `next_route`: `blocked_by_recovery_findings`

Existing completed changes already created the strict gate, taxonomy checker,
precheck command, repair planner, and target-vs-repository recovery reporting.
They intentionally did not bulk-migrate legacy pages.

This change owns the next layer: applying explicit, reviewable frontmatter
repair batches until the whole-wiki strict gate can pass, or until remaining
items are explicitly split into separate reviewed follow-ups.

## What Changes

- Use the existing frontmatter repair planner to select explicit batches.
- Start with the first planner batch: ADR 0001-0010.
- Apply only approved frontmatter fields.
- Record before/after target-level precheck evidence for every changed page.
- Record whole-wiki residual blocker counts after each batch.
- Keep relation fields, taxonomy config, MOC pages, ADR decision content, and
  OpenSpec lifecycle state out of the repair apply path.

## Out of Scope

- Changing taxonomy vocabulary or checker scoring.
- Inferring business domains from prose.
- Writing relation fields or graph edges.
- Rewriting ADR decisions, governance text, or page bodies.
- Treating generated batch evidence as archive-ready proof until recovery is
  re-run and the medical case next action is updated by the proper workflow.

## Acceptance

- Each repaired page has a target-level precheck before and after the edit.
- Applied fields are limited to approved frontmatter keys.
- Whole-wiki strict gate residual counts are recorded after each batch.
- The active medical case remains blocked unless recovery actually reports a
  clean route.
