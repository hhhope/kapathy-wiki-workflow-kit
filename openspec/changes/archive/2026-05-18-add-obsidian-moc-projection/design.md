# Design: Obsidian MOC projection

## Model

`frontmatter` remains the structure source of truth. MOC pages are generated
Markdown projection artifacts for Obsidian graph visibility.

Supported inputs:

- `domain`
- `canonical_object`
- `related_objects`
- `derived_from`
- `validates`
- `formalizes`
- other existing graph relation fields already extracted by
  `scripts/extract_wiki_graph.py`

Generated MOC paths:

```text
wiki/moc/domain-<domain>.md
wiki/moc/object-<canonical_object>.md
wiki/moc/relation-<relation_type>.md
```

Each generated file uses a bounded generated block:

```md
<!-- BEGIN GENERATED MOC: domain=wiki -->
...
<!-- END GENERATED MOC -->
```

The generator may create files or replace content inside the generated block.
It must not remove manual content outside the generated block.

## Runtime Boundaries

| Surface | Role | Boundary |
| --- | --- | --- |
| `wiki-react` | classify `obsidian_graph_projection` and route to graph/status/apply/generator | does not write files |
| eval | validate traces for projection routing boundaries | does not classify natural language or write files |
| graph summary | expose MOC candidates | does not write files |
| status | compare MOC candidates to current `wiki/moc` files | does not write files |
| apply preview | describe create/update/noop plan | does not write files |
| MOC generator | explicit write surface | writes only when invoked with `--apply` |

## Health

Status reports:

- missing MOC files
- stale generated blocks
- current MOC pages that are not in the candidate set
- generated block count and stale count

Broken wikilink checks are limited to generated links that point to known page
stems or MOC page stems. This is a structural check, not Obsidian runtime proof.

## Verification

Verification should include:

- unit tests for MOC candidate derivation and generated block idempotence
- graph summary includes MOC candidates
- status manifest and markdown include MOC health
- apply preview reports MOC create/update/noop plan without writing files
- generator dry-run does not write, `--apply` writes generated blocks
- decision trace eval rejects projection traces that try to write from
  status/graph/apply/react/eval
