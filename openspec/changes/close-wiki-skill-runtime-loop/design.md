# Design

## Source Of Truth

The current wiki runtime source of truth is `.codex/skills/wiki-*`.
Slash-style files under `commands/` and `plugins/report-wiki-portfolio/commands/`
are removed from active runtime ownership.

## Skill Contract Shape

Each wiki skill owns:

- trigger/purpose
- scripts to run or reference
- artifacts to read
- summary fields to report
- boundaries
- next repair or inspection route

Skills must not reference `plugins/report-wiki-portfolio/commands`.
Skills must not use `/wiki:` invocation text as current runtime guidance.

## Frontmatter Repair Loop

`wiki-status` surfaces strict frontmatter gate data from
`scripts/build_wiki_status.py`. `wiki-apply` routes explicit page frontmatter
fixes to `scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`.
`wiki-frontmatter-taxonomy` remains the specialized frontmatter authority.

## Historical Boundary

Archived OpenSpec records may still mention `/wiki:*`; they are historical
evidence and not current runtime truth.
