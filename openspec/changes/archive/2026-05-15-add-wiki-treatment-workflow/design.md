# Design

## Treatment Input

Treatment consumes the adjudication package because that package still contains
the candidate frontmatter fields needed to write pages. Review-decision records
remain human-readable confirmation evidence, but they do not carry enough data
to safely mutate pages by themselves.

## Approval Model

A detail can enter treatment only when all conditions are true:

- `safe_to_apply_frontmatter` is true.
- `risk_flags` is empty.
- the judgment state is `accept` or `likely`.
- either the candidate domain is explicitly approved or the detail ref is
  explicitly approved.

This makes domain approval a concrete gate without creating a broad approval
registry yet.

## Write Boundary

Treatment may write only page frontmatter fields from
`candidate.suggested_frontmatter`.

Treatment must not write:

- relation fields
- taxonomy config
- MOC pages
- ADRs as decisions
- OpenSpec state

The CLI defaults to JSON dry-run output. Page writes require `--apply`.

## Treatment Records

When explicitly requested, the CLI writes a Markdown treatment record under
`wiki/ops/wiki-treatment-runs/`. A record describes planned/applied treatment
items and skipped items; it is not a surgery approval.

Generated treatment records are excluded from future adjudication input for the
same reason as doctor and review-decision records: they are medical-loop
evidence artifacts, not new patient pages.
