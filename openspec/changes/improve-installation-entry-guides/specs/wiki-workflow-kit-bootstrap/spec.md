## MODIFIED Requirements

### Requirement: Repository SHALL provide a bootstrap path for the validated wiki workflow kit

When a user wants to initialize a new repository with the validated wiki workflow setup, the repository SHALL provide a bootstrap path that installs the current best-practice kit.

#### Scenario: New repository bootstrap

- **WHEN** a user initializes a new repository with the workflow kit
- **THEN** the repository SHALL create the required starter structure
- **AND** it SHALL install entry files, wiki scaffold, skills, OpenSpec, Obsidian, and examples
- **AND** it SHALL include the documented minimum inbox and intake entrypoints whenever the quick-start flow depends on them

### Requirement: Repository SHALL generate separate AI entry files for AGENTS and CLAUDE

The bootstrap path SHALL generate `AGENTS.md` for Codex/Cursor and `CLAUDE.md` for Claude while keeping the core workflow assets shared.

#### Scenario: AI entrypoints are created

- **WHEN** the bootstrap script initializes a target repository
- **THEN** it SHALL create both `AGENTS.md` and `CLAUDE.md`
- **AND** the shared workflow assets SHALL remain common across platforms

### Requirement: Repository SHALL verify installed paths according to installation mode

The workflow kit verification flow SHALL validate the installed repository against the selected installation mode instead of assuming one fixed set of required files.

#### Scenario: Optional install surfaces are disabled

- **WHEN** a target repository is initialized without optional surfaces such as Obsidian or examples
- **THEN** the verification flow SHALL pass if all mode-appropriate required paths are present
- **AND** it SHALL report any missing optional surfaces separately from true installation failures
