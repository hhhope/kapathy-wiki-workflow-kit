# Evaluation: repair legacy wiki frontmatter batches

## Batch 14n Evidence

Approved batch:

- Batch 14n: clean ops method, learning, product contract, and explore pages
  using doctor candidate frontmatter only

Target set:

- `wiki/ops/example-driven-wiki-capture.md`
- `wiki/ops/feishu-image-client-freeze-explore-2026-05-09.md`
- `wiki/ops/karpathy-skills-learning-retro-2026-04-16.md`
- `wiki/ops/learning-source-routing-gap-explore-2026-05-09.md`
- `wiki/ops/llm-wiki-core-product-contract.md`
- `wiki/ops/main-thread.md`
- `wiki/ops/multi-system-branch-spec-explore-2026-05-12.md`

Applied fields:

- `layer: ops`
- `domain`: `wiki`, `public-report-output`, or
  `product-engineering-collaboration` from existing frontmatter or doctor
  candidate evidence
- `ops_area`: `learning-capture`, `report-quality`, `wiki-runtime`, or
  `workflow-trace`
- `canonical_object` and `artifact_type` where missing

After target counts:

- all 7 target pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 258
- `summary.error`: 258
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/nirvana-weekly-intake-2026-04-13.md`, and
  `wiki/ops/nirvana-weekly-reminder-2026-04-13.md`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Existing relation fields were preserved where already present.
- No page bodies, taxonomy config, checker logic, MOC pages, ADRs, skills, or
  OpenSpec lifecycle state were changed.

## Batch 14o Evidence

Approved batch:

- Batch 14o: clean nirvana project-management and reminder ops pages.

Target set:

- `wiki/ops/nirvana-preview-intake.md`
- `wiki/ops/nirvana-weekly-intake-2026-04-13.md`
- `wiki/ops/nirvana-weekly-reminder-2026-04-13.md`
- `wiki/ops/project-management-weekly-loop.md`
- `wiki/ops/reminders.md`

Applied fields:

- `layer: ops`
- `domain: nirvana` for the preview intake with existing domain evidence
- `domain: nirvana-project` for the project weekly intake and reminder
- `domain: wiki` for the generic project-management loop and reminder panel
- `ops_area`: `source-intake` or `workflow-trace`
- missing `canonical_object` and `artifact_type`

After target counts:

- all 5 target pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 234
- `summary.error`: 234
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/nirvana-涅槃产品上架梳理-intake.md`, and
  `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Page bodies were not changed.
- The `reminders.md` domain used existing `sample-reminder.md` frontmatter as
  the local precedent for a generic reminder panel.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

## Batch 14p Evidence

Approved batch:

- Batch 14p: clean nirvana intake and public report explore ops pages.

Target set:

- `wiki/ops/nirvana-协议支付涅槃需求文档-intake.md`
- `wiki/ops/nirvana-涅槃产品上架梳理-intake.md`
- `wiki/ops/public-report-skill-gate-wording-explore-2026-05-11.md`

Applied fields:

- `canonical_object` and `artifact_type` for the existing `nirvana` protocol
  payment intake.
- `layer: ops`, `ops_area: workflow-trace`, `canonical_object`, and
  `artifact_type` for the existing `nirvana` product-listing intake.
- `layer: ops`, `ops_area: workflow-trace`, `canonical_object`, and
  `artifact_type` for the existing `report-workflow` public-report explore
  trace.

After target counts:

- all 3 target pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 222
- `summary.error`: 222
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`, and
  `wiki/ops/product-alignment-drift-explore-2026-05-09.md`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Page bodies were not changed.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

## Batch 14q Evidence

Approved batch:

- Batch 14q: clean product/runtime drift, product plan, and scorecard
  calibration ops pages.

Target set:

- `wiki/ops/product-alignment-drift-explore-2026-05-09.md`
- `wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md`
- `wiki/ops/report-wiki-product-plan-2026-05-09.md`
- `wiki/ops/scope-drift-retro.md`
- `wiki/ops/scorecard-calibration-gap-explore-2026-05-09.md`

Applied fields:

- `layer: ops`
- `domain: wiki` for product alignment, product capability, product plan, and
  scope drift pages.
- `domain: agent-harness` for the scorecard calibration gap page from doctor
  candidate evidence.
- `ops_area`: `wiki-runtime` or `workflow-trace`
- missing identity fields on `scope-drift-retro.md`

