---
canonical_object: wiki-context-injection
artifact_type: spec
formalizes:
- wiki-context-injection
derived_from:
- wiki-runtime-auto-routing
---

# wiki-context-injection / spec

## Purpose

Capture the repository's minimal automatic context-injection contract on top of runtime
auto routing, while keeping the output bounded, repository-local, and
non-autonomous.

## Requirements

### Requirement: Repository SHALL support bounded automatic context injection on top of runtime auto routing

The repository SHALL support a downstream automatic context-injection step that reads
runtime auto-routing output and derives a bounded injected-context bundle.

#### Scenario: Runtime auto-routing artifact is available

- **WHEN** the repository has a runtime auto-routing artifact
- **THEN** it SHALL be able to derive explicit first-pass injected context and secondary context

### Requirement: Repository SHALL preserve blocked-object boundaries during automatic context injection

The repository SHALL not flatten blocked objects into injected first-pass context.

#### Scenario: Automatic context-injection artifact is generated

- **WHEN** automatic context injection runs
- **THEN** blocked objects SHALL remain explicitly separated from the injected-context bundle

### Requirement: Repository SHALL preserve proof boundaries for automatic context-injection output

The repository SHALL distinguish bounded injected-context guidance from agent autonomy
or self-directed execution.

#### Scenario: Automatic context-injection artifact is generated

- **WHEN** the repository produces automatic context-injection output
- **THEN** it SHALL state that the result is bounded repository-local injected-context guidance only
