# behavior-replay-gate Specification

## Purpose
TBD - created by archiving change generalize-behavior-replay-gate. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL require replay evidence for future runtime behavior claims

The repository SHALL require behavior replay evidence when a change,
completion claim, or governance artifact asserts that a runtime behavior will
trigger, stop, route, reject, or persist differently in future sessions before
treating the claim as complete or archive-ready.

#### Scenario: Runtime trigger behavior is changed or declared reliable

- **WHEN** a repo `AGENTS.md` runtime trigger, skill trigger, OpenSpec hard
  stop, route, refusal path, or future-behavior claim is added, changed, or
  declared reliable
- **THEN** the change SHALL include behavior replay evidence
- **AND** the evidence SHALL show how a future agent can reproduce the expected
  behavior from repo-visible artifacts rather than chat memory

#### Scenario: Behavior replay evidence is recorded

- **WHEN** behavior replay evidence is required
- **THEN** it SHALL preserve at least:
  - input or situation shape
  - trigger condition
  - expected route, stop, refusal, or persistence behavior
  - repo-visible artifact a future agent should read
  - expected output, non-output, or boundary decision
  - promotion or non-promotion boundary
  - residual risk or proof boundary

#### Scenario: Specialized replay gate already exists

- **WHEN** a specialized replay gate exists for the behavior, such as skill
  evaluation evidence, local skill pressure tests, link-trigger replay,
  disagreement replay, or re-anchor replay
- **THEN** the repository MAY satisfy the generic behavior replay gate through
  that specialized evidence
- **AND** the evidence SHALL still state the proof boundary

#### Scenario: Replay proof is evaluated

- **WHEN** behavior replay evidence passes
- **THEN** the repository SHALL treat the pass as bounded replay proof
- **AND** it SHALL NOT overclaim multi-session rollout telemetry, semantic
  certainty, or automatic enforcement unless that stronger proof exists

### Requirement: Behavior replay gate SHALL stay narrow

Behavior replay SHALL not become a tax on every analysis or learning note.

#### Scenario: Work does not claim future runtime behavior

- **WHEN** work is a one-off analysis, candidate learning note, source summary,
  ordinary wiki capture, or exploratory thought that does not claim a future
  runtime trigger, stop condition, route, refusal, or persistence behavior
- **THEN** the behavior replay gate SHALL NOT be required by default

#### Scenario: Candidate learning is proposed for promotion

- **WHEN** candidate learning is proposed for repo `AGENTS.md`, root
  `AGENTS.md`, OpenSpec `SHALL`, skill hard rules, archive-ready claims, or
  another future runtime behavior claim
- **THEN** the behavior replay gate SHALL apply in addition to any
  source-evidence or promotion gate