After target counts:

- all 5 target pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 200
- `summary.error`: 200
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`,
  `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`,
  and `wiki/ops/wiki-doctor-runs/...`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Existing relation fields were preserved.
- Page bodies were not changed.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

## Batch 14r Evidence

Approved batch:

- Batch 14r: clean team overview, visual routing repair, and wiki command ops
  pages.

Target set:

- `wiki/ops/team-knowledge-base-overview-report-gate-review.md`
- `wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md`
- `wiki/ops/visual-output-routing-residual-fallback-repair-2026-05-11.md`
- `wiki/ops/visual-output-routing-skill-fix-evidence-2026-05-11.md`
- `wiki/ops/wiki-runtime-command-surface-explore-2026-05-09.md`
- `wiki/ops/wiki-status-slash-command-reanchor.md`

Applied fields:

- `layer: ops`
- `domain: agent-harness` for the team knowledge-base overview review
- `domain: wiki` for visual-output-routing and wiki command pages
- `ops_area`: `wiki-runtime` or `workflow-trace`
- missing identity fields for wiki command pages

After target counts:

- all 6 target pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 172
- `summary.error`: 172
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`,
  `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`,
  and `wiki/ops/wiki-doctor-runs/...`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Existing relation fields were preserved.
- Page bodies were not changed.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

## Batch 14s Evidence

Approved batch:

- Batch 14s: tracked wiki-doctor run record pages.

Target set:

- `wiki/ops/wiki-doctor-runs/2026-05-14-130526-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-14-131652-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-15-035845-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-15-041628-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-15-043329-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-15-064214-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-18-014824-review.md`
- `wiki/ops/wiki-doctor-runs/2026-05-18-015919-review.md`

Applied fields:

- `layer: ops`
- `domain: wiki`
- `ops_area: wiki-runtime`
- `canonical_object: wiki-doctor-review`
- `artifact_type: review` or `diagnosis` based on the record title

After target counts:

- sampled target prechecks for the first, one diagnosis, and last page reported
  `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 124
- `summary.error`: 124
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`,
  `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`,
  and `wiki/ops/wiki-recovery-runs/...`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Page bodies were not changed.
- The existing detailed doctor review page already had compliant frontmatter
  and was not changed.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

## Batch 14t Evidence

Approved batch:

- Batch 14t: tracked recovery, review-decision, treatment, and surgery run
  record pages.

Target set:

- `wiki/ops/wiki-recovery-runs/2026-05-18-014833-recovery.md`
- `wiki/ops/wiki-recovery-runs/2026-05-18-015928-recovery.md`
- `wiki/ops/wiki-review-decisions/2026-05-15-013923-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-15-040152-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-15-042538-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-15-043333-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-15-062939-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-15-064420-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-18-014829-review-decisions.md`
- `wiki/ops/wiki-review-decisions/2026-05-18-015923-review-decisions.md`
- `wiki/ops/wiki-surgery-runs/2026-05-18-023550-surgery.md`
- `wiki/ops/wiki-treatment-runs/2026-05-15-041020-treatment.md`
- `wiki/ops/wiki-treatment-runs/2026-05-15-065102-treatment.md`
- `wiki/ops/wiki-treatment-runs/2026-05-18-014811-treatment.md`
- `wiki/ops/wiki-treatment-runs/2026-05-18-015905-treatment.md`

Applied fields:

- `layer: ops`
- `domain: wiki`
- `ops_area: wiki-runtime`
- `canonical_object`: `wiki-recovery`, `wiki-review-decisions`,
  `wiki-surgery`, or `wiki-treatment`
- `artifact_type`: `recovery`, `review-decision`, `surgery-plan`, or
  `treatment`

After target counts:

- sampled target prechecks for recovery, review-decision, treatment, and
  surgery pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 34
