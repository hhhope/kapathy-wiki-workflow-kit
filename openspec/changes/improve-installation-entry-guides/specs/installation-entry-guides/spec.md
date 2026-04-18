## ADDED Requirements

### Requirement: Repository SHALL provide a bilingual root onboarding entrypoint

The repository SHALL use the root `README.md` as the canonical onboarding page for new readers and adopters of the workflow kit.

#### Scenario: Chinese reader opens the repository first

- **WHEN** a Chinese-speaking contributor opens the repository root
- **THEN** the root `README.md` SHALL explain the repository purpose, quick start, prerequisites, runtime entrypoints, and verification flow in Chinese
- **AND** it SHALL point to the canonical wiki and inbox entry pages needed to start using the kit

#### Scenario: English reader opens the repository first

- **WHEN** an English-speaking contributor opens the repository root
- **THEN** the root `README.md` SHALL provide a separate English section with equivalent onboarding information
- **AND** it SHALL not rely on mixed-language paragraphs to convey required setup steps

### Requirement: Repository SHALL document runtime and tool prerequisites explicitly

The onboarding flow SHALL list required and optional tools for adopting the workflow kit.

#### Scenario: Contributor prepares the local environment

- **WHEN** a contributor follows the root onboarding instructions
- **THEN** the repository SHALL identify the required runtime tools for the documented flow
- **AND** it SHALL distinguish required tools from optional tools such as Obsidian and Feishu/Lark CLI integrations
- **AND** it SHALL explain which runtime entrypoint applies to Codex, Cursor, and Claude

### Requirement: Repository SHALL record Feishu-source alignment state explicitly

When the referenced Feishu article cannot be fully mirrored into the repo, the repository SHALL keep a repo-visible comparison record instead of implying the source has already been synced.

#### Scenario: Source article body is unavailable in the current environment

- **WHEN** the repository cannot fetch the full Feishu article body
- **THEN** it SHALL provide a page that records the original source link, what has already been reflected in the repo, and which source details still need syncing
- **AND** the root onboarding flow SHALL link to that comparison page when discussing the article
