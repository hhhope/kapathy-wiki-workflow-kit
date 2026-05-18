# Proposal: add Obsidian MOC projection

## Summary

Add a controlled projection layer that turns explicit wiki graph/frontmatter
structure into Obsidian-visible MOC pages without making status, graph, apply,
react, or eval mutate wiki pages implicitly.

## Motivation

Obsidian graph views only see links in Markdown content. The repository's
agent/runtime graph currently uses frontmatter fields such as `domain`,
`canonical_object`, `related_objects`, `derived_from`, `validates`, and
`formalizes`. That structure is useful to agents, but it is mostly invisible in
Obsidian unless projected into `[[wikilinks]]`.

The desired behavior is a governed projection:

```text
frontmatter / graph structure
  -> MOC candidates
  -> status health and apply preview
  -> explicit generator writes wiki/moc/*.md
```

## Scope

- Add MOC candidate derivation for domain, object, and relation groups.
- Surface MOC candidates in graph summary output.
- Surface MOC health in wiki status output.
- Add apply-preview output for MOC generation.
- Add an explicit MOC generator with dry-run default and `--apply` write mode.
- Add eval coverage for `obsidian_graph_projection` routing boundaries.

## Non-Goals

- Do not build a graph UI.
- Do not make `/wiki:status` write files.
- Do not make `/wiki:graph` write files.
- Do not make `/wiki:apply` execute writes.
- Do not make `wiki-react` or eval generate MOC pages.
- Do not add per-page relation blocks.
