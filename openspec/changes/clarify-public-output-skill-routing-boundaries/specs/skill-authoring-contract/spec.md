## ADDED Requirements

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
