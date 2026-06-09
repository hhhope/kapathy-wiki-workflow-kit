# req-human-review-phase Specification

## ADDED Requirements

### Requirement: Human Review Worker Phase

The requirements workflow SHALL include a bounded `req-human-review` worker
phase after `req-acceptance` and before `req-handoff`.

#### Scenario: Route After Acceptance

- **GIVEN** a requirements case has structured user stories and acceptance
  mappings
- **WHEN** the user asks for a human-readable requirement review
- **THEN** `req-agent` SHALL route to `req-human-review` before `req-handoff`

### Requirement: Human Review Is Not A Normal Entry

`req-human-review` SHALL NOT be a normal user-facing entry point. Ordinary use
SHALL route through `req-agent`.

#### Scenario: Direct Worker Invocation

- **GIVEN** a user has not explicitly requested debug or worker-context behavior
- **WHEN** an agent considers using `req-human-review`
- **THEN** the agent SHALL route through `req-agent` instead

### Requirement: Human Review Template Completeness

Human Review output SHALL include case identity, source coverage, domain
judgment, scope boundaries, roles, user stories, scenario coverage, rule/status
coverage, acceptance scope, gap classification, detailed-design gate status,
synchronization proof, and agent usage instructions.

#### Scenario: Human Review Has Story Gaps

- **GIVEN** scenario analysis identifies a missing requirement boundary
- **WHEN** the boundary changes demand facts
- **THEN** Human Review SHALL record the gap and require machine case
  synchronization

### Requirement: Human Review Synchronization Gate

`req-handoff` SHALL block when Human Review contains demand facts that are not
represented in the machine requirements case.

#### Scenario: Unsynchronized Demand Facts

- **GIVEN** Human Review adds or changes user stories, acceptance, scope,
  domain, roles, readiness, or blockers
- **WHEN** those facts are not synchronized to the machine case
- **THEN** `req-handoff` SHALL report the block and not create an OpenSpec draft

### Requirement: Review Prompt Classification

Human Review SHALL distinguish demand facts from review prompts and
detailed-design gate gaps.

#### Scenario: Prompt Is Not A Demand Fact

- **GIVEN** Human Review includes a reviewer question that does not change the
  requirements case
- **WHEN** the review is prepared for handoff
- **THEN** the question MAY remain as a review prompt without changing machine
  case data
