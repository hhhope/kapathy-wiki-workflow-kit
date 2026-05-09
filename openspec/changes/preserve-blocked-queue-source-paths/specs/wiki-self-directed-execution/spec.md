## ADDED Requirements

### Requirement: Self-directed execution SHALL expose blocked action source refs

The repository SHALL expose source references on blocked execution entries when
those references exist, while preserving blocked execution state.

#### Scenario: Blocked excluded object has source refs

- **WHEN** bounded self-directed execution builds a blocked entry from an
  excluded object with source refs
- **THEN** the blocked entry SHALL include action source refs
- **AND** the blocked entry SHALL remain in `do_not_execute`
- **AND** it SHALL NOT be promoted into execute-now or deferred-follow-up actions
