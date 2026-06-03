---
name: req-agent
description: Use when the user asks to intake, clarify, check, gate, or hand off requirements work before development.
---

Use this skill as the single normal Codex-facing entry point for requirements
analysis and OpenSpec handoff readiness.

The agent must classify user intent, resolve or create the requirements case,
validate state, then route to one bounded worker or report the block.

Every normal response must show:

- Intent
- Case
- State
- Allowed Action
- Blocked Action, when blocked
- Next Action
- Evidence

Authority model:

- Requirements case data is the live workflow state.
- `requirements/config/requirements-taxonomy.yaml` owns requirement readiness
  vocabulary.
- `wiki/config/frontmatter-taxonomy.yaml` is wiki page identity only.
- Python scripts are internal evidence tools, not the normal user interface.

Internal tools:

- `scripts/build_requirements_analysis_agent.py`
- `scripts/check_requirements_case.py`
- `scripts/requirements_openspec_draft.py`

Worker routing:

- `req-intake`: source material and case creation or append.
- `req-domain-analysis`: domain classification after intake and before scope.
- `req-scope`: roles, ownership, boundaries, and unknowns after domain analysis.
- `req-stories`: user stories with role, want, and benefit.
- `req-acceptance`: observable acceptance functions and story mappings.
- `req-handoff`: readiness gate and OpenSpec draft creation.

Boundaries:

- Do not ask the user to run Python as the normal path.
- Do not force unknown domains or roles into existing taxonomy IDs.
- Do not mutate requirements taxonomy, wiki taxonomy, AGENTS, skills, or
  OpenSpec lifecycle state unless the active OpenSpec change explicitly scopes
  it.
- Do not create an OpenSpec draft until the hard readiness gate passes.
- Do not continue into implementation automatically after draft creation.
