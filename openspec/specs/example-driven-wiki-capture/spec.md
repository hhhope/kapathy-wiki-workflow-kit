# example-driven-wiki-capture Specification

## Purpose
TBD - created by archiving change formalize-example-driven-wiki-capture. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL capture extracted reusable learning from examples without requiring an extra reminder

When an external repo, README, article, or concrete in-chat example produces a reusable learning for repository workflow or operating behavior, the repository SHALL create or update a repo-visible record without waiting for an additional user reminder.

#### Scenario: External example yields reusable workflow learning

- **WHEN** the user provides an external example and the discussion extracts what the repository should reuse, modify, reject, or follow up
- **THEN** the system SHALL create or update a repo-visible wiki record in the same turn
- **AND** it SHALL not require a second instruction such as "write this to wiki"

### Requirement: Example-driven records SHALL preserve the adaptation boundary

The repository SHALL preserve not only the source summary but also the adaptation boundary between the source and the repository.

#### Scenario: Learning is captured from an example

- **WHEN** the repository writes an example-driven learning record
- **THEN** that record SHALL preserve at least:
  - source reference
  - what was reused
  - what was modified
  - what was not yet formalized
  - next step

### Requirement: Example-driven records SHALL route to the lowest correct repository layer

The repository SHALL route example-driven learnings to the lowest durable layer that preserves their usefulness.

#### Scenario: Learning changes current operating behavior

- **WHEN** the example-driven learning primarily affects project workflow, governance, or operating behavior
- **THEN** the repository SHALL prefer `wiki/ops`

#### Scenario: Learning is best kept as a validated output example

- **WHEN** the example-driven learning is primarily a reusable demonstration of output shape
- **THEN** the repository SHALL prefer `wiki/examples`

#### Scenario: Learning looks reusable across projects

- **WHEN** an example-driven learning already exists in the project wiki and appears generalizable beyond the current repository
- **THEN** the repository MAY add it to `wiki/team-lore-candidates.md`

