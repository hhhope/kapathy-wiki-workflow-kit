# wiki-medical-agent Specification

## ADDED Requirements

### Requirement: Normal medical-loop entry SHALL route through wiki-medical-agent

Ordinary non-legacy/debug user requests SHALL use `wiki-medical-agent` as the
user-facing controller for wiki medical-loop status, diagnosis, confirmation,
treatment, surgery, recovery, or archive checks.

#### Scenario: User asks to apply confirmed treatment candidates

- **WHEN** the user asks to apply confirmed treatment candidates
- **THEN** the controller SHALL classify intent as `treatment_apply`
- **AND** resolve exactly one active case file
- **AND** validate executable confirmed treatment decisions before applying

#### Scenario: No active case exists

- **GIVEN** no active medical case file exists
- **WHEN** the user asks for status or diagnosis
- **THEN** the controller SHALL allow the request
- **AND** report that no active case is resolved
- **WHEN** the user asks for treatment, surgery, or recovery
- **THEN** the controller SHALL block the write action
- **AND** require diagnosis or explicit case creation before execution

#### Scenario: Multiple active cases exist

- **GIVEN** more than one active medical case file exists
- **WHEN** the user asks for treatment, surgery, recovery, or another write action
- **THEN** the controller SHALL block the write action
- **AND** require the user to select exactly one active case before execution

#### Scenario: Normal old stage skill usage redirects

- **GIVEN** a user invokes an old stage skill without explicit legacy or debug mode
- **WHEN** the request is for doctor, confirm, treatment, surgery, or recovery work
- **THEN** the stage skill SHALL redirect ordinary usage to `wiki-medical-agent`
- **AND** explicit legacy or debug mode SHALL remain evidence-only

### Requirement: Case file SHALL be the only authority

The controller SHALL treat stage records as evidence attachments. It SHALL not
execute treatment, surgery, or recovery authority from raw stage records unless
the result has been synchronized into the active case file.

#### Scenario: Legacy stage record exists

- **GIVEN** a doctor, confirm, treatment, surgery, or recovery record exists
- **WHEN** it is not attached to the active case file
- **THEN** it SHALL NOT change case state

### Requirement: Treatment apply SHALL be followed by recovery

Treatment apply SHALL update the active case file, attach treatment evidence,
run recovery, attach recovery evidence, and set `Next Action`.

#### Scenario: Apply succeeds and recovery passes

- **GIVEN** the active case has executable confirmed treatment decisions
- **WHEN** the controller applies them successfully
- **THEN** it SHALL run recovery
- **AND** set the case next action from the recovery result

### Requirement: New findings SHALL not auto-execute

New findings SHALL enter `Proposed Decisions`, `surgery_required`, or `blocked`
state when they come from doctor, surgery, or recovery. They SHALL NOT be
applied automatically.

#### Scenario: Recovery finds new candidates

- **WHEN** recovery discovers new treatment candidates
- **THEN** the controller SHALL write them to `Proposed Decisions`
- **AND** set `Next Action` to `awaiting_confirmation`
