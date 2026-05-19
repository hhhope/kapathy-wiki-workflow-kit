# wiki-medical-agent Specification

## Purpose
TBD - created by archiving change add-medical-agent-moc-surgery-preview. Update Purpose after archive.
## Requirements
### Requirement: Medical agent SHALL route MOC preview requests to surgery preview

The medical agent SHALL recognize explicit MOC preview, review, and surgery
requests and route them to a read-only `moc_surgery_preview` action.

#### Scenario: User requests MOC surgery preview with one active case

- **WHEN** the user asks for MOC preview, MOC review, MOC surgery, Obsidian graph
  preview, or knowledge-map review
- **AND** exactly one active medical case exists
- **THEN** the medical agent SHALL return intent `moc_surgery_preview`
- **AND** it SHALL build a MOC dry-run plan
- **AND** it SHALL pass the MOC plan into surgery preview
- **AND** it SHALL return compact `moc_projection` and `surgery_preview` payload
  fields
- **AND** it SHALL NOT write `wiki/moc`.

#### Scenario: User requests MOC preview without an active case

- **WHEN** no active medical case exists
- **THEN** the medical agent SHALL block `moc_surgery_preview`
- **AND** it SHALL return `blocked_reason: no_active_case`.

#### Scenario: User requests MOC preview with multiple active cases

- **WHEN** multiple active medical cases exist
- **THEN** the medical agent SHALL block `moc_surgery_preview`
- **AND** it SHALL return `blocked_reason: multiple_active_cases`
- **AND** it SHALL return active-case selection behavior
- **AND** it SHALL NOT build or apply MOC writes.

#### Scenario: User requests ordinary treatment preview

- **WHEN** the user asks to preview confirmed treatment candidates
- **AND** the request does not contain a MOC signal
- **THEN** the medical agent SHALL keep routing to `treatment_preview`.

### Requirement: MOC surgery preview SHALL preserve medical-loop boundaries

The medical agent SHALL treat MOC projection changes as surgery preview items,
not treatment items.

#### Scenario: MOC surgery preview runs

- **WHEN** `moc_surgery_preview` is allowed
- **THEN** the medical agent SHALL NOT write treatment records
- **AND** it SHALL NOT write surgery records
- **AND** it SHALL NOT update the active case file
- **AND** it SHALL NOT mutate `Confirmed Decisions`.

