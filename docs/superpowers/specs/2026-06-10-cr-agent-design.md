# CR Agent Skill Package Design

Date: 2026-06-10
Status: design-approved-for-spec-review
Repository: report-wiki-portfolio

## Problem

The current CR skill surface is useful but fragmented.

`code-review` provides a Chinese report template and a small checkpoint model.
`release-diff-cr` provides release-diff evidence such as commit ranges,
authors, changed files, and mainline direct commits. These pieces do not yet
form a lifecycle agent.

The observed mandao-customer incident showed the gap clearly:

- the correct release range could expose a `keyType` change from `2` to `5`
- the release-diff scan could register a blocking mainline-direct issue
- the final gate could still remain permissive because issue registration and
  gate calculation were not unified
- branch review and release review could be confused by comparing a feature
  branch to `master` instead of previous online mainline to production target

The missing capability is not another report template. It is a CR lifecycle
agent with clear intake, branch governance, technical review, evidence review,
issue registry, hard gate, report output, and replay.

## Goal

Design a `cr-agent` skill package that behaves like `req-agent` and wiki-agent
surfaces: one normal entry point, bounded workers, explicit state, reusable
evidence, and hard gates.

The first implementation should preserve the useful parts of existing
`code-review` and `release-diff-cr`, but make the decision flow stricter:

- classify the CR type before reviewing
- prove the comparison range is valid
- run technical CR as a first-class path
- keep release evidence as a separate support path
- put all findings into one issue registry
- make gate conclusion derive only from the issue registry and required
  evidence
- support replay cases for known failure modes

## Non-Goals

- Do not replace human reviewers or claim deep business certainty from static
  diff alone.
- Do not hard-code one incident's domain nouns as universal rules.
- Do not make release evidence checks a substitute for technical CR.
- Do not treat feature-branch CR as a complete release gate.
- Do not require every technical dimension to become a separate mature skill in
  the first version.
- Do not make report rendering recalculate gate decisions.

## Core Positioning

```text
cr-agent = CR lifecycle controller
cr-branch-governance = range and version trust gate
cr-diff = deterministic diff evidence builder
cr-technical-review = technical CR coordinator
cr-evidence = release and delivery evidence checker
cr-issues = single source of CR findings
cr-gate = final decision engine
cr-report = renderer only
cr-replay = evaluation and incident replay surface
```

The agent should separate facts, judgments, and output:

- `cr-diff` produces facts.
- review workers produce findings.
- `cr-issues` normalizes findings.
- `cr-gate` makes the final decision.
- `cr-report` renders the decision and evidence.

## CR Types

`cr-agent` must classify the request before routing:

| CR type | Primary comparison | Primary risk |
|---|---|---|
| `merge_cr` | feature branch or commit range to target branch | code correctness and maintainability |
| `release_cr` | previous online mainline version to production target | hidden release content, missed validation, incomplete package |
| `hotfix_cr` | incident baseline to hotfix target | blast radius, rollback, incomplete urgent verification |
| `post_incident_cr` | incident before/after range | root-cause evidence and prevention gaps |
| `db_cr` | migration or DDL range | data integrity, rollback, lock and runtime risk |
| `config_cr` | config change range or config artifact | environment drift and operational blast radius |

If a user asks for release CR but provides only feature-branch diff evidence,
`cr-agent` must block release-gate claims and route the run as `merge_cr` unless
the user provides the previous online version and production target.

## Worker Package

### `cr-agent`

The single normal user-facing entry point.

Responsibilities:

- classify intent and CR type
- resolve or create the CR case
- validate required input for that CR type
- route to one bounded worker at a time
- show state in every normal response
- prevent implementation or report claims when gates are blocked

Normal response shape:

```text
Intent
CR Case
CR Type
Range
State
Allowed Action
Blocked Action
Next Action
Evidence
```

### `cr-intake`

Collects the CR input package.

Required fields:

- project root or repository identifier
- CR type
- start ref and end ref, or branch and target
- Jira, requirement, incident, or release ticket references when available
- test, UAT, production, rollback, and impact-confirmation evidence when
  available
- requested output mode: status, gate, report, replay, or full CR

Output:

- a normalized CR case skeleton
- missing-input blockers
- the next valid worker

### `cr-branch-governance`

Validates that the review range is trustworthy.

Checks:

- release CR uses previous online mainline version to production target
- merge CR uses feature range to target branch
- start ref is an ancestor of end ref unless explicitly marked as archaeology
- mainline direct commits are identified
- production target commit is proved covered by UAT or the gap is recorded
- test, UAT, release, and master branches are compared when those refs are
  provided
- non-merge commits have ticket or approved exception evidence
- cherry-pick, revert, conflict-resolution, and long-lived branch risks are
  surfaced
- package completeness is checked for code, SQL, config, scripts, and rollback
  assets

Hard blockers:

- wrong baseline for the declared CR type
- unclear release range
- feature-branch CR presented as release gate
- mainline direct commit without approval or validation evidence
- production commit not covered by UAT evidence for release CR
- unrelated commits in release range without explicit disposition

### `cr-diff`

Builds deterministic diff evidence. It does not make business conclusions.

