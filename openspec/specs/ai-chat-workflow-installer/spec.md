## ADDED Requirements

### Requirement: Repository SHALL define a canonical AI chat workflow installer model

When the repository needs to install its workflow and skill system into multiple AI chat runtimes, it SHALL define one canonical installer model owned by the repository rather than relying on unrelated per-platform drafts.

#### Scenario: Contributor needs one repository-owned installation model

- **WHEN** a contributor wants to package the repository workflow for multiple AI chat runtimes
- **THEN** the repository SHALL define one canonical installer model
- **AND** that model SHALL identify canonical workflow inputs separately from platform-specific outputs

### Requirement: Repository SHALL support adapter outputs for Codex, Cursor, and Claude

The canonical installer model SHALL define explicit adapter outputs for Codex, Cursor, and Claude instead of implying that one raw file can be copied unchanged to every platform.

#### Scenario: Cross-platform installation is prepared

- **WHEN** the repository prepares an installation flow for Codex, Cursor, and Claude
- **THEN** it SHALL define an explicit adapter output for each target
- **AND** it SHALL preserve shared workflow intent across those adapters
- **AND** it SHALL not present a single universal raw skill file as the complete installation surface

### Requirement: Repository SHALL provide a shareable explainer for the installer model

The repository SHALL provide a shareable explanation artifact for the installer model so that the installation logic, platform mapping, and scope boundaries can be communicated outside the repository chat history.

#### Scenario: Feishu-facing explanation is needed

- **WHEN** a contributor needs to share the installer approach in Feishu
- **THEN** the repository SHALL provide a shareable explainer artifact
- **AND** the explainer SHALL include purpose, platform mappings, and scope boundaries
