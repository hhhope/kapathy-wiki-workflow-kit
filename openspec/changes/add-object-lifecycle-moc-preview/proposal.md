# Proposal: object lifecycle MOC preview

## Summary

Improve Obsidian MOC object previews so `object-*` pages show a readable
lifecycle progression instead of a flat page list.

## Problem

The current MOC dry-run can identify object pages, but each object MOC is a
flat list of pages. This makes high-volume domains such as `domain-wiki` noisy
and does not show how a topic progressed from source or learning material into
OpenSpec specs, ADRs, methods, and evidence.

Fields such as `ops_area` are useful process metadata, but they are not content
topics. Grouping by `learning-capture`, `workflow-trace`, or
`agent-governance` would turn actions into the navigation structure and would
not answer what the object is about.

## Scope

In scope:

- Add lifecycle sections to generated `object-*` MOC previews.
- Keep `domain-*` and `relation-*` MOCs unchanged in this first version.
- Keep the generator dry-run by default and preserve explicit `--apply`.
- Add tests for lifecycle grouping and existing dry-run/apply behavior.
- Record evaluation evidence for the preview change.

Out of scope:

- Applying generated `wiki/moc` files in this change.
- Changing wiki frontmatter taxonomy values.
- Reclassifying existing wiki pages.
- Making `ops_area` a primary MOC navigation dimension.
- Proving Obsidian UI graph layout quality.

## Success Criteria

- Object MOC previews group links into lifecycle sections such as learning,
  specification, decision, method, evidence, and other.
- Section grouping is derived from explicit graph node metadata and relation
  types already present in the graph output.
- The dry-run summary remains non-writing.
- Existing MOC apply behavior still preserves manual content outside generated
  blocks.
