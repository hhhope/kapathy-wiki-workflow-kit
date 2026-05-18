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

## Batch 2 Baseline

Planner/apply command:

```bash
python3 scripts/build_wiki_frontmatter_repair.py --limit 10 --approved-frontmatter-json '<approved ADR 0011-0020 frontmatter>' --apply
```

Planner result:

- `source_blocking_count`: 856
- `selected_count`: 10
- `review_needed_count`: 10
- selected paths: `wiki/adr/0011` through `wiki/adr/0020`

Approved deterministic fields:

- ADR 0011-0019: `layer: adr`, `domain: none`, `artifact_type: adr`,
  `canonical_object` from filename stem after the ADR number prefix
- ADR 0020: `layer: adr`, `domain: none` only, preserving existing
  `canonical_object`, `artifact_type`, `formalizes`, and `derived_from`

Batch 2 apply result:

- `applied_count`: 10
- `blocked_count`: 0
- `skipped_count`: 0
- ADR 0011-0019 each had `before.entry_count: 6`
- ADR 0020 had `before.entry_count: 4`
- every batch 2 page had `after.entry_count: 0`

Focused target prechecks after apply:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0011-canonical-ai-chat-installer-source-with-platform-adapters.md
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md
```

Result:

- both targets report `target.entry_count: 0`
- both commands exit nonzero only because the whole-wiki gate still has
  unrelated residual blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 5
```

Result:

- `passed`: false
- `blocking_count`: 798
- `summary.error`: 798
- top remaining ADR samples start at `wiki/adr/0021`

Residual boundary:

- Batch 2 reduced blockers by 58.
- The whole-wiki frontmatter gate remains blocked.
- Medical recovery/archive is still not clean.

## Runtime Note

The repair script currently repeats whole-wiki frontmatter scans during target
evidence collection. Batch 1 and batch 2 completed, but each batch took several
minutes. A later optimization may cache the full report or add a faster
target-only path; this batch did not change checker or repair tooling.
