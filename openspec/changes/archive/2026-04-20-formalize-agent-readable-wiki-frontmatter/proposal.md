# Proposal: Formalize Agent-Readable Wiki Frontmatter

## Why

The repository now has a naming model for evolution-bearing pages, but naming alone
does not give agents enough structure to read page identity and relations directly.

The next missing layer is a minimal structured metadata contract for covered layers.
Without that contract, relation analysis and future graph extraction still depend too
heavily on prose and link guessing.

## What Changes

This change formalizes a minimal frontmatter and relation-field model for covered layers.

The model will define:

- required identity fields for covered-layer pages
- required relation fields for linking one object page to another
- which fields are stable anchors vs. optional descriptive helpers
- rollout policy for new pages vs. existing pages

This change only covers:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

This change does not:

- implement graph tooling
- implement relation extraction scripts
- rename old pages
- migrate old pages in bulk

## Success Criteria

- Covered-layer pages have a shared minimal metadata model for object identity.
- Covered-layer pages can express direct relation edges without relying only on prose.
- New pages in covered layers have clear required fields.
- Existing pages are not forced into immediate bulk migration.