- `summary.error`: 34
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`,
  `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`,
  and `wiki/ops/wiki-surgery-runs/2026-05-15-044434-surgery.md`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Page bodies were not changed.
- The untracked `wiki/ops/wiki-surgery-runs/2026-05-15-044434-surgery.md`
  was not changed or staged in this batch.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

## Batch 14u Evidence

Approved batch:

- Batch 14u: clean visual-output-routing drift and account-clearing
  scenario-matrix ops pages.

Target set:

- `wiki/ops/visual-output-routing-drift-explore-2026-05-11.md`
- `wiki/ops/宝财通分账开通迁移场景对照表-2026-04-16.md`

Applied fields:

- `layer: ops`
- `domain: wiki`, `ops_area: wiki-runtime` for the visual-output-routing
  drift explore page, matching the already accepted agent/workflow drift
  interpretation.
- `domain: account-clearing`, `ops_area: workflow-trace` for the 宝财通
  scenario matrix, because the page content is a business migration scenario
  trace for split-account opening.
- Existing `canonical_object`, `artifact_type`, and relation fields were
  preserved.

After target counts:

- both target pages reported `target.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 26
- `summary.error`: 26
- top remaining samples include `wiki/mnt/...`, `wiki/ops/index.md`,
  dirty `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`,
  dirty
  `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`,
  and untracked
  `wiki/ops/wiki-surgery-runs/2026-05-15-044434-surgery.md`

OpenSpec validation:

```bash
openspec validate repair-legacy-wiki-frontmatter-batches --strict
```

Result:

- `Change 'repair-legacy-wiki-frontmatter-batches' is valid`
- PostHog DNS flush failed after validation; this did not change the command's
  successful validation result.

Boundary:

- No relation fields were added.
- Page bodies were not changed.
- The dirty obsidian/team drift files, untracked surgery run, `wiki/mnt`
  mirror paths, `wiki/ops/index.md`, and wiki template were not changed in this
  batch.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, templates, or
  OpenSpec lifecycle state were changed.

## Batch 14v Evidence

Approved batch:

- Batch 14v: tracked ops index, tracked template, and dirty tracked pages using
  frontmatter-only staging for dirty files.

Target set:

- `wiki/ops/index.md`
- `wiki/templates/decision-checkpoint-template.md`
- `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`
- `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`

Applied fields:

- `wiki/ops/index.md`: `layer: ops`, `domain: none`,
  `ops_area: workflow-trace`, `canonical_object: wiki-ops-index`,
  `artifact_type: index`, following the structural index convention from
  batch 10.
- `wiki/templates/decision-checkpoint-template.md`: `layer: examples`,
  `domain: wiki`, describing the template file itself and not a generated
  target page.
- `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`: `layer: ops`,
  `domain: wiki`, `ops_area: learning-capture`.
- `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`:
  `layer: ops`, `domain: public-report-output`,
  `ops_area: report-quality`.

After target counts:

- all 4 target pages reported `target.entry_count: 0`

Whole-wiki residual:

- target precheck output after this batch reported `blocking_count: 10`
- remaining blocking paths are two untracked `wiki/mnt/...` mirror paths and
  the untracked
  `wiki/ops/wiki-surgery-runs/2026-05-15-044434-surgery.md`
- producer warnings remain non-blocking warnings

Boundary:

- No relation fields were added.
- Page bodies were not intentionally changed by this batch.
- The dirty obsidian/team drift pages had pre-existing table-formatting diffs;
  only the frontmatter hunks are task-related for this batch commit.
- No taxonomy config, checker logic, MOC pages, ADRs, skills, or OpenSpec
  lifecycle state were changed.

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

## Classification Plan Evidence

Added:

- `classification-plan.md`

Planner command:

```bash
python3 -c '<group remaining frontmatter errors by route group>'
```

Result:

- blocked page count: 165
- `SOURCE_DOMAIN_LAYER`: 5 pages
- `SOURCE_UNCLASSIFIED_FLAG`: 3 pages
- `REPORT_DOMAIN_LAYER`: 1 page
- `INDEX_PAGE_DECISION`: 7 pages
- `ROOT_PUBLIC_PAGE_DECISION`: 15 pages
- `TEMPLATE_DECISION`: 1 page
- `MNT_MIRROR_REVIEW`: 2 pages
- `OPS_AREA_DOMAIN_ONLY`: 44 pages
- `OPS_FORBIDDEN_DOMAIN_REMAP`: 37 pages
- `OPS_IDENTITY_REBUILD`: 50 pages

Boundary:

- No wiki page frontmatter was changed in this step.
- The next field-writing step requires approval for a named batch from
  `classification-plan.md`.

## Batch 7-9 Evidence

Approved batches:

- Batch 7: Sources With Existing Source Identity
- Batch 8: Unclassified Meeting Sources
- Batch 9: Single Product Report

Applied fields:

- Batch 7 source pages: `layer: sources` and
  `domain: product-engineering-collaboration`.
