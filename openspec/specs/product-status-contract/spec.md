# product-status-contract Specification

## Purpose
TBD - created by archiving change add-product-status-contract. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL define a product status contract

The repository SHALL define a product-level status contract for objects moving
through the report-wiki operating backbone.

#### Scenario: Product object is classified

- **WHEN** the repository summarizes product status
- **THEN** each classified object SHALL use an explicit object type such as
  source, learning, structure, output, behavior, status, or governance
- **AND** unknown object types SHALL be reported as unknown rather than inferred
  semantically from prose

### Requirement: Product status SHALL name target states and source layers

The product status contract SHALL preserve where evidence currently lives and
what product state the object is trying to reach.

#### Scenario: Product object is summarized

- **WHEN** the repository summarizes a product object
- **THEN** it SHALL include a source layer such as inbox, source, ops, report,
  spec, archive, or generated status when that layer is explicit
- **AND** it SHALL include a target state only when the state is explicit or
  conservatively derived from structural metadata

### Requirement: Product status SHALL use conservative readiness labels

The product status contract SHALL use readiness labels that preserve evidence
boundaries, including invalid, draft-only, blocked, unresolved, review-ready,
and accepted.

#### Scenario: Evidence is missing

- **WHEN** an object has a clear target but lacks required evidence
- **THEN** the object SHALL be marked blocked or unresolved
- **AND** the system SHALL NOT inflate its readiness score or label

#### Scenario: Target is unclear

- **WHEN** an object cannot be mapped to an explicit target state
- **THEN** the object SHALL remain invalid or draft-only

### Requirement: Product status SHALL separate score types

The product status contract SHALL distinguish score types instead of treating
all scores as product readiness.

#### Scenario: Local diagnostic score exists

- **WHEN** an artifact has a diagnostic, admission, quality, or behavior replay
score
- **THEN** the product status contract SHALL preserve the score type
- **AND** diagnostic or admission scores SHALL NOT be treated as review-ready
quality proof

### Requirement: Product status SHALL expose status transitions

The product status contract SHALL name the next expected transition in the
product backbone when it can be derived from explicit repository state.

#### Scenario: Unresolved status pressure exists

- **WHEN** a source, learning, output, behavior, or governance object is blocked
  or incomplete
- **THEN** the product status summary SHALL expose the next inspection or
  transition needed
- **AND** it SHALL preserve whether the transition is evidence collection,
  learning reuse, output review, behavior replay, archive review, or no action

### Requirement: Product status SHALL expose explicit identity and relation coverage

The product status contract SHALL expose identity and relation coverage only
from explicit structural metadata.

#### Scenario: Wiki pages are summarized

- **WHEN** wiki pages are included in the generated status manifest
- **THEN** the product status summary SHALL count pages with and without
  explicit canonical identity
- **AND** it SHALL count pages with and without explicit relation metadata
- **AND** it SHALL NOT claim graph-based semantic understanding from those
  counts

