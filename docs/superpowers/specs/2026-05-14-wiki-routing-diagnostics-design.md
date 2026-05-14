# Wiki Routing And Diagnostics Design

Date: 2026-05-14
Status: design-approved-for-review
Repository: report-wiki-portfolio

## Problem

The wiki has enough runtime commands to inspect its state, but the user-facing
operation model is unclear. Users still have to remember whether to use
`wiki-status`, `wiki-graph`, `wiki-scorecard`, `wiki-query`, or `wiki-apply`.
That makes the system feel fragmented even when each command has a reasonable
local boundary.

Two concrete failures exposed the gap:

- Domain taxonomy is configured in `wiki/config/frontmatter-taxonomy.yaml`, but
  `wiki-status` does not surface taxonomy drift as part of the normal health
  view.
- `wiki/ops/agents-governance-drift-retro.md` has explicit `derived_from` and
  `related_objects` frontmatter, but the graph parser currently reads those
  relation fields as empty when the YAML list is indented. The graph therefore
  shows a weak or isolated object even though the page contains relation data.

The issue is not that the wiki lacks commands. The issue is that routing,
health, graph diagnostics, taxonomy diagnostics, and repair planning are not a
single usable loop.

## Goals

- Make AI routing the default so users do not need to memorize wiki commands.
- Make `wiki-status` the default health entry point.
- Include domain taxonomy health in the status surface using the existing
  taxonomy config as the only vocabulary authority.
- Include graph parse health in the status surface so relation extraction
  failures are visible before users manually inspect graph JSON.
- Keep `wiki-graph` as a structural drilldown tool, not a general health
  dashboard or repair command.
- Keep `wiki-scorecard` focused on usability and caution signals.
- Use `wiki-apply` for repair plans only; runtime, rule, skill, or script
  changes still require OpenSpec.

## Non-Goals

- Do not create a broad `wiki-doctor` command in the first pass.
- Do not automatically batch-migrate legacy wiki pages.
- Do not infer business domains from prose.
- Do not include OpenSpec change specs in domain taxonomy checks.
- Do not remove `openspec/specs` from raw graph extraction.
- Do not turn scorecard output into hidden semantic ranking or retrieval proof.
- Do not let `wiki-apply` edit runtime files directly.

## User Operation Model

Users should be able to describe intent in natural language. The agent should
route the request before asking the user to name a command.

| User intent | Default route | Purpose |
| --- | --- | --- |
| New material or files | `wiki-inbox` | Intake pending files and suggest source / ops routing. |
| Find prior context | `wiki-query`, then `wiki-context` when needed | Retrieve bounded pages and reading order. |
| Ask whether wiki is healthy | `wiki-status` | Show inbox, OpenSpec, identity, relation, domain, and parse health. |
| Ask why a page or object is not connected | `wiki-graph` | Drill into node, object, layer, artifact, and relation structure. |
| Ask what is worth reading or safe to rely on | `wiki-scorecard` | Show preferred, cautious, and blocked objects with proof boundaries. |
| Ask how to fix a wiki/runtime issue | `wiki-apply` | Produce a repair plan and route implementation to OpenSpec when needed. |
| Ask to change rules, scripts, skills, AGENTS, or runtime behavior | OpenSpec | Propose and implement behavior changes with evaluation evidence. |

This routing table belongs in repo guidance or command documentation. It should
not duplicate the full taxonomy vocabulary.

## Status Surface

`wiki-status` should remain the first diagnostic command. It already reports
wiki counts, source records, inbox state, OpenSpec state, identity coverage, and
relation coverage. It should add two sections.

### Domain Taxonomy Health

This section is derived from `wiki/config/frontmatter-taxonomy.yaml` and
`scripts/check_wiki_frontmatter.py`. The status output should summarize counts
and unresolved items for:

- `forbidden_domain`
- `unknown_domain`
- `unclassified_without_flag`
- `missing_ops_area_on_ops_page`
- `producer_hardcoded_forbidden_domain`
- `possible_unregistered_producer`

Example unresolved item:

```text
wiki/ops/agents-governance-drift-retro.md
type: domain_taxonomy_drift
problem: forbidden_domain personal-ops
repair_route: page-frontmatter-fix
```

The status command should not duplicate known domains or allowed `ops_area`
values. It should read the checker report.