- Batch 8 meeting-source pages: `layer: sources`, keep
  `domain: unclassified`, and add `classification_needed: true`.
- Batch 9 report page: `layer: reports` and
  `domain: product-engineering-collaboration`.

Target after counts:

- all 9 target pages reported `after.entry_count: 0`.

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 683
- `summary.error`: 683

Boundary:

- `wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md`
  had pre-existing non-frontmatter table formatting changes. Only this
  batch's frontmatter hunk is task-related for the commit.

## Batch 10 Evidence

Approved batch:

- Batch 10: Index Pages

Applied convention:

- Structural index pages use `domain: none`.
- Index page `layer` follows the directory it indexes.
- Root `wiki/index.md` uses `layer: status` as the wiki overview/status entry.
- `wiki/sources/index.md` uses `source_type: index` to satisfy the source-page
  strict gate without pretending to be upstream evidence.

Target set:

- `wiki/domains/index.md`
- `wiki/examples/index.md`
- `wiki/index.md`
- `wiki/reports/index.md`
- `wiki/sources/index.md`
- `wiki/status/index.md`
- `wiki/timeline/index.md`

Before target counts:

- six index pages had 2 errors: `domain` and `layer`
- `wiki/sources/index.md` had 4 errors: `domain`, `layer`, and `source_type`
  including the source-page expected-layer check

After target counts:

- all 7 target pages reported `after.entry_count: 0`
- all 7 target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 667
- `summary.error`: 667

Boundary:

- No taxonomy config or checker logic was changed.
- The `domain: none` convention was applied only to structural index pages.

## Batch 11 Evidence

Approved batch:

- Batch 11: Root And Public Pages

Applied fields:

- Root workflow/guidance pages:
  - `layer: ops`
  - domain by content: `ai-workflow`, `report-workflow`, or `wiki`
- Public/report pages:
  - `layer: reports`
  - domain by report subject: `product-engineering-collaboration`,
    `ai-workflow`, `nirvana-project`, or `wiki`
- Timeline page:
  - `layer: timeline`
  - `domain: wiki`

Target set:

- `wiki/ai-chat-workflow-installer.md`
- `wiki/ai-workflow.md`
- `wiki/inbox-intake.md`
- `wiki/language-policy.md`
- `wiki/role-boundaries.md`
- `wiki/team-lore-candidates.md`
- `wiki/reports/agentic-visual-assets-image-model/README.md`
- `wiki/reports/ai-chat-workflow-installer-feishu-share.md`
- `wiki/reports/nirvana-handover-account-owner.md`
- `wiki/reports/team-knowledge-base-migration.md`
- `wiki/reports/team-knowledge-base-overview.md`
- `wiki/reports/team-knowledge-base-roadmap.md`
- `wiki/reports/team-knowledge-base-runtime.md`
- `wiki/reports/team-knowledge-base-validation-cases.md`
- `wiki/timeline/2026-04-20-agent-readable-wiki-evolution.md`

Before target counts:

- all 15 pages had 2 errors: `domain` and `layer`

After target counts:

- all 15 target pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 637
- `summary.error`: 637

Boundary:

- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 13a Evidence

Approved batch:

- Batch 13a: wiki-runtime ops pages with existing identity

Applied fields:

- `layer: ops`
- `domain: wiki`
- `ops_area: wiki-runtime`

Target set:

- `wiki/ops/account-knowledge-base-workbench.md`
- `wiki/ops/agent-readable-wiki-artifact-grouping.md`
- `wiki/ops/agent-readable-wiki-context-injection.md`
- `wiki/ops/agent-readable-wiki-graph-extraction.md`
- `wiki/ops/agent-readable-wiki-relation-analysis.md`
- `wiki/ops/agent-readable-wiki-relation-reading-view.md`
- `wiki/ops/agent-readable-wiki-runtime-auto-routing.md`
- `wiki/ops/agent-readable-wiki-runtime-context-source-integration.md`
- `wiki/ops/agent-readable-wiki-runtime-context.md`
- `wiki/ops/agent-readable-wiki-self-directed-execution.md`
- `wiki/ops/agent-readable-wiki-utilization-layer.md`
- `wiki/ops/wiki-readable-views-validation-harness.md`

Before target counts:

- all 12 pages had 4 errors covering `layer`, `domain`, and `ops_area`
- 3 pages also had forbidden `domain: personal-ops`

After target counts:

- all 12 target pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 589
- `summary.error`: 589

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 14m Evidence

