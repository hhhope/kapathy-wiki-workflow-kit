## MODIFIED Requirements

### Requirement: Repository SHALL capture extracted reusable learning from examples without requiring an extra reminder

When an external repo, README, article, or concrete in-chat example produces a reusable learning for repository workflow or operating behavior, the repository SHALL create or update a repo-visible record without waiting for an additional user reminder.

#### Scenario: Behavior is replay-validated after publication

- **WHEN** the repository validates whether `example-driven wiki capture` worked in a real session
- **THEN** that validation SHALL leave repo-visible replay evidence
- **AND** the evidence SHALL include the baseline expectation, the replay result, and the resulting wiki record or page

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

#### Scenario: Learning is promoted into a behavior asset

- **WHEN** an external article, external repo, README, or in-chat example is used to support a behavior-asset rule, hard constraint, spec requirement, skill rule, or archive-ready conclusion
- **THEN** the promotion SHALL record one accepted evidence shape:
  - external-document excerpt with URL and exact section or line reference
  - local demo or fixture with RED/GREEN, input/output, and command or manual replay record
  - git-like project comparison with repository, commit or path, and observable structure or behavior difference
- **AND** unsupported learning SHALL remain a candidate observation
- **AND** unsupported learning SHALL NOT be promoted into repo `AGENTS.md`, root `AGENTS.md`, spec `SHALL`, skill hard rules, or archive-ready claims

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
