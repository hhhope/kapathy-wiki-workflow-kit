## ADDED Requirements

### Requirement: Repository SHALL separate Chinese and English README sections structurally

The root README SHALL not rely on a mixed-language opening block to introduce the repository.

#### Scenario: Reader lands at the top of the README

- **WHEN** a user opens the root README
- **THEN** the content before the Chinese section SHALL not contain English descriptive prose
- **AND** the English descriptive content SHALL appear inside a separate English section

### Requirement: Repository SHALL prefer hyperlinks for README navigation targets

The root README SHALL use markdown links for repository entrypoints and documentation targets whenever the content is acting as navigation rather than a literal command.

#### Scenario: Reader uses the README as a navigation hub

- **WHEN** the README points the reader to repository pages or entry files
- **THEN** those targets SHALL be presented as markdown hyperlinks where practical
- **AND** literal shell commands SHALL remain code-formatted rather than being turned into links
