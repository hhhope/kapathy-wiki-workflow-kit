## ADDED Requirements

### Requirement: Source integration SHALL preserve blocked-object trace sources

The repository SHALL preserve repository-local source references for blocked
objects as trace-only evidence without promoting those objects into preferred or
supporting source targets.

#### Scenario: Blocked object has repository-local pages

- **WHEN** source integration resolves runtime context
- **AND** a blocked object has repository-local graph pages
- **THEN** the blocked object SHALL include trace-only source references
- **AND** those references SHALL NOT be included in preferred or supporting
  source lists
