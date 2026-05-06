## MODIFIED Requirements

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

#### Scenario: Root context governance rejects fake progressive disclosure

- **WHEN** a successor change governs `~/.codex/AGENTS.md` for drift-resistant progressive loading
- **THEN** the change SHALL record default loaded context and triggered loaded context evidence in `evaluation.md`
- **AND** it SHALL treat line count as supporting evidence only
- **AND** moving text to a support file SHALL NOT count as reduction when the support file remains on the default loaded path
- **AND** any root-local support file SHALL remain trigger-gated routing detail, not a repo policy page or a new governance layer
- **AND** `~/.codex/AGENTS.md` SHALL retain always-on hard stops and the routing principles needed to preserve behavior
- **AND** the change SHALL NOT edit repo `AGENTS.md`, repo `.codex/skills/`, repo `wiki/`, repo `rules/`, or `~/.claude/CLAUDE.md`
