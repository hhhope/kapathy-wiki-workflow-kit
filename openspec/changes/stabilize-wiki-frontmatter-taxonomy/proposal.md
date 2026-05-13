# stabilize-wiki-frontmatter-taxonomy

## Why

The repository currently allows `domain` to mean both real business or topic
domain and personal operations layer. This caused pages with
`domain: personal-ops` to look like business-domain records even though
`wiki/ops` is an operations and governance layer.

The drift is not limited to existing pages. Repo-local skills, templates,
scripts, and AI-authored markdown can each produce frontmatter differently.
The repository needs one contract, one gate skill, and one checker to stop new
drift and make legacy drift visible.

## What Changes

- Add `wiki/config/frontmatter-taxonomy.yaml` as the single taxonomy contract.
- Add `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` as the routing gate for
  wiki frontmatter work.
- Add `scripts/check_wiki_frontmatter.py` to report content drift, registered
  producer drift, and possible unregistered producer warnings.
- Add AGENTS routing so frontmatter changes must use the taxonomy skill and
  checker before completion claims.
- Update known producer templates and `scripts/inbox_intake.py` so they stop
  generating `domain: personal-ops`.
- Migrate five sample pages to prove `domain: none`, real domains, and
  `ops_area` behavior.
- Record RED/GREEN evidence in `evaluation.md`.

## Out of Scope

- Batch migration of all legacy ops pages.
- Full business domain taxonomy redesign.
- Scorecard scoring formula changes.
- Graph UI, query engine, or broad static analysis of arbitrary Python code.
- Global agent instruction changes.

## Source Design

- `docs/superpowers/specs/2026-05-13-wiki-frontmatter-taxonomy-design.md`
