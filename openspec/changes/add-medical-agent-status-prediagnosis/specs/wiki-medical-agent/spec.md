# wiki-medical-agent Specification Delta

## ADDED Requirements

### Requirement: Status responses SHALL include prediagnosis for continuation intent

The `wiki-medical-agent` response contract SHALL require a read-only
prediagnosis before asking the user for missing details when the
medical-agent result is non-executing status and the live user request is to
continue, modify, apply, repair, or decide next steps.

#### Scenario: User asks what to do next from archive-ready state

- **GIVEN** the medical-agent result is `archive_ready`
- **WHEN** the user asks what to do next
- **THEN** the agent SHALL report the script result
- **AND** interpret the live user intent
- **AND** recommend the next safe route instead of only repeating status fields

#### Scenario: User asks to modify generated or sensitive wiki output

- **GIVEN** the medical-agent result is non-executing status
- **WHEN** the user asks to modify generated or sensitive wiki output
- **THEN** the agent SHALL preserve existing write boundaries
- **AND** provide a read-only prediagnosis of the likely route before asking for
  missing details

#### Scenario: User selects a previously offered option

- **GIVEN** the agent previously offered numbered options
- **WHEN** the user replies with a bare option number
- **THEN** the agent SHALL preserve live thread context
- **AND** continue the selected option without requiring the user to restate the
  full target
