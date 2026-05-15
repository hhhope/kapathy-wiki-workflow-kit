# Add Wiki Recovery Records

## Why

The medical loop now reaches surgery planning, but it still needs recovery:
after treatment or surgery, the repository should rerun bounded checks and
preserve a复查 record. Recovery proves the post-operation state; it does not
approve or apply repairs.

## What Changes

- Add a `wiki-recovery` runner that executes bounded non-mutating checks.
- Capture command, exit code, parsed summaries, and proof boundaries.
- Write optional Markdown recovery records under `wiki/ops/wiki-recovery-runs/`.
- Exclude generated recovery records from later doctor/adjudication input.

## Out Of Scope

- Applying treatment or surgery.
- Writing status files.
- Writing MOC pages.
- Mutating frontmatter, taxonomy config, relation fields, ADRs, or OpenSpec
  state.

