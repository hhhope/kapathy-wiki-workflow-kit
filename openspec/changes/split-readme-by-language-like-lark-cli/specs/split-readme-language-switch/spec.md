## ADDED Requirements

### Requirement: Repository SHALL switch README language through linked companion files

The repository SHALL present Chinese and English README content as separate files connected by top-level language switch links.

#### Scenario: Reader opens the root README

- **WHEN** a user opens `README.md`
- **THEN** the file SHALL contain the Chinese documentation body
- **AND** the file SHALL include a link to `README.en.md`
- **AND** the file SHALL not include the full English documentation body

#### Scenario: Reader opens the English README

- **WHEN** a user opens `README.en.md`
- **THEN** the file SHALL contain the English documentation body
- **AND** the file SHALL include a link back to `README.md`
- **AND** the file SHALL not include the full Chinese documentation body

### Requirement: Repository SHALL keep README navigation link-first

The repository SHALL use markdown links for documentation and repository entrypoints when the content is acting as navigation.

#### Scenario: Reader uses README as a repository map

- **WHEN** the README points to repository pages or entry files
- **THEN** those targets SHALL be rendered as markdown hyperlinks where practical
- **AND** literal shell commands SHALL remain code-formatted rather than being turned into links
