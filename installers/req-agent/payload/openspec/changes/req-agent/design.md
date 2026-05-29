# Design

## Controller Shape

`req-agent` is the only normal user-facing entry. It classifies live user
intent, resolves or creates the requirements case, reads current state, and
routes to exactly one bounded next action.

Every normal `req-agent` response must include:

- Intent
- Case
- State
- Allowed Action
- Blocked Action, when blocked
- Next Action
- Evidence

## Skill Surface

The first implementation uses six repo-local skills:

```text
req-agent
req-intake
req-scope
req-stories
req-acceptance
req-handoff
```

`req-agent` is the controller. The other five skills are bounded workers and
must not present themselves as normal entry points.

## Worker Boundaries

`req-intake` accepts source material, records provenance, and creates or appends
to a requirements case. It does not decide readiness.

`req-scope` normalizes domain, roles, ownership, boundaries, and unknowns. It
uses `requirements/config/requirements-taxonomy.yaml` as requirements
vocabulary. Unknown domains or roles remain candidates until confirmed.

`req-stories` extracts and checks user stories, including role, want, and
benefit. It does not write acceptance conclusions.

`req-acceptance` extracts observable acceptance functions and maintains
bidirectional user-story mappings.

`req-handoff` runs the hard readiness gate and creates an OpenSpec draft only
after readiness passes. Draft creation is a stop condition; implementation
requires separate user review and approval.

## Authority

Requirements case data and `requirements/config/requirements-taxonomy.yaml` own
requirements readiness. `wiki/config/frontmatter-taxonomy.yaml` remains wiki
page-identity metadata only.

Existing Python scripts remain internal tools:

- `scripts/build_requirements_analysis_agent.py`
- `scripts/check_requirements_case.py`
- `scripts/requirements_openspec_draft.py`

Codex may run them to collect evidence, but ordinary user guidance should route
through `req-agent`, not ask the user to run Python directly.

## Superseded Direction

The uncommitted `add-requirements-analysis-agent-skill-entry` change is too
narrow because it adds one entry skill around existing scripts. This change
replaces that direction with a controller-plus-workers lifecycle design.

## Behavior Evidence

Because this changes repo-local skill behavior, implementation must include:

- baseline failure evidence for the old no-skill or single-entry behavior;
- after-change replay for controller routing, worker non-entry boundaries,
  readiness blocking, and post-handoff stop behavior;
- prior-art/common-rule dedupe evidence;
- behavior-asset checker output.
