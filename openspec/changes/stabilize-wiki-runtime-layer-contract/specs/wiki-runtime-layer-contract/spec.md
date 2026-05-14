## Purpose

Define a stable wiki runtime layer contract so repo-local skills, observation
tools, eval harnesses, scorecards, and OpenSpec gates do not drift across
responsibilities.

## ADDED Requirements

### Requirement: Repository SHALL publish a wiki runtime layer contract

The repository SHALL publish a repo-visible architecture contract that defines
the wiki runtime layers and their ownership.

#### Scenario: User asks how the wiki runtime is structured

- **WHEN** a user or agent needs the runtime architecture
- **THEN** `wiki/ops/wiki-runtime-layer-contract.md` SHALL provide an
  architecture diagram
- **AND** it SHALL define core loop, skill entrypoints, decision contract,
  observation tools, boundaries, and eval/lifecycle gates.

### Requirement: Wiki-react SHALL be an explicit router, not a replacement for domain skills

The contract SHALL define `wiki-react` as the explicit router and
decision-trace entrypoint while preserving direct domain skill entrypoints.

#### Scenario: User knows the requested wiki task

- **WHEN** the user explicitly asks for status, query, repair, exploration, or
  scorecard work
- **THEN** the matching domain skill MAY be invoked directly
- **AND** high-risk domain skills SHALL still use `decision_trace` before
  action when required.

### Requirement: Eval, scorecard, and behavior gate SHALL remain separate

The contract SHALL prevent scorecard, trace eval, and behavior-asset checks from
claiming each other's responsibilities.

#### Scenario: Runtime evidence is evaluated

- **WHEN** scorecard, trace eval, or behavior-asset checker output is used
- **THEN** scorecard SHALL remain an observation source
- **AND** trace eval SHALL validate agent-produced decision traces
- **AND** behavior-asset checker SHALL validate behavior-change evidence.

### Requirement: Active specs SHALL avoid obsolete slash-command naming

Active wiki runtime specs SHALL not use obsolete slash-command names after the
supported runtime has moved to repo-local skills.

#### Scenario: Active specs are inspected

- **WHEN** active `openspec/specs` paths are inspected
- **THEN** no active wiki runtime spec path SHALL include
  `slash-command`
- **AND** archived specs MAY retain historical names.
