## ADDED Requirements

### Requirement: Repository SHALL provide a public report quality gate

The repository SHALL provide a repo-local skill that gates reader-facing
reports, Feishu review drafts, public share drafts, and H5/report-style outputs
before they are published, synced, or claimed ready for review.

#### Scenario: User asks for a reader-facing material

- **WHEN** the user asks to write, polish, create, sync, or prepare a public
  report, Feishu review draft, H5/share draft, or reader-facing material
- **THEN** the system SHALL route the output through the public report quality
  gate before publishing or syncing

#### Scenario: User provides a reference artifact for output shape

- **WHEN** the user provides a Feishu page, article, example, visual, or
  existing report as a reference for the output shape
- **THEN** the gate SHALL require a reference structure map before writing or
  rewriting the reader-facing draft
- **AND** if the reference is a Feishu wiki node with child pages or a reading
  map with concrete links, the gate SHALL require linked-page readback before
  the Reference Structure Gate can pass

### Requirement: Public report gate SHALL enforce hard publish blockers

The public report gate SHALL block publish or Feishu sync when any hard gate
fails.

#### Scenario: Voice gate fails

- **WHEN** a reader-facing draft contains chat residue, slogan simplification,
  loose narrator, weak section openings, internal ops leakage, or tone mismatch
- **THEN** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

#### Scenario: Core narrative drifts

- **WHEN** the stated story or reader promise changes during the draft, such as
  rewriting an evolution path into a static responsibility split
- **THEN** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

#### Scenario: Multi-part content is overloaded into one article

- **WHEN** the material spans multiple reader jobs such as overview, runtime,
  migration, validation, and roadmap
- **THEN** the gate SHALL require an explicit split strategy before reader-facing
  publication or sync

#### Scenario: A hard gate is not fully passed

- **WHEN** any hard gate is failed, partial, unknown, or not tested
- **THEN** the draft SHALL NOT receive a numeric score
- **AND** the scorecard SHALL be recorded as `INVALID`
- **AND** the draft SHALL NOT be published, synced to Feishu, or claimed ready
  for review

#### Scenario: Reference visuals are missing

- **WHEN** the reference artifact uses essential visuals for structure,
  sequence, contrast, maturity, or decision logic
- **AND** the reader-facing draft lacks corresponding visual assets or a
  concrete visual plan
- **THEN** the Visual Gate SHALL fail rather than treating the gap as a residual
  risk

### Requirement: Public report gate SHALL preserve existing workflow gates

The public report gate SHALL coordinate existing source, learning, visual,
Feishu, and verification skills without replacing their boundaries.

#### Scenario: Source or reference learning is needed

- **WHEN** a reader-facing report uses external articles, repositories, Feishu
  pages, or examples as references
- **THEN** the system SHALL still preserve the applicable learning-capture,
  source-grounding, and adaptation-boundary gates

#### Scenario: Feishu sync is requested

- **WHEN** the draft is intended for Feishu creation or update
- **THEN** the system SHALL pass the public report quality gate before using
  Feishu document write operations

### Requirement: Public report gate SHALL preserve a repo-visible gate review artifact

The public report gate SHALL preserve the quality decision in a repo-visible
artifact before Feishu sync, publication, or a review-ready claim.

#### Scenario: Reader-facing draft is prepared for Feishu or review

- **WHEN** a reader-facing draft is intended for Feishu sync, publication, or a
  review-ready claim
- **THEN** the system SHALL create or update a `wiki/ops/*-report-gate-review.md`
  artifact before the sync, publication, or claim
- **AND** the artifact SHALL include the reference structure map, hard gate
  results, scorecard, decision, residual risks, and proof boundary
- **AND** when the reference contains linked pages, the artifact SHALL include
  linked-page titles, links or tokens, and confirmed page jobs

#### Scenario: Feishu write is completed

- **WHEN** a Feishu document is created or updated after passing the public
  report quality gate
- **THEN** the gate review artifact SHALL record the Feishu update result and
  read-back verification
- **AND** the Feishu document SHALL NOT be treated as the process evidence by
  itself
