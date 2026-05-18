## ADDED Requirements

### Requirement: Wiki status command surface SHALL preserve a user-facing capability name

The repository SHALL define the wiki status command surface separately from the package or plugin namespace so the user-facing capability name remains explicit.

#### Scenario: Short wiki status invocation is supported
- **WHEN** the local command runtime supports a `/wiki:status` invocation or
  alias for the repo wiki status capability
- **THEN** the repository SHALL expose that invocation or alias
- **AND** it SHALL route to the existing wiki status behavior.

#### Scenario: Short wiki status invocation is not supported
- **WHEN** local command runtime evidence shows that `/wiki:status` cannot be
  exposed without breaking package or plugin constraints
- **THEN** the repository SHALL keep the supported prefixed invocation
- **AND** it SHALL record the constraint as decision evidence.

### Requirement: Wiki status command surface SHALL remain status-only

The wiki status command surface SHALL preserve the status-only boundary defined by the existing wiki status specs.

#### Scenario: Wiki status command is invoked
- **WHEN** the wiki status command or alias runs
- **THEN** it SHALL refresh or summarize wiki status artifacts only
- **AND** it SHALL NOT apply repairs, mutate frontmatter, create or archive
  OpenSpec changes, run graph/query workflows, or mark tasks complete.

### Requirement: Wiki status command surface changes SHALL be verified before claims

The repository SHALL include local evidence before claiming a wiki status command name or alias is supported.

#### Scenario: Command surface is changed or confirmed
- **WHEN** implementation changes or confirms the wiki status command surface
- **THEN** the change SHALL include focused validation or replay evidence for
  the supported invocation
- **AND** it SHALL include evidence that status-only boundaries still hold.
