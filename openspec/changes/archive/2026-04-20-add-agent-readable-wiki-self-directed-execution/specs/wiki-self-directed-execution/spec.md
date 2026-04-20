## ADDED Requirements

### Requirement: Repository SHALL support bounded self-directed execution on top of context injection

The repository SHALL support a downstream bounded self-directed execution step that
reads automatic context-injection output and derives a bounded execution-plan bundle.

#### Scenario: Automatic context-injection artifact is available

- **WHEN** the repository has an automatic context-injection artifact
- **THEN** it SHALL be able to derive explicit execute-now and deferred-follow-up actions

### Requirement: Repository SHALL preserve blocked-object boundaries during bounded self-directed execution

The repository SHALL not flatten blocked objects into execute-now actions.

#### Scenario: Bounded self-directed execution artifact is generated

- **WHEN** bounded self-directed execution runs
- **THEN** blocked objects SHALL remain explicitly separated from the generated execution plan

### Requirement: Repository SHALL preserve proof boundaries for bounded self-directed execution output

The repository SHALL distinguish bounded execution guidance from unrestricted agent
autonomy or self-directed execution without guardrails.

#### Scenario: Bounded self-directed execution artifact is generated

- **WHEN** the repository produces bounded self-directed execution output
- **THEN** it SHALL state that the result is bounded repository-local execution guidance only
