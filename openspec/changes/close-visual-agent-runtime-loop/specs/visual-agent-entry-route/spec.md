# visual-agent-entry-route Specification

## ADDED Requirements

### Requirement: Visual agent child workers SHALL be discoverable

This repository SHALL publish discoverable ordinary visual child workers for
repo-local `visual-agent` routes unless they are explicitly documented as
runtime/system tools or host-repo gates.

#### Scenario: Runtime loads visual-agent in this repository

- **WHEN** the runtime skill surface includes `.codex/skills/visual-agent`
- **THEN** ordinary visual workers named as bundled child routes SHALL exist
  under `.codex/skills/<worker>/SKILL.md`
- **AND** `imagegen` SHALL remain documented as a runtime/system image tool
- **AND** `public-report-quality-gate` SHALL remain documented as a host-repo
  parent gate rather than a visual worker

#### Scenario: Worker is not installed

- **WHEN** `visual-agent` would route to a worker that is not discoverable in
  the current runtime
- **THEN** the response SHALL keep ownership in `visual-agent`
- **AND** it SHALL mark the worker availability as blocked instead of claiming a
  child-worker route

### Requirement: Visual agent triggers SHALL not rely on fixed colloquial lists

The repo-local visual-agent trigger model SHALL classify visual-deliverable
intent by output role, transformation role, medium-selection role, or visual
repair role rather than relying on a fixed list of colloquial phrases.

#### Scenario: Casual visual wording appears

- **WHEN** the user uses casual or incomplete wording
- **AND** the intended deliverable is visual
- **THEN** `visual-agent` SHALL trigger from visual-deliverable intent
- **AND** it SHALL NOT require a fixed keyword to match
