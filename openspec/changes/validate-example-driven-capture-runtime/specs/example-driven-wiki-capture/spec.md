## MODIFIED Requirements

### Requirement: Repository SHALL capture extracted reusable learning from examples without requiring an extra reminder

When an external repo, README, article, or concrete in-chat example produces a reusable learning for repository workflow or operating behavior, the repository SHALL create or update a repo-visible record without waiting for an additional user reminder.

#### Scenario: Behavior is replay-validated after publication

- **WHEN** the repository validates whether `example-driven wiki capture` worked in a real session
- **THEN** that validation SHALL leave repo-visible replay evidence
- **AND** the evidence SHALL include the baseline expectation, the replay result, and the resulting wiki record or page
