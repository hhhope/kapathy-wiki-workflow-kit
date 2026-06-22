# account-skills-mirror Specification

## ADDED Requirements

### Requirement: Account skills mirror SHALL avoid plugin mode

The repository SHALL mirror the external account-skills package as ordinary
repo content without plugin marketplace packaging or runtime plugin
registration.

#### Scenario: Mirror source into skills-drafts

- **WHEN** the user asks to upload `D:\skills\account-skills` here without plugin
  mode
- **THEN** the content SHALL be placed under `skills-drafts/account-skills/`
- **AND** the mirror SHALL NOT add plugin marketplace routing or active
  `.codex/skills` runtime registration

#### Scenario: Plugin and local state are excluded

- **WHEN** the mirror is created
- **THEN** `.claude-plugin/`, `.git/`, `.idea/`, and `graphify-out/` SHALL be
  absent from the target
- **AND** ordinary skill and kit content such as `skills/`,
  `account-cr-agent/`, `codex-integration-kit/`, and `req-agent-kit/` SHALL be
  present when available in the source

### Requirement: Mirror README SHALL document direct usage

The mirror SHALL include a README for direct non-plugin usage.

#### Scenario: README describes non-plugin use

- **WHEN** a reader opens `skills-drafts/account-skills/README.md`
- **THEN** it SHALL state that this is a direct mirror and not plugin mode
- **AND** it SHALL describe how to inspect or copy ordinary skill folders
- **AND** it SHALL NOT present plugin marketplace install commands as the
  primary path
