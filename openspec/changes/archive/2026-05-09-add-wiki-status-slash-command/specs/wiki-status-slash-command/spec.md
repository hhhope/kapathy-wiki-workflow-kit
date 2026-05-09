## ADDED Requirements

### Requirement: Repository SHALL expose wiki status as a slash command

The repository SHALL provide a Claude slash command that refreshes and surfaces
the generated wiki status artifacts.

#### Scenario: User invokes wiki status command

- **WHEN** the user invokes `/wiki:status`
- **THEN** the command SHALL run the wiki status generator
- **AND** it SHALL point the user to `wiki/status/manifest.json` and
  `wiki/status/wiki-status.md`

### Requirement: Wiki status slash command SHALL preserve scope boundaries

The wiki status slash command SHALL remain a thin status wrapper and SHALL NOT
implement query, scorecard calibration, graph UI, or learning-to-change
orchestration.

#### Scenario: Command completes

- **WHEN** the command finishes refreshing status
- **THEN** it SHALL summarize status output only
- **AND** it SHALL NOT open, modify, or archive OpenSpec changes
