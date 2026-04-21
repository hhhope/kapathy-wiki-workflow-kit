# repo-agents-governance-phase0 Specification

## Purpose
TBD - created by archiving change align-repo-agents-governance-phase0. Update
Purpose after archive.

## Requirements

### Requirement: Repo `AGENTS.md` migration SHALL wait for an accepted Phase 0 mainline

The repository SHALL treat repo-level `AGENTS.md` migration as blocked until a
repo-visible Phase 0 mainline is accepted.

#### Scenario: Contributor wants to start repo `AGENTS.md` migration
- **WHEN** a contributor wants to compress, proxy-migrate, or otherwise
  restructure the repo `AGENTS.md`
- **THEN** the repository SHALL require an accepted repo-visible Phase 0
  mainline first
- **AND** candidate wiki playbooks or distill pages alone SHALL NOT count as
  acceptance

### Requirement: Phase 0 acceptance SHALL stay repo-scoped unless widened explicitly

The repository SHALL keep repo-level Phase 0 governance separate from root
dotfile alignment unless a later change explicitly widens scope.

#### Scenario: Root dotfiles are mentioned during repo Phase 0 work
- **WHEN** `~/.codex/AGENTS.md` or `~/.claude/CLAUDE.md` are discussed during
  repo Phase 0 governance work
- **THEN** the repository SHALL treat them as deferred by default
- **AND** they SHALL NOT automatically become part of the active repo change

### Requirement: Phase 0 completion SHALL remove local ADR identity conflicts

The repository SHALL not call repo Phase 0 complete while the ADR identity
surface still contains duplicate numbering that affects current governance
references.

#### Scenario: Duplicate ADR numbering still exists
- **WHEN** repo Phase 0 readiness is checked
- **AND** the current governance surface still contains duplicate ADR numbering
- **THEN** the change SHALL remain incomplete

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