Evidence:

- commit list
- merge commits and source branches
- first-parent non-merge commits
- changed files and file statuses
- authors and committers
- per-author changed scope
- numstat and large-diff hints
- file categories such as code, config, SQL, test, docs, dependency, generated
- high-risk text or path hits for later scope routing

Existing `release-diff-cr` functionality belongs mostly here.

### `cr-scope`

Maps diff evidence into review scope.

Scope dimensions:

- account, payment, settlement, clearing, merchant onboarding, or customer
  domain paths
- certificate, `keyType`, cryptography, terminal key, or encryption/decryption
  changes
- DB, DDL, migration, data repair, or rollback scripts
- external channel, old frontend gateway, third-party, or upstream/downstream
  integration contracts
- auth, authorization, role, token, PII, or compliance-sensitive paths
- scheduled jobs, MQ, async processing, idempotency, or retry paths
- config center, environment-specific config, registry, or deployment settings

Output:

- triggered technical dimensions
- required evidence checks
- suggested reviewers
- scope uncertainty items

### `cr-technical-review`

Coordinates technical CR. This is the main reviewer path, not a side check.

First version can implement this as one skill with explicit dimensions. Mature
dimensions can later split into separate workers.

Dimensions:

- `cr-correctness`
- `cr-robustness`
- `cr-security`
- `cr-architecture`
- `cr-data`
- `cr-integration`
- `cr-observability`
- `cr-testability`
- `cr-tech-debt`

Each dimension emits normalized findings into `cr-issues`.

### Technical Dimensions

`cr-correctness` checks business logic, state transitions, branch coverage,
boundary values, null handling, and behavior regressions.

`cr-robustness` checks exception handling, timeout, retry, fallback,
idempotency, concurrency, duplicate execution, partial failure, and resource
cleanup.

`cr-security` checks authentication, authorization, sensitive data exposure,
secret handling, encryption/decryption, key material, logging, injection, token
handling, and regulated data handling.

`cr-architecture` checks responsibility boundaries, module coupling, duplicated
logic, oversize files, over-abstraction, under-abstraction, and local pattern
consistency.

`cr-data` checks transaction boundaries, lock behavior, isolation assumptions,
pagination, consistency, DDL risk, migration rollback, data repair scripts, and
runtime validation SQL.

`cr-integration` checks external APIs, channel protocols, upstream/downstream
compatibility, config contracts, environment drift, old/new system coexistence,
and partner impact.

`cr-observability` checks logs, metrics, alerts, trace context, error messages,
and incident diagnosis usefulness.

`cr-testability` checks unit, integration, regression, compatibility,
performance, and failure-path evidence for changed behavior.

`cr-tech-debt` records new or exposed debt, whether it blocks release, allowed
deferral, owner, date, and required follow-up.

### `cr-evidence`

Checks release and delivery evidence. It does not review code quality.

Evidence categories:

- Jira or requirement linkage
- test evidence
- UAT or pre-production coverage for the same commit or range
- rollback plan and rollback assets
- impact-owner confirmation
- config, SQL, script, and deployment package completeness
- incident or hotfix approval evidence when applicable

Output:

- missing-evidence issues
- weak-evidence warnings
- evidence links attached to existing technical or branch issues

### `cr-issues`

Owns the single CR issue registry.

All workers must write findings through this model:

```text
CR-ID
source_worker
severity
category
title
evidence
impact
required_action
owner
blocking
status
related_files
related_commits
```

Severity values:

- `critical`
- `high`
- `medium`
- `low`
- `info`

Status values:

- `open`
- `needs_confirmation`
- `accepted_risk`
- `fixed`
- `waived`

Only `fixed`, `waived`, or explicitly accepted non-blocking risks can stop an
issue from blocking through `cr-gate`.

### `cr-gate`

The only worker that decides the final gate conclusion.

Conclusions:

- `allow`
- `conditional`
- `blocked`

Hard rules:

- any open blocking issue => `blocked`
- wrong baseline => `blocked`
- release range unclear => `blocked`
- feature-branch CR presented as release gate => `blocked`
- mainline direct commit without approval and validation evidence => `blocked`
- production commit not covered by UAT evidence for release CR => `blocked`
- high-risk integration or security change without compatibility and test
  evidence => `blocked`
- DDL or data repair without rollback or validation evidence => `blocked`
- critical security issue => `blocked`
- missing required reviewer for a triggered high-risk dimension =>
  `conditional` or `blocked` depending on CR type

The gate must derive from `cr-issues` and required evidence. It must not be
manually overridden by report text.

### `cr-report`

Renders Chinese CR output. It does not create new findings or recalculate gate
logic.

Outputs:

- main CR report
- per-author review files when author data exists
- issue table
- gate conclusion
- technical review sections
- evidence section
- branch governance section
- follow-up or debt backlog entries when requested

Required report sections:

- change summary
- CR type and range
- branch governance result
- technical review result
- evidence result
- issue registry
- gate conclusion
- test evidence
- release and rollback risk
- owner and reviewer assignments

### `cr-replay`

Provides behavior replay and regression evidence for the CR agent.

Initial replay scenarios:

| Scenario | Expected result |
|---|---|
| mandao-customer `keyType` release range | mainline direct issue, integration compatibility review, blocked if UAT/approval evidence missing |
| feature branch compared to master for release CR | wrong baseline, blocked release-gate claim |
| DDL without rollback evidence | data review issue, blocked |
| sensitive token or private key committed | security issue, blocked |
| missing tests for high-risk integration change | evidence issue, blocked or conditional by configured CR type |
| branch has unrelated commits in release range | branch governance issue, blocked or needs confirmation |

Replay evidence must capture:

- input situation
- triggered worker
- expected issue
- expected gate
- proof boundary
- residual risk

## Data Flow

```text
user request
  -> cr-agent
  -> cr-intake
  -> cr-branch-governance
  -> cr-diff
  -> cr-scope
  -> cr-technical-review
  -> cr-evidence
  -> cr-issues
  -> cr-gate
  -> cr-report
  -> cr-replay when evaluating behavior
```

`cr-issues` is not merely an output table. It is the state surface used by
`cr-gate`.

## Authority Model

```text
Git / release refs
  own commit and file facts

CR case
  owns intent, CR type, range, evidence references, issue state, and gate state

technical review workers
  own dimension-specific findings

cr-gate
  owns final allow / conditional / blocked conclusion

cr-report
  owns presentation only
```

## Hard Boundaries

- Do not compare a release using a guessed feature-branch diff when previous
  online version is required.
- Do not let a branch or release-diff issue bypass the issue registry.
- Do not let report templates override gate conclusions.
- Do not infer a concrete downstream outage from static code alone; instead,
  raise compatibility evidence requirements.
- Do not convert missing evidence into "allow" by default.
- Do not mark CR complete when required CR skills are missing; record missing
  review dependency.

## First Implementation Slice

The first implementation should be small enough to land safely:

1. Add `cr-agent` entry skill.
2. Add worker skills for:
   - `cr-intake`
   - `cr-branch-governance`
   - `cr-diff`
   - `cr-scope`
   - `cr-technical-review`
   - `cr-evidence`
   - `cr-issues`
   - `cr-gate`
   - `cr-report`
   - `cr-replay`
3. Adapt existing `release-diff-cr` as the first `cr-diff` provider.
4. Adapt existing `code-review` as the first `cr-technical-review` and
   `cr-report` provider.
5. Fix the gate closure bug: blocking `cr_scan_issues` must force blocked gate
   and `--fail-on blocker` behavior.
6. Add replay fixtures for the mandao-customer incident shape and baseline
   misuse.

The first version may keep technical sub-dimensions inside
`cr-technical-review` rather than creating nine separate mature skill files.

## Error Handling

When input is incomplete:

- `cr-agent` returns `blocked_action` and asks for the missing ref, evidence, or
  CR type.
- `cr-branch-governance` blocks release CR if the range cannot be proved.
- `cr-diff` reports unresolved refs instead of guessing merge bases.
- `cr-scope` records uncertainty instead of inventing domain impact.
- `cr-technical-review` marks missing specialized reviewer dependencies.
- `cr-evidence` records missing evidence as issues.
- `cr-gate` remains blocked or conditional until issue state changes.

When repository state is dirty:

- CR evidence can still be generated from explicit refs.
- report-writing must not stage unrelated files.
- generated reports should identify whether they reviewed committed refs or
  working-tree changes.

## Testing Strategy

Minimum test layers:

- unit tests for CR type classification
- unit tests for branch governance blockers
- unit tests for issue registry normalization
- unit tests for gate conclusions
- fixture tests for release-diff JSON and report output
- replay tests for known failure modes

Required first replay cases:

1. Mandao-customer range with mainline direct `keyType` change:
   expected branch issue plus compatibility review trigger, blocked when
   approval/UAT evidence is absent.
2. Feature branch diff used as release CR:
   expected wrong-baseline blocker.
3. Blocking issue produced by release diff:
   expected final gate `blocked`.
4. DDL file without rollback evidence:
   expected data issue and blocked gate.
5. High-risk integration path without test evidence:
   expected evidence issue and non-allow gate.

## Success Criteria

- A CR request is always classified before review starts.
- Release CR cannot be satisfied by feature branch diff alone.
- Branch governance findings, technical findings, and evidence findings all
  enter one issue registry.
- Any open blocking issue changes final gate to `blocked`.
- Existing release-diff and code-review capabilities are reused rather than
  discarded.
- Reports render the gate conclusion from `cr-gate` without recomputation.
- Replay can prove the mandao-customer incident shape would be blocked at least
  by branch governance and evidence gaps, even without claiming static code can
  prove the concrete downstream outage.

## Residual Risks

- Static CR cannot know every downstream compatibility fact. It can require
  evidence and block release claims when the evidence is absent.
- Too many worker files can add ceremony. The first implementation should keep
  technical sub-dimensions inside `cr-technical-review` until a dimension earns
  a standalone skill.
- Strict release gates may need project-specific configuration for teams with
  different branch models.
- Existing CR reports may not have enough structured data to backfill all issue
  fields. The first version should support best-effort import with explicit
  unknowns.