Approved batch:

- Batch 14m: clean governance replay/method ops pages with missing
  frontmatter and doctor-run candidate frontmatter

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area` from the prior doctor-run candidate frontmatter
- `canonical_object` and `artifact_type` from existing frontmatter where
  present, otherwise from the prior doctor-run candidate frontmatter

Target set:

- `wiki/ops/agents-governance-drift-distill-replay-validation-2026-04-21.md`
- `wiki/ops/conversation-handoff-mode.md`
- `wiki/ops/disagreement-management-method.md`
- `wiki/ops/disagreement-management-replay-harness.md`
- `wiki/ops/disagreement-management-replay-validation-2026-04-20.md`
- `wiki/ops/distill-calibration-replay-harness.md`

Before target counts:

- pages with existing identity had 4 errors for missing `layer`, `domain`,
  `ops_area`, and unexpected `layer`
- pages without frontmatter identity had 6 errors covering missing `layer`,
  missing `domain`, missing `ops_area`, missing `canonical_object`, missing
  `artifact_type`, and unexpected `layer`

After target counts:

- all 6 target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 294
- `summary.error`: 294

Boundary:

- Relation candidates from the doctor run were not applied.
- Existing body text, taxonomy config, checker logic, MOC, ADR, and OpenSpec
  lifecycle state were not changed.

## Batch 14l Evidence

Approved batch:

- Batch 14l: clean wiki method ops pages with missing frontmatter and
  doctor-run candidate frontmatter

Applied fields:

- `wiki/ops/agent-readable-wiki-frontmatter.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: wiki-runtime`
  - `canonical_object: agent-readable-wiki-frontmatter`
  - `artifact_type: method`
- `wiki/ops/agent-readable-wiki-naming-model.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: wiki-runtime`
  - `canonical_object: agent-readable-wiki-naming-model`
  - `artifact_type: method`
- `wiki/ops/codex-handoff-rules.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: workflow-trace`
  - `canonical_object: codex-handoff-rules`
  - `artifact_type: method`

Before target counts:

- all 3 pages had 6 errors covering missing `layer`, missing `domain`, missing
  `ops_area`, missing `canonical_object`, missing `artifact_type`, and
  unexpected `layer`

After target counts:

- all 3 target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed`: false
- `blocking_count`: 324
- `summary.error`: 324

Boundary:

- Relation candidates from the doctor run were not applied.
- Existing body text, taxonomy config, checker logic, MOC, ADR, and OpenSpec
  lifecycle state were not changed.

## Batch 14k Evidence

Approved batch:

- Batch 14k: remaining forbidden-domain ops pages that already had unrelated
  working-tree edits

Applied fields:

- `wiki/ops/account-knowledge-base-structure-explore.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: learning-capture`
  - `canonical_object: account-knowledge-base-structure`
  - `artifact_type: explore`
- `wiki/ops/agent-harness-article-learning.md`
  - `domain: agent-harness`
  - `layer: ops`
  - `ops_area: learning-capture`
  - existing `canonical_object` and `artifact_type` values were preserved

Before target counts:

- `account-knowledge-base-structure-explore.md` had 6 errors covering forbidden
  `domain: personal-ops`, missing `layer`, missing `ops_area`, missing
  `canonical_object`, and missing `artifact_type`
- `agent-harness-article-learning.md` had 4 errors covering forbidden
  `domain: personal-ops`, missing `layer`, and missing `ops_area`

After target counts:

- both target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 342
- `summary.error`: 342

Boundary:

- These files had unrelated pre-existing working-tree edits; only the
  frontmatter hunks listed above were staged for commit.
- Relation candidates from the doctor run were not applied.
- Existing body text, taxonomy config, checker logic, MOC, ADR, and OpenSpec
  lifecycle state were not changed.

## Batch 14j Evidence

Approved batch:

- Batch 14j: clean unclassified meeting/intake ops pages requiring explicit
  `classification_needed: true`

Applied fields:

- `domain: unclassified` was preserved on all target pages.
- `classification_needed: true`
- `layer: ops`
- `ops_area: workflow-trace`
- Missing `canonical_object` and `artifact_type` values were filled from
  existing title/source path and prior doctor-run candidate frontmatter.

Target set:

