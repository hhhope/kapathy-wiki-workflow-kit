## MODIFIED Requirements

### Requirement: Repository SHALL expose a preview-only wiki queue command

The repository SHALL provide `/wiki:queue` as a preview-only queue view derived
from bounded self-directed execution output.

#### Scenario: User previews possible wiki work

- **WHEN** the user invokes `/wiki:queue`
- **THEN** the command SHALL group candidate work as ready, needs user
  decision, and blocked
- **AND** it SHALL include source paths and caution notes when source references
  are available, including for blocked items
- **AND** it SHALL NOT create, modify, archive, or queue OpenSpec changes
- **AND** it SHALL NOT execute queued work or mark tasks complete
