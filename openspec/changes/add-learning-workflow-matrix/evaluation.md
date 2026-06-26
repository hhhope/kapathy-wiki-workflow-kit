# Evaluation: Learning Workflow Matrix

## Pressure Scenarios

| Case | Input or situation shape | Trigger condition | Expected route | Repo-visible artifact | Expected output | Promotion or non-promotion boundary | Proof boundary |
|---|---|---|---|---|---|---|---|
| positive technical OCR learning | User provides `https://github.com/alibaba/open-code-review` and asks whether it helps `cr-agent` | GitHub repo in active learning/adaptation thread | `learning-capture` -> technical L2 | `.codex/skills/learning-capture/references/learning-types.md` | Distinguish architecture/tooling learning from code-quality claims | Do not promote into CR-agent behavior without OpenSpec | Local pressure evidence only |
| positive Stripe research | User asks for Stripe company path with source queue and public H5 output | Company path, long timeline, multi-source evidence pool | `learning-capture` -> company-case L3 | `.codex/skills/learning-capture/references/source-queue.md` | Research reconstruction, evidence matrix, proof boundary, output transformation | Do not claim saturation without P0/P1 source stability | Local pressure evidence only |
| positive public writing | User asks to turn research learning into an external article/H5/PPT | Reader-facing output intent | `learning-capture` -> public writing method reference | `.codex/skills/learning-capture/references/public-writing-method.md` | Article intent, reader path, thesis, evidence placement, claim strength | Public gate remains separate | Local pressure evidence only |
| positive governance workflow | User asks whether learning workflow should change `learning-capture` or AGENTS | Behavior asset effect | `learning-capture` -> governance L2/L3 plus OpenSpec boundary | `openspec/changes/add-learning-workflow-matrix/` | Prior-art scan, promotion boundary, pressure tests | Do not edit behavior assets from conversation alone | Local pressure evidence only |
| negative should-not-trigger quick lookup | User asks latest factual answer with no local reuse intent | No learning, reuse, wiki, or method-calibration context | Do not trigger `learning-capture` | none | Answer lookup directly | No durable learning artifact | Local pressure evidence only |
| negative should-not-trigger raw fetch | User asks only to fetch raw WeChat body text | Raw extraction only | Use `weixin-reader` or source fetch path | none | Raw extracted text or fetch blocker | No learning matrix output | Local pressure evidence only |

## RED Baseline

Baseline command:

```bash
sed -n '1,140p' .codex/skills/learning-capture/SKILL.md
```

Observed baseline:

- Existing controller routes by evidence object: article, repo/README, example, or unclear source.
- Existing controller does not define L0/L1/L2/L3.
- Existing controller does not define learning type selection.
- Existing controller does not define source queue, evidence saturation, or public-writing transformation.
- Existing pressure scenarios do not cover OCR technical learning, Stripe L3 company reconstruction, public-writing transformation, or governance behavior promotion.

RED result: FAIL. The old wording cannot route the approved matrix.

## GREEN Result

Focused checks:

```bash
PYTHONPATH=. .venv-taxonomy/bin/pytest tests/test_learning_capture_consolidation.py tests/test_learning_record_checker.py -q
```

Result:

```text
7 passed in 4.51s
```

Checker fixtures:

```bash
python3 scripts/check_learning_record.py scripts/examples/learning-record-l2-valid.yaml
python3 scripts/check_learning_record.py scripts/examples/learning-record-l3-missing-proof-boundary.yaml
```

Result:

- L2 valid fixture exited `0` with no output.
- L3 missing proof-boundary fixture exited `1` and printed `missing required field: proof_boundary`.

Behavior asset gate:

```bash
python3 scripts/check_behavior_assets.py
```

Result: exited `1` only because unrelated active changes fail the existing repository gate. The failures are listed under `Residual Risks`; no `add-learning-workflow-matrix` behavior-asset error was reported.

Repo health gate:

```bash
python3 scripts/repo_health_check.py
```

Result: exited `1` because of pre-existing draft skill runtime surface failures and the same unrelated behavior-asset evaluation failures. The failures are listed under `Residual Risks`; no new failure for `add-learning-workflow-matrix` was reported.

