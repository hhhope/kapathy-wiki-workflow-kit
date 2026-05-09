## Baseline

Before this change, the repository had several related but competing product
frames:

- `wiki/ops/report-wiki-product-plan-2026-05-09.md` described a report-wiki
  operating system and listed status, graph, query, and hot-cache gaps.
- `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md` compared against
  `Ar9av/obsidian-wiki` and identified manifest/status/query/hot-cache gaps.
- `wiki/ops/product-alignment-drift-explore-2026-05-09.md` diagnosed local
  drift between governance atoms and operating backbone.
- Office-hours design iterations briefly over-promoted
  learning-to-change orchestration as the next main product.

The missing baseline was a repo-visible contract that clearly separated LLM Wiki
core value from agent-learning enhancements.

## RED Scenario

Input shape:

```text
User says:
  LLM Wiki is my core value.
  Agent self-service learning is an enhancement.
  Treat these separately.
```

Old behavior risk:

```text
The agent treats "learning-to-change orchestration" as the north star, or jumps
to scorecards, graph UI, Feishu delivery, or task dashboards without defining
the LLM Wiki core loop first.
```

Expected new behavior:

```text
The agent first reads the LLM Wiki core product contract, preserves the
Capture/Compile/Retrieve/Apply loop, and classifies learning, scorecard,
graph/lint, and change orchestration as enhancements unless a later OpenSpec
selects them.
```

## GREEN Evidence

OpenSpec validation:

- `openspec validate define-llm-wiki-core-contract --strict` passed.
- The command printed PostHog DNS flush errors after the valid result; those are
  telemetry network noise and not validation failures.

Contract boundary readback:

- `rg` confirmed `LLM Wiki = durable compiled context for agents and humans`.
- `rg` confirmed `Capture once. Compile once. Retrieve cheaply. Apply safely.`
- `rg` confirmed the `Core Versus Enhancement` section.
- `rg` confirmed `learning-to-change orchestration is P2, not the product north star`.

Scope readback:

- Touched task files are limited to:
  - OpenSpec artifacts under `openspec/changes/define-llm-wiki-core-contract/`
  - `wiki/ops/llm-wiki-core-product-contract.md`
  - `wiki/ops/index.md`
- No manifest generator, query skill, hot-cache generator, graph UI, scorecard
  edit, Feishu sync change, or learning-to-change queue was implemented.

## Residual Risks

- This change defines product direction but does not compute source freshness,
  build query tooling, or generate a hot cache.
- The contract is not runtime enforcement until follow-up changes wire it into
  skills, status reports, or agent reading routes.
- Historical pages may still use older product language until later alignment
  changes update or supersede them.
