## ADDED Requirements

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
