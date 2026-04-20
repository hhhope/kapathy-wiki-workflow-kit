# disagreement-management-method Specification

## Purpose
TBD - created by archiving change formalize-disagreement-management-method. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL preserve disagreement as calibration material before promoting it into conclusion layers

When a repository-default workflow disagreement is still performing goal-calibration work, the repository SHALL preserve it as calibration material before promoting it into `ADR`, spec, skill, or other conclusion-oriented layers.

#### Scenario: Disagreement becomes repo-visible before stable decision
- **WHEN** a live disagreement is still doing calibration work
- **AND** it has enough shape to require durable repo-visible preservation
- **BUT** it is not yet stable enough for `ADR`, spec, or skill promotion
- **THEN** the repository SHALL prefer `wiki/ops retro`

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

#### Scenario: Executable replay record is validated
- **WHEN** the repository validates a structured disagreement replay record
- **THEN** the repository SHALL provide an executable checker for the replay record shape
- **AND** the checker SHALL fail when required replay fields or required pass-condition checks are missing

### Requirement: Archive review SHALL check disagreement preservation and promotion

When an OpenSpec change reaches archive review, the repository SHALL check whether disagreement material was lost, should remain in method/retro form, or should already have been promoted to a stable decision layer.

#### Scenario: Archive review runs on a completed change
- **WHEN** archive review is performed on a completed change
- **THEN** the review SHALL check whether the change generated disagreement material that:
  - should remain in method or retro form
  - should be promoted to ADR
  - was flattened away without a durable record

### Requirement: Executable replay proof SHALL stay structural and honest

When the repository provides an executable replay harness, it SHALL keep the proof boundary explicit and avoid pretending to semantically understand the underlying disagreement.

#### Scenario: Checker passes on a replay record
- **WHEN** the executable harness passes on a replay record
- **THEN** that pass SHALL mean the structured replay contract is satisfied
- **AND** it SHALL NOT claim that the disagreement itself has been semantically validated automatically

