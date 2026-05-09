## 1. Change Setup

- [x] 1.1 Create proposal, design, spec delta, tasks, and evaluation artifacts.
- [x] 1.2 Record RED baseline before changing skill behavior.

## 2. Skill Changes

- [x] 2.1 Update `learning-capture` to distinguish source domain from reusable capability type.
  <!-- 2026-05-08 — SKILL.md and routing/article/repo/example references now separate domain/topic from reusable capability type -->
- [x] 2.2 Update learning routing/reference docs with the output-use handoff.
  <!-- 2026-05-08 — added learning-capture/references/output-use.md and output-use fields -->
- [x] 2.3 Update `public-report-quality-gate` to require a learning use map before reference-shaped drafting or review-ready claims.
  <!-- 2026-05-08 — SKILL.md and gate-review artifact require learning use map before drafting/sync/review-ready claims -->
- [x] 2.4 Update gate-review artifact guidance and pressure scenarios.
  <!-- 2026-05-08 — added Learning Use Gate, learning-use-map reference, and pressure replay cases -->

## 3. Evaluation

- [x] 3.1 Record GREEN replay for the Account Harness Wiki scenario.
  <!-- 2026-05-08 — evaluation.md maps Account Harness / WaytoAGI / WeChat references to output uses and skip boundary -->
- [x] 3.2 Verify skill bodies remain compact and heavy detail lives in references.
  <!-- 2026-05-08 — wc -l: learning-capture 95 lines, public-report-quality-gate 70 lines -->
- [x] 3.3 Run `openspec validate connect-learning-capture-to-output-gates --strict`.
  <!-- 2026-05-08 — passed; PostHog DNS noise ignored -->
- [x] 3.4 Record residual risks and non-goals.
  <!-- 2026-05-08 — evaluation.md records manual proof, no script enforcement, no article rewrite/Feishu update -->
