## Purpose

Define the repository's path for generating a sanitized, runnable LLM-WIKI seed
repository from the current LLM-Wiki runtime system.

## ADDED Requirements

### Requirement: Repository SHALL generate a manifest-driven LLM-WIKI seed repository

The repository SHALL provide a manifest-driven path for generating a seed
repository for `hhhope/LLM-WIKI`.

#### Scenario: Seed repository is generated

- **WHEN** the seed builder is run with a target directory
- **THEN** it SHALL copy only allowlisted files and directories
- **AND** it SHALL create required wiki runtime directories
- **AND** it SHALL write minimal root files and sanitized seed wiki pages
- **AND** it SHALL reject non-empty targets unless explicit force is provided.

### Requirement: Seed repository SHALL preserve the real wiki runtime surface

The seed repository SHALL preserve the current repo-local wiki runtime,
learning, public-output, OpenSpec, and medical-loop skill surface.

#### Scenario: Skill surface is copied

- **WHEN** the seed repository is generated
- **THEN** it SHALL include required `.codex/skills/wiki-*` skills
- **AND** it SHALL include learning-capture and public-report gate skills
- **AND** it SHALL include OpenSpec lifecycle helper skills
- **AND** it SHALL include medical-loop stage skills
- **AND** it SHALL NOT replace those skills with generic `ingest`, `query`,
  `lint`, or `medical-agent` placeholder directories.

### Requirement: Seed repository SHALL exclude private history and archive dumps

The seed repository SHALL copy the system, not the current repository history.

#### Scenario: Private or historical paths exist in the source repository

- **WHEN** the seed repository is generated
- **THEN** it SHALL NOT copy `inbox/`, `logs/`, private report bundles, full
  medical-loop history, or full OpenSpec archive history
- **AND** it SHALL use sanitized seed pages for public examples.

### Requirement: Seed repository SHALL provide minimal verification

The repository SHALL provide a verifier and minimal runtime verification path
for the generated seed.

#### Scenario: Seed verification runs

- **WHEN** the verifier runs against a generated seed repository
- **THEN** it SHALL check required root, skill, config, script, wiki, and
  sanitized sample paths
- **AND** it SHALL check that forbidden private/archive paths are absent.

#### Scenario: Runtime verification runs

- **WHEN** minimal runtime verification is run in the generated target
- **THEN** taxonomy, status, graph, scorecard, and medical-loop preview commands
  SHALL either pass or produce bounded seed-safe fixes
- **AND** verification SHALL NOT import private historical content only to make
  a check pass.
