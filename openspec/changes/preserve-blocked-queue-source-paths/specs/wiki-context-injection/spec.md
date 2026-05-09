## ADDED Requirements

### Requirement: Context injection SHALL carry excluded source refs without injecting them

The repository SHALL preserve blocked-object source references in excluded
objects without turning them into injected context excerpts.

#### Scenario: Blocked routed object is excluded from injection

- **WHEN** context injection reads a blocked routing entry with trace-only source
  references
- **THEN** the excluded object SHALL preserve those references as excluded source
  refs
- **AND** the references SHALL NOT be included in injected first-pass or
  secondary context excerpts
