## 1. Change Setup

- [x] 1.1 Create OpenSpec proposal, design, spec delta, tasks, and evaluation artifacts.
  <!-- 2026-05-08 — created proposal/design/tasks/evaluation plus spec delta for public-report-quality-gate -->
- [x] 1.2 Record RED baseline before adding the skill.
  <!-- 2026-05-08 — evaluation.md records missing skill, missing AGENTS route, missing voice/reference/split/narrative gates -->

## 2. Skill and References

- [x] 2.1 Add `.codex/skills/public-report-quality-gate/SKILL.md`.
  <!-- 2026-05-08 — added compact skill body with triggers, hard rules, load pointers, and common mistakes -->
- [x] 2.2 Add scorecard reference with hard gates and 80-point pass threshold.
  <!-- 2026-05-08 — scorecard.md defines six hard gates, voice gate detail, 100-point rubric, and threshold bands -->
- [x] 2.3 Add template routing reference for overview/runtime/migration/validation/roadmap-style report groups.
  <!-- 2026-05-08 — report-group-templates.md defines reference map, split routing, four-page group pattern, optional roadmap, and public skeleton -->
- [x] 2.4 Add pressure scenarios covering triggers, non-triggers, and the failed knowledge-base draft pattern.
  <!-- 2026-05-08 — pressure-scenarios.md covers should-trigger, should-not-trigger, and failed knowledge-base replay -->
- [x] 2.5 Add gate-review artifact contract for stable process evidence.
  <!-- 2026-05-08 — gate-review-artifact.md requires wiki/ops/*-report-gate-review.md before Feishu sync or review-ready claims -->

## 3. Repo Routing

- [x] 3.1 Add `public-report-quality-gate` to repo `AGENTS.md` high-frequency skill routing.
  <!-- 2026-05-08 — AGENTS.md now routes reader-facing reports / Feishu review drafts / H5-share drafts through the skill -->
- [x] 3.2 Keep the skill positioned as a reader-facing output gate, not a source-reading or Feishu API replacement.
  <!-- 2026-05-08 — SKILL.md hard rules preserve source, learning, visual, Feishu, and verification skills under their own boundaries -->

## 4. Evaluation

- [x] 4.1 Record GREEN pressure scenario results.
  <!-- 2026-05-08 — evaluation.md records PASS for runtime skill, AGENTS route, voice/reference/split/narrative/publish gates -->
- [x] 4.2 Verify OpenSpec strict validation.
  <!-- 2026-05-08 — openspec validate add-public-report-quality-gate --strict passed; PostHog DNS noise ignored -->
- [x] 4.3 Verify skill body remains compact and long details live in references.
  <!-- 2026-05-08 — SKILL.md 52 lines; scorecard/template/pressure details live in references -->
- [x] 4.4 Record residual risks and non-goals.
  <!-- 2026-05-08 — evaluation.md records static/manual proof, no source/visual/Feishu proof, historical report risk, and no reviewer-agent template -->
- [x] 4.5 Record archive-blocking replay correction for stable process artifacts.
  <!-- 2026-05-08 — evaluation.md adds RED/GREEN for missing gate-review artifact stability; pressure scenarios now fail chat-only or /tmp-only scoring -->
- [x] 4.6 Patch reference-readback scoring regression.
  <!-- 2026-05-08 — linked reference pages are now required before Reference Structure Gate PASS; missing essential visuals fail Visual Gate; hard gate FAIL/PARTIAL/UNKNOWN/NOT TESTED forces scorecard INVALID -->
