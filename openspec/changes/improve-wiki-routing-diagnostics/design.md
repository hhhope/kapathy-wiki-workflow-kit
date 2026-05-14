# Design

## Routing Boundary

The user operation model should be command-selection guidance, not a new
autonomous runtime. Users may describe intent in natural language, and the agent
routes to the bounded command:

| User intent | Default route | Purpose |
| --- | --- | --- |
| New material or files | `wiki-inbox` | Intake pending files and suggest source / ops routing. |
| Find prior context | `wiki-query`, then `wiki-context` when needed | Retrieve bounded pages and reading order. |
| Ask whether wiki is healthy | `wiki-status` | Show inbox, OpenSpec, identity, relation, domain, and parse health. |
| Ask why a page or object is not connected | `wiki-graph` | Drill into node, object, layer, artifact, and relation structure. |
| Ask what is worth reading or safe to rely on | `wiki-scorecard` | Show preferred, cautious, and blocked objects with proof boundaries. |
| Ask how to fix a wiki/runtime issue | `wiki-apply` | Produce a repair plan and route implementation to OpenSpec when needed. |
| Ask to change rules, scripts, skills, AGENTS, or runtime behavior | OpenSpec | Propose and implement behavior changes with evaluation evidence. |

This table belongs in command documentation and repo guidance. It must not
duplicate the full taxonomy vocabulary.

## Status Surface

`wiki-status` remains the first diagnostic command. It already reports wiki
counts, source records, inbox state, OpenSpec state, identity coverage, and
relation coverage.

This change adds two manifest sections and two Markdown sections:

- `domain_taxonomy_health`
- `graph_parse_health`

Domain taxonomy health is derived from
`wiki/config/frontmatter-taxonomy.yaml` through
`scripts/check_wiki_frontmatter.py`. Status should summarize drift counts and
show bounded sample entries. It must read the checker output and must not
duplicate allowed domain or `ops_area` vocabularies.

Graph parse health detects suspicious relation extraction. The first pass
reports pages where raw frontmatter contains supported relation field names but
the parsed metadata has no values for those fields. This exposes relation
parser failures before a user manually inspects graph JSON.

## Parser Boundary

The shared frontmatter parser should support the repository's normal simple YAML
frontmatter shapes:

- scalar values
- inline lists
- list blocks indented either at column zero or under the field key

This parser is still a bounded frontmatter helper. It is not a full YAML
semantic layer for arbitrary markdown content.

## Graph Boundary

Raw graph extraction continues to include:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

Readable graph summaries should collapse spec details in representative pages by
default so a user sees the object and wiki evidence first. Spec nodes remain in
node counts, source layers, artifact types, and formalization proof.

## Repair Planning Boundary

`wiki-apply` is a bridge from diagnostics to action. It can summarize repair
routes, including:

- `page-frontmatter-fix`
- `taxonomy-config-fix`
- `runtime-parser-fix`
- `readable-graph-fix`

It must not silently edit runtime files. Runtime, rule, skill, AGENTS, or script
changes continue to require OpenSpec.

## Verification

Verification should include focused unit tests plus live command checks:

- parser handles indented YAML relation lists
- status manifest includes taxonomy and graph parse health
- status Markdown renders those sections
- graph summary collapses spec representative pages while retaining spec counts
- command docs include routing and repair boundaries
- live `build_wiki_status.py`, `extract_wiki_graph.py`, and graph summary
  commands run