- `wiki/ops/20260415100517-转写-yan的快速会议-纪要文本-1-intake.md`
- `wiki/ops/20260415100517-转写-yan的快速会议-逐字稿文本-1-intake.md`
- `wiki/ops/宝财通分账开通与迁移边界提醒-2026-04-16.md`
- `wiki/ops/文字转写-呼呼的快速会议-276823523-intake.md`

Before target counts:

- 2 pages had 6 errors covering missing `layer`, missing `ops_area`, missing
  `canonical_object`, missing `artifact_type`, unexpected `layer`, and
  `unclassified_without_flag`
- 1 intake page had the same 6-error shape
- 1 reminder page had 4 errors because it already had `canonical_object` and
  `artifact_type`

After target counts:

- all 4 target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 352
- `summary.error`: 352

Boundary:

- The pages remained explicitly unclassified; no business domain was invented.
- Relation candidates from the doctor run were not applied.
- Existing body text, taxonomy config, checker logic, MOC, ADR, and OpenSpec
  lifecycle state were not changed.

## Batch 14i Evidence

Approved batch:

- Batch 14i: clean learning/runtime trace ops pages with doctor-run candidate
  frontmatter and forbidden `domain: personal-ops`

Applied fields:

- `wiki/ops/example-driven-capture-runtime-validation-2026-04-18.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: learning-capture`
  - `canonical_object: example-driven-capture-runtime-validation`
  - `artifact_type: method`
- `wiki/ops/gstack-lark-learning-retro-2026-04-18.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: learning-capture`
  - `canonical_object: gstack-lark-learning`
  - `artifact_type: retro`
- `wiki/ops/hermes-self-evolution-gap-explore-2026-04-16.md`
  - `domain: wiki`
  - `layer: ops`
  - `ops_area: workflow-trace`
  - `canonical_object: hermes-self-evolution-gap`
  - `artifact_type: explore`

Before target counts:

- all 3 pages had 6 errors covering forbidden `domain: personal-ops`, missing
  `layer`, missing `ops_area`, missing `canonical_object`, and missing
  `artifact_type`

After target counts:

- all 3 target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 374
- `summary.error`: 374

Boundary:

- Relation candidates from the doctor run were not applied.
- Existing body text, taxonomy config, checker logic, MOC, ADR, and OpenSpec
  lifecycle state were not changed.
- Dirty pages with unrelated user changes were skipped.

## Batch 14h Evidence

Approved batch:

- Batch 14h: clean sample ops pages with doctor-run candidate frontmatter and
  forbidden `domain: personal-ops`

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area: workflow-trace`
- `canonical_object` and `artifact_type` from the stable sample filename/title
  and prior doctor-run candidate frontmatter

Target set:

- `wiki/ops/sample-codex-handoff.md`
- `wiki/ops/sample-disagreement-retro.md`
- `wiki/ops/sample-explore-trace.md`
- `wiki/ops/sample-focus-thread.md`
- `wiki/ops/sample-intake.md`
- `wiki/ops/sample-reminder.md`

Before target counts:

- all 6 pages had 6 errors covering forbidden `domain: personal-ops`, missing
  `layer`, missing `ops_area`, missing `canonical_object`, and missing
  `artifact_type`

After target counts:

- all 6 target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 392
- `summary.error`: 392

Boundary:

- Relation candidates from the doctor run were not applied.
- The pages stayed in `wiki/ops`; no sample migration, page body edit,
  taxonomy config edit, checker logic edit, MOC edit, ADR edit, or OpenSpec
  lifecycle state change was attempted.

## Batch 14g Evidence

Approved batch:

- Batch 14g: clean agent-governance gate-gap ops pages with filename/title
  identity and forbidden `domain: personal-ops`

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area: agent-governance`
- `canonical_object: agent-governance-gate-gap`
- `artifact_type: explore` for the explore trace page
- `artifact_type: retro` for the retro page

Target set:

- `wiki/ops/agent-governance-gate-gap-explore-2026-04-18.md`
- `wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md`

Before target counts:

- both pages had 6 errors covering forbidden `domain: personal-ops`, missing
  `layer`, missing `ops_area`, missing `canonical_object`, and missing
  `artifact_type`

After target counts:

- both target precheck runs reported `target.entry_count: 0`; the precheck
  commands still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 428
- `summary.error`: 428

Boundary:

- Identity values came from the stable filename/title object and artifact
  suffixes, with matching prior doctor-run evidence.
- No relation fields, body text, taxonomy config, checker logic, MOC, ADR, or
  OpenSpec lifecycle state was changed.

