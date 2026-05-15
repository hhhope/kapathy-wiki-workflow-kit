# Add Wiki Treatment Workflow

## Why

The LLM-WIKI medical loop now has doctor diagnosis and review-decision records,
but it still lacks the treatment step. After a user confirms low-risk findings,
the repository needs a bounded way to apply only approved frontmatter repairs
without turning treatment into surgery.

## What Changes

- Add a `wiki-treatment` planning and execution layer.
- Default to dry-run treatment plans.
- Allow frontmatter writes only when `--apply` is combined with explicit
  approved domains or detail refs.
- Leave taxonomy, relation, MOC, ADR, governance, and OpenSpec changes out of
  treatment.
- Add treatment records under `wiki/ops/wiki-treatment-runs/` when explicitly
  requested.

## Out Of Scope

- Batch surgery.
- MOC projection writes.
- Taxonomy mutation.
- Relation writes.
- Archiving completed OpenSpec changes.

