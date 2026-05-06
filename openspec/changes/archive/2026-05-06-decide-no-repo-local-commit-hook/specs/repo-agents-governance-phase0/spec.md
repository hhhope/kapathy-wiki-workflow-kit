## MODIFIED Requirements

### Requirement: Commit-gate status SHALL be explicit before Phase 1 begins

The repository SHALL make the repo-local commit-gate status explicit before
Phase 1 `AGENTS.md` migration begins.

#### Scenario: Phase 1 is considered after Phase 0

- **WHEN** the repository is deciding whether Phase 1 migration may begin
- **THEN** it SHALL have an explicit repo-visible decision for the repo-local
  commit gate
- **AND** that decision SHALL state either:
  - the gate is required and must exist before migration
  - or the gate is deferred and must be decided by the Phase 1 change itself
  - or the gate is not part of the default governance path and requires a
    later reversing change before implementation
