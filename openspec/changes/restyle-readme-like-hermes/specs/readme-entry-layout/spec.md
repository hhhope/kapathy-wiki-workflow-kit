## ADDED Requirements

### Requirement: Repository SHALL use a high-signal entry layout for the root README

The root README SHALL present the repository as an installable workflow surface with a scan-friendly entry layout rather than only a repository summary.

#### Scenario: Reader scans the repository root for the first time

- **WHEN** a user opens the root `README.md`
- **THEN** the README SHALL present a clear identity statement near the top
- **AND** it SHALL include a quick-install section, a getting-started section, a runtime quick reference, and a documentation index
- **AND** the layout SHALL help the reader find the first useful command within one screen

### Requirement: Repository SHALL preserve Chinese-first bilingual separation in the root README

The repository SHALL keep Chinese as the primary language while still providing a complete English counterpart in separate sections.

#### Scenario: Bilingual reader uses the entry README

- **WHEN** the root README presents Chinese and English guidance
- **THEN** the Chinese guidance SHALL appear first
- **AND** the English guidance SHALL appear as a separate corresponding section
- **AND** the README SHALL not depend on mixed-language paragraphs to convey required setup or runtime information
