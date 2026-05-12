# skill-authoring-contract Specification

## Purpose
TBD - created by archiving change harden-skill-authoring-contract. Update Purpose after archive.
## Requirements
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

### Requirement: Skill authoring SHALL classify routing ownership before semantic skill changes

When creating or semantically editing a skill, the authoring process SHALL
classify the skill's routing ownership before claiming the behavior change is
complete.

#### Scenario: Contributor creates or semantically edits a skill

- **WHEN** a contributor creates or semantically edits a skill
- **THEN** the authoring evidence SHALL classify the skill as a high-level
  router/gate, module, tool wrapper, or reference helper
- **AND** the evidence SHALL state what intent class the skill owns or does not
  own

#### Scenario: Module skill affects delivery-sensitive output

- **WHEN** a module skill affects reader-facing, Feishu-facing, visual,
  source-learning, or other delivery-sensitive output
- **THEN** the authoring evidence SHALL name the applicable parent router/gate
  or state that no parent applies
- **AND** the module SHALL preserve the parent router/gate's blockers instead
  of silently becoming an independent route

#### Scenario: New visual skill is added for public materials

- **WHEN** a new or changed visual skill can produce assets for public reports,
  H5/share drafts, Feishu review drafts, or other reader-facing materials
- **THEN** the authoring evidence SHALL include a pressure scenario showing the
  skill does not bypass the public report gate for those outputs

