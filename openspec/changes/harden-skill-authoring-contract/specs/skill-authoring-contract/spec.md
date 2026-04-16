## ADDED Requirements

### Requirement: Repository SHALL define a language contract for skill authoring

The repository SHALL explicitly distinguish the language default for wiki content from the language default for behavior assets, while shared skill-authoring guidance SHALL define the default behavior-asset language.

#### Scenario: Contributor authors a repo-local skill
- **WHEN** a contributor creates or edits `.codex/skills/*`
- **THEN** the shared skill-authoring guidance SHALL treat the skill as English-first
- **AND** the repository SHALL keep `wiki/*` Chinese-first
- **AND** the wiki's Chinese-first writing policy SHALL NOT be treated as the default for the skill body

### Requirement: Repository SHALL require repo-constraint scanning before skill authoring

Before creating or semantically editing a repo-local skill, the shared skill-authoring guidance SHALL require scanning repo-local execution and delivery constraints that affect the skill contract.

#### Scenario: Skill affects reader-facing or external delivery
- **WHEN** a skill being authored affects reader-facing, Feishu-facing, or other delivery-specific output behavior
- **THEN** the author SHALL scan the relevant repo-local constraints first
- **AND** the resulting skill SHALL reflect those constraints explicitly or by reference

### Requirement: Repository SHALL optimize project-local skills for low-token retrieval

Project-local skill bodies SHALL stay compact and move longer examples or templates out of the main body when possible, with shared guidance defining the compact body pattern.

#### Scenario: Skill contains long examples or duplicated repo context
- **WHEN** a project-local skill starts accumulating repeated repo context, long examples, or templates
- **THEN** the repository SHALL move that material to `references/` or another linked file
- **AND** the main `SKILL.md` SHALL keep only the trigger, hard rules, and concise anti-pattern guidance
