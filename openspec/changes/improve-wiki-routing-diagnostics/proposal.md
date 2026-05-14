# improve-wiki-routing-diagnostics

## Why

The wiki runtime has several inspection commands, but the recovery path is still
fragmented. A user has to remember whether to run status, graph, scorecard,
query, or apply before they can understand what is wrong.

Two concrete failures exposed the problem:

- Domain taxonomy drift is available through
  `scripts/check_wiki_frontmatter.py`, but it is not surfaced in the normal
  `wiki-status` health view.
- Frontmatter relation fields such as `derived_from` and `related_objects` can
  be present as ordinary indented YAML lists while the graph parser reads them
  as empty. The graph then silently under-reports relation coverage.

## What Changes

- Add wiki routing guidance that makes `wiki-status` the default health entry
  point and clarifies when to use graph, scorecard, query, apply, and OpenSpec.
- Extend `wiki-status` so the generated manifest and Markdown status include
  domain taxonomy health from the existing taxonomy checker.
- Extend `wiki-status` so the generated manifest and Markdown status include
  graph parse health for raw relation fields that parse as empty.
- Fix the shared frontmatter parser so normal indented YAML list frontmatter is
  parsed into relation values.
- Keep `wiki-graph` as a structural drilldown tool and keep raw
  `openspec/specs` graph nodes.
- Make readable graph summaries collapse spec-node details by default while
  retaining spec evidence in counts and artifact summaries.
- Make `wiki-apply` documentation describe repair-plan routes without directly
  editing runtime files.

## Out of Scope

- Creating a broad `wiki-doctor` command.
- Automatically migrating legacy wiki pages.
- Inferring business domains from prose.
- Adding OpenSpec specs to domain taxonomy checks.
- Removing `openspec/specs` from raw graph extraction.
- Turning scorecard output into hidden semantic ranking or retrieval proof.
- Letting `wiki-apply` edit scripts, skills, AGENTS, or runtime behavior.

## Source Design

- `docs/superpowers/specs/2026-05-14-wiki-routing-diagnostics-design.md`
