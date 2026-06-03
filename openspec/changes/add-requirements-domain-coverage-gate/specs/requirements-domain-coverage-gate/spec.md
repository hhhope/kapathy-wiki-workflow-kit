## ADDED Requirements

### Requirement: Strict requirements readiness SHALL include domain coverage

Strict taxonomy v2 requirements cases SHALL expose a domain coverage gate before
being considered ready for OpenSpec handoff.

#### Scenario: Valid domain model without coverage is blocked
- **GIVEN** a requirements case has a confirmed `domain_model`
- **AND** it has confirmed roles, user stories, acceptance functions, and
  bidirectional mappings
- **AND** at least one required or in-scope subdomain/context has no explicit
  story or acceptance coverage
- **WHEN** the requirements checker runs in strict taxonomy v2 mode
- **THEN** the checker SHALL report `domain_coverage_gate.passed=false`
- **AND** the final hard gate SHALL NOT pass

#### Scenario: Covered or explicitly deferred contexts can pass
- **GIVEN** each required or in-scope subdomain/context is classified as
  `full_coverage`, `light_coverage`, `out_of_scope`, or `follow_up`
- **AND** non-full classifications include a reason and evidence anchor
- **WHEN** the requirements checker runs
- **THEN** the checker MAY pass the domain coverage gate if all other readiness
  rules pass

### Requirement: User stories SHALL bind to domain lifecycle evidence

Strict taxonomy v2 user stories SHALL identify the domain, context, and
aggregate lifecycle evidence they cover.

#### Scenario: Story without domain lifecycle references is blocked
- **GIVEN** a strict taxonomy v2 requirements case has a user story
- **AND** the story has `role_ref`, `want`, `benefit`, and acceptance mappings
- **BUT** the story has no `domain_refs`, `context_refs`, or `aggregate_refs`
- **WHEN** the checker runs
- **THEN** the checker SHALL report a story domain-coverage blocker

#### Scenario: Unknown lifecycle reference is blocked unless explicitly candidate
- **GIVEN** a story references a context or aggregate root not registered in the
  active requirements taxonomy
- **AND** the reference is not preserved as a candidate or follow-up term with a
  reason
- **WHEN** the checker runs
- **THEN** the checker SHALL report an unknown coverage reference blocker

### Requirement: Acceptance functions SHALL classify observable coverage

Strict taxonomy v2 acceptance functions SHALL identify whether they cover state
changes, context handoffs, failure paths, or evidence paths.

#### Scenario: Aggregate lifecycle lacks state-change acceptance
- **GIVEN** an in-scope aggregate lifecycle appears in domain coverage
- **AND** no mapped acceptance function covers an observable state change for
  that lifecycle
- **WHEN** the checker runs
- **THEN** the checker SHALL block readiness with a state-change coverage
  blocker

#### Scenario: Context handoff lacks handoff acceptance
- **GIVEN** `domain_model.context_handoffs` includes a handoff between two
  bounded contexts
- **AND** no mapped acceptance function covers that handoff
- **AND** the handoff is not explicitly classified as `light_coverage` or
  `follow_up`
- **WHEN** the checker runs
- **THEN** the checker SHALL block readiness with a handoff coverage blocker

#### Scenario: Failure and evidence paths are required when surfaced
- **GIVEN** source material or taxonomy trigger rules surface failure paths or
  audit evidence paths
- **AND** no acceptance function covers them as `failure_path` or `evidence`
- **WHEN** the checker runs
- **THEN** the checker SHALL block readiness with the corresponding coverage
  blocker

### Requirement: OpenSpec handoff SHALL preserve coverage evidence

OpenSpec draft generation from a requirements case SHALL include domain
coverage evidence and SHALL refuse cases whose domain coverage gate is blocked.

#### Scenario: Coverage-ready case produces coverage section
- **GIVEN** a requirements case passes domain model, domain coverage, and
  delivery gates
- **WHEN** OpenSpec draft generation runs
- **THEN** the generated draft SHALL include domain coverage, context coverage,
  aggregate lifecycle coverage, and acceptance coverage evidence

#### Scenario: Coverage-blocked case refuses draft creation
- **GIVEN** a requirements case has any domain coverage blocker
- **WHEN** OpenSpec draft generation runs
- **THEN** draft creation SHALL be refused
- **AND** the blocker list SHALL identify the missing coverage
