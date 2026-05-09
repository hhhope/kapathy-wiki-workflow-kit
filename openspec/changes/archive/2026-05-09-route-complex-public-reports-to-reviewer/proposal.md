## Why

The public report quality gate has started accumulating heavy responsibilities:
reference mapping, template choice, learning-use mapping, scoring, residual
risk, Feishu readiness, and read-back evidence. That makes the runtime skill too
heavy for ordinary reader-facing edits.

The Account Harness Wiki repair exposed the missing boundary: complex public
materials need a reviewer role before drafting, while simple materials should
not pay the cost of a full reviewer workflow.

## What Changes

- Keep `public-report-quality-gate` as the lightweight trigger and escalation
  gate.
- Add a repo-local manual reviewer template for complex reader-facing outputs.
- Define escalation signals for when complex materials must route to the
  reviewer.
- Require the gate-review artifact to record whether reviewer routing was
  required, run, skipped, or blocked.

## Impact

- Adds `.codex/agents/public-report-reviewer.md`.
- Updates `.codex/skills/public-report-quality-gate/` references and pressure
  scenarios.
- Adds OpenSpec coverage and evaluation evidence.
- Does not spawn sub-agents automatically.
- Does not rewrite existing Feishu documents.
