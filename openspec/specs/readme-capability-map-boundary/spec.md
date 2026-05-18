# readme-capability-map-boundary Specification

## Purpose
TBD - created by archiving change document-readme-capability-map-boundary. Update Purpose after archive.
## Requirements
### Requirement: README SHALL describe the project capability map

The repository README SHALL summarize the wiki layers, core capabilities,
runtime surfaces, and governance sources so future contributors and agents can
orient themselves before choosing a detailed artifact.

#### Scenario: Reader opens the repository cold

- **WHEN** a reader starts from README
- **THEN** the README SHALL identify the major repository layers
- **AND** it SHALL summarize the main capabilities those layers support
- **AND** it SHALL point to deeper runtime or governance artifacts instead of
  embedding all operational detail.

### Requirement: README SHALL NOT become runtime authority

The repository README SHALL remain project description and orientation. It
SHALL NOT be treated as the runtime entrypoint, behavior source of truth, or
permission to bypass OpenSpec, ADR, skills, command docs, or generated status
evidence.

#### Scenario: README mentions runtime or MOC projection

- **WHEN** README describes wiki runtime surfaces or future Obsidian MOC
  projection
- **THEN** the repository SHALL treat those descriptions as orientation
- **AND** behavior changes SHALL still require the appropriate OpenSpec,
  ADR, skill, command-doc, or runtime implementation artifact.

### Requirement: README SHALL distinguish current capabilities from future projection work

The repository README SHALL distinguish current wiki runtime and graph
diagnostic capabilities from future Obsidian-visible projection work.

#### Scenario: README describes MOC projection

- **WHEN** README mentions future `wiki/moc` or Obsidian graph projection
- **THEN** it SHALL identify the capability as planned or future unless an
  approved implementation artifact exists
- **AND** it SHALL NOT imply that status, graph, apply, react, or eval already
  generate MOC pages.