Manual replay:

| Case | Result |
|---|---|
| positive technical OCR learning | GREEN: controller links levels, learning types, research methods, evidence strength, output contract, and distinguishes technical learning from code-quality promotion |
| positive Stripe research | GREEN: L3 level, company-case type, source queue, evidence matrix, saturation, and proof-boundary references exist |
| positive public writing | GREEN: public-writing reference exists and states learning notes are not publish-ready without citation surface |
| positive governance workflow | GREEN: OpenSpec and behavior-asset promotion boundary remains explicit |
| negative should-not-trigger quick lookup | GREEN: existing no-learning rule remains in `SKILL.md` |
| negative should-not-trigger raw fetch | GREEN: existing raw-fetch / `weixin-reader` rule remains in `SKILL.md` |

## Prior-Art / Common-Rule Dedupe

Scanned:

- repo `AGENTS.md`
- `PROJECT.md`
- `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`
- `wiki/ops/learning-agent-architecture-patterns-2026-06-24.md`
- `openspec/specs/skill-authoring-contract/spec.md`
- `openspec/specs/skill-evaluation-evidence/spec.md`
- `openspec/specs/local-skill-pressure-tests/spec.md`
- `.codex/skills/learning-capture/SKILL.md`
- `.codex/skills/learning-capture/references/pressure-scenarios.md`
- `/home/yan/.codex/skills/writing-skills/SKILL.md`
- `/home/yan/.codex/skills/test-driven-development/SKILL.md`

Owns:

- Learning-level and learning-type routing inside `learning-capture`.
- Structured L2/L3 learning output contracts.
- Source queue and proof-boundary concepts for L3 learning.

References:

- Repo workflow gates and OpenSpec lifecycle remain owned by `AGENTS.md` and OpenSpec specs.
- Skill-authoring test discipline remains owned by writing-skills and test-driven-development.
- Public report readiness remains owned by the public-report gate.

Rejects:

- Promoting conversation-only learning directly into `AGENTS.md`.
- Creating a full state machine in the first implementation.
- Treating local wiki artifacts as industry benchmark materials.

## Residual Risks

- Local pressure evidence is not multi-end rollout proof.
- The checker validates structure, not judgment correctness.
- Public citation verification remains a separate future capability.
- Parent gate preservation evidence: public report readiness remains owned by the public-report gate and is not replaced by `learning-capture`.
- Unrelated behavior-asset checker drift observed:
  - `ERROR missing_required_section openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Missing required evaluation section: ## Pressure Scenarios`
  - `ERROR missing_required_section openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Missing required evaluation section: ## RED Baseline`
  - `ERROR missing_required_section openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Missing required evaluation section: ## GREEN Result`
  - `ERROR missing_positive_scenario openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Evaluation requires a positive trigger scenario.`
  - `ERROR missing_negative_scenario openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Evaluation requires a negative or should-not-trigger scenario.`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: input or situation shape`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: trigger condition`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: expected route`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: repo-visible artifact`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: expected output`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: promotion or non-promotion boundary`
  - `ERROR weak_replay_evidence openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Replay evidence does not mention: proof boundary`
  - `ERROR missing_prior_art_dedupe openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md: Behavior-asset change requires prior-art/common-rule dedupe evidence. Missing: ## Prior-Art / Common-Rule Dedupe, Scanned:, Owns:, References:, Rejects:`
  - `ERROR missing_evaluation openspec/changes/realign-stripe-h5-redesign-sections: Behavior-asset change requires evaluation.md.`
- Unrelated repo health drift observed:
  - `FAIL draft-skill-runtime-surface` for existing `skills-drafts/account-skills/**/SKILL.md` files.
  - `FAIL skill-evaluation-evidence` for `openspec/changes/initialize-llm-wiki-seed-repo`.
  - `FAIL behavior-asset-evaluation` for `openspec/changes/initialize-llm-wiki-seed-repo` and `openspec/changes/realign-stripe-h5-redesign-sections`.
