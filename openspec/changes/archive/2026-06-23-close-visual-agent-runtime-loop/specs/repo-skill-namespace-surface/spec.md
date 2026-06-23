# repo-skill-namespace-surface Specification

## ADDED Requirements

### Requirement: Repo-local skill surface SHALL distinguish bundled skills from external runtime tools

Repo-local behavior assets SHALL distinguish skills bundled under
`.codex/skills/` from runtime/system tools and host-repo parent gates when
describing routing.

#### Scenario: Visual package is installed locally

- **WHEN** a repo-local visual routing skill references a child worker
- **THEN** the referenced child worker SHALL either exist under `.codex/skills/`
  or be explicitly marked as runtime/system or host-provided
- **AND** evaluation evidence SHALL include a discovery check for the bundled
  skill names