## Batch 14f Evidence

Approved batch:

- Batch 14f: clean conversation handoff sample with existing identity and
  forbidden `domain: personal-ops`

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area: agent-governance`

Target set:

- `wiki/ops/sample-handoff-topic.md`

Before target counts:

- the page had 4 errors covering forbidden `domain: personal-ops`,
  missing `layer`, and missing `ops_area`

After target counts:

- the target precheck run reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 440
- `summary.error`: 440

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- The page stayed in `wiki/ops`; no sample migration or relation edits were
  attempted.
- No body text, taxonomy config, checker logic, MOC, ADR, or OpenSpec lifecycle
  state was changed.

## Batch 14e Evidence

Approved batch:

- Batch 14e: unresolved intelligence-native organization intake with existing
  identity and forbidden `domain: personal-ops`

Applied fields:

- `domain: unclassified`
- `classification_needed: true`
- `layer: ops`
- `ops_area: learning-capture`

Target set:

- `wiki/ops/intelligence-native-organization-intake.md`

Before target counts:

- the page had 4 errors covering forbidden `domain: personal-ops`,
  missing `layer`, and missing `ops_area`

After target counts:

- the target page reported `after.entry_count: 0`
- the target precheck run reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 444
- `summary.error`: 444

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- A real taxonomy domain was not invented; `classification_needed: true`
  keeps this as explicit unresolved classification.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 14d Evidence

Approved batch:

- Batch 14d: clean non-governance ops pages with existing identity and
  forbidden `domain: personal-ops`

Applied fields:

- `wiki/ops/agent-harness-article-learning-intake.md`
  - `domain: agent-harness`
  - `layer: ops`
  - `ops_area: learning-capture`
- `wiki/ops/reference-driven-output-calibration-retro.md`
  - `domain: public-report-output`
  - `layer: ops`
  - `ops_area: report-quality`

Before target counts:

- both pages had 4 errors covering forbidden `domain: personal-ops`, missing
  `layer`, and missing `ops_area`

After target counts:

- both target pages reported `after.entry_count: 0`
- both target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 448
- `summary.error`: 448

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- `wiki/ops/intelligence-native-organization-intake.md` was left untouched
  because its taxonomy domain needs a separate decision.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 14c Evidence

Approved batch:

- Batch 14c: clean completion/reanchor/root governance ops pages with existing
  identity and forbidden `domain: personal-ops`

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area: agent-governance`

Target set:

- `wiki/ops/completion-bridge-drift-explore-2026-05-12.md`
- `wiki/ops/live-conversation-reanchor-gate-replay-harness.md`
- `wiki/ops/live-conversation-reanchor-gate-retro.md`
- `wiki/ops/root-capability-extraction-retro.md`

Before target counts:

- all 4 pages had 4 errors covering forbidden `domain: personal-ops`,
  missing `layer`, and missing `ops_area`

After target counts:

- all 4 target pages reported `after.entry_count: 0`
- all 4 target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 456
- `summary.error`: 456

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 14b Evidence

Approved batch:

