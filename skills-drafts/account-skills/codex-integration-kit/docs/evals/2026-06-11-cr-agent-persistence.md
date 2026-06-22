# CR Agent Persistence and Review Completeness Eval - 2026-06-11

## Change

Tightened CR Agent skills so CR results are not only delivered in chat when a
reviewed repository has a `CR/` directory. The workflow must persist the CR
report, TODO ledger entries, issue registry, technical debt, bad smells,
Sonar/static-analysis evidence gaps, security risk, and business risk.

## Pressure Scenario

Input shape:

- User invokes `$account-cr-agent` for a branch review.
- Reviewed repo already has `CR/yqt-trade/` and `TODO_BACKLOG.md`.
- Diff touches external bank callback, account-opening state, sensitive logging,
  tests, rollback, and UAT evidence.

Expected route:

- `cr-agent` routes intake, branch governance, diff, scope, technical review,
  evidence, issues, gate, and report.
- `cr-report` writes a dated CR report into the repo CR directory.
- `cr-report` appends blocking TODOs to the CR TODO ledger.
- `cr-technical-review` emits security, business, technical debt, and
  Sonar-style findings instead of stopping at the first blocker.
- `cr-evidence` records missing Sonar/security/test/UAT/rollback/raw callback
  samples as evidence gaps.

## RED Baseline

Command:

```bash
python3 -m unittest tests.test_cr_agent_skills
```

Result before skill edits:

- Failed 4 assertions.
- Missing markers:
  - `Persisted CR Output`
  - `Sonar or static-analysis status`
  - `technical debt register`
  - `Sonar-style code smells`

This captured the old behavior gap: CR Agent could complete a chat report while
omitting durable CR records and broader review dimensions.

## GREEN Result

Commands:

```bash
python3 -m unittest tests.test_cr_agent_skills
python3 -m unittest tests.test_cr_agent_plugin_marketplace
```

Results after skill edits:

- `tests.test_cr_agent_skills`: 11 tests passed.
- `tests.test_cr_agent_plugin_marketplace`: 5 tests passed.

Coverage added:

- Root `skills/cr-*` now require persisted CR output and review completeness.
- Plugin package `account-cr-agent/skills/cr-*` is checked for the same markers.
- Plugin marketplace tests now run with standard-library `unittest`, avoiding a
  pytest dependency for this package check.

## Residual Risks

- These tests verify skill contract text, not a live Codex runtime replay.
- Real persistence still depends on target repo permissions and destination
  naming conventions.
- Installed plugin cache will not update inside an already-running Codex
  session; users must reinstall/update and restart Codex to pick up new skill
  content.


## Follow-up: Fixed Report Layout

Observed issue:

- A persisted `account-gateway` report satisfied the CR Agent section contract but
  did not match the established yqt/account CR report layout.

Contract tightened:

- `cr-report` now requires the fixed Chinese CR report layout from
  `skills/code-review/SKILL.md` and prior project CR reports.
- Root `skills/cr-report/SKILL.md` and plugin
  `account-cr-agent/skills/cr-report/SKILL.md` must both include the same layout
  markers.

Additional GREEN checks:

```bash
python3 -m unittest tests.test_cr_agent_skills tests.test_cr_agent_plugin_marketplace
```

Expected coverage:

- Report title style `代码评审报告 — {project} YYYY-MM-DD`.
- Required headings including `最终结论（是否可发布）`, `评分卡（100分）`,
  `技术审查结果`, and `TODO 跟踪`.
- Plugin package copy contains the same fixed-layout contract.


Same-day overwrite rule:

- If `cr/{project}/YYYY-MM-DD.md` or `CR/{project}/YYYY-MM-DD.md` already exists,
  the current CR run updates that same dated report rather than creating a second
  report or preserving stale gate conclusions.
- TODO ledger writes are idempotent by TODO-ID so reruns update existing same-day
  entries and append only new CR items.
