## ADDED Requirements

### Requirement: OpenSpec apply workflow SHALL keep execution overlays subordinate to tasks

The repository SHALL treat any detailed execution plan used inside an OpenSpec change, including a Superpowers plan, as an execution overlay rather than as a second progress ledger.

#### Scenario: Execution overlay is used during an OpenSpec change

- **WHEN** a contributor creates or uses a detailed execution plan inside an
  OpenSpec change
- **THEN** the plan SHALL declare that `tasks.md` is the only progress and
  completion ledger
- **AND** the plan SHALL avoid independent task ids such as `Task 1`, `Task 2`,
  or similar parallel task numbering
- **AND** the plan SHALL avoid progress checkboxes
- **AND** the plan SHALL organize execution tactics under strategy sections
  such as TDD, module, verification, commit, or handoff strategy

#### Scenario: Commit strategy is documented in an execution overlay

- **WHEN** an execution overlay documents commit slices
- **THEN** it SHALL treat commits as recovery evidence
- **AND** it SHALL NOT treat commit slices as OpenSpec task completion
- **AND** it SHALL keep OpenSpec task completion in `tasks.md`

#### Scenario: OpenSpec task progress changes during execution

- **WHEN** an OpenSpec task completion boundary has been satisfied and verified
- **THEN** `tasks.md` SHALL be updated at that boundary
- **AND** `tasks.md` SHALL NOT be deferred to a final sync step when earlier
  OpenSpec task boundaries have already been completed
