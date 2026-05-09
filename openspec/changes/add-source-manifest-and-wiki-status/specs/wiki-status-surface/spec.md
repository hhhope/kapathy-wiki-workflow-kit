## ADDED Requirements

### Requirement: Repository SHALL provide a wiki manifest artifact

The repository SHALL provide a repeatable workflow that emits a machine-readable
manifest for wiki pages, source records, inbox files, and active OpenSpec change
task state.

#### Scenario: Wiki manifest is generated

- **WHEN** the manifest workflow is run
- **THEN** it SHALL emit a JSON manifest artifact
- **AND** the manifest SHALL include wiki page records, source records, inbox
  file records, and OpenSpec change records

### Requirement: Repository SHALL identify inbox files not represented by source records

The manifest workflow SHALL compare inbox files with source records that declare
`source_path`.

#### Scenario: Inbox file has no matching source record

- **WHEN** an inbox file is not represented by any wiki source record
- **THEN** the manifest SHALL mark that inbox file as pending

#### Scenario: Inbox file has a matching source record

- **WHEN** a source page declares a matching `source_path`
- **THEN** the manifest SHALL mark the inbox file as represented

### Requirement: Repository SHALL provide a reader-facing wiki status report

The repository SHALL provide a generated Markdown status report that summarizes
the manifest for humans and agents.

#### Scenario: Wiki status report is generated

- **WHEN** the status workflow is run
- **THEN** it SHALL emit a Markdown status report
- **AND** the report SHALL summarize wiki sections, source records, pending
  inbox files, active OpenSpec changes, complete active-directory changes, and
  next actions

### Requirement: Wiki status SHALL remain scoped to visibility

The wiki status workflow SHALL NOT implement query, scorecard calibration, graph
UI, or learning-to-change orchestration.

#### Scenario: Status workflow is run

- **WHEN** the status workflow completes
- **THEN** it SHALL provide visibility artifacts only
- **AND** it SHALL NOT open, modify, or archive OpenSpec changes
