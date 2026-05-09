---
canonical_object: wiki-self-directed-execution
artifact_type: spec
formalizes:
- wiki-self-directed-execution
derived_from:
- wiki-context-injection
---

# wiki-self-directed-execution / spec

## Purpose

Capture the repository's minimal bounded self-directed execution contract on top of
automatic context injection, while keeping the output bounded, repository-local, and
non-autonomous.
## Requirements
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

### Requirement: Self-directed execution SHALL expose blocked action source refs

The repository SHALL expose source references on blocked execution entries when
those references exist, while preserving blocked execution state.

#### Scenario: Blocked excluded object has source refs

- **WHEN** bounded self-directed execution builds a blocked entry from an
  excluded object with source refs
- **THEN** the blocked entry SHALL include action source refs
- **AND** the blocked entry SHALL remain in `do_not_execute`
- **AND** it SHALL NOT be promoted into execute-now or deferred-follow-up actions
