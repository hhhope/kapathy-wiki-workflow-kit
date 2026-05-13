## Purpose

Define a repo-local wiki frontmatter taxonomy contract that prevents operations
layer metadata from masquerading as business-domain metadata.

## Requirements

### Requirement: Repository SHALL provide a single frontmatter taxonomy contract

The repository SHALL define wiki frontmatter taxonomy values and validation
policies in `wiki/config/frontmatter-taxonomy.yaml`.

#### Scenario: Agent needs taxonomy values

- **WHEN** an agent, skill, or script needs allowed domains, forbidden domains,
  `ops_area` values, path rules, producer paths, or severity
- **THEN** it SHALL read `wiki/config/frontmatter-taxonomy.yaml`
- **AND** it SHALL NOT duplicate those vocabularies in AGENTS or skill bodies

### Requirement: Repository SHALL distinguish domain from operations area

The repository SHALL reserve `domain` for real business or topic domains and use
`ops_area` for operations or governance workflow categories.

#### Scenario: Pure operations page has no business domain

- **WHEN** a pure `wiki/ops` governance page is migrated under the new contract
- **THEN** it SHALL use `layer: ops`
- **AND** it SHALL use `domain: none`
- **AND** it SHALL use a valid `ops_area`

#### Scenario: Business intake page lives in ops

- **WHEN** a `wiki/ops` intake page records business-related source intake
- **THEN** it SHALL use `layer: ops`
- **AND** it SHALL use the real domain when known
- **AND** it SHALL use `domain: unclassified` with `classification_needed: true`
  when the real domain is not known
- **AND** it SHALL use `ops_area: source-intake`

### Requirement: Repository SHALL reject forbidden domain drift

The repository SHALL treat `domain: personal-ops` as forbidden for new or
touched frontmatter.

#### Scenario: Content uses forbidden domain

- **WHEN** the checker scans a wiki page with `domain: personal-ops`
- **THEN** it SHALL report `forbidden_domain`
- **AND** the severity SHALL be `error`

#### Scenario: Producer hardcodes forbidden domain

- **WHEN** the checker scans a registered producer template containing
  `domain: personal-ops`
- **THEN** it SHALL report `producer_hardcoded_forbidden_domain`
- **AND** the severity SHALL be `error`

### Requirement: Repository SHALL expose taxonomy drift reports

The checker SHALL emit both JSON and Markdown reports.

#### Scenario: Checker runs

- **WHEN** `python3 scripts/check_wiki_frontmatter.py` runs
- **THEN** it SHALL write `/tmp/wiki-frontmatter-taxonomy-report.json`
- **AND** it SHALL write `/tmp/wiki-frontmatter-taxonomy-report.md`
- **AND** the reports SHALL include content drift, producer drift, possible
  unregistered producer warnings, and summary counts by severity

### Requirement: AGENTS SHALL route frontmatter changes through the taxonomy gate

Repo AGENTS SHALL not duplicate taxonomy vocabulary, but SHALL require the
taxonomy skill and checker for frontmatter work.

#### Scenario: Agent creates or modifies wiki frontmatter

- **WHEN** an agent creates or modifies wiki frontmatter, wiki templates, or
  repo-local frontmatter producers
- **THEN** it SHALL load `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`
- **AND** it SHALL run the taxonomy checker before claiming taxonomy compliance
  or completion
