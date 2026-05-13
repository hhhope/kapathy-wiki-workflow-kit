# behavior-asset-prior-art-gate Specification

## ADDED Requirements

### Requirement: Behavior-asset changes SHALL include prior-art dedupe evidence

Semantic changes to behavior assets SHALL record how the proposed rule relates
to existing global, common, and repo-local behavior assets before the rule is
considered complete.

#### Scenario: Active behavior-asset change touches rules or AGENTS

- **WHEN** an active OpenSpec change semantically changes `skills/*`,
  `rules/*`, or `AGENTS.md`
- **THEN** the change SHALL include `evaluation.md`
- **AND** the evaluation SHALL include a prior-art/common-rule dedupe section
- **AND** that section SHALL identify scanned sources, owned behavior,
  referenced behavior, and rejected or non-promoted behavior

#### Scenario: Proposed behavior belongs to a common/global rule

- **WHEN** an external article, README, example, or conversation suggests a
  generic engineering policy already covered by global/common rules
- **THEN** the repo-local behavior asset SHALL reference the existing rule
  instead of duplicating the generic policy
- **AND** the evaluation SHALL preserve the non-promotion boundary

### Requirement: Prior-art gate SHALL stay structural and maintainable

The checker SHALL verify the existence of dedupe evidence without trying to
perform full semantic overlap analysis.

#### Scenario: Checker inspects a behavior-asset change

- **WHEN** `python3 scripts/check_behavior_assets.py` runs
- **AND** a non-grandfathered active change touches `skills/*`, `rules/*`, or
  `AGENTS.md`
- **THEN** it SHALL report an error if the required prior-art dedupe evidence is
  missing
- **AND** it SHALL not require a hardcoded vocabulary list of all possible rule
  domains
