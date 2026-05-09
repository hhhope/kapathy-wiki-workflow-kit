## RED Baseline

Date: 2026-05-08

| Scenario | Current Evidence | RED Result |
|---|---|---|
| Public report gate is available as a runtime skill | `.codex/skills/public-report-quality-gate/SKILL.md` does not exist. | FAIL |
| Repo entrypoint routes reader-facing report drafts through the gate | repo `AGENTS.md` High-Frequency Skills does not list `public-report-quality-gate`. | FAIL |
| Voice gate blocks chat-like public drafts | `wiki/language-policy.md` governs zh/en mixing, but no current report gate blocks chat residue, slogan simplification, loose narrator, or internal ops leakage. | FAIL |
| Reference-driven drafts must map the reference structure before writing | Current learning/example guidance preserves reference source and reuse boundaries, but no public-report gate requires a reference structure map before output. | FAIL |
| Multi-part report groups must split before Feishu review drafts | Current report template has no split gate for overview/runtime/migration/validation/roadmap groups. | FAIL |
| Core narrative drift blocks publish readiness | No current gate would fail the `lore -> team-lore -> wiki` story being rewritten as a static responsibility table. | FAIL |
| Feishu review drafts produce repo-visible process evidence | The first GREEN implementation required gate checks but did not require a stable `wiki/ops/*-report-gate-review.md` artifact before Feishu sync. | FAIL |

## GREEN Result

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Public report gate is available as a runtime skill | `.codex/skills/public-report-quality-gate/SKILL.md` exists with trigger-only description, hard rules, references, and common mistakes. | PASS |
| Repo entrypoint routes reader-facing report drafts through the gate | repo `AGENTS.md` High-Frequency Skills lists `.codex/skills/public-report-quality-gate/SKILL.md` for reader-facing reports, Feishu review drafts, H5/share drafts, public materials, and reference-shaped outputs. | PASS |
| Voice gate blocks chat-like public drafts | `references/scorecard.md` defines Voice Gate as a hard gate and lists chat residue, slogan simplification, loose narrator, weak section openings, internal ops leakage, and tone mismatch as fail conditions. | PASS |
| Reference-driven drafts must map the reference structure before writing | `SKILL.md` requires a reference structure map when a reference artifact is provided; `report-group-templates.md` defines the required map fields. | PASS |
| Multi-part report groups must split before Feishu review drafts | `scorecard.md` and `report-group-templates.md` require split strategy for overview/runtime/migration/validation/roadmap-shaped material. | PASS |
| Core narrative drift blocks publish readiness | `scorecard.md` defines Narrative Gate as a hard gate; `pressure-scenarios.md` replays the `lore -> team-lore -> wiki` failure as expected FAIL until rewritten as an evolution path. | PASS |
| Feishu sync waits for quality gates | `SKILL.md` and `scorecard.md` block publish/sync/review-ready claims when hard gates fail. | PASS |
| Feishu review drafts produce repo-visible process evidence | `SKILL.md` requires a `wiki/ops/*-report-gate-review.md` artifact before Feishu sync or review-ready claims; `gate-review-artifact.md` defines required sections and update/read-back evidence; pressure scenarios fail chat-only or `/tmp`-only scoring. | PASS |

## Residual Risks

- Pressure evidence is static/manual, not multi-session rollout proof.
- The skill gates reader-facing output quality; it does not prove source
  correctness, visual rendering quality, or Feishu API success by itself.
- Existing historical reports may still be below the new quality gate until
  reviewed separately.
- No manual reviewer agent template is added in this change; the skill is the
  runtime trigger surface.
- The gate-review artifact contract is still manual; no script currently checks
  section completeness.

## Regression RED Baseline: Reference Readback Gap

Date: 2026-05-08

| Scenario | Evidence | RED Result |
|---|---|---|
| Reference wiki node has child pages, but the gate allows scoring before linked-page readback | `wiki/ops/team-knowledge-base-overview-report-gate-review.md` recorded `92 / 100` before reading the linked runtime, install/migration, validation, and roadmap articles. | FAIL |
| Reference entry page has essential visuals, but missing local visuals are treated as residual risk | The same gate review recorded `Visual Gate: PASS with residual risk` even though the reference entry uses actual visuals before key tables. | FAIL |
| Hard gate failure still receives a numeric score | The same gate review later had to mark the `92 / 100` score `INVALID` after Reference Structure Gate was corrected to FAIL. | FAIL |

## Regression GREEN Result: Reference Readback Gap

| Scenario | GREEN Evidence | Result |
|---|---|---|
| Linked reference pages must be read before Reference Structure Gate passes | `SKILL.md`, `scorecard.md`, `report-group-templates.md`, and `spec.md` now require linked-page readback when a reference has child pages or concrete reading-map links. | PASS |
| Missing essential visuals block reference-shaped review readiness | `SKILL.md`, `scorecard.md`, `pressure-scenarios.md`, and `spec.md` now make missing corresponding visual assets or a concrete visual plan a Visual Gate failure. | PASS |
| Hard gate failure cannot receive a numeric score | `SKILL.md`, `scorecard.md`, `gate-review-artifact.md`, `pressure-scenarios.md`, and `spec.md` now require `INVALID` scorecard when any hard gate is failed, partial, unknown, or not tested. | PASS |
| Workflow no longer drafts before reference mapping | `gate-review-artifact.md` now orders the stable workflow as gate-review artifact, reference map/readback, split strategy, then draft. | PASS |
