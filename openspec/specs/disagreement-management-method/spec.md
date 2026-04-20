# disagreement-management-method Specification

## Purpose
TBD - created by archiving change formalize-disagreement-management-method. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL preserve disagreement as calibration material before promoting it into conclusion layers

When a repository-default workflow disagreement is still performing goal-calibration work, the repository SHALL preserve it as calibration material before promoting it into `ADR`, spec, skill, or other conclusion-oriented layers.

#### Scenario: Replay validation checks a new disagreement shape
- **WHEN** the repository validates the disagreement-management method against another disagreement shape
- **THEN** that replay SHALL preserve the disagreement as calibration material first
- **AND** the replay evidence SHALL keep the method boundary explicit rather than collapsing into endpoint-only conclusions

### Requirement: Repository SHALL preserve a minimum raw material package before summarizing or naming disagreement

Before the repository summarizes, names, or promotes a disagreement, it SHALL preserve the minimum raw material needed to reconstruct its calibration value.

#### Scenario: Disagreement is captured before interpretation
- **WHEN** the repository captures an active disagreement
- **THEN** it SHALL preserve at least:
  - rejected framing
  - correction pressure
  - redirection moment
  - current clarity state
  - protected target, if visible

### Requirement: Repository SHALL preserve explicit anti-compression states

The repository SHALL preserve explicit "not yet" states when the disagreement has invalidated the surface object but has not yet earned a confident interpretation.

#### Scenario: Deeper goal is not yet clearly visible
- **WHEN** the disagreement is clearly doing protective work
- **AND** the deeper goal is not yet visible enough to name confidently
- **THEN** the repository SHALL preserve an explicit unclear state
- **AND** it SHALL NOT pretend the deeper goal is already understood

#### Scenario: Pattern naming is premature
- **WHEN** the disagreement is still mainly visible as correction pressure or rejected framing
- **THEN** the repository SHALL preserve a "do not name the pattern yet" state
- **AND** it SHALL NOT treat a cleaner abstraction as automatically more faithful

### Requirement: Repository SHALL gate first positive naming on disagreement evolution

The repository SHALL only allow the first positive naming of a disagreement when that naming can explain the disagreement's evolution rather than merely summarize the endpoint.

#### Scenario: First positive naming is proposed
- **WHEN** a proposed name for the disagreement is introduced
- **THEN** the repository SHALL require that:
  - the rejected object has stabilized
  - redirection has occurred
  - the name explains the movement of the disagreement, not only the result

### Requirement: Repository SHALL keep method language subordinate to disagreement material

The repository SHALL treat the disagreement-management method as a mirror of disagreement material rather than a filter that reshapes it.

#### Scenario: Framework conflicts with the disagreement
- **WHEN** the method language and the preserved disagreement material point in different directions
- **THEN** the repository SHALL preserve the disagreement material
- **AND** it SHALL weaken or revise the framework instead of forcing the material into the method

### Requirement: Repository SHALL provide a reusable replay harness for disagreement-management validation

When the repository validates disagreement-management behavior, it SHALL provide a reusable replay harness that keeps replay proof distinct from rollout proof.

#### Scenario: Future contributor replays a disagreement thread
- **WHEN** a contributor validates the method on a disagreement thread
- **THEN** the repository SHALL provide a harness that captures at least:
  - disagreement shape
  - rejected framing
  - correction pressure
  - redirection moment
  - clarity state
  - protected target, if visible
  - RED baseline
  - GREEN result
  - residual risk

#### Scenario: Replay validation is recorded
- **WHEN** the repository records replay validation evidence
- **THEN** it SHALL state that replay / harness validation is stronger than narrative design-only reasoning
- **AND** it SHALL NOT claim rollout proof from replay evidence alone

