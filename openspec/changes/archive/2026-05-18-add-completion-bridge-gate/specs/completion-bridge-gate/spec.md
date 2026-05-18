## ADDED Requirements

### Requirement: Completion bridge gate reconnects scoped completion to the original user question

The repository SHALL require scoped completion and archive-ready reports to distinguish delivery evidence from the user's original north-star, method experiment, or evaluation question when such a question was explicit.

#### Scenario: Completed work had an explicit original experiment question
- **WHEN** an OpenSpec-scoped task completes
- **AND** the initiating conversation or active trace included an explicit
  method experiment, north-star, or evaluation question
- **THEN** the completion report SHALL include the delivery result
- **AND** it SHALL identify the original question
- **AND** it SHALL answer that question, partially answer it, or state why it
  remains unanswered.

#### Scenario: Completion report only lists engineering artifacts
- **WHEN** a final report only lists files, commits, tests, or OpenSpec status
- **AND** an explicit original experiment question was present
- **THEN** the report SHALL be considered incomplete for the completion bridge
  gate.

### Requirement: Completion bridge gate SHALL preserve OpenSpec stop boundaries

The completion bridge SHALL not authorize implementation beyond the completed scope.

#### Scenario: Bridge answer identifies a follow-up
- **WHEN** the bridge answer identifies a needed workflow change, retro, or
  follow-up implementation
- **THEN** the next action SHALL be routed to archive review, a new OpenSpec
  proposal, or an explicit user decision
- **AND** the assistant SHALL NOT continue implementation inside the completed
  change unless that work is already in scope.

### Requirement: Completion bridge gate SHALL stay lightweight when no broader question exists

The repository SHALL avoid turning every small completion report into a verbose retrospective.

#### Scenario: No original north-star or experiment question was explicit
- **WHEN** a task is narrow and the user did not ask a broader process,
  evaluation, or north-star question
- **THEN** a concise delivery summary with verification evidence SHALL satisfy
  the completion bridge gate.

### Requirement: Completion bridge evidence is replayable before runtime behavior claims

The repository SHALL require replayable evidence before treating a workflow change as complete when that change claims future completion reports will bridge back to the user's original question.

#### Scenario: Behavior asset or workflow guidance is changed
- **WHEN** implementation changes repo guidance, skills, rules, or runtime
  routing for completion reports
- **THEN** the change SHALL include replay evidence with input shape, trigger
  condition, expected bridge output, blocked continuation boundary, and residual
  risk.
