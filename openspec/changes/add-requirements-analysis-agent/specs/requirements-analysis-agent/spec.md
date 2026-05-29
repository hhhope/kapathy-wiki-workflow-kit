## Purpose

Define an intent-aware requirements analysis agent that gates requirement readiness before OpenSpec draft handoff.

## ADDED Requirements

### Requirement: Agent SHALL classify requirements intent before action

The agent SHALL classify user intent before creating, updating, checking, or handoff-routing a requirements case.

#### Scenario: User provides new requirement material

- **WHEN** the user provides a requirement document or requirement-like material
- **THEN** the agent SHALL return intent `new_requirement_intake`
- **AND** it SHALL NOT run implementation or OpenSpec draft generation directly

#### Scenario: User asks if the requirement is ready

- **WHEN** the user asks whether the requirement can proceed
- **THEN** the agent SHALL return intent `check_requirements_ready`
- **AND** it SHALL run the requirements case checker when a case is available

### Requirement: Agent SHALL surface domain candidates for unknown domains

The agent SHALL not force unknown domains into existing domain IDs.

#### Scenario: Requirement material does not match a known domain

- **WHEN** no domain in `requirements-taxonomy.yaml` clearly matches the material
- **THEN** the agent SHALL return domain status `candidate_pending`
- **AND** it SHALL include candidate domains with reasons
- **AND** it SHALL require user confirmation before hard-gate readiness

### Requirement: Taxonomy SHALL seed account settlement and clearing requirement vocabulary

The requirements taxonomy SHALL define the first-version requirement readiness vocabulary independently from wiki frontmatter taxonomy.

#### Scenario: Initial taxonomy is loaded

- **WHEN** the requirements taxonomy is loaded
- **THEN** it SHALL include known domains for account, settlement, and clearing
- **AND** it SHALL include role vocabulary for retail operations, financial operations, product, finance, clearing, compliance, retail customer, financial customer, system actor, engineering, QA, and risk control
- **AND** the role vocabulary SHALL distinguish business actors, operation owners, system actors, and delivery owners

### Requirement: Requirements gate SHALL not depend on wiki taxonomy

The requirements gate SHALL use requirements taxonomy and requirements case data as its readiness authority, even when a case file is stored under the wiki tree.

#### Scenario: Requirement case is stored inside wiki

- **WHEN** a requirements case file path is under `wiki/`
- **THEN** the requirements checker SHALL evaluate it with `requirements/config/requirements-taxonomy.yaml`
- **AND** it SHALL NOT require `wiki/config/frontmatter-taxonomy.yaml` to pass the requirements hard gate
- **AND** missing or unrelated wiki frontmatter SHALL NOT block requirement readiness

### Requirement: Checker SHALL enforce the first-version hard gate

The checker SHALL block requirement readiness unless confirmed domain, roles, user stories, and acceptance functions are complete and traceable.

#### Scenario: User story lacks acceptance mapping

- **WHEN** a user story has no acceptance function reference
- **THEN** the checker SHALL fail the hard gate
- **AND** it SHALL include a blocking reason naming the user story

### Requirement: Checker SHALL classify detailed-design material as soft warning

Detailed design sections SHALL not become first-version requirement authority.

#### Scenario: Case contains detailed design evidence

- **WHEN** a requirements case includes business-rule, exception-scenario, API, DDL, ADR, test-plan, or release-plan sections
- **THEN** the checker SHALL classify them as soft warnings or design evidence
- **AND** it SHALL NOT fail the hard gate solely because of those sections

### Requirement: Agent SHALL block OpenSpec draft before readiness

The agent SHALL create OpenSpec drafts only after the requirements hard gate has passed.

#### Scenario: Draft requested while case is blocked

- **WHEN** user intent is `create_openspec_draft`
- **AND** the requirements case is not `requirements_ready`
- **THEN** the agent SHALL block draft creation
- **AND** it SHALL return checker blocking reasons

### Requirement: Agent SHALL create traceable OpenSpec drafts after readiness

The agent SHALL generate OpenSpec draft artifacts from confirmed requirement data after readiness passes.

#### Scenario: Draft requested for ready case

- **WHEN** user intent is `create_openspec_draft`
- **AND** the requirements case status is `requirements_ready`
- **THEN** the agent SHALL create proposal, design, tasks, and spec draft files
- **AND** each OpenSpec requirement SHALL trace to user story and acceptance function IDs
- **AND** implementation SHALL still require user review after draft creation

#### Scenario: Draft change id already exists

- **WHEN** user intent is `create_openspec_draft`
- **AND** the target OpenSpec change id already exists
- **THEN** the agent SHALL NOT overwrite existing OpenSpec artifacts
- **AND** it SHALL return a blocking reason that asks for a different change id or explicit user selection
