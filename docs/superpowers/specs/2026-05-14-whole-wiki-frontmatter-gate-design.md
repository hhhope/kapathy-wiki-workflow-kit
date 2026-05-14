# Whole Wiki Frontmatter Gate Design

Date: 2026-05-14
Status: design-approved-for-implementation
Repository: report-wiki-portfolio

## Problem

The current frontmatter taxonomy gate is too narrow. It reports visible drift
such as `domain: personal-ops` and unclassified pages without
`classification_needed: true`, but it does not enforce the configured path
rules across the whole wiki.

Two concrete misses exposed the gap:

- `wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md` is an ops page
  without `layer`, `domain`, or `ops_area`, but the checker does not report it.
- `wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md`
  lacks taxonomy frontmatter fields, but ADR pages are not covered by taxonomy
  path rules.

That means `wiki-status` can display "Domain Taxonomy Health" while users infer
a stronger claim than the checker actually proves.

## Goal

Make whole-wiki frontmatter governance strict, explicit, configurable, and
scorecarded.

The repository should treat frontmatter health as more than a narrow taxonomy
drift report. It should expose:

- taxonomy validity
- required-field completeness
- graph identity coverage
- relation-field shape
- scorecard pass/fail status

## Non-Goals

- Do not silently migrate every legacy page in this change.
- Do not invent business domains from prose.
- Do not make scorecard scoring semantic or embedding-based.
- Do not remove existing graph/status/product-status surfaces.
- Do not hide legacy debt as warnings when the configured gate says strict.

## Core Decision

Create ADR-0032:

```text
Whole Wiki Frontmatter Gate Must Be Strict And Scorecarded
```

The ADR should decide:

- all `wiki/**` markdown pages are subject to frontmatter governance
- strictness is configuration-driven, not hardcoded in AGENTS, skills, or chat
- `taxonomy drift` and `frontmatter completeness` are separate health surfaces
- the checker must emit a scorecard, not only a flat drift list
- status must render the scorecard and blocking counts
- archive review and frontmatter completion claims must read the same checker
  evidence

## Configuration Model

Extend `wiki/config/frontmatter-taxonomy.yaml` with whole-wiki gate settings.

Suggested shape:

```yaml
strict_gate:
  enabled: true
  minimum_pass_score: 100
  blocking_severities:
    - error

  rule_sets:
    whole_wiki:
      path_glob: "wiki/**/*.md"
      required:
        - layer
        - domain

    ops_pages:
      path_glob: "wiki/ops/**/*.md"
      required:
        - ops_area
        - canonical_object
        - artifact_type
      expected:
        layer: ops

    adr_pages:
      path_glob: "wiki/adr/**/*.md"
      required:
        - canonical_object
        - artifact_type
      expected:
        layer: adr
        domain: none

    source_pages:
      path_glob: "wiki/sources/**/*.md"
      required:
        - source_type
      expected:
        layer: sources

scorecard:
  dimensions:
    completeness: 40
    taxonomy_validity: 25
    identity_coverage: 20
    relation_shape: 15
```

The exact values live only in YAML. ADR and skills should reference the config
without duplicating full vocabulary.

## Checker Model

`scripts/check_wiki_frontmatter.py` should build one report with multiple
sections:

- `summary`: severity counts and total entries
- `entries`: detailed findings
- `scorecard`: dimensions, points lost, score, pass/fail
- `strict_gate`: enabled, minimum score, blocking severities, pass/fail
- `proof_boundary`: what the checker does and does not prove

The checker should report missing required fields for every page matched by a
strict rule set. It should also keep current taxonomy checks:

- forbidden domains
- unknown domains where configured
- `domain: unclassified` without `classification_needed: true`
- registered producer drift
- possible producer warnings

## Status Model

`wiki-status` should render:

- frontmatter strict gate result
- frontmatter scorecard
- top blocking examples
- existing domain taxonomy health
- existing graph parse health

The status surface must not imply that a narrow taxonomy drift report is full
frontmatter compliance.

## Testing Model

RED tests must include the two observed misses:

- an ops page with no `layer/domain/ops_area` must be reported as error
- an ADR page with no `layer/domain` must be reported as error

GREEN tests should show:

- strict rule sets are read from config
- missing required fields become entries
- scorecard fails when errors exist
- status renders strict gate and scorecard
- compliant pages avoid those errors

## Rollout Boundary

This change intentionally exposes existing debt. It does not need to migrate all
legacy pages before the gate exists. The correct first state is:

- checker reports the full backlog
- status makes the backlog visible
- future work can either migrate pages or add explicit, reviewed exceptions

Exceptions must be configuration entries with reason and owner. Chat-only
exceptions do not count.

