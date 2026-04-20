---
canonical_object: wiki-runtime-context-source-integration
artifact_type: spec
formalizes:
- wiki-runtime-context-source-integration
derived_from:
- wiki-runtime-context
---

# wiki-runtime-context-source-integration / spec

## Purpose

Capture the repository's minimal runtime-context source-integration contract on top of
runtime context, while keeping the output bounded, repository-local, and
non-autonomous.

## Requirements

### Requirement: Repository SHALL support bounded source integration on top of runtime context

The repository SHALL support a downstream source-integration step that reads runtime
context and resolves canonical objects into bounded repository-visible source
references.

#### Scenario: Runtime-context artifact is available

- **WHEN** the repository has a runtime-context artifact
- **THEN** it SHALL be able to derive source references for preferred and supporting objects

### Requirement: Repository SHALL preserve blocked-object boundaries during source integration

The repository SHALL not flatten blocked objects into first-pass source targets.

#### Scenario: Source-integrated runtime artifact is generated

- **WHEN** source integration runs
- **THEN** blocked objects SHALL remain explicitly separated from preferred and supporting source lists

### Requirement: Repository SHALL preserve proof boundaries for source-integrated runtime output

The repository SHALL distinguish repository-local source integration from external
retrieval proof or autonomous runtime behavior.

#### Scenario: Source-integrated runtime artifact is generated

- **WHEN** the repository produces source-integrated runtime output
- **THEN** it SHALL state that the result is bounded repository-local source guidance only