- Batch 14b: clean behavior/Codex/OpenSpec governance ops pages with existing
  identity and forbidden `domain: personal-ops`

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area: agent-governance`

Target set:

- `wiki/ops/behavior-asset-governance-design-trace.md`
- `wiki/ops/behavior-asset-governance-zh.md`
- `wiki/ops/check-to-wiki-routing-explore.md`
- `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md`
- `wiki/ops/openspec-explore-trigger-drift-retro.md`
- `wiki/ops/superpowers-brainstorming-skill-visibility-explore-2026-05-14.md`

Before target counts:

- all 6 pages had 4 errors covering forbidden `domain: personal-ops`,
  missing `layer`, and missing `ops_area`

After target counts:

- all 6 target pages reported `after.entry_count: 0`
- all 6 target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 472
- `summary.error`: 472

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 13e Evidence

Approved batch:

- Batch 13e: agent-harness learning-capture ops pages with existing identity

Applied fields:

- `layer: ops`
- `ops_area: learning-capture`

Target set:

- `wiki/ops/evolver-self-evolving-harness-reading-notes.md`
- `wiki/ops/harness-engineering-overview-reading-notes.md`

Before target counts:

- both pages had 3 errors covering `layer` and `ops_area`

After target counts:

- both target pages reported `after.entry_count: 0`
- both target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 527
- `summary.error`: 527

Boundary:

- Existing `domain`, `canonical_object`, and `artifact_type` values were
  preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 14a Evidence

Approved batch:

- Batch 14a: clean `agents-governance-*` ops pages with existing identity and
  forbidden `domain: personal-ops`

Applied fields:

- `domain: wiki`
- `layer: ops`
- `ops_area: agent-governance`

Target set:

- `wiki/ops/agents-governance-281-compression-retro-2026-05-06.md`
- `wiki/ops/agents-governance-drift-distill-2026-04-21.md`
- `wiki/ops/agents-governance-drift-distill-calibration-retro.md`
- `wiki/ops/agents-governance-drift-explore.md`
- `wiki/ops/agents-governance-drift-playbook-2026-04-21.md`
- `wiki/ops/agents-governance-drift-retro.md`
- `wiki/ops/agents-governance-remediation-explore-2026-04-21.md`

Before target counts:

- all 7 pages had 4 errors covering forbidden `domain: personal-ops`,
  missing `layer`, and missing `ops_area`

After target counts:

- all 7 target pages reported `after.entry_count: 0`
- all 7 target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 496
- `summary.error`: 496

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 13f Evidence

Approved batch:

- Batch 13f: ai-workflow trace ops page with existing identity

Applied fields:

- `layer: ops`
- `ops_area: workflow-trace`

Target set:

- `wiki/ops/ai-chat-一键安装-skill-探索-2026-04-17.md`

Before target counts:

- the page had 3 errors covering `layer` and `ops_area`

After target counts:

- the target page reported `after.entry_count: 0`
- the target precheck run reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 524
- `summary.error`: 524

Boundary:

- Existing `domain`, `canonical_object`, and `artifact_type` values were
  preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 13d Evidence

Approved batch:

- Batch 13d: product-engineering source-intake ops pages with existing identity

Applied fields:

- `layer: ops`
- `domain: product-engineering-collaboration`
- `ops_area: source-intake`

Target set:

- `wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md`
- `wiki/ops/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md`

Before target counts:

- both pages had 4 errors covering `layer`, `domain`, and `ops_area`

After target counts:

- both target pages reported `after.entry_count: 0`
- both target precheck runs reported `target.entry_count: 0`; the precheck
  command still exited non-zero because the whole-wiki gate retained unrelated
  blockers

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 533
- `summary.error`: 533

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 13c Evidence

Approved batch:

- Batch 13c: product-engineering workflow-trace ops pages with existing
  identity

Applied fields:

- `layer: ops`
- `domain: product-engineering-collaboration`
- `ops_area: workflow-trace`

Target set:

- `wiki/ops/agentic-collaboration-company-playbook-page-explore-2026-05-11.md`
- `wiki/ops/agentic-company-playbook-quality-failure-root-cause-explore-2026-05-11.md`
- `wiki/ops/agentic-product-engineering-collaboration-company-playbook-role-change-diagnosis-2026-05-12.md`
- `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-role-change-design-2026-05-12.md`
- `wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md`
- `wiki/ops/agentic-product-engineering-collaboration-split-execution-2026-05-11.md`
- `wiki/ops/agentic-product-engineering-collaboration-workflow-gate-2026-05-11.md`

Before target counts:

- all 7 pages had 4 errors covering `layer`, `domain`, and `ops_area`

After target counts:

- all 7 target pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 541
- `summary.error`: 541

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.

## Batch 13b Evidence

Approved batch:

- Batch 13b: product-engineering report-quality ops pages with existing
  identity

Applied fields:

- `layer: ops`
- `domain: product-engineering-collaboration`
- `ops_area: report-quality`

Target set:

- `wiki/ops/agentic-product-engineering-collaboration-company-playbook-report-gate-review.md`
- `wiki/ops/agentic-product-engineering-collaboration-image-model-visual-qa-2026-05-11.md`
- `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md`
- `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`
- `wiki/ops/agentic-product-engineering-collaboration-visual-production-brief-2026-05-11.md`

Before target counts:

- all 5 pages had 4 errors covering `layer`, `domain`, and `ops_area`

After target counts:

- all 5 target pages reported `after.entry_count: 0`

Whole-wiki residual command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 8
```

Result:

- `passed`: false
- `blocking_count`: 569
- `summary.error`: 569

Boundary:

- Existing `canonical_object` and `artifact_type` values were preserved.
- No relation fields, body text, taxonomy config, or checker logic were
  changed.
