# OpenSpec Router Scenario Replay

> Supports OpenSpec change: `add-openspec-router-governance`.
> This replay distinguishes skill-level routing from full OpenSpec governance
> verification.

## Scope

Manual replay against:

- `.codex/skills/openspec-router/SKILL.md`
- `docs/superpowers/specs/2026-05-15-openspec-router-design.md`
- `openspec/changes/add-openspec-router-governance/specs/agent-workflow-routing/spec.md`

## Results

| Case | Input | Expected route | Pass | Notes |
|---|---|---|---|---|
| 1 | `$superpowers:brainstorming 帮我看医疗病例模型` | `Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.` | yes | OpenSpec is context only until Superpowers review passes. |
| 2 | `可以继续做` during `ask-or-present` | Advance current Superpowers gate only | yes | Short approval cannot jump to OpenSpec edit or commit. |
| 3 | `确认继续把` after written spec review | Handoff accepted lifecycle content into OpenSpec | yes | OpenSpec may receive accepted content after review. |
| 4 | `那你做吧` | Propose if no active change; implement only if active tasks exist | yes | Prevents implementation without lifecycle scope. |
| 5 | `都验证了吗` | `Route: verify -> evidence check; no mock evidence accepted for live acceptance.` | yes | Verification requires real command evidence or explicit blocker. |
| 6 | `archive` | Check OpenSpec tasks, validation, verification, and archive review | yes | Superpowers completion cannot archive. |
| 7 | `$superpowers:brainstorming ... 可以继续做` | `Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.` | yes | Prevents the current direct OpenSpec edit and commit bypass. |

## Verdict

The router covers the observed failure mode when it is loaded before mixed
Superpowers/OpenSpec work. Full governance verification is recorded in the
OpenSpec change evaluation.
