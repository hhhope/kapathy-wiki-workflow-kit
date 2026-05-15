# Design

## Model

The repository keeps four separate workflow layers:

1. Intent routing: `openspec-router`
   - Decides current intent and allowed gate.
   - Emits one compact route line.
   - Prevents method gates and lifecycle gates from bypassing each other.

2. Method discipline: Superpowers
   - Owns brainstorming, writing plans, TDD, execution, and review workflows.
   - Produces secondary artifacts under `docs/superpowers/`.

3. Lifecycle authority: OpenSpec
   - Owns proposal, design, specs, tasks, verification, completion, and archive.
   - Remains the source of truth for large changes.

4. Repo discipline: AGENTS.md
   - Owns health checks, REQ/OpenSpec selection, git discipline, validation,
     commit behavior, and safety boundaries.

The router is not a truth source. It is a pre-action gate that keeps existing
truth sources in the correct order.

## AGENTS.md Rule

Add `Workflow Routing` after the existing `Workflow Change Gate`.

The section requires `openspec-router` before mixed Superpowers/OpenSpec work,
workflow repair, implementation, verification, archive, or ambiguous large
tasks. It also states that the router does not relax OpenSpec gates and that
`$superpowers:brainstorming` keeps OpenSpec read-only until Superpowers written
spec review passes.

## PROJECT.md Rule

Add one operating-model bullet:

```text
Agent workflow routing preserves OpenSpec lifecycle authority while allowing
Superpowers method workflows to run without bypassing review gates.
```

PROJECT.md stays implementation-neutral and does not mention Codex-specific
paths.

## Superpowers Artifact Binding

Router Superpowers artifacts support this OpenSpec change:

- `docs/superpowers/specs/2026-05-15-openspec-router-design.md`
- `docs/superpowers/plans/2026-05-15-openspec-router.md`
- `docs/superpowers/specs/2026-05-15-openspec-router-replay.md`

These artifacts are working material. OpenSpec remains lifecycle authority.

## Verification

Verification must distinguish local skill replay from project governance
replay. The governance replay checks:

- PROJECT declares OpenSpec authority and routing preservation.
- AGENTS invokes router before mixed workflows and does not relax OpenSpec.
- OpenSpec delta spec contains the workflow router requirement.
- `.codex/skills/openspec-router/SKILL.md` defines route line, intent, gate,
  and hard rules.
- Original incident routes to Superpowers review before OpenSpec edits.
- Behavior-asset checks run and any existing blockers are recorded.
- `openspec validate add-openspec-router-governance --strict` passes.
