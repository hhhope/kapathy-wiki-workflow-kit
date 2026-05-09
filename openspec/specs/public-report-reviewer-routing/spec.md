# public-report-reviewer-routing Specification

## Purpose
TBD - created by archiving change route-complex-public-reports-to-reviewer. Update Purpose after archive.
## Requirements
### Requirement: Complex public reports SHALL route to a manual reviewer

The repository SHALL provide a manual reviewer role template for complex
reader-facing materials instead of putting all review logic inside the
lightweight public report quality gate.

#### Scenario: Complex public report is requested

- **WHEN** a reader-facing report, Feishu review draft, H5/share draft, or
  public material has at least two complexity signals
- **THEN** the system SHALL mark reviewer routing as required before drafting or
  review-ready claims
- **AND** the system SHALL NOT silently choose the final template without the
  user or reviewer decision

#### Scenario: Complexity signals are evaluated

- **WHEN** the public report gate evaluates reviewer routing
- **THEN** it SHALL check for signals including multi-page or series output,
  external reference structure, Feishu/H5/public target, scorecard or
  gate-review evidence, user-reported drift or failed draft, template choice,
  visual-style choice, and learning-use mapping

#### Scenario: Simple public edit is requested

- **WHEN** a reader-facing edit is single-page, has no external reference
  structure, does not require scoring, and has no drift or template-choice
  concern
- **THEN** reviewer routing MAY be skipped
- **AND** the public report quality gate SHALL still apply its ordinary hard
  gates

### Requirement: Reviewer template SHALL preserve template-choice and scoring boundaries

The manual reviewer SHALL protect the fork points that the main drafting agent
previously skipped.

#### Scenario: Reviewer runs before drafting

- **WHEN** reviewer routing is required
- **THEN** the reviewer SHALL check proposition, list 2-3 candidate templates,
  recommend one, and require user selection before drafting unless the user has
  already selected a template explicitly
- **AND** it SHALL review learning-use mapping, hard gates, and score evidence

#### Scenario: Score is assigned

- **WHEN** the reviewer or gate-review artifact reports a score
- **THEN** it SHALL distinguish rubric-schema checks from draft-quality scoring
- **AND** a schema total of 100 SHALL NOT be treated as evidence that the draft
  quality score is 100

### Requirement: Reviewer routing SHALL be observable

Reviewer routing decisions SHALL be preserved in repo-visible process evidence.

#### Scenario: Gate review artifact is created

- **WHEN** a gate-review artifact is created or updated for a reader-facing
  output
- **THEN** it SHALL record whether reviewer routing was required, run, skipped,
  blocked, or not applicable
- **AND** it SHALL include the reviewer result when reviewer routing was
  required

### Requirement: Reviewer template SHALL NOT auto-spawn sub-agents

The reviewer template SHALL be a manual role template, not an automatic
delegation mechanism.

#### Scenario: Reviewer routing is required

- **WHEN** the gate says reviewer routing is required
- **THEN** the system MAY load the reviewer template or ask the user to run the
  reviewer flow
- **AND** it SHALL NOT spawn a sub-agent unless the user explicitly asks for
  sub-agent delegation
