# Wiki Frontmatter Taxonomy Drift Control Design

Date: 2026-05-13
Status: design-approved-for-review
Repository: report-wiki-portfolio

## Problem

The repository currently lets `domain` carry incompatible meanings. Some pages
use it for real business or topic domains, while many `wiki/ops` pages use
`domain: personal-ops` to mean "this belongs to the operations layer." That
mixes content taxonomy with workflow placement.

This drift affects users and agents:

- `personal-ops` looks like a business domain even though `wiki/ops/index.md`
  defines ops as the personal workflow and governance layer.
- `wiki/domains/` remains thin while `wiki/ops/` holds most operational records.
- Skills, templates, scripts, and manual AI drafts can each generate
  frontmatter differently.
- A rule written only in prompts or agent instructions can drift from templates
  and scripts that actually create files.

## Goal

Create a single repo-local taxonomy contract for wiki frontmatter and force all
repo-local frontmatter producers to validate against it before completion.

The first version should stop new `domain: personal-ops` drift, make existing
drift visible, and prove the intended model on a small set of migrated examples.

## Non-Goals

- Do not batch-migrate all existing `wiki/ops` pages.
- Do not redesign the full business domain taxonomy.
- Do not rewrite scorecard scoring formulas.
- Do not build a graph UI or query engine.
- Do not create a broad Python static analyzer for all possible code patterns.
- Do not move this rule set into global agent instructions.

## Core Model

The design separates four concepts that are currently blurred:

```yaml
layer: ops
domain: none
ops_area: agent-governance
canonical_object: behavior-replay-gate
artifact_type: method
```

- `layer` answers where the page lives in the wiki structure.
- `domain` answers the real business or topic domain only.
- `ops_area` answers which operational or governance workflow the page serves.
- `canonical_object` remains the stable object identity for graph/runtime use.
- `artifact_type` remains the document shape.

`personal-ops` is no longer a valid `domain` for new or touched frontmatter.

`domain: none` and `domain: unclassified` have distinct meanings:

- `none`: the page is confirmed to have no business or topic domain, such as a
  pure governance method page.
- `unclassified`: the page should have a real domain, but the current input is
  not enough to classify it.

When `domain: unclassified` is used, the page should also carry
`classification_needed: true`.

## Single Rule Source

Add one repo-local config file:

```text
wiki/config/frontmatter-taxonomy.yaml
```

It is the only source for taxonomy vocabulary and policies. It should define:

- field meanings
- allowed `layer` values
- allowed `ops_area` values
- known `domain` values
- forbidden `domain` values
- path rules
- severity levels
- registered producer paths
- sample migration paths for the first rollout

Example shape:

```yaml
version: 1

fields:
  layer:
    allowed:
      - sources
      - domains
      - timeline
      - reports
      - ops
      - adr
      - spec
      - examples

  domain:
    meaning: business_or_topic_only
    allow_none: true
    require_classification_flag_for_unclassified: true
    forbidden:
      - personal-ops
    known:
      - none
      - unclassified
      - nirvana
      - nirvana-project
      - account-clearing
      - agentic-collaboration
      - report-workflow
      - wiki
      - agent-harness

  ops_area:
    allowed:
      - agent-governance
      - learning-capture
      - wiki-runtime
      - report-quality
      - meeting-notes
      - source-intake
      - workflow-trace

path_rules:
  wiki/ops:
    required:
      - layer
      - domain
      - ops_area
    layer: ops
    domain_policy: none_or_real_domain_or_unclassified

  wiki/domains:
    required:
      - layer
      - domain
    layer: domains
    domain_policy: required_real_domain

  wiki/sources:
    required:
      - layer
      - domain
    layer: sources
    domain_policy: real_domain_or_unclassified

severity:
  forbidden_domain: error
  missing_ops_area_on_ops_page: error
  missing_domain_on_touched_ops_page: error
  producer_hardcoded_forbidden_domain: error
  unknown_domain: warn
  missing_layer_on_legacy_page: warn
  possible_unregistered_producer: warn

producer_paths:
  templates:
    - wiki/templates/*.md
    - .codex/skills/**/references/*template*.md
  scripts:
    - scripts/inbox_intake.py

sample_migration_paths:
  - wiki/ops/behavior-replay-gate.md
  - wiki/ops/learning-capture-routing.md
  - wiki/ops/agent-readable-wiki-semantic-scoring.md
  - wiki/ops/nirvana-协议支付涅槃需求文档-intake.md
  - wiki/ops/nirvana-preview-intake.md
```

The taxonomy skill and checker must read this file. They must not duplicate its
allowed values.

## Repo Skill Gate

Add a repo-local skill:

```text
.codex/skills/wiki-frontmatter-taxonomy/SKILL.md
```

The skill owns the workflow, not the vocabulary. It should:

- trigger when creating or modifying wiki frontmatter, wiki templates, or
  repo-local producers that generate wiki frontmatter
- load `wiki/config/frontmatter-taxonomy.yaml`
- classify user, AI, script, and template values as hints until validated
- run `scripts/check_wiki_frontmatter.py`
- explain drift reports and required fixes
- avoid copying domain or `ops_area` vocabularies into the skill body

Existing producer skills and templates should route through this gate when they
generate wiki frontmatter. The important first producer template is:

```text
.codex/skills/article-learning-capture/references/wiki-template.md
```

