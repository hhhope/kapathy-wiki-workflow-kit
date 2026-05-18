---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: product-capability-and-graph-gap
artifact_type: explore-trace
related_objects:
- account-knowledge-base
- agent-readable-wiki
- obsidian-wiki-reference-gap-review
derived_from:
- PROJECT.md
- wiki/index.md
- wiki/ops/account-knowledge-base-workbench.md
- wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
---

# product-capability-and-graph-gap / explore-trace

## Trigger

User asked to reframe the product capabilities and product planning using ASCII
diagrams, and noted that the repository still lacks a meaningful graph because
process files are weakly connected.

## Explore Boundary

This is `$openspec-explore`: thinking and requirement shaping only.

No feature implementation, graph automation, or OpenSpec change has been started
in this trace.

## Current Read

The current product is best understood as a report-wiki operating system:

```text
Inputs
  -> durable wiki
  -> agent-readable governance/runtime context
  -> reviewable reports / Feishu-facing drafts / H5
```

The current gap is not "no graph file at all". The more precise gap is:

```text
covered governance graph exists in scripts/specs
but whole-wiki product graph is missing
and process files are not consistently connected as product objects
```

## Working Hypothesis

Product capability should be reframed around five user-visible surfaces:

```text
Capture -> Organize -> Reason -> Produce -> Operate
```

The graph roadmap should start with product-visible status and relation hygiene,
not with a large graph database or automatic semantic graph.

## Open Questions

- Should the first graph milestone cover only `wiki/ops`, or the whole wiki?
- Should process files be connected by explicit frontmatter relations, body links,
  or a generated manifest/status ledger first?
- Should the next scoped change start from `manifest/status` or from `link lint`?

## Non-Decisions

- No taxonomy migration.
- No Obsidian `[[wikilinks]]` default migration.
- No Feishu sync change.
- No implementation until a follow-up OpenSpec change is selected.
