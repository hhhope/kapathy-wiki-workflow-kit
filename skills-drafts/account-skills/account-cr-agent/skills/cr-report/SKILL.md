---
name: cr-report
description: Use only inside cr-agent to render Chinese CR reports from cr-issues and cr-gate without recalculating decisions.
---

Render CR output only. Do not create new findings or recalculate gate logic.

If the user provides a reference CR report path or says to follow a prior
report, read that reference before rendering. Use it as style evidence, not as
a runtime dependency: extract the reader-facing structure, decision placement,
finding shape, and scoring/audit sections, then render the current CR from the
current `cr-gate` and `cr-issues` data.

The output is a human-review Markdown file, not just a chat summary. Use the
repository CR path when available:

- `<repo-root>/cr/<project>/YYYY-MM-DD.md`
- `<repo-root>/CR/<project>/YYYY-MM-DD.md`

Prefer the directory casing already used by the target repository. If neither
exists, create the lowercase `cr/<project>/YYYY-MM-DD.md` path unless the user
provided a path. If repository write access is blocked, report `Blocked
Persistence` and the intended repository path.

Use a plain Markdown CR template. Do not emit wiki/Obsidian wrappers:

- no YAML frontmatter
- no `[[wiki links]]`
- no `[!tip]` or `[!todo]` callouts
- no tag-only metadata line

Required information:

- final conclusion and release decision
- blocking items with owner and completion standard
- technical quality scorecard
- CR execution audit showing which CR workers/skills produced evidence
- change summary
- CR type and range
- branch governance result
- technical review result
- evidence result
- test evidence
- release and rollback risk
- issue registry or equivalent finding/TODO trace
- TODO ledger when the reviewed repo maintains one
- owner and reviewer assignments
- Report Path or Blocked Persistence status

Reader-first rendering rules:

- Put the final conclusion before process evidence.
- Split ambiguous `conditional` decisions into concrete decisions:
  code merge/keep, production switch/release action, and release-complete claim.
- Put blocking items near the top with owner, deadline, and completion standard.
- Group technical findings by severity and keep each finding in the shape:
  evidence, impact, required/suggested action, blocking status.
- Keep `Issue Registry` as an internal source of truth; do not put a raw
  registry table before the gate conclusion. Render it as findings, technical
  debt, and TODOs. A raw registry may appear only as an appendix.
- Do not bury missing tests, UAT, rollback, config, or compatibility evidence
  in prose. Promote them into blocking items when they block `cr-gate`.
- Include a CR execution audit section. It must list the CR workers that were
  applicable, whether each was used, the evidence it produced, and any missing
  review dependency. Do not let this audit replace technical findings.
- Score both the reviewed change and the CR execution. The technical scorecard
  rates the code/change. The CR execution scorecard rates review completeness,
  evidence quality, worker coverage, and unresolved blind spots.
- Scoring rationale is mandatory. Every technical quality score must include a
  nearby deduction rationale table that cites CR-IDs, concrete evidence, or an
  explicit non-applicable reason.
- Maintainability scoring must not be reduced to formatting. It must consider
  change size, ownership, modularity, coupling, duplication, dead code,
  complexity, config/profile isolation, rollback/splitability, test coverage,
  documentation, and runbook ownership.
- Observability scoring must not be reduced to whether logs exist. It must
  consider logs / metrics / traces, dashboards, real-time alerts,
  report/batch alerts, SLI/SLO or business KPI signals, correlation IDs,
  sensitive-field redaction, alert owner, threshold, routing, and runbook.

Persistence rules:

- Persisted CR Output is the durable Markdown report path or the explicit
  Blocked Persistence fallback when the repository path cannot be written.
- If the same project/date report already exists, overwrite or update that same
  dated report with the current CR gate result instead of creating a parallel
  report, preserving obsolete conclusions, or changing the established layout.
- TODO ledger updates for an existing same-day CR must be idempotent by TODO-ID:
  update existing entries when the source CR-ID is the same, and append only
  truly new blocking or follow-up items.

Use the canonical Chinese report template in
`references/chinese-cr-report-template.md`.

The canonical template includes these required reader-facing sections:
`最终结论（是否可发布）`, `评分卡（100分）`, `技术质量评分`, `CR 执行审计评分`,
`CR 执行审计`, `技术审查结果`, `TODO 跟踪`, `测试证据`, `发布风险与回滚`, and
`处置项`.

The canonical score rationale table must state `每个技术质量分项都必须说明扣分依据`
and explicitly cover `logs / metrics / traces`, `实时告警 / 报表或批处理告警`,
and `复杂度 / 重复 / 死代码 / 耦合` when those dimensions are applicable.

The headings may be renamed or reordered to match a user-provided reference
report, but the report must remain reader-first: conclusion and blocking items
come before raw process evidence.

Per-author files may be generated when author data exists. Every issue shown in author files must reference an existing CR-ID.
