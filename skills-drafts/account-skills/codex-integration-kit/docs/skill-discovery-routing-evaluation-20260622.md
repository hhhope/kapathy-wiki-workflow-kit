# Skill Discovery Routing Evaluation - 2026-06-22

## Scope

This pass covers package-level skill discovery wording that could train future
agents to route by fixed phrases instead of intent, scope, and artifact shape.

It follows the writing-skills rule that semantic skill edits need pressure
evidence. This is fixture/manual evidence for package text, not live rollout
proof.

## Pressure Scenarios

- A user uses casual wording for a visual artifact. Expected: route through
  `visual-agent`, then choose the proper visual worker; do not jump to
  `frontend-visual-governor` unless the target is an existing UI surface.
- A user asks for an existing dashboard/page/chart visual polish. Expected:
  `visual-agent` remains the controller and routes to
  `frontend-visual-governor` as a child worker.
- A user asks for API inventory, detailed design, exception handling, Apifox
  docs, API tests, or agent-task collaboration using non-canonical wording.
  Expected: descriptions match intent and work shape, not quoted trigger words.
- A future maintainer reads the README skill template. Expected: it teaches
  `Use when...` intent/symptom descriptions, not fixed keyword trigger tables.

## RED Baseline

Before this pass, several top-level skills used discovery wording shaped like
"when the user mentions these words". That made phrase matching look like the
normal routing mechanism and conflicted with the visual-agent contract, where
casual language must generalize by visual-deliverable intent.

Old visual companion references also pointed Feishu writing flows at a removed
Xiaohongshu-style worker, which could bypass the packaged `visual-agent`
controller.

## GREEN Result

- `visual-agent` is the visual controller.
- `frontend-visual-governor` is explicitly a child worker for existing
  frontend/UI repair only.
- Top-level skill descriptions that previously taught fixed phrase matching now
  use `Use when...` wording with intent, artifact, symptom, and exclusion
  boundaries.
- Visual worker internals avoid keyword-trigger language where the wording could
  be mistaken for routing. They use structure, scene, and semantic signals.
- Feishu writing visual companions route through `visual-agent` and the bundled
  visual workers.

## Evidence

- Strict discovery scan over `skills`, `account-cr-agent/skills`,
  `codex-integration-kit`, and `README.md` returns no matches for fixed-phrase
  discovery wording or the removed Xiaohongshu-style worker name.
- Remaining broad `触发条件` / `关键词` hits are business-condition fields,
  checkpoint-matching docs, templates, or visual label/content guidance rather
  than top-level skill discovery rules.
- `git diff --check` passes.

## Residual Risks

This does not prove live runtime selection in every installed environment.
Installed copies outside this branch must be updated before the behavior can be
assumed in those environments.
