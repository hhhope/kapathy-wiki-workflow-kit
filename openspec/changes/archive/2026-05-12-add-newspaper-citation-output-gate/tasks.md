## 1. Change Setup

- [x] 1.1 Create proposal, design, tasks, and spec delta artifacts.
- [x] 1.2 Validate the OpenSpec change strictly.
  <!-- 2026-05-12 — `openspec validate add-newspaper-citation-output-gate --strict` passed; PostHog DNS noise ignored. -->

## 2. Skill And Reference Updates

- [x] 2.1 Update `public-report-quality-gate` with the Newspaper Citation Surface Gate.
  <!-- 2026-05-12 — SKILL.md now requires reader-visible citation surface for newspaper-style H5/share packages and public newspaper drafts. -->
- [x] 2.2 Update public-report gate references with citation surface fields and pressure scenarios.
  <!-- 2026-05-12 — gate-review artifact now includes Newspaper Citation Surface; pressure scenarios include the current newspaper replay. -->
- [x] 2.3 Update learning output-use guidance to distinguish internal learning use from reader-visible citations.
  <!-- 2026-05-12 — output-use guidance now states internal learning maps do not replace newspaper reader-visible citations. -->

## 3. Evaluation

- [x] 3.1 Record RED baseline using the current newspaper artifact: source map exists, but review-ready newspaper citation surface is not guaranteed.
  <!-- 2026-05-12 — evaluation.md records missing old citation-surface rule and current newspaper replay gap. -->
- [x] 3.2 Record GREEN replay showing the gate blocks review-ready claims unless a citation surface or skip boundary exists.
  <!-- 2026-05-12 — pressure scenarios and evaluation.md record expected gate behavior. -->
- [x] 3.3 Run `openspec validate add-newspaper-citation-output-gate --strict`.
  <!-- 2026-05-12 — passed after skill/reference changes; PostHog DNS noise ignored. -->
- [x] 3.4 Record residual risks and non-goals.
  <!-- 2026-05-12 — evaluation.md records manual guidance boundary, current-newspaper scope, and editorial citation judgment. -->
