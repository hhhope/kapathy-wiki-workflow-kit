## Purpose

Extend the wiki status surface so health checks include domain taxonomy and
graph parse diagnostics.

## ADDED Requirements

### Requirement: Wiki status SHALL surface domain taxonomy health

The wiki status manifest and Markdown report SHALL summarize domain taxonomy
health from the existing frontmatter taxonomy checker.

#### Scenario: Taxonomy drift exists

- **WHEN** `python3 scripts/build_wiki_status.py` is run
- **AND** `scripts/check_wiki_frontmatter.py` reports taxonomy drift
- **THEN** `wiki/status/manifest.json` SHALL include
  `domain_taxonomy_health`
- **AND** `wiki/status/wiki-status.md` SHALL render a domain taxonomy health
  section with severity counts and bounded sample entries
- **AND** the status surface SHALL NOT duplicate allowed domain or `ops_area`
  vocabularies from `wiki/config/frontmatter-taxonomy.yaml`

### Requirement: Wiki status SHALL surface graph parse health

The wiki status manifest and Markdown report SHALL expose suspicious relation
parse failures before users manually inspect graph artifacts.

#### Scenario: Raw relation field parses as empty

- **WHEN** a wiki page frontmatter contains a supported relation field such as
  `derived_from` or `related_objects`
- **AND** the parsed relation value is empty
- **THEN** `wiki/status/manifest.json` SHALL include a `graph_parse_health`
  entry for the page
- **AND** the entry SHALL include the page path, relation field names, problem,
  and repair route
- **AND** `wiki/status/wiki-status.md` SHALL render graph parse health
  summary and samples

### Requirement: Wiki status SHALL remain diagnostic only

The wiki status workflow SHALL report health without applying repairs.

#### Scenario: Status detects a repair candidate

- **WHEN** domain taxonomy or graph parse health reports drift
- **THEN** wiki status SHALL keep the result as diagnostic output
- **AND** it SHALL NOT modify frontmatter, taxonomy config, runtime scripts,
  skills, AGENTS, or OpenSpec lifecycle state

