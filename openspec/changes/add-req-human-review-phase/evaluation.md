# Evaluation

## Pressure Scenarios

| Scenario | Expected Result |
| --- | --- |
| Positive: A requirements case has a Human Review document that adds scenario gaps but does not update user stories. | `req-human-review` treats story/acceptance additions as demand facts and requires machine case synchronization before handoff. |
| Positive: A user asks for a readable requirements review after acceptance extraction. | `req-agent` routes to `req-human-review`, not directly to `req-handoff` and not to a standalone normal entry skill. |
| Negative / should-not-trigger: Human Review includes a question that is only a reviewer prompt. | The prompt remains classified as `review_prompt` and does not modify machine case facts. |
| Negative / should-not-trigger: A user tries to invoke `req-human-review` as a normal entry point. | The parent gate is preserved: ordinary use routes through `req-agent`; direct worker use is debug/evidence only. |
| Human Review identifies missing current-state material, business rule table, or system boundary contract. | The missing input is classified as `design_gate_gap`; detailed design remains blocked while requirement review may still be ready. |

## RED Baseline

The Baofu legal SMS case showed the old behavior failure:

- Human Review scenario matrices were added first.
- New boundary facts appeared in the human-readable document.
- User stories and acceptance mappings were not updated until the user asked,
  "用户故事没增加？"

This is a valid RED baseline because the existing route lacked a bounded
Human Review worker, fixed template, and synchronization gate.

## GREEN Result

After this change, the expected route is:

- `req-agent` keeps normal entry control.
- `req-human-review` produces the Human Review artifact from the machine case
  and source evidence.
- Demand facts in the review must be synchronized into the machine case before
  `req-handoff`.
- The Human Review template includes user stories, scenario coverage,
  acceptance scope, gap classification, detailed-design gates, and
  synchronization proof.

## Behavior Replay

- Input or situation shape: a requirements case has structured stories and
  acceptance functions, plus a Human Review document or a user request for
  readable requirement review.
- Trigger condition: user asks for Human Review, or an existing Human Review
  artifact contains possible demand facts before handoff.
- Expected route: `req-agent` routes to `req-human-review` after
  `req-acceptance` and before `req-handoff`.
- Repo-visible artifact: `.codex/skills/req-human-review/SKILL.md`,
  `.codex/skills/req-agent/SKILL.md`, `.codex/skills/req-handoff/SKILL.md`,
  and `wiki/templates/requirements-human-review-template.md`.
- Expected output: Human Review includes source coverage, domain judgment,
  user stories, scenario matrix, rule/status matrix, acceptance scope, gap
  classification, detailed-design gates, and synchronization proof.
- Promotion or non-promotion boundary: `demand_fact` entries are promoted to
  the machine case; `review_prompt` remains review-only; `design_gate_gap`
  blocks detailed design but does not replace requirement readiness.
- Proof boundary: this change proves repo-local routing text, template shape,
  and manual synchronization evidence; it does not prove automatic parsing of
  Human Review files.

## Parent Gate Preservation

The parent gate is preserved because `req-agent` remains the only normal
Codex-facing requirements entry. `req-human-review` follows the existing worker
pattern: ordinary use routes through `req-agent`, and direct use is only for
explicit debug or worker context.

## Prior-Art / Common-Rule Dedupe

Scanned:

- repo `AGENTS.md`
- repo `PROJECT.md`
- `.codex/skills/req-agent/SKILL.md`
- `.codex/skills/req-handoff/SKILL.md`
- `.codex/skills/req-stories/SKILL.md`
- `.codex/skills/req-acceptance/SKILL.md`
- `openspec/changes/req-agent`
- `openspec/changes/add-req-domain-analysis-skill`
- `openspec/changes/enforce-req-agent-design-hard-gates`
- `openspec/specs/skill-authoring-contract/spec.md`
- `openspec/specs/skill-evaluation-evidence/spec.md`
- `openspec/specs/local-skill-pressure-tests/spec.md`
- `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md`

Owns:

- `req-human-review` as a bounded requirements worker phase.
- Human Review template shape.
- Human Review synchronization gate before `req-handoff`.

References:

- `req-agent` normal entry and controller ownership.
- Existing worker non-entry pattern.
- Existing detailed-design hard gates and requirements checker.
- Repo skill authoring and behavior-asset evaluation gates.

Rejects:

- A standalone normal-entry Human Review skill.
- Making Human Review a second source of truth.
- Restating generic skill-authoring, git, testing, or behavior-asset rules in
  the new worker body.

## Residual Risks

- First release relies on manual synchronization proof, not full automatic
  parsing of Human Review documents.
- Existing Human Review documents may need manual normalization if used as
  future examples.
- `req-human-review` can still be misused if invoked directly without explicit
  worker/debug context; the skill description follows the existing worker
  non-entry pattern to reduce that risk.

## Verification Evidence

- `rg -n "req-human-review|Human Review|demand_fact|requirements-human-review-template|req-acceptance|req-handoff" ...`:
  confirmed route, worker, handoff gate, template, and OpenSpec change coverage.
- `PYTHONPATH=. python3 scripts/check_requirements_case.py wiki/ops/requirements-cases/2026-06-09-015054-baofu-multi-channel-legal-sms-verification.md --format markdown`:
  `requirements_ready`, hard gate passed, detailed-design gate still false.
- `openspec validate add-req-human-review-phase --strict`: valid. PostHog
  telemetry flush emitted DNS errors after validation; validation exit code was
  0.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/templates/requirements-human-review-template.md`:
  non-zero due to existing repo-wide README/MANIFEST frontmatter drift; target
  entry_count was 0 and no target-specific entry errors were reported.
- `python3 scripts/check_behavior_assets.py`: non-zero only for existing
  `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md` drift after
  this change's evaluation was corrected.
