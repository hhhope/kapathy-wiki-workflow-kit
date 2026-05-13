## Purpose

Define an executable behavior-asset evaluation gate for semantic skill changes
and repo runtime-routing changes.

## ADDED Requirements

### Requirement: Repository SHALL evaluate behavior-asset changes with executable evidence

Behavior-asset changes SHALL include evaluation evidence that proves more than
section presence.

#### Scenario: Active change edits a behavior asset

- **WHEN** an active OpenSpec change references or edits `.codex/skills/*`,
  `AGENTS.md` runtime routing, skill triggers, parent gates, hard stops,
  publish/sync behavior, or future runtime behavior
- **THEN** the change SHALL include `evaluation.md`
- **AND** the evaluation SHALL include pressure scenarios, RED baseline, GREEN
  result, residual risks, replay fields, positive and negative cases, and proof
  boundary

### Requirement: Repository SHALL expose a behavior asset checker

The repository SHALL provide a local checker that users and agents can run.

#### Scenario: User runs the checker

- **WHEN** `python3 scripts/check_behavior_assets.py` runs
- **THEN** it SHALL inspect active OpenSpec changes and current behavior assets
- **AND** it SHALL write JSON and Markdown reports under `/tmp`
- **AND** it SHALL exit non-zero when error-severity drift exists

### Requirement: Agent Intent Routing SHALL not duplicate the skill route table

Agent Intent Routing SHALL remain a pre-action classification rule and SHALL
not duplicate the High-Frequency Skills routing table.

#### Scenario: Agent Intent Routing contains a route table

- **WHEN** `AGENTS.md` has `High-Frequency Skills`
- **AND** `Agent Intent Routing` contains `Minimum routes` or a multi-row
  parent-gate route table
- **THEN** the behavior asset checker SHALL report error-severity route-table
  ownership drift

### Requirement: Repo health check SHALL aggregate behavior asset results

The repo health check SHALL expose behavior asset evaluation as a named check.

#### Scenario: Behavior asset checker fails

- **WHEN** `python3 scripts/repo_health_check.py` runs
- **AND** behavior asset evaluation has error-severity entries
- **THEN** repo health check SHALL report `FAIL behavior-asset-evaluation`
