## ADDED Requirements

### Requirement: Project-management weekly skill SHALL require structural TDD for editable weekly visuals
When the agent edits an HTML, gantt, or similar weekly visual file, the skill SHALL require a failing structural check before the edit and a passing check after the edit.

#### Scenario: Agent edits a weekly visual
- **WHEN** the agent edits an editable weekly visual file such as `html`, `h5`, or gantt-like layout
- **THEN** the skill SHALL direct the agent to perform a RED structural check first and a GREEN check after the change
