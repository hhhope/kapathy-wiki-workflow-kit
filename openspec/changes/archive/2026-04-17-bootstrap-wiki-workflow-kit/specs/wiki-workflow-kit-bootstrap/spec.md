## ADDED Requirements

### Requirement: Repository SHALL provide a bootstrap path for the validated wiki workflow kit

When a user wants to initialize a new repository with the validated wiki workflow setup, the repository SHALL provide a bootstrap path that installs the current best-practice kit.

#### Scenario: New repository bootstrap

- **WHEN** a user initializes a new repository with the workflow kit
- **THEN** the repository SHALL create the required starter structure
- **AND** it SHALL install entry files, wiki scaffold, skills, OpenSpec, Obsidian, and examples

### Requirement: Repository SHALL install current validated example families

The bootstrap path SHALL install examples based on current supported task families rather than placeholder demo files.

#### Scenario: Examples are installed

- **WHEN** the bootstrap script installs example content
- **THEN** it SHALL include examples for meeting notes, project management, learning notes, Weixin reading, GitHub analysis, and explore trace

### Requirement: Repository SHALL generate separate AI entry files for AGENTS and CLAUDE

The bootstrap path SHALL generate `AGENTS.md` for Codex/Cursor and `CLAUDE.md` for Claude while keeping the core workflow assets shared.

#### Scenario: AI entrypoints are created

- **WHEN** the bootstrap script initializes a target repository
- **THEN** it SHALL create both `AGENTS.md` and `CLAUDE.md`
- **AND** the shared workflow assets SHALL remain common across platforms