It currently hardcodes `domain: personal-ops` and should be updated under the
OpenSpec implementation change.

## AGENTS Boundary

Repo `AGENTS.md` should not contain the taxonomy vocabulary. It should contain
only the hard route and completion gate:

```text
When creating or modifying wiki frontmatter, wiki templates, or repo-local
frontmatter producers, load `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`.

Before claiming taxonomy compliance or completion, run the repo frontmatter
taxonomy checker. Do not claim compliance from memory.
```

This prevents AGENTS, the skill, and YAML from becoming three independent rule
sources.

## Checker

Add:

```text
scripts/check_wiki_frontmatter.py
```

The checker is the machine evidence source. It should read
`wiki/config/frontmatter-taxonomy.yaml` and produce:

```text
/tmp/wiki-frontmatter-taxonomy-report.json
/tmp/wiki-frontmatter-taxonomy-report.md
```

It should perform four checks in version 1.

### Content Drift

Scan `wiki/**/*.md` and report:

- forbidden domain values, especially `domain: personal-ops`
- `wiki/ops` pages listed in `sample_migration_paths` missing `domain`
- `wiki/ops` pages missing `ops_area`
- `domain: unclassified` without `classification_needed: true`
- path and `layer` mismatches

Legacy missing fields can warn rather than fail. Forbidden domain values and
sample migration violations should fail.

### Registered Producer Drift

Scan registered producer paths from YAML:

- `wiki/templates/*.md`
- `.codex/skills/**/references/*template*.md`
- `scripts/inbox_intake.py`

Report hardcoded forbidden values and known direct producer patterns that bypass
the taxonomy contract.

### Possible Unregistered Producer Warning

Do not build a broad static analyzer. Use a text-level warning only:

- if a repo-local script or skill reference contains frontmatter-looking text
  such as `---` plus `domain:` but is not listed in `producer_paths`, emit
  `possible_unregistered_producer` as a warning.

This catches obvious producer drift without trying to understand all Python
string construction patterns.

### Report Shape

The Markdown report should be readable by maintainers and include:

- summary counts by severity
- content drift entries
- registered producer drift entries
- possible unregistered producer warnings
- next actions

The JSON report should preserve structured entries for future automation.

## Producer Handling

Repo-local producers are the only source code scanned. External users and AI
systems are not scanned; their natural-language input is treated as a hint.

For repo producers:

- templates should use controlled placeholders rather than hardcoded
  `personal-ops`
- scripts should not directly trust folder names as final `domain`
- `scripts/inbox_intake.py` may infer a `domain_hint`, but final frontmatter
  must validate against the taxonomy contract
- any new script or template that creates wiki frontmatter must be registered in
  `producer_paths`

The first implementation should prefer validation and explicit drift reports
over automatic rewriting.

## Sample Migration

Migrate only a small sample set to prove the boundary:

- `wiki/ops/behavior-replay-gate.md`
  - `layer: ops`
  - `domain: none`
  - `ops_area: agent-governance`
- `wiki/ops/learning-capture-routing.md`
  - `layer: ops`
  - `domain: none`
  - `ops_area: learning-capture`
- `wiki/ops/agent-readable-wiki-semantic-scoring.md`
  - `layer: ops`
  - `domain: none`
  - `ops_area: wiki-runtime`
- `wiki/ops/nirvana-协议支付涅槃需求文档-intake.md`
  - `layer: ops`
  - `domain: nirvana`
  - `ops_area: source-intake`
- `wiki/ops/nirvana-preview-intake.md`
  - `layer: ops`
  - `domain: nirvana`
  - `ops_area: source-intake`

These examples prove `none`, real domain, and `ops_area` behavior without
turning the change into a full migration.

## Validation Evidence

Because the change affects repo-local skills, the OpenSpec implementation must
include `evaluation.md` with:

- pressure scenarios
- RED baseline
- GREEN result
- residual risks

Minimum evidence:

- RED: existing article-learning wiki template hardcodes
  `domain: personal-ops`; checker reports it as producer drift.
- RED: an ops governance page with `domain: personal-ops` reports content
  drift.
- GREEN: migrated sample governance pages pass with `domain: none` and
  appropriate `ops_area`.
- GREEN: migrated business intake pages pass with real `domain` and
  `ops_area: source-intake`.
- GREEN: producer templates no longer hardcode `domain: personal-ops`.
- Residual risk: legacy pages still contain drift until future migration.

## OpenSpec Change

This is a repo workflow and taxonomy behavior change, so implementation should
start with an OpenSpec change such as:

```text
stabilize-wiki-frontmatter-taxonomy
```

The change should cover:

- taxonomy YAML contract
- taxonomy repo skill
- checker script
- AGENTS route and completion gate
- registered producer template updates
- sample page migration
- evaluation evidence

It should not include full legacy migration, scorecard algorithm changes, or a
complete business domain taxonomy rebuild.

## Success Criteria

- New or touched wiki frontmatter cannot silently use `domain: personal-ops`.
- `domain: none` and `domain: unclassified` are distinguishable and checked.
- `wiki/ops` pages have an explicit `ops_area` when brought under the new model.
- Repo producer templates that create wiki frontmatter are registered and
  checked.
- AGENTS, the taxonomy skill, and checker all point to the YAML contract instead
  of duplicating the vocabulary.
- The first implementation produces a drift report that makes legacy cleanup
  visible without requiring immediate batch migration.
