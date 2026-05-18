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

## Batch 3 Evidence

Batch 3 target set:

- `wiki/adr/0021` through `wiki/adr/0030`

Before target counts:

- ADR 0021-0025: `before.entry_count: 4`
- ADR 0026: `before.entry_count: 6`
- ADR 0027: `before.entry_count: 4`
- ADR 0028-0029: `before.entry_count: 6`
- ADR 0030: `before.entry_count: 4`

Approved deterministic fields:

- ADR pages with existing partial frontmatter: add only `layer: adr` and
  `domain: none`, preserving existing `canonical_object`, `artifact_type`, and
  relation fields.
- ADR pages without frontmatter: add `layer: adr`, `domain: none`,
  `artifact_type: adr`, and `canonical_object` from filename stem after the ADR
  number prefix.

After target counts:

- every batch 3 page reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 5
```

Result:

- `passed`: false
- `blocking_count`: 752
- `summary.error`: 752
- top remaining ADR sample starts at `wiki/adr/0031`

Residual boundary:

- Batch 3 reduced blockers by 46.
- The whole-wiki frontmatter gate remains blocked.
- Medical recovery/archive is still not clean.

## Batch 4 Evidence

Batch 4 target set:

- `wiki/adr/0031-root-capability-extraction-boundary.md`
- `wiki/adr/index.md`

Before target counts:

- ADR 0031: `before.entry_count: 4`
- ADR index: `before.entry_count: 6`

Approved deterministic fields:

- ADR 0031: add only `layer: adr` and `domain: none`, preserving existing
  `canonical_object`, `artifact_type`, and relation fields.
- ADR index: add `layer: adr`, `domain: none`,
  `canonical_object: wiki-adr-index`, and `artifact_type: index`.

After target counts:

- both batch 4 pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 5
```

Result:

- `passed`: false
- `blocking_count`: 742
- `summary.error`: 742
- top remaining samples have moved out of numbered ADR pages into mixed wiki
  root, domain, example, and ops pages

Residual boundary:

- Batch 4 reduced blockers by 10.
- The remaining work is no longer a pure ADR-number batch and needs layer-by-
  layer review before broad apply.

## Batch 5 Evidence

Planner review:

- The next blocker set moved into mixed root, domains, examples, and ops pages.
- `wiki/domains/index.md` and `wiki/examples/index.md` need an explicit domain
  decision and were deferred.
- Batch 5 therefore includes only pages whose existing frontmatter already has
  a domain value and whose only target blocker is missing `layer`.

Batch 5 target set:

- `wiki/domains/account-clearing.md`
- `wiki/examples/explore-trace-example.md`
- `wiki/examples/github-analysis-example.md`
- `wiki/examples/learning-note-example.md`
- `wiki/examples/meeting-note-example.md`
- `wiki/examples/project-weekly-example.md`
- `wiki/examples/weixin-summary-example.md`

Before target counts:

- every batch 5 page reported `before.entry_count: 1`
- every batch 5 target entry was `missing_required_field: layer`

Approved deterministic fields:

- `wiki/domains/account-clearing.md`: add only `layer: domains`; keep existing
  `domain: account-clearing`.
- `wiki/examples/*.md`: add only `layer: examples`; keep existing
  `domain: workflow-example`.

After target counts:

- all 7 batch 5 pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 5
```

Result:

- `passed`: false
- `blocking_count`: 735
- `summary.error`: 735
- top remaining samples include mixed root pages, deferred index pages, and ops
  pages that still need `ops_area` / identity review

Residual boundary:

- Batch 5 reduced blockers by 7.
- `wiki/domains/index.md` and `wiki/examples/index.md` remain intentionally
  unresolved because they need a domain classification decision, not just a
  layer insertion.

## Batch 6 Evidence

Batch 6 target set:

- `wiki/reports/management-weekly-ops.md`
- `wiki/reports/nirvana-delivery-board.md`
- `wiki/reports/nirvana-feature-tech-alignment.md`
- `wiki/reports/nirvana-phase1-leadership-brief.md`
- `wiki/reports/nirvana-phase1-pm-review.md`
- `wiki/sources/feishu-weekly-sync-sample.md`
- `wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md`
- `wiki/sources/nirvana-weekly-2026-04-13.md`
- `wiki/sources/nirvana-weekly-view-2026-04-13.md`
- `wiki/sources/nirvana-优化后图示.md`
- `wiki/sources/nirvana-协议支付涅槃需求文档.md`
- `wiki/sources/nirvana-最终方案.md`
- `wiki/sources/nirvana-涅槃产品上架梳理.md`
- `wiki/sources/nirvana-清算的内容.md`
- `wiki/sources/nirvana-现状.md`
- `wiki/timeline/2026-q2.md`

Before target counts:

- every batch 6 page appeared in the layer-only target list.

Approved deterministic fields:

- `wiki/reports/*.md`: add only `layer: reports`; keep existing domain and
  legacy report metadata unchanged.
- `wiki/sources/*.md`: add only `layer: sources`; keep existing domain and
  `source_type` unchanged.
- `wiki/timeline/*.md`: add only `layer: timeline`; keep existing domain
  unchanged.

After target counts:

- all 16 batch 6 pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 5
```

Result:

- `passed`: false
- `blocking_count`: 709
- `summary.error`: 709
- top remaining samples are now mixed root/index pages and ops pages requiring
  explicit domain/ops identity classification

Residual boundary:

- Batch 6 reduced blockers by 26 because source pages had both whole-wiki
  `layer` requirements and source-page expected-layer checks.

## Post-Batch 6 Medical Status

Command:

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text '$report-wiki-portfolio:wiki-medical-agent'
```

Result:

- `intent`: `status`
- `state`: `blocked`
- `allowed_action`: `report_status`
- `next_action`: `blocked`
- `executable_count`: 10

Remaining blocker shape:

- `blocking_count`: 709
- there are no remaining `layer`-only blocker pages
- largest remaining groups require mixed classification:
  - 65 pages with `domain`, `layer`, and `ops_area`
  - 51 pages with `artifact_type`, `canonical_object`, `domain`, `layer`, and
    `ops_area`
  - 30 root/index-style pages with `domain` and `layer`

Residual boundary:

- More automatic layer-only repair would now be unsafe.
- Next work must split root/index pages, mirrored `wiki/mnt` paths, and ops
  pages into an approved classification plan before applying more fields.
