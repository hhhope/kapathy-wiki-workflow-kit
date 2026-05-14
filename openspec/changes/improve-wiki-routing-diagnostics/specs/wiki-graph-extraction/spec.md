## Purpose

Clarify relation parsing and readable graph summary behavior without weakening
raw graph extraction.

## ADDED Requirements

### Requirement: Wiki graph extraction SHALL parse indented relation lists

The shared frontmatter parser used by wiki graph and status workflows SHALL
parse normal indented YAML list values for supported relation fields.

#### Scenario: Relation field uses indented list syntax

- **WHEN** a wiki page frontmatter contains `derived_from:` followed by
  indented `- value` entries
- **THEN** the parser SHALL return those entries as relation values
- **AND** graph extraction SHALL emit relation edges for the parsed values
- **AND** product status relation coverage SHALL count the page as having
  relations

### Requirement: Readable graph summaries SHALL collapse spec representative pages by default

Readable graph summaries SHALL keep spec evidence in counts while avoiding
spec-heavy representative page lists by default.

#### Scenario: Object has wiki and OpenSpec nodes

- **WHEN** `scripts/summarize_wiki_graph.py` summarizes an object with
  `openspec/specs` nodes and non-spec wiki nodes
- **THEN** the object view SHALL retain raw node count, `openspec/specs` source
  layer, and `spec` artifact type
- **AND** representative pages SHALL prefer non-spec pages
- **AND** the summary SHALL expose how many spec pages were collapsed

### Requirement: Raw graph extraction SHALL keep OpenSpec spec nodes

Raw graph extraction SHALL continue to include OpenSpec spec nodes as
formalization evidence.

#### Scenario: Graph extraction runs

- **WHEN** `python3 scripts/extract_wiki_graph.py` runs
- **THEN** covered layers SHALL still include `openspec/specs`
- **AND** spec nodes SHALL remain present in raw graph output

