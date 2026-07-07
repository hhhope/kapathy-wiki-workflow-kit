# account-cr-agent-mirror-sync Specification

## ADDED Requirements

### Requirement: Account CR Agent mirror SHALL preserve installed coverage-gate source

The repository SHALL keep the non-runtime account CR agent mirror aligned with
the currently selected installed source when the user asks to sync it.

#### Scenario: Installed CR agent has coverage-gate files

- **WHEN** the installed `cr-agent` source contains coverage rules, scripts,
  tests, and replay fixtures
- **THEN** the repo mirror under `skills-drafts/account-skills/` SHALL include
  those ordinary source files
- **AND** transient bytecode caches SHALL remain excluded
- **AND** the mirror SHALL NOT become active `.codex/skills` runtime
  registration

### Requirement: Account CR Agent sync SHALL record behavior proof boundaries

The repository SHALL preserve evaluation evidence for behavior-asset mirror
syncs that affect future skill promotion or diagnosis.

#### Scenario: CR agent mirror sync is completed

- **WHEN** the CR agent mirror is updated from installed source
- **THEN** the change SHALL include pressure scenarios, RED baseline, GREEN
  result, prior-art dedupe, validation results, and residual risks
- **AND** the evidence SHALL distinguish mirror sync from runtime activation,
  plugin publication, and multi-session rollout proof
