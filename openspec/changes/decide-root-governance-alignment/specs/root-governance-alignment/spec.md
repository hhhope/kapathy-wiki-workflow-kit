## ADDED Requirements

### Requirement: Repository SHALL decide root governance alignment before closure

Before treating `agents-governance-drift` as closed, the repository SHALL record
the relationship between repo-level governance and personal root dotfile
governance.

#### Scenario: Root governance drift remains open
- **WHEN** repo `AGENTS.md`, root `~/.codex/AGENTS.md`, and root
  `~/.claude/CLAUDE.md` can diverge on shared governance behavior
- **THEN** the repository SHALL keep root governance alignment visible as an
  open decision
- **AND** it SHALL NOT treat repo-local Phase 0 closure as closure of the root
  governance topic

### Requirement: Root behavior assets MUST follow spec-driven design sequencing

The repository MUST record the design boundary and evaluation evidence in the
active OpenSpec change before editing personal root behavior assets from this
governance thread.

#### Scenario: Chat-level plan asks for implementation
- **WHEN** a chat-level plan targets personal global `AGENTS.md`, skill
  skeletons, or replay-harness collaboration
- **THEN** the repository SHALL record proposal/design/tasks/evaluation first
- **AND** it SHALL defer root dotfile, skill, and repo guidance edits until the
  SDD boundary is accepted

### Requirement: Repository SHALL gate wiki promotion for root governance design

Root-governance design material SHALL NOT be promoted directly into a wiki
method page or ADR before the active OpenSpec design boundary is accepted.

#### Scenario: Design discussion exposes a correction
- **WHEN** the discussion corrects the implementation path or wiki landing path
- **THEN** the active OpenSpec change SHALL be the first durable design surface
- **AND** wiki landing SHALL be limited to targeted trace or retro material
  unless a later stable decision justifies method or ADR promotion
