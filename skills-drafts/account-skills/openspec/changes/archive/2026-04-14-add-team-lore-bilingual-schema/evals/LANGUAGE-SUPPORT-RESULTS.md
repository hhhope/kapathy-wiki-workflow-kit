# Language Support Results — minimal alias contract

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This file records before/after evidence for the minimal mixed-language routing step in the draft migration slice.

## RED — Before alias update

Observed gaps:

- the draft page contract mentioned language support, but the draft pages themselves did not expose explicit routing aliases
- the updated templates improved readability and boundaries, but mixed-language routing still depended on title similarity and lucky terminology overlap
- `DRAFT-RESULTS.md` still showed mixed-language compatibility as the weakest dimension

Why this was still RED:

- an English-first or Chinese-first page could still be routed inconsistently if the prompt used a different term family
- there was no explicit page field carrying cross-language routing intent

## GREEN — After alias update

The minimal language-support step now adds:

- `Aliases` to the page contract
- `Aliases` to the four Lore templates
- `Aliases` to the first five draft migration pages

The change intentionally stops at `Aliases` instead of adding full bilingual summaries immediately.

Why:

- aliases are the smallest routing-oriented field that can be checked structurally
- they improve cross-language hit quality without forcing a second full content rewrite
- they let us test whether explicit routing aids are enough before expanding into fuller bilingual surfaces

## Verification

Manual and structural evidence:

- all target draft pages now expose `## Aliases`
- all updated Lore templates now expose `## Aliases`
- `DRAFT-RESULTS.md` now records mixed-language compatibility as improved from `0 Pass / 2 Partial / 2 Fail` to `1 Pass / 3 Partial / 0 Fail`

## Limits

- this is routing support, not full bilingual content
- this does not prove mixed-language first-load interpretation is fully solved
- fuller bilingual summaries or mirrored sections remain follow-up work if the alias layer is insufficient
