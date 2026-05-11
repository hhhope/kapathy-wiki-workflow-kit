# wiki-status-slash-command Specification

## Purpose
TBD - created by archiving change add-wiki-status-slash-command. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL expose wiki status as a Codex skill

The repository SHALL provide a repo-local Codex skill that refreshes and
summarizes the generated wiki status surface.

#### Scenario: User invokes wiki status

- **WHEN** the user invokes the repo's wiki status skill
- **THEN** the skill source SHALL exist at `.codex/skills/wiki-status/SKILL.md`
- **AND** it SHALL run or reference `python3 scripts/build_wiki_status.py`
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
