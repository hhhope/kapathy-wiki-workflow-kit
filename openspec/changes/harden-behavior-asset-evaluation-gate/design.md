# Behavior Asset Evaluation Gate Design

## Problem

The current skill and runtime-routing gates catch some missing evidence, but the
minimum check is too shallow. A change can pass by adding `evaluation.md` with
the right section names while still duplicating routing ownership, missing
negative cases, or proving only that text exists.

The recent Agent Intent Routing drift exposed the gap: `High-Frequency Skills`
already owned the runtime skill route table, but the new `Agent Intent Routing`
section added another route table. Existing tests and evaluation confirmed that
routing text existed; they did not verify that ownership stayed non-overlapping.

## Goals

- Treat semantic edits to `.codex/skills/*` and runtime behavior edits in
  `AGENTS.md` as behavior-asset changes.
- Make evaluation evidence meaningful enough to catch shallow proof and routing
  drift.
- Provide a local checker that the user can run directly, similar to the wiki
  frontmatter taxonomy checker.
- Keep rule vocabulary in a config file, not duplicated across `AGENTS.md`,
  skills, and Python code.
- Keep the first implementation focused on active OpenSpec changes and current
  repo governance files.

## Non-Goals

- Do not build a general static analyzer for all Markdown semantics.
- Do not scan archived OpenSpec changes by default.
- Do not require multi-session rollout telemetry as the minimum gate.
- Do not replace human review of behavior design; the checker only catches
  explicit structural and evidence gaps.

## Recommended Architecture

Use a three-layer model:

1. `AGENTS.md` owns the hard runtime rule.
2. `wiki/config/behavior-asset-evaluation.yaml` owns the detailed checker
   contract.
3. `scripts/check_behavior_assets.py` validates active changes and current
   behavior assets, then `scripts/repo_health_check.py` aggregates the result.

This mirrors the wiki frontmatter pattern: short hard rule in `AGENTS.md`,
structured source of truth in `wiki/config`, executable checker in `scripts`,
and readable report output for audit.

## Behavior Asset Scope

Covered files:

- `AGENTS.md`
- `.codex/skills/**/SKILL.md`
- `.codex/skills/**/references/*.md` when they define triggers, gates, pressure
  scenarios, scorecards, routing, publish/sync rules, or completion behavior
- active OpenSpec specs that add or change future runtime behavior

Covered behavior claims:

- trigger
- route
- stop
- reject
- publish
- sync
- complete
- archive-ready
- parent gate
- lightweight path
- full gate
- future agent behavior

## Evaluation Contract

A behavior-asset change must include `evaluation.md` with evidence that is
stronger than section presence.

Required sections:

- `## Pressure Scenarios`
- `## RED Baseline`
- `## GREEN Result`
- `## Residual Risks`

Required replay fields:

- input or situation shape
- trigger condition
- expected route, stop, refusal, or boundary behavior
- repo-visible artifact a future agent should read
- expected output or non-output
- promotion or non-promotion boundary
- proof boundary or residual risk

Required scenario mix:

- at least one positive trigger case
- at least one negative or should-not-trigger case
- at least one parent-gate preservation case when the change mentions a gate,
  route, module, lightweight path, full path, publish, sync, or reader-facing
  output
- at least one structural anti-drift case when the change edits `AGENTS.md`
  routing or a skill that declares ownership

Required proof:

- RED baseline must include an observed failure, missing artifact, failing
  command, or explicit before-state check.
- GREEN result must include a rerunnable command or a manual replay record with
  file paths and expected observations.
- Evaluation must not rely only on “text exists” assertions when the change
  modifies runtime routing or skill ownership.

## Ownership Rules

The first checker contract should encode the current drift class directly:

- `High-Frequency Skills` is the repo skill routing table.
- `Agent Intent Routing` is a pre-action classification rule, not another full
  route table.
- `Agent Intent Routing` may reference `High-Frequency Skills`, but must not
  contain a multi-row parent-gate route table or a `Minimum routes` section.
- A delivery-sensitive module skill must name its parent gate or state that no
  parent applies.
- A module or child skill must not claim review-ready, publish-ready, sync-ready,
  or complete status if the parent gate still has blockers.

## Checker Design

Add `scripts/check_behavior_assets.py`.

Inputs:

- repo root
- `wiki/config/behavior-asset-evaluation.yaml`
- active change directories under `openspec/changes/*`, excluding `archive`
- current behavior assets in `AGENTS.md` and `.codex/skills`

Outputs:

- terminal summary with `PASS` or `FAIL`
- `/tmp/behavior-asset-evaluation-report.json`
- `/tmp/behavior-asset-evaluation-report.md`

Checks:

- active behavior-asset change has `evaluation.md`
- required evaluation sections exist
- required replay fields exist
- positive and negative pressure scenarios are present
- parent-gate preservation evidence is present when applicable
- `Agent Intent Routing` does not duplicate the `High-Frequency Skills` route
  table
- behavior evaluation does not only contain presence-style evidence for a
  routing or ownership change

Severity:

- missing evaluation for covered active change: error
- missing required section: error
- missing negative scenario: error
- missing parent-gate preservation when applicable: error
- duplicated route table ownership: error
- weak command/manual replay evidence: warn for first rollout, candidate error
  after the first checker proves useful

## Health-Check Integration

`scripts/repo_health_check.py` remains an aggregator. It should call the new
checker and expose a named result such as `behavior-asset-evaluation`.

The user-facing commands become:

```bash
python3 scripts/check_behavior_assets.py
python3 scripts/repo_health_check.py
```

`repo_health_check.py` should not duplicate the evaluation vocabulary. It should
surface checker failures and details.

## Test Strategy

Unit tests should use temporary repositories, like the existing repo health
tests.

RED cases:

- active change edits `.codex/skills/*` without `evaluation.md`
- active change edits `AGENTS.md` runtime routing without `evaluation.md`
- `evaluation.md` has the four section names but no negative scenario
- `evaluation.md` has only “text exists” evidence for a routing change
- `AGENTS.md` contains both `High-Frequency Skills` and an `Agent Intent
  Routing` `Minimum routes` table

GREEN cases:

- active skill change with positive, negative, parent-gate, RED/GREEN, and proof
  boundary evidence passes
- active `AGENTS.md` routing change with real replay fields passes
- `Agent Intent Routing` references `High-Frequency Skills` without duplicating
  the table
- `repo_health_check.py` reports the checker as a named passing/failing result

## Rollout Boundary

First rollout should be strict on active changes and current known drift, but
not attempt historical cleanup. Archived changes are evidence history, not the
first enforcement target.

The existing Agent Intent Routing overlap should be fixed by the same follow-up
change that introduces the checker, so the new checker proves it can catch the
actual drift that motivated it.

## Residual Risks

- Text-level checks can still miss subtle semantic drift.
- Manual replay records can be honest but incomplete.
- If future agents ignore repo `AGENTS.md`, this repo-local checker cannot force
  runtime behavior.
- Over-tight checks may make small skill wording fixes feel heavy; the config
  should keep severities adjustable.
