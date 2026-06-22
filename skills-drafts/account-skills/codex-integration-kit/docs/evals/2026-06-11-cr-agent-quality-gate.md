# CR Agent Quality Gate Eval - 2026-06-11

## Change

Tightened CR Agent quality gates so technical quality scores cannot be reported
without deduction rationale, and broadened maintainability and observability
review dimensions.

## External References Checked

- GitHub protected branches: required status checks must pass before protected
  branch changes can merge; this maps to CR gate completion checks.
- GitHub CODEOWNERS: changed code can require owner review; this maps to
  maintainability ownership and reviewer evidence.
- GitHub code scanning alerts: alerts can appear in pull requests, carry
  severity/details, and can be tracked; this maps to issue trace and alert
  evidence.
- OpenTelemetry observability primer: observable systems need emitted signals
  such as traces, metrics, and logs; this maps to CR observability scoring.
- Google SRE monitoring and SLO alerting: dashboards, golden signals, SLI/SLO
  alert quality, precision, recall, detection time, and reset time inform the
  alerting checks.

## Pressure Scenario

Input shape:

- CR report gives `可维护性（10）：2` and `可观测性（10）：5`.
- The report lists logs and worktree noise but does not explain scoring
  deductions per technical quality dimension.
- The reviewed change touches MQ, scheduling/reporting, external integration,
  data routing, or production operation paths.

Expected route:

- `cr-technical-review` scans maintainability beyond formatting: change size,
  ownership, modularity, coupling, duplication, dead code, complexity,
  config/profile isolation, rollback/splitability, tests, docs, and runbook.
- `cr-technical-review` scans observability beyond logs: logs, metrics, traces,
  dashboards, real-time alerts, report/batch alerts, SLI/SLO or business KPI
  signals, correlation IDs, redaction, owner, threshold, routing, and runbook.
- `cr-gate` blocks report/gate/full CR when technical quality scores lack
  rationale tied to CR-IDs or concrete evidence.
- `cr-report` renders a deduction rationale table immediately after the
  technical quality scorecard.

## RED Baseline

Command:

```bash
python3 -m unittest \
  tests.test_cr_agent_skills.CRAgentSkillPackageTest.test_gate_and_issues_contracts_are_explicit \
  tests.test_cr_agent_skills.CRAgentSkillPackageTest.test_technical_review_keeps_technical_cr_primary \
  tests.test_cr_agent_skills.CRAgentSkillPackageTest.test_report_requires_issue_ledger_and_todo_persistence \
  tests.test_cr_agent_plugin_marketplace.CRAgentPluginMarketplaceTest.test_cr_agent_plugin_contains_persistence_and_review_completeness_rules
```

Result before skill edits:

- 4 tests failed.
- Missing markers included:
  - `missing quality score rationale`
  - `logs, metrics, traces, dashboards`
  - `real-time alerts, report/batch alerts`
  - `Scoring rationale is mandatory`

This captured the old behavior gap: CR reports could contain numeric quality
scores while the gate and report contract did not force per-dimension evidence.

## GREEN Result

Commands:

```bash
python3 -m unittest tests.test_cr_agent_skills tests.test_cr_agent_plugin_marketplace
```

Result after skill edits:

- 16 tests passed.

Coverage:

- Root skills and plugin package copies contain the same stricter gate rules.
- `cr-gate` blocks missing score rationale and incomplete observability evidence
  for high-risk release/full CR.
- `cr-technical-review` includes broad maintainability and observability
  dimensions.
- `cr-report` and the Chinese template require a score deduction rationale table.

## Residual Risks

- These tests verify skill contract text, not live Codex behavior in an
  installed runtime.
- Real observability evidence still depends on target repo telemetry, alerting,
  dashboard, and ownership systems.
- Installed plugin cache must be synced or reinstalled for a currently running
  Codex session to pick up the updated skill text.
