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
