# Evaluation: repair legacy wiki frontmatter batches

## Batch 1 Baseline

Planner command:

```bash
python3 scripts/build_wiki_frontmatter_repair.py --limit 10
```

Result:

- `source_blocking_count`: 916
- `selected_count`: 10
- `review_needed_count`: 10
- selected paths: `wiki/adr/0001` through `wiki/adr/0010`
- required fields: `layer`, `domain`, `canonical_object`, `artifact_type`
- exact precheck hints: `layer: adr`, `domain: none`

Approved deterministic fields:

- `artifact_type: adr`
- `canonical_object`: filename stem after the ADR number prefix

## Batch 1 Apply

Apply command:

```bash
python3 scripts/build_wiki_frontmatter_repair.py --limit 10 --approved-frontmatter-json '<approved ADR 0001-0010 frontmatter>' --apply
```

Result:

- `applied_count`: 10
- `blocked_count`: 0
- `skipped_count`: 0
- changed files: `wiki/adr/0001` through `wiki/adr/0010`
- approved fields only: `artifact_type`, `canonical_object`, `domain`, `layer`
- relation fields: none
- page bodies: unchanged

Target evidence from the apply result:

- every batch 1 page had `before.entry_count: 6`
- every batch 1 page had `after.entry_count: 0`

Focused target prechecks after apply:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0001-repository-default-workflow-changes-require-openspec.md
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md
```

Result:

- both targets report `target.entry_count: 0`
- both commands exit nonzero only because the whole-wiki gate still has
  unrelated residual blockers

## Residual Whole-Wiki Gate

Command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 5
```

Result:

- `passed`: false
- `blocking_count`: 856
- `summary.error`: 856
- top remaining ADR samples start at `wiki/adr/0011`

Residual boundary:

- Batch 1 reduced blockers by 60.
- The whole-wiki frontmatter gate remains blocked.
- Medical recovery/archive is still not clean until later batches or a scoped
  follow-up resolves the remaining blockers.
