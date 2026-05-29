## ADDED Requirements

### Requirement: req-agent SHALL be the normal requirements entry

The repository SHALL route ordinary user requests for requirements intake,
scope clarification, story extraction, acceptance extraction, readiness gating,
or OpenSpec draft handoff through `req-agent`.

#### Scenario: User asks whether a requirement can enter development

- **WHEN** the user asks whether requirement material is ready for development
- **THEN** Codex SHALL load `req-agent`
- **AND** it SHALL report Intent, Case, State, Allowed Action, Blocked Action
  when blocked, Next Action, and Evidence
- **AND** it SHALL NOT ask the user to run Python as the normal path

#### Scenario: User asks for raw requirements analysis agent usage

- **WHEN** the user asks for the requirements agent, requirement gate, domain
  recognition, user stories, acceptance functions, or OpenSpec handoff
- **THEN** Codex SHALL route through `req-agent`
- **AND** Python scripts SHALL be treated as internal evidence tools

### Requirement: Worker skills SHALL have bounded responsibilities

The repository SHALL provide bounded worker skills for requirements intake,
scope, stories, acceptance, and handoff. These workers SHALL not replace
`req-agent` as the normal entry.

#### Scenario: User invokes a worker for ordinary requirements work

- **WHEN** a user invokes `req-intake`, `req-scope`, `req-stories`,
  `req-acceptance`, or `req-handoff` without explicit debug or worker context
- **THEN** the worker SHALL redirect ordinary usage to `req-agent`
- **AND** it SHALL state its bounded responsibility

#### Scenario: req-agent routes to a worker

- **WHEN** `req-agent` identifies the next allowed action
- **THEN** it MAY route to the matching worker skill
- **AND** that worker SHALL stay within its bounded lifecycle slice

### Requirement: req-scope SHALL preserve requirements authority

`req-scope` SHALL use requirements case data and
`requirements/config/requirements-taxonomy.yaml` as requirements authority.

#### Scenario: Unknown domain or role appears

- **WHEN** source material contains a domain or role not confirmed in the
  requirements taxonomy
- **THEN** `req-scope` SHALL mark it as candidate or awaiting confirmation
- **AND** it SHALL NOT force the value into an existing taxonomy ID
- **AND** it SHALL NOT mutate the taxonomy without a separate approved workflow

### Requirement: req-stories and req-acceptance SHALL keep traceability

Story extraction and acceptance extraction SHALL preserve bidirectional
traceability between user stories and acceptance functions.

#### Scenario: Acceptance function lacks story mapping

- **WHEN** an acceptance function has no related user story
- **THEN** the workflow SHALL keep the case blocked from handoff
- **AND** it SHALL report the missing mapping as evidence

#### Scenario: User story lacks acceptance mapping

- **WHEN** a user story has no acceptance function mapping
- **THEN** the workflow SHALL keep the case blocked from handoff
- **AND** it SHALL report the missing mapping as evidence

### Requirement: req-handoff SHALL gate OpenSpec draft creation

`req-handoff` SHALL create OpenSpec draft artifacts only after the requirements
hard gate passes.

#### Scenario: Handoff is requested before readiness

- **WHEN** the user asks to create an OpenSpec draft
- **AND** the requirements case is not ready
- **THEN** `req-handoff` SHALL block draft creation
- **AND** it SHALL report readiness blockers

#### Scenario: Handoff succeeds

- **WHEN** the requirements hard gate passes
- **AND** the user asks to create an OpenSpec draft
- **THEN** `req-handoff` SHALL generate proposal, design, tasks, and spec draft
  files
- **AND** it SHALL require user review before implementation
- **AND** it SHALL NOT continue into implementation automatically

### Requirement: req-agent SHALL replace the narrow skill-entry direction

The `req-agent` lifecycle split SHALL supersede the narrower single
`requirements-analysis-agent` skill-entry approach for normal Codex usage.

#### Scenario: Existing narrow follow-up artifacts are present

- **WHEN** uncommitted `add-requirements-analysis-agent-skill-entry` artifacts
  or single-entry tests exist
- **THEN** this change SHALL retire, replace, or explicitly supersede them
- **AND** the final behavior SHALL use the six-skill `req-agent` surface
