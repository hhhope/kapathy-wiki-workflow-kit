# Add Wiki Surgery Planning

## Why

Treatment now covers explicitly approved low-risk frontmatter repair. The next
missing layer is surgery planning: large, structural, governance-sensitive, or
MOC-related work must be turned into a reviewable surgery plan before any write
happens.

## What Changes

- Add a `wiki-surgery` planning layer.
- Classify adjudication risks into surgery buckets.
- Include MOC projection dry-run entries as surgery inputs when provided.
- Write optional Markdown surgery records under `wiki/ops/wiki-surgery-runs/`.
- Keep surgery planning non-writing: no frontmatter, taxonomy, relation, MOC,
  ADR, or OpenSpec state mutation.

## Out Of Scope

- Applying surgery.
- Writing MOC pages.
- Mutating taxonomy config.
- Writing relations.
- Creating or completing OpenSpec changes from surgery items.
- Recovery record implementation.

