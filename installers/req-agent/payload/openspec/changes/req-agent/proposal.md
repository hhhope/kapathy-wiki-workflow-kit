# req-agent

## Why

The requirements analysis work already added taxonomy, case data, checker, and
OpenSpec draft helpers, but normal Codex usage still drifts toward raw Python
commands or one oversized skill entry. That repeats the failure the user
identified: the workflow is not a single "requirements-analysis-agent" wrapper.

The intended model is closer to `wiki-medical-agent`: a short Codex-facing
controller owns intent, case, state, allowed action, blocked action, and next
action; bounded workers own one lifecycle slice; Python scripts remain internal
evidence and validation tools.

## What Changes

- Add `req-agent` as the single normal Codex-facing requirements controller.
- Add five bounded worker skills:
  - `req-intake`
  - `req-scope`
  - `req-stories`
  - `req-acceptance`
  - `req-handoff`
- Treat `req-handoff` as the readiness gate plus OpenSpec draft handoff.
- Preserve existing Python helpers as internal evidence collectors and gates,
  not normal user entry points.
- Replace the narrower uncommitted
  `add-requirements-analysis-agent-skill-entry` direction with this lifecycle
  split.

## Out of Scope

- Changing requirements taxonomy vocabulary.
- Adding new readiness hard-gate fields beyond the existing confirmed domain,
  roles, user stories, acceptance functions, and story/acceptance mapping.
- Implementing generated OpenSpec drafts.
- Archiving `add-requirements-analysis-agent`.
- Building full natural-language extraction beyond the bounded skill routing
  and existing deterministic scripts.

## Prior Art

- `wiki-medical-agent` normal-entry pattern.
- `wiki/ops/requirements-agent-skill-isolation-explore-2026-05-29.md`.
- `openspec/changes/add-requirements-analysis-agent`.
- `requirements/config/requirements-taxonomy.yaml`.
