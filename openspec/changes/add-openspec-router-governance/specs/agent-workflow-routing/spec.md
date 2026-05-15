## ADDED Requirements

### Requirement: Mixed workflow actions use an explicit router

The repository SHALL use an explicit workflow router before mixed
Superpowers/OpenSpec actions so method gates, lifecycle gates, and repo
discipline remain ordered. The router SHALL NOT replace OpenSpec as the
authoritative lifecycle source of truth.

#### Scenario: Mixed Superpowers and OpenSpec request routes before edits

- **WHEN** a user request mentions Superpowers and OpenSpec, or otherwise mixes
  method workflow with lifecycle workflow
- **THEN** the agent uses the repo-local `openspec-router` before editing files
- **AND** the agent emits the compact route line required by the router.

#### Scenario: Brainstorming keeps OpenSpec read-only until review

- **WHEN** `$superpowers:brainstorming` is active
- **THEN** OpenSpec artifacts are read-only until Superpowers written
  design/spec review passes
- **AND** short approvals advance only the current gate.

#### Scenario: Superpowers artifacts are bound to OpenSpec

- **WHEN** a Superpowers artifact supports an OpenSpec-scoped governance topic
- **THEN** the artifact identifies the OpenSpec change it supports
- **OR** it explicitly marks itself as pre-change exploration.

#### Scenario: Implementation and archive require OpenSpec evidence

- **WHEN** implementation, completion, or archive is requested
- **THEN** Superpowers artifacts alone are not sufficient evidence
- **AND** the active OpenSpec change tasks, validation, verification, and
  archive review remain authoritative.

#### Scenario: Governance replay verifies the full stack

- **WHEN** router governance is verified
- **THEN** replay covers PROJECT, AGENTS, OpenSpec delta specs, the router
  skill, and the original incident route
- **AND** skill-only replay is not treated as complete governance verification.
