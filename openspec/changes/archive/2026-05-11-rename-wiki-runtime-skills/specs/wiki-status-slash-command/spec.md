## REMOVED Requirements

### Requirement: Repository SHALL expose wiki status as a repo-level Codex slash command

The repository SHALL provide a repo-local Codex plugin command that refreshes
and surfaces the generated wiki status artifacts, using the wiki capability
namespace as the user-facing command name.

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

## ADDED Requirements

### Requirement: Repository SHALL expose wiki status as a Codex skill

The repository SHALL provide an installable user-scope Codex skill that refreshes
and summarizes the generated wiki status surface.

#### Scenario: User invokes wiki status

- **WHEN** the user invokes `$wiki-status`
- **THEN** the skill SHALL run or reference `python3 scripts/build_wiki_status.py`
- **AND** it SHALL read `wiki/status/manifest.json`
- **AND** it SHALL read `wiki/status/wiki-status.md`
- **AND** it SHALL preserve the existing wiki status boundary

### Requirement: Wiki status skill SHALL preserve scope boundaries

The wiki status skill SHALL remain a thin status wrapper and SHALL NOT implement
a natural-language query engine, scorecard, graph UI, or change queue.

#### Scenario: Wiki status skill completes

- **WHEN** `$wiki-status` reports the current wiki status
- **THEN** it SHALL NOT create, modify, or archive OpenSpec changes
- **AND** it SHALL NOT mark OpenSpec tasks complete
- **AND** it SHALL NOT claim hidden semantic search or runtime autonomy
