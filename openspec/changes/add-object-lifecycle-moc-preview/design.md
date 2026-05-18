# Design: object lifecycle MOC preview

## Architecture

Keep MOC candidate generation in `scripts/wiki_moc_projection.py`.

The first version changes only object candidate line rendering:

```text
object canonical_object
  -> grouped graph nodes for that object
  -> lifecycle sections
  -> generated object MOC block
```

Domain candidates remain domain page lists. Relation candidates remain relation
edge lists.

## Lifecycle Sections

Use explicit graph metadata rather than inferred prose:

| Section | Source signal |
| --- | --- |
| Sources / Learning | `artifact_type` such as `intake`, `reading-notes`, `learning-note`, `article-evidence-matrix` |
| Specification | `source_layer: openspec/specs` or `artifact_type: spec` |
| Decisions | `source_layer: wiki/adr` or `artifact_type: adr` |
| Methods / Runtime | `artifact_type` such as `method`, `product-contract`, `ops-overview`, `ops-model`, `playbook` |
| Evidence / Replay | `artifact_type` such as `review`, `review-decision`, `diagnosis`, `recovery`, `treatment`, `surgery-plan`, `replay-harness`, `replay-validation`, `skill_fix_evidence` |
| Other | Anything not covered above |

Within each section, keep deterministic sorting by path and artifact type.

## Boundaries

This change does not use `ops_area` as a top-level navigation dimension. It may
still show source layer and artifact type as page metadata.

This change does not write MOC pages unless the existing explicit `--apply`
flag is used. The default command remains preview-only.

## Verification

- Add RED tests for object lifecycle sections.
- Run `python3 -m unittest tests.test_wiki_moc_projection`.
- Run `python3 scripts/build_wiki_moc_projection.py` and inspect the preview.
- Run `python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10`.
- Run `openspec validate add-object-lifecycle-moc-preview --strict`.
