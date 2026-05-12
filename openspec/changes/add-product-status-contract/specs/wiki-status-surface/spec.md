## MODIFIED Requirements

### Requirement: Repository SHALL provide a wiki manifest artifact

The repository SHALL provide a repeatable workflow that emits a machine-readable
manifest for wiki pages, source records, inbox files, active OpenSpec change
task state, and minimal product-status contract fields.

#### Scenario: Wiki manifest is generated

- **WHEN** the manifest workflow is run
- **THEN** it SHALL emit a JSON manifest artifact
- **AND** the manifest SHALL include wiki page records, source records, inbox
  file records, OpenSpec change records, and a `product_status` summary
- **AND** the `product_status` summary SHALL include a contract version, object
  type counts, source layer counts, readiness counts, explicit identity and
  relation coverage, and unresolved items

### Requirement: Repository SHALL provide a reader-facing wiki status report

The repository SHALL provide a generated Markdown status report that summarizes
the manifest for humans and agents.

#### Scenario: Wiki status report is generated

- **WHEN** the status workflow is run
- **THEN** it SHALL emit a Markdown status report
- **AND** the report SHALL summarize wiki sections, source records, pending
  inbox files, active OpenSpec changes, complete active-directory changes,
  product status counts, explicit identity and relation coverage, unresolved
  product-status items, and next actions

### Requirement: Wiki status SHALL remain scoped to visibility

The wiki status workflow SHALL NOT implement query, scorecard calibration, graph
UI, learning-to-change orchestration, or autonomous product-state transitions.

#### Scenario: Status workflow is run

- **WHEN** the status workflow completes
- **THEN** it SHALL provide visibility artifacts only
- **AND** it SHALL NOT open, modify, archive, or create OpenSpec changes
- **AND** it SHALL NOT mark product objects accepted without explicit evidence
