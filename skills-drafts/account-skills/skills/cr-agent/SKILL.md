---
name: cr-agent
description: Use when the user asks to run, prepare, gate, diagnose, or report code review, release review, branch review, or CR evidence.
---

Use this skill as the single normal user-facing entry point for CR lifecycle work.

The agent must classify CR intent, resolve or create the CR case, validate the
range and evidence, then route to one bounded worker or report the block.

When the requested mode is `report`, `gate`, or `full CR`, the run must write
the human-review CR Markdown file before the final user response. The final
response must include the report path. If repository write access is blocked,
write the report to `/tmp`, report that fallback path, and state the blocked
repository path. Do not treat a chat-only CR summary as complete.

Report mode must route final rendering through `cr-report` after `cr-gate` and
`cr-issues` data exist. The report must use the bundled reader-first Chinese CR
template from `cr-report/references/chinese-cr-report-template.md` unless the
user provides a reference report. A user-provided historical report is style
evidence only: read it to extract structure, decision placement, finding shape,
and scoring/audit conventions, but do not treat that file as a runtime
dependency.

The written report must include both technical quality scoring and CR execution
audit scoring. It must also include a CR execution audit table that lists each
applicable worker/skill, whether it executed, the evidence produced, and any
gap or risk. If worker execution evidence is missing, mark the gap explicitly;
do not infer worker completion from the final report wording.

Coverage gate is mandatory for `gate`, `report`, `replay`, and `full CR` modes:

- Load rule config from `<this-skill>/rules/global.yaml`, `CR/<project>/cr-agent.yaml`,
  and `CR/<project>/cases/<case-id>/cr-agent.yaml`.
- Missing or invalid global config blocks the CR. Repo and case config may add
  terms or stricter checks, but must not weaken global required checks.
- Build coverage artifacts before technical conclusions: `state.json`,
  `diff-units.jsonl`, `facts.jsonl`, `review-groups.jsonl`, `checks.jsonl`,
  `checker-results.jsonl`, `issues.jsonl`, `gate.json`, and `report.md`.
- Every diff unit must close through a check, valid N/A, or blocked status.
  Unmatched hunks still require a general logic check.
- Any open diff unit, open required check, blocked check, invalid N/A, high
  issue, high-risk unresolved question, wrong range, or stale artifact blocks
  the gate.
- Manually confirmed findings must be persisted before report completion:
  write a structured issue registry entry, link it to check IDs and diff unit
  IDs when available, write a checker result with `issue` or `blocked` status,
  and re-evaluate the gate from the updated artifacts. If the finding cannot
  yet be mapped, record a `manual_review_gap` and keep the CR blocked.
- Use `scripts/coverage_gate.py` for artifact generation and
  `scripts/eval_cr_replay.py` for replay validation.

Case coverage artifacts and formal human CR reports are separate outputs:

- `CR/<project>/cases/<case-id>/report.md` is the coverage artifact summary.
- `CR/<project>/<report-target>.md` is the formal human CR report.

Do not claim `report`, `gate`, or `full CR` complete when only the case coverage
artifact exists.

Formal reports must state `Report State: stage_report` when any required check
is open or blocked, any manual review gap exists, or checker/issue linkage is
incomplete. Use `complete_cr_report` only after required checks are closed or
waived and the gate has been re-evaluated from the final issue/checker
artifacts.

Every normal response must show:

- Intent
- CR Case
- CR Type
- Range
- State
- Allowed Action
- Blocked Action, when blocked
- Next Action
- Evidence
- Persisted CR Output, when a report or gate result is written
- Blocked Persistence, when the repo expects a CR artifact but it cannot be written

Supported CR types:

- `merge_cr`: feature branch or commit range to target branch.
- `release_cr`: previous online mainline version to production target.
- `hotfix_cr`: incident baseline to hotfix target.
- `post_incident_cr`: incident before/after range.
- `db_cr`: DDL, migration, or data repair range.
- `config_cr`: config change range or config artifact.

Worker routing:

- `cr-intake`: normalize project, CR type, range, tickets, evidence, and output mode.
- `cr-branch-governance`: validate branch, version, baseline, and release package trust.
- `cr-diff`: produce deterministic diff evidence.
- `cr-scope`: map diff evidence into review scope and triggered dimensions.
- `cr-technical-review`: coordinate technical CR dimensions.
- `cr-evidence`: check Jira, test, UAT, rollback, impact, and package evidence.
- `cr-issues`: maintain the normalized CR issue registry.
- `cr-gate`: produce the final `allow`, `conditional`, or `blocked` decision.
- `cr-report`: render the Chinese CR report without recalculating gate decisions.
- `cr-replay`: evaluate behavior against replay fixtures.

Persisted CR Output:

- If the reviewed repo has a `CR/` directory and the user asks for report, gate,
  full CR, or a persistent review record, write the CR report into that directory
  using the repo's existing date/project naming pattern.
- If the repo has a CR TODO ledger, append blocking and follow-up TODOs there.
- Report the written path as `Persisted CR Output`.
- If writing is blocked by permissions, ambiguity, or missing destination rules,
  report `Blocked Persistence` and keep the gate result visible in chat.

Boundaries:

- Do not treat feature-branch CR as release CR.
- Do not compare a release using a guessed branch diff when previous online version is required.
- Do not let branch, technical, or evidence findings bypass `cr-issues`.
- Do not leave confirmed findings only in prose or chat. If a finding appears
  in the formal report, it must also exist in `issues.jsonl` or be called out
  as a blocked persistence/linkage gap.
- Do not let report wording override `cr-gate`.
- Do not claim CR coverage from prose. The coverage ledger and checks are the
  source of truth.
- Do not treat the case coverage artifact as the formal human CR report.
- Do not hard-code local reference-report paths in CR skills or reports.
- Do not infer concrete downstream outages from static diff alone; require compatibility evidence instead.
- Do not claim CR complete when required review dependencies are missing.
- Do not stop after only the first blocking issue when other CR dimensions were triggered.
- Do not use wiki/Obsidian wrappers for `plugin_plain` CR reports: no YAML
  frontmatter, `[[wiki links]]`, `[!tip]`, `[!todo]`, or tag callouts.
- For `repo_existing`, preserve wiki/Obsidian wrappers only when a chosen
  repository reference report already uses them.
