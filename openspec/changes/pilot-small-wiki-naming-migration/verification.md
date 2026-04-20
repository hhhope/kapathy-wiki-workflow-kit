# Verification: Pilot Small Wiki Naming Migration

## Pilot Family

- canonical object: `conversation-handoff`
- migrated pages:
  - `wiki/ops/conversation-handoff-mode.md`
  - `wiki/ops/sample-handoff-topic.md`
- updated local navigation:
  - `wiki/ops/index.md`

## Applied Migration

- aligned page titles to:
  - `conversation-handoff / method`
  - `conversation-handoff / sample`
- added required identity fields:
  - `canonical_object`
  - `artifact_type`
- added minimal typed relation fields:
  - `formalizes` on the method page
  - `derived_from` and `validates` on the sample page

## Boundary Decision

This pilot intentionally did **not** rename file paths.

Reason:

- the page-title and frontmatter migration already proves the model on legacy pages
- renaming file paths in the first pilot would force unrelated archive-history link churn
- the pilot goal is migration evidence, not broad repository cleanup

## Local Navigation Check

- `wiki/ops/index.md` now points to the migrated pages using the new title core
- no old title strings remain in the pilot navigation surface

## Graph Extraction Check

Command run:

```bash
python3 scripts/extract_wiki_graph.py
```

Observed result:

- `wiki/ops/conversation-handoff-mode.md` appears as:
  - `canonical_object: conversation-handoff`
  - `artifact_type: method`
- `wiki/ops/sample-handoff-topic.md` appears as:
  - `canonical_object: conversation-handoff`
  - `artifact_type: sample`
- extracted typed edges from the migrated pages:
  - `formalizes -> conversation-handoff`
  - `derived_from -> chat://handoff-mode/sample-north-star`
  - `validates -> conversation-handoff`

Summary at verification time:

- `node_count: 18`
- `edge_count: 3`
- `warning_count: 56`

## OpenSpec Validation Check

Command run:

```bash
openspec validate pilot-small-wiki-naming-migration
```

Result:

- change is valid
- PostHog telemetry emitted network errors to `edge.openspec.dev`
- telemetry failure did not block validation
