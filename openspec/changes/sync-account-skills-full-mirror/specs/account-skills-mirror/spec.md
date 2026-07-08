# account-skills-mirror Specification

## MODIFIED Requirements

### Requirement: Account skills mirror SHALL avoid plugin mode

The repository SHALL mirror the external account-skills package as ordinary
repo content without plugin marketplace packaging or runtime plugin
registration.

#### Scenario: Mirror source into skills-drafts

- **WHEN** the user asks to sync `account-skills` into this repository without
  plugin mode
- **THEN** the content SHALL be placed under `skills-drafts/account-skills/`
- **AND** the mirror SHALL NOT add plugin marketplace routing or active
  `.codex/skills` runtime registration

#### Scenario: Plugin and local state are excluded

- **WHEN** the mirror is refreshed from the external source
- **THEN** `.claude-plugin/`, `.codex-plugin/`, `.git/`, `.idea/`,
  `.agents/`, `graphify-out/`, and `__pycache__/` SHALL be absent from the
  target
- **AND** tests that require excluded plugin manifests SHALL be excluded from
  the no-plugin mirror
- **AND** ordinary skill and kit content such as `skills/`,
  `account-cr-agent/`, `codex-integration-kit/`, and `req-agent-kit/` SHALL be
  present when available in the source

#### Scenario: Repo-specific mirror README files exist

- **WHEN** source README files contain plugin or package-local usage guidance
- **THEN** the repo mirror MAY preserve repo-specific README files that document
  direct non-plugin usage and mirror boundaries
- **AND** those preserved README exceptions SHALL be named in evaluation
  evidence.
