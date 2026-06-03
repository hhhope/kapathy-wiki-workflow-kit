# Evaluation

## Pressure Scenarios

Positive trigger scenario:

- Input: Agent service subscription payment material with paid service access,
  recurring billing, usage/seat billing, split settlement, and real funds
  processing.
- Expected route: `req-agent` routes intake to `req-domain-analysis`, which
  emits actors plus DDD `domain_model`; `req-scope` assigns
  `role_obligations` to concrete owners or open questions.
- Expected output: `subscription_owner` may appear in
  `domain_model.role_obligations`, but it must not be treated as a source actor
  or default user-story role.

Negative scenario:

- Input: material mentions a novel term such as `carbon credit wallet`.
- Expected route: keep it as a candidate/open question.
- Expected output: do not create a formal taxonomy id and do not force it into
  an existing payment context.

## RED Baseline

- `rg -n "actors|role_obligations|domain_model|bounded_contexts|fact owner|subscription_owner|user-story actors" .codex/skills/req-domain-analysis/SKILL.md .codex/skills/req-scope/SKILL.md` -> no matches.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_analysis_agent` -> failed because analysis output had no `domain_model` or `actors`.

## GREEN Result

- `req-domain-analysis` now requires actor evidence, DDD `domain_model`, role
  obligations, and context handoffs.
- `req-scope` now assigns role obligations to concrete owners or open
  questions and keeps source actors as the user-story role starting point.
- `PYTHONPATH=. python3 -m unittest tests.test_requirements_ddd_analysis_agent tests.test_requirements_analysis_agent` -> passed, `Ran 15 tests`.

## Behavior Replay

- Input or situation shape: requirement material about Agent service
  subscription payments, including real funds processing and paid service
  access.
- Trigger condition: taxonomy v2 is active and `req-agent` routes through
  `req-domain-analysis` before scope.
- Expected route or stop behavior: domain analysis produces DDD evidence;
  scope assigns obligations; no OpenSpec draft is created until strict
  readiness passes.
- Repo-visible artifact a future agent should read:
  `.codex/skills/req-domain-analysis/SKILL.md`,
  `.codex/skills/req-scope/SKILL.md`, and this OpenSpec change.
- Expected output or non-output: `subscription_owner` appears only as a role
  obligation unless the source explicitly names it as an actor.
- Promotion or non-promotion boundary: unknown terms remain candidates and are
  not promoted into taxonomy by this workflow.
- Residual risk or proof boundary: this is local behavior and unit-test proof;
  broad multi-session behavior rollout remains follow-up evidence.

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`, relevant OpenSpec specs for skill
  authoring/evaluation, current `req-agent`, `req-domain-analysis`, and
  `req-scope` skills, plus current requirements DDD taxonomy changes.
- Owns: repo-local requirements worker guidance for DDD actor versus role
  obligation output.
- References: repo `AGENTS.md` behavior-asset gates, OpenSpec lifecycle rules,
  and the existing `req-agent` controller route.
- Rejects: copying generic DDD theory or old flat role vocabulary into skill
  hard rules.

## Residual Risks

- Heuristic DDD analysis covers the first Agent subscription payment pattern;
  broader payment cases may need additional examples.
- The current evidence does not prove Feishu-facing output quality.
