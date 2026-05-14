## Purpose

Ensure repeated drift during `$superpowers:brainstorming` leaves repo-visible
evidence before the design conversation continues or escalates into behavior
changes.

## ADDED Requirements

### Requirement: Repository SHALL record repeated brainstorming drift before continuation

The repository SHALL stop the current brainstorming continuation and create or
update a repo-visible `wiki/ops` drift trace before proceeding when
`$superpowers:brainstorming` is active and the user explicitly flags repeated
drift.

#### Scenario: User flags repeated brainstorming drift

- **WHEN** the user says the brainstorming flow has drifted repeatedly
- **AND** the discussion has crossed between design, runtime, skill, OpenSpec,
  ADR, or repair-execution layers
- **THEN** the repository SHALL create or update a `wiki/ops` trace
- **AND** the trace SHALL record original intent, drift chain, rejected framing,
  corrected framing, cause analysis, affected active change, ADR status, and
  next allowed action
- **AND** continuation SHALL resume only after the trace exists or the user
  explicitly cancels trace creation.

### Requirement: Brainstorming drift traces SHALL stay distinct from ADRs

The repository SHALL treat brainstorming drift traces as retro evidence, not as
stable decisions.

#### Scenario: Drift may imply a future stable rule

- **WHEN** a brainstorming drift trace identifies a candidate governance rule
- **THEN** the trace SHALL preserve the evidence and analysis
- **AND** it SHALL NOT create or imply an ADR decision by itself
- **AND** any ADR promotion SHALL require a later explicit decision path.

### Requirement: Brainstorming drift trace SHALL not silently mutate runtime behavior

The trace requirement SHALL not be treated as permission to change runtime,
skill, AGENTS, or OpenSpec lifecycle behavior without scoped implementation.

#### Scenario: Trace records a missing behavior rule

- **WHEN** the trace identifies missing skill or runtime behavior
- **THEN** the next action SHALL identify the needed implementation path
- **AND** the trace itself SHALL NOT modify scripts, skills, AGENTS, accepted
  ADRs, or completed OpenSpec tasks.
