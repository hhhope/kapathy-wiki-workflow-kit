## ADDED Requirements

### Requirement: Public report gate SHALL enforce reference output shape fidelity

The public report gate SHALL verify the selected output shape when a user
request or reference artifact establishes one, and SHALL block review-ready,
publish, or sync claims when the draft silently replaces that shape with a
different primary structure.

#### Scenario: Draft silently changes selected output shape

- **WHEN** a user request or reference artifact establishes an output shape
- **AND** the draft changes to a different primary structure without explicit
  user approval
- **THEN** the Reference Output Shape Gate SHALL fail
- **AND** the draft SHALL NOT be claimed review-ready, published, or synced
  until repaired or explicitly approved by the user

#### Scenario: Production route leaks into reader-facing content

- **WHEN** the selected output shape is reader-facing content
- **AND** production instructions, image prompts, tool notes, or Hybrid routing
  text appear inside that content
- **THEN** the Reference Output Shape Gate SHALL fail
- **AND** the production route SHALL be moved to a separate asset brief,
  worklog, or other non-reader-facing location

#### Scenario: Gate review records shape replay

- **WHEN** a reference-shaped draft is prepared for review, publish, or sync
- **THEN** the gate-review artifact SHALL record the selected output shape,
  retained patterns, rejected patterns, user-approved shape changes, and replay
  result
