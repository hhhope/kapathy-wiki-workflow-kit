# Evaluation

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`: semantic `.codex/skills/*` changes require evaluation evidence,
  prior-art dedupe, and behavior-asset validation.
- `PROJECT.md`: OpenSpec owns lifecycle and implementation progress.
- `.codex/skills/req-agent/SKILL.md`: parent normal entry point and worker
  routing.
- `.codex/skills/req-intake/SKILL.md`: intake does not normalize domain.
- `.codex/skills/req-scope/SKILL.md`: existing scope worker currently owns
  domain, roles, ownership, boundaries, and unknowns.
- `requirements/config/requirements-taxonomy.yaml`: active requirements domain
  vocabulary.
- `openspec/changes/define-requirements-domain-standards-and-payment-skeleton`:
  active DDD domain standard and payment skeleton.
- `openspec/specs/skill-authoring-contract/spec.md`,
  `openspec/specs/skill-evaluation-evidence/spec.md`, and
  `openspec/specs/local-skill-pressure-tests/spec.md`: required skill evidence
  shape.

Owns:

- `req-domain-analysis` owns only the worker step that classifies requirement
  material against the domain standard and active taxonomy.

References:

- `req-agent` remains the parent gate and normal user-facing entry point.
- `req-scope` remains responsible for roles, ownership, boundaries, and
  unknowns after domain analysis.
- Requirements taxonomy remains the source of valid domain IDs and aliases.

Rejects:

- Moving the DDD standard into `req-scope`.
- Letting a feature name, system name, team name, or case slug become a
  top-level domain without the domain-card standard.
- Editing taxonomy directly from the worker skill.

## Pressure Scenarios

Positive trigger scenario:

- Input or situation shape: a requirements case has intake material about Agent
  subscription payments with candidates such as `subscription_payments`,
  `marketplace_settlement`, `channel`, and `billing_revenue`.
- Trigger condition: intake is complete and the next decision is domain
  classification before scope.
- Expected route: `req-agent` routes to `req-domain-analysis` before
  `req-scope`.
- Repo-visible artifact: `.codex/skills/req-agent/SKILL.md`,
  `.codex/skills/req-domain-analysis/SKILL.md`, this OpenSpec change, and
  `requirements/config/requirements-taxonomy.yaml`.
- Expected output: primary domain candidate such as `billing_revenue`,
  collaborating domain candidates, classification of feature/case/system names,
  open questions, and no readiness or implementation claim.
- Promotion or non-promotion boundary: only accepted taxonomy changes go through
  an OpenSpec change; the worker output is evidence, not taxonomy mutation.
- Proof boundary: local skill and route evidence only; multi-session runtime
  rollout is not proven.

Negative or should-not-trigger scenario:

- Input or situation shape: a user asks to create stories or acceptance
  functions for a case whose domain has already been confirmed.
- Trigger condition: no domain classification decision is pending.
- Expected route: `req-agent` routes to `req-stories` or `req-acceptance`, not
  `req-domain-analysis`.
- Repo-visible artifact: `.codex/skills/req-agent/SKILL.md` and the
  requirements case state.
- Expected output: story or acceptance work proceeds without reopening domain
  classification.
- Promotion or non-promotion boundary: the worker must not become a generic
  brainstorming step for every requirements action.
- Proof boundary: local route reasoning only.

Parent gate preservation scenario:

- Input or situation shape: user directly says to use `req-domain-analysis`
  while performing ordinary requirements intake.
- Trigger condition: no explicit debug or worker context is present.
- Expected route: preserve parent gate by using `req-agent` as the normal entry
  point.
- Repo-visible artifact: `.codex/skills/req-domain-analysis/SKILL.md` and
  `.codex/skills/req-agent/SKILL.md`.
- Expected output: normal `req-agent` response fields remain authoritative.
- Promotion or non-promotion boundary: direct worker output is evidence only and
  cannot create OpenSpec drafts or implementation authorization.
- Proof boundary: behavior-asset replay, not a live multi-agent rollout.

## RED Baseline

Observed failing behavior before implementation:

- `test -e .codex/skills/req-domain-analysis/SKILL.md; echo $?` returned `1`,
  proving the worker skill does not exist yet.
- `rg -n "req-domain-analysis|req-scope|Worker routing|domain"
  .codex/skills/req-agent/SKILL.md .codex/skills/req-intake/SKILL.md
  .codex/skills/req-scope/SKILL.md` showed `req-agent` routes domain work
  directly to `req-scope`.
- `req-intake` says it does not normalize domain, while `req-scope` currently
  combines domain, roles, ownership, boundaries, and unknowns.

Why this is the right RED case:

- It demonstrates the missing step that caused domain skeleton questions to
  collapse into scope/function discussion.
- It proves the old wording cannot express the intake -> domain analysis ->
  scope flow.

## GREEN Result

Pending until `.codex/skills/req-domain-analysis/SKILL.md`,
`.codex/skills/req-agent/SKILL.md`, and validation evidence are updated.

## Residual Risks

- The worker is a skill, so future sessions still need to load `req-agent` or
  the worker explicitly for the behavior to activate.
- This change proves local behavior-asset routing, not broad multi-end rollout.
