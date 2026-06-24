# Design: Learning Workflow Matrix

## Architecture

Use:

```text
learning-capture controller
  -> references/levels.md
  -> references/learning-types.md
  -> references/research-methods.md
  -> references/evidence-strength.md
  -> references/source-queue.md
  -> references/output-contract.md
  -> references/public-writing-method.md
  -> scripts/check_learning_record.py
  -> evaluation.md pressure scenarios
```

`SKILL.md` owns trigger and routing only. Reference files own tables and detailed method contracts. Python scripts own structural checks only.

## Behavior Boundary

When a request reaches L2 or L3, the agent must state:

- learning level;
- learning type;
- required inputs;
- methods to use;
- expected outputs;
- whether the task must split.

When a claim affects behavior assets, OpenSpec specs, AGENTS guidance, public reports, H5, PPT, or Feishu-facing review output, the agent must preserve promotion boundaries instead of promoting directly from a source note.

## Checker Boundary

`scripts/check_learning_record.py` validates required fields and evidence/proof-boundary presence. It does not decide whether a business strategy, technical architecture, or market judgment is correct.

## Prior Art

The implementation references:

- repo `AGENTS.md` workflow gates;
- `openspec/specs/skill-authoring-contract/spec.md`;
- `openspec/specs/skill-evaluation-evidence/spec.md`;
- `openspec/specs/local-skill-pressure-tests/spec.md`;
- `docs/superpowers/specs/2026-06-24-learning-workflow-matrix-design.md`;
- `wiki/ops/learning-agent-architecture-patterns-2026-06-24.md`.
