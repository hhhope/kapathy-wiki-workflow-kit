# root-governance-alignment Specification

## Purpose
TBD - created by archiving change decide-root-governance-alignment. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL decide root governance alignment before closure

Before treating `agents-governance-drift` as closed, the repository SHALL keep root governance alignment visible as an open decision until a reviewed relationship is accepted.

#### Scenario: Root governance drift remains open
- **WHEN** repo `AGENTS.md`, root `~/.codex/AGENTS.md`, and root
  `~/.claude/CLAUDE.md` can diverge on shared governance behavior
- **THEN** the repository SHALL keep root governance alignment visible as an
  open decision
- **AND** it SHALL NOT treat repo-local Phase 0 closure as closure of the root
  governance topic

### Requirement: Root behavior assets MUST follow spec-driven design sequencing

The repository MUST record the design boundary and evaluation evidence in the active OpenSpec change before editing personal root behavior assets from this governance thread.

#### Scenario: Chat-level plan asks for implementation

- **WHEN** a chat-level plan targets personal global `AGENTS.md`, skill skeletons, or replay-harness collaboration
- **THEN** the repository SHALL record proposal/design/tasks/evaluation first
- **AND** it SHALL defer root dotfile, skill, and repo guidance edits until the SDD boundary is accepted

#### Scenario: Root compression change applies adopted governance model

- **WHEN** a change applies the adopted Pattern Catalog to `~/.codex/AGENTS.md`
- **THEN** the change SHALL declare Root AGENTS as its target pattern in `tasks.md`
- **AND** the change SHALL record before and after line counts in `evaluation.md`
- **AND** the change SHALL map each edited line back to one row of the adopted Issue Routing Table or to a Pattern Catalog field (Purpose / Owns / Anti-patterns)
- **AND** the change SHALL NOT edit repo `AGENTS.md`, `rules/`, `skills/`, or wiki method pages in the same change

### Requirement: Repository SHALL gate wiki promotion for root governance design

Root-governance design material SHALL NOT be promoted directly into a wiki method page or ADR before the active OpenSpec design boundary is accepted.

#### Scenario: Design discussion exposes a correction
- **WHEN** the discussion corrects the implementation path or wiki landing path
- **THEN** the active OpenSpec change SHALL be the first durable design surface
- **AND** wiki landing SHALL be limited to targeted trace or retro material
  unless a later stable decision justifies method or ADR promotion

### Requirement: Behavior-asset changes SHALL pass the Self-Check Checklist before completion

Any change that edits a behavior-asset layer (root `AGENTS.md`, repo `AGENTS.md`, `rules/`, `skills/`) SHALL run the Self-Check Checklist recorded in `design.md` before marking any behavior-asset editing task in `tasks.md` complete, declaring each checklist item as `applicable`, `not applicable`, or `blocker` per the declaration rule in `design.md`.

#### Scenario: Behavior-asset editing task is about to be marked complete
- **WHEN** a task in a behavior-asset change edits a behavior-asset layer and is about to be marked complete
- **AND** the Self-Check Checklist contains items not yet declared as `applicable`, `not applicable`, or `blocker`
- **THEN** the task SHALL remain open
- **AND** the undeclared or `blocker` items SHALL be recorded in `tasks.md` or in `evaluation.md`

#### Scenario: Checklist item does not apply to the change
- **WHEN** a Self-Check Checklist item does not apply to the current change (for example, a design-only or candidate-only change that does not add new requirements, or a change that does not alter trigger or refusal semantics)
- **THEN** the change SHALL mark that item `not applicable` with a recorded reason
- **AND** the item SHALL NOT block task completion on that basis alone

### Requirement: Behavior-asset changes SHOULD declare Pattern Catalog fields before completion

Any change that edits a behavior-asset layer SHOULD declare the Pattern Catalog fields (Purpose, Owns, Must Not Own, Required Evidence, Anti-patterns) for its target pattern type in `design.md` or `evaluation.md` before any task in `tasks.md` is marked complete. Promotion of this requirement to SHALL is a candidate pending the review gate in `tasks.md` task 3b.15; until that gate closes, only SHOULD binds.

#### Scenario: Pattern fields missing
- **WHEN** a behavior-asset change does not declare the Pattern Catalog fields
  for its target pattern type
- **THEN** the change SHOULD record the missing fields as a tracked follow-up
  in `tasks.md` or `evaluation.md`
- **AND** the missing fields SHALL NOT block task completion until the SHOULD
  is promoted to SHALL by the review gate

