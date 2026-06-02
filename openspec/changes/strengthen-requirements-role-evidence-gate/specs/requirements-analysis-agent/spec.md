## ADDED Requirements

### Requirement: Requirements cases SHALL use case-local role instances for strict handoff

Strict requirements readiness SHALL require user stories to reference confirmed
case-local role instances rather than bare taxonomy role buckets.

#### Scenario: Story references a confirmed role instance

- **GIVEN** a requirements case has role `R-embedded-account-front`
- **AND** the role has `status: confirmed`
- **AND** `confirmed_as: system_actor` maps to requirements taxonomy
- **WHEN** user story `US-006` has `role_ref: R-embedded-account-front`
- **THEN** the strict checker SHALL accept the story role reference

#### Scenario: Story uses legacy bare role

- **GIVEN** a user story has `role: system_actor`
- **AND** it has no `role_ref`
- **WHEN** strict readiness is checked
- **THEN** the checker SHALL block with `story_role_ref_missing`

### Requirement: Requirements checker SHALL validate object-aware evidence anchors

The checker SHALL require traceable evidence anchors without requiring every
object to use the field name `evidence_refs`.

#### Scenario: Acceptance function has source acceptance

- **GIVEN** acceptance function `AF-014` has `source_acceptance: AC-014`
- **WHEN** strict readiness is checked
- **THEN** evidence validation for that acceptance function SHALL pass

#### Scenario: Acceptance function has no evidence anchor

- **GIVEN** an acceptance function has no `evidence_refs`, `evidence_anchor`,
  `source_section`, `source_quote`, `source_line`, `source_acceptance`, or
  `source_functions`
- **WHEN** strict readiness is checked
- **THEN** the checker SHALL block with `acceptance_evidence_missing`

### Requirement: Legacy case files SHALL remain readable

Compatibility mode SHALL allow existing legacy case files to be checked without
requiring immediate migration.

#### Scenario: Legacy case checked in compatibility mode

- **GIVEN** a legacy case uses `story.role`
- **WHEN** compatibility mode is used
- **THEN** the checker SHALL use existing taxonomy role validation
- **AND** the summary SHALL include `legacy_compatible: true`

### Requirement: OpenSpec draft generation SHALL require strict readiness

OpenSpec draft creation SHALL use strict readiness and SHALL NOT generate drafts
from candidate or legacy-only role mappings.

#### Scenario: Candidate role is referenced by a story

- **GIVEN** a story references role `R-unknown-ops`
- **AND** that role has `status: candidate_pending`
- **WHEN** OpenSpec draft creation is requested
- **THEN** draft creation SHALL be blocked
