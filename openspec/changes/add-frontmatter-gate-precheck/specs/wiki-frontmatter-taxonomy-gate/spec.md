## Purpose

Keep the strict whole-wiki frontmatter gate executable without forcing agents to
load full taxonomy or full drift reports during routine checks.

## ADDED Requirements

### Requirement: Frontmatter gate SHALL expose a compact precheck entrypoint

The repository SHALL provide a Python precheck command for routine frontmatter
gate checks that reads the configured taxonomy and emits bounded
agent-readable evidence.

#### Scenario: Strict gate has blocking entries

- **WHEN** the frontmatter strict gate has blocking entries
- **THEN** the precheck command SHALL exit non-zero
- **AND** it SHALL report pass/fail, score, minimum score, blocking count,
  summary counts, bounded top blockers, and full report paths
- **AND** it SHALL NOT require agents to load the full taxonomy YAML or full
  drift report into conversation context

#### Scenario: A target path is supplied

- **WHEN** the precheck command is run with `--target PATH`
- **THEN** the output SHALL include bounded entries for that target when
  matching findings exist
- **AND** it SHALL include bounded repair hints for required fields, expected
  values, and relevant allowed values
- **AND** it SHALL preserve the whole-gate pass/fail result

### Requirement: Frontmatter taxonomy skill SHALL prefer precheck for routine checks

Agents SHALL use the compact precheck as the default routine frontmatter gate
entrypoint.

#### Scenario: Agent checks frontmatter compliance without editing taxonomy

- **WHEN** an agent is checking frontmatter compliance or remaining drift
- **THEN** the skill SHALL route the agent to the compact precheck first
- **AND** the skill SHALL reserve full YAML/checker loading for taxonomy edits,
  checker debugging, or insufficient precheck evidence
