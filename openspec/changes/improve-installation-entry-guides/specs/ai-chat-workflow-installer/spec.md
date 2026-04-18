## MODIFIED Requirements

### Requirement: Repository SHALL support adapter outputs for Codex, Cursor, and Claude

The canonical installer model SHALL define explicit adapter outputs for Codex, Cursor, and Claude instead of implying that one raw file can be copied unchanged to every platform.

#### Scenario: Cross-platform installation is prepared

- **WHEN** the repository prepares an installation flow for Codex, Cursor, and Claude
- **THEN** it SHALL define an explicit adapter output for each target
- **AND** it SHALL preserve shared workflow intent across those adapters
- **AND** it SHALL not present a single universal raw skill file as the complete installation surface
- **AND** reader-facing onboarding SHALL state which adapter artifacts are already present in the repository versus which adapters are only documented boundaries
