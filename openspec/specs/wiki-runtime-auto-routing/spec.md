---
canonical_object: wiki-runtime-auto-routing
artifact_type: spec
formalizes:
- wiki-runtime-auto-routing
derived_from:
- wiki-runtime-context-source-integration
---

# wiki-runtime-auto-routing / spec

## Purpose

Capture the repository's minimal runtime auto-routing contract on top of runtime
context source integration, while keeping the output bounded, repository-local, and
non-autonomous.
## Requirements
### Requirement: Repository SHALL support bounded runtime auto routing on top of source integration

The repository SHALL support a downstream runtime auto-routing step that reads
source-integrated runtime output and derives a bounded first-pass reading plan.

#### Scenario: Source-integrated runtime artifact is available

- **WHEN** the repository has a source-integrated runtime artifact
- **THEN** it SHALL be able to derive explicit first-pass and second-pass source routes

### Requirement: Repository SHALL preserve blocked-object boundaries during runtime auto routing

The repository SHALL not flatten blocked objects into first-pass or second-pass reading
routes.

#### Scenario: Runtime auto-routing artifact is generated

- **WHEN** runtime auto routing runs
- **THEN** blocked objects SHALL remain explicitly separated from the generated reading plan

### Requirement: Repository SHALL preserve proof boundaries for runtime auto-routing output

The repository SHALL distinguish bounded runtime auto-routing guidance from autonomous
runtime execution or context injection.

#### Scenario: Runtime auto-routing artifact is generated

- **WHEN** the repository produces runtime auto-routing output
- **THEN** it SHALL state that the result is bounded repository-local routing guidance only

### Requirement: Runtime auto routing SHALL carry blocked trace sources without routing them

The repository SHALL carry blocked-object source references as trace-only
metadata while keeping blocked objects outside first-pass and second-pass routes.

#### Scenario: Blocked object enters runtime auto routing

- **WHEN** runtime auto routing reads a source-integrated blocked object with
  trace-only source references
- **THEN** the corresponding `do_not_open_first` entry SHALL preserve those
  references as blocked metadata
- **AND** the references SHALL NOT be emitted as first-pass or second-pass route
  sources
