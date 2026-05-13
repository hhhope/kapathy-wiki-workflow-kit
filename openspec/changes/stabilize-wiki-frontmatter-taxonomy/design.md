# Design

## Contract Boundary

`wiki/config/frontmatter-taxonomy.yaml` is the only source for allowed values,
forbidden values, path rules, severity, producer paths, and sample migration
paths. AGENTS and skills must not duplicate taxonomy vocabularies.

## Runtime Boundary

`.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` owns workflow only:

- when to load the taxonomy contract
- how to treat user and AI language as classification hints
- how to run the checker
- how to interpret drift

## Checker Boundary

`scripts/check_wiki_frontmatter.py` reads the YAML contract and emits:

- `/tmp/wiki-frontmatter-taxonomy-report.json`
- `/tmp/wiki-frontmatter-taxonomy-report.md`

The checker validates repository content and registered producers. It only emits
text-level warnings for possible unregistered producers and does not attempt
general Python static analysis.

## Producer Boundary

Repo-local templates and scripts that create wiki frontmatter must be registered
under `producer_paths`. External users and AI systems are not scanned; their
language becomes hints that must validate before being treated as final
frontmatter.

## Migration Boundary

Only pages in `sample_migration_paths` are required to pass the first rollout as
new-model pages. Legacy pages can continue to produce warnings until a later
migration change.
