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

Distinguish report targets:

- `CR/<project>/cases/<case-id>/report.md` is a case coverage artifact.
- `CR/<project>/<report-target>.md` is the formal human CR report.

The case coverage artifact must not replace the formal human CR report. The
formal report must link or name the case artifact when available and must show
the coverage matrix, but it remains reader-first.

Use an explicit report profile:

- `plugin_plain`: canonical plain Chinese CR report.
- `repo_existing`: preserve the repository's established report wrappers or
  layout when a prior report is the chosen style reference.

The required CR sections cannot be dropped under either profile. Coverage
artifacts are always plain machine-oriented Markdown.

Scope wrapper rules by profile:

- `plugin_plain` forbids wiki/Obsidian wrappers: no YAML frontmatter,
  `[[wiki links]]`, `[!tip]` or `[!todo]` callouts, or tag-only metadata line.
- `repo_existing` may preserve wiki/Obsidian wrappers when the chosen reference
  report already uses them. Preserve only established repository style; do not
  invent wrappers for repositories that do not already use them.

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
- coverage summary: files, hunks, checks, triggered rules, review groups, waivers
- coverage matrix by rule with open, blocked, satisfied, issue, N/A, and waived counts
- report state: `stage_report` when review/check closure is incomplete, or
  `complete_cr_report` only after required checks are closed or waived and gate
  evaluation is current
- blocker source breakdown: open diff units, open required checks, blocked
  checks, confirmed high/severe issues, invalid N/A, missing evidence, and
  wrong/stale range when present
- bounded open-check drilldown with representative check IDs, rule IDs, titles,
  linked diff units or review groups, plus the full `checks.jsonl` path
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
- Do not collapse open checks and confirmed findings into one generic blocker.
  Show both when both exist. A report with open required checks is a stage
  report, not a complete CR report.
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
- If the same ticket and same release range already have a formal report,
  append a new review round or write an explicit versioned report target.
- Supported repeated-CR strategies are `append_round`, `ticket_version`, and
  `date_version`.
- If the target cannot be determined safely, block the report write and ask for
  a report target decision.
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
