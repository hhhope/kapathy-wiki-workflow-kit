# Design

## Decision Boundary

The durable decision belongs in `wiki/adr/0032-whole-wiki-frontmatter-gate-must-be-strict-and-scorecarded.md`.

The ADR defines the policy:

- whole `wiki/**` frontmatter is governed
- strictness is config-driven
- scorecard evidence is required
- status must separate narrow taxonomy drift from whole-wiki frontmatter
  completeness

## Configuration Boundary

`wiki/config/frontmatter-taxonomy.yaml` remains the only taxonomy and gate
configuration source. This change extends it with:

- `strict_gate.enabled`
- `strict_gate.minimum_pass_score`
- `strict_gate.blocking_severities`
- `strict_gate.rule_sets`
- `scorecard.dimensions`

Rules are path-glob based. The checker interprets config; it does not own the
policy vocabulary.

## Checker Boundary

`scripts/check_wiki_frontmatter.py` emits the evidence:

- flat `entries`
- severity summary
- strict gate result
- scorecard dimensions
- proof boundary

The checker reports configured missing fields as `missing_required_field`. It
keeps current taxonomy checks for forbidden domains, unclassified flags,
registered producers, and possible producer warnings.

## Status Boundary

`scripts/build_wiki_status.py` consumes checker output and
`scripts/wiki_status_render.py` renders:

- strict gate pass/fail
- score
- scorecard dimensions
- blocking count
- sample blocking entries

Status remains diagnostic and must not apply repairs.

## Test Boundary

Tests must include the two concrete missed shapes:

- ops page missing strict metadata
- ADR page missing strict metadata

They should also verify that compliant pages avoid those strict-gate errors and
that status renders the scorecard.

## Rollout Boundary

This change may make the current repo fail the strict checker because legacy
pages are incomplete. That is expected. The goal is to make the backlog visible,
not to hide it.

Future migrations can reduce the scorecard debt. Exceptions require explicit
config entries with reason and owner.

