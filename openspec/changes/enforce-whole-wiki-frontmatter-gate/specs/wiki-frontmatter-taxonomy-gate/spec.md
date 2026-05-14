## Purpose

Define a strict, scorecarded frontmatter gate for the entire wiki.

## ADDED Requirements

### Requirement: Repository SHALL govern frontmatter across the whole wiki

The repository SHALL apply configured frontmatter rule sets to all covered
`wiki/**` markdown pages.

#### Scenario: Ops page misses required metadata

- **WHEN** a `wiki/ops` page lacks configured required fields such as `layer`,
  `domain`, or `ops_area`
- **THEN** the frontmatter checker SHALL report error-severity entries
- **AND** the strict gate SHALL fail

#### Scenario: ADR page misses required metadata

- **WHEN** a `wiki/adr` page lacks configured required fields such as `layer` or
  `domain`
- **THEN** the frontmatter checker SHALL report error-severity entries
- **AND** the strict gate SHALL fail

### Requirement: Frontmatter checker SHALL emit a scorecard

The frontmatter checker SHALL emit a scorecard derived from configured
dimensions and frontmatter findings.

#### Scenario: Blocking entries exist

- **WHEN** checker entries include blocking severities
- **THEN** the report SHALL include a scorecard with score, pass/fail, dimension
  details, and points lost
- **AND** the strict gate SHALL fail when score is below the configured minimum

### Requirement: Wiki status SHALL render strict frontmatter gate evidence

Wiki status SHALL make strict frontmatter gate results visible.

#### Scenario: Status is refreshed

- **WHEN** `python3 scripts/build_wiki_status.py` runs
- **THEN** `wiki/status/manifest.json` SHALL include strict gate and scorecard
  data from the frontmatter checker
- **AND** `wiki/status/wiki-status.md` SHALL render the strict gate result,
  scorecard, blocking count, and sample blocking entries

### Requirement: Frontmatter compliance claims SHALL use checker evidence

Agents SHALL NOT claim frontmatter compliance from narrow drift checks.

#### Scenario: Checker has strict-gate failures

- **WHEN** the strict frontmatter gate fails
- **THEN** agents SHALL report the failure and remaining inspection points
- **AND** they SHALL NOT claim whole-wiki frontmatter compliance

