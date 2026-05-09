## ADDED Requirements

### Requirement: Runtime auto routing SHALL carry blocked trace sources without routing them

The repository SHALL carry blocked-object source references as trace-only
metadata while keeping blocked objects outside first-pass and second-pass routes.

#### Scenario: Blocked object enters runtime auto routing

- **WHEN** runtime auto routing reads a source-integrated blocked object with
  trace-only source references
- **THEN** the corresponding `do_not_open_first` entry SHALL preserve those
  references as blocked metadata
- **AND** the references SHALL NOT be emitted as first-pass or second-pass route
  sources
