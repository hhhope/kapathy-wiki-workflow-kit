# enforce-whole-wiki-frontmatter-gate

## Why

The current frontmatter taxonomy checker is too narrow. It reports selected
drift but does not enforce whole-wiki frontmatter completeness. Users can see a
status health surface and reasonably assume the entire wiki is covered when
important pages are still missing required metadata.

Concrete misses:

- `wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md` lacks
  `layer`, `domain`, and `ops_area` but is not reported.
- `wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md`
  lacks taxonomy frontmatter fields and ADR pages are not covered by taxonomy
  path rules.

## What Changes

- Add ADR-0032 to make whole-wiki strict frontmatter governance a stable
  repository decision.
- Extend `wiki/config/frontmatter-taxonomy.yaml` with strict whole-wiki gate and
  scorecard configuration.
- Extend `scripts/check_wiki_frontmatter.py` so configured rule sets apply
  across `wiki/**`.
- Emit a frontmatter scorecard and strict-gate pass/fail result.
- Render strict frontmatter scorecard data in wiki status.
- Add RED/GREEN tests for the observed missed pages and scorecard behavior.

## Out of Scope

- Bulk-migrating every existing legacy page to pass the new gate.
- Inferring missing business domains from page prose.
- Replacing graph extraction or product status.
- Adding semantic ranking, embeddings, or hidden retrieval scoring.

## Source Design

- `docs/superpowers/specs/2026-05-14-whole-wiki-frontmatter-gate-design.md`