### Graph Parse Health

This section detects suspicious relation extraction. The first pass should catch
pages where raw frontmatter contains relation field names but parsed metadata
has empty relation values.

Example unresolved item:

```text
wiki/ops/agents-governance-drift-retro.md
type: graph_parse_health
problem: raw related_objects or derived_from exists, parsed relation is empty
repair_route: runtime-parser-fix
```

The intended root repair is to make the shared frontmatter parser handle normal
YAML list indentation. The status surface should expose the issue before that
repair is made so users can see why relation coverage is low.

## Graph Drilldown

`wiki-graph` should keep extracting the raw machine graph from covered layers:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

Raw graph extraction should continue to include `openspec/specs` because specs
prove formalization depth and connect methods, ADRs, and runtime behavior.

Readable graph summaries should not flood the user with spec nodes by default.
They should group by `canonical_object` and collapse spec details:

```text
agents-governance-drift
  wiki/ops: retro, distill, explore, playbook
  wiki/adr: 2 derived decisions
  specs: 0
  relation_count: 6
```

When spec details matter, such as archive review or formalization proof, the
agent can expand them.

## Scorecard Role

`wiki-scorecard` should remain a usability and caution layer. It should consume
graph and relation analysis but should not repair graph or taxonomy issues.

When graph parse health or taxonomy health is degraded, scorecard summaries
should explain that caution reason rather than pretending the low score reflects
weak underlying knowledge.

## Repair Planning

`wiki-apply` should become the bridge from diagnostics to action. It should
produce repair plans with explicit route types:

| Repair route | Example | Execution boundary |
| --- | --- | --- |
| `page-frontmatter-fix` | Replace `domain: personal-ops` with `domain: none` and valid `ops_area` for pure governance pages. | Can be implemented only when page scope is explicit. |
| `taxonomy-config-fix` | Add a stable new business domain to `wiki/config/frontmatter-taxonomy.yaml`. | Requires OpenSpec because it changes repo taxonomy behavior. |
| `runtime-parser-fix` | Replace the custom frontmatter parser with YAML parsing that supports indented lists. | Requires OpenSpec because it changes runtime extraction behavior. |
| `readable-graph-fix` | Collapse `artifact_type: spec` in default readable graph summaries. | Requires OpenSpec because it changes command output behavior. |

`wiki-apply` should not silently edit scripts, skills, AGENTS, or runtime
behavior. It should state the recommended OpenSpec change when implementation is
needed.

## Domain Boundary

Domain remains configuration-driven:

```text
wiki/config/frontmatter-taxonomy.yaml
```

The durable model is:

- `domain` means real business or topic domain.
- `ops_area` means operations or governance workflow.
- `layer` means wiki placement.

Examples:

```yaml
layer: ops
domain: none
ops_area: agent-governance
```

```yaml
layer: ops
domain: unclassified
classification_needed: true
ops_area: source-intake
```

`personal-ops` remains forbidden. Unknown values remain warnings unless the
taxonomy config changes their severity.

## Implementation Boundary

This design does not itself change runtime behavior. The next implementation
work should be an OpenSpec change because it affects wiki command behavior,
runtime parsing, and status output.

Suggested OpenSpec change id:

```text
improve-wiki-routing-diagnostics
```

The implementation should include tests for:

- AI routing documentation includes status, graph, scorecard, apply, and
  OpenSpec boundaries.
- `wiki-status` includes taxonomy drift counts from the existing checker.
- `wiki-status` includes graph parse health for indented YAML relation lists.
- `wiki-graph` still includes raw `openspec/specs` nodes.
- readable graph summary collapses spec nodes by default.
- `wiki-apply` emits repair plans without directly editing runtime files.

## Success Criteria

- A user can ask "wiki 现在健康吗" and receive one status summary that includes
  inbox, OpenSpec, identity, relation, domain, and parse health.
- A page like `wiki/ops/agents-governance-drift-retro.md` is no longer silently
  treated as relation-free when raw relation fields are present.
- Domain drift is visible in normal status output rather than requiring a
  separate taxonomy checker run.
- Users do not need to remember which wiki command to run for common tasks.
- Runtime changes remain governed by OpenSpec instead of being hidden inside a
  diagnostic command.
