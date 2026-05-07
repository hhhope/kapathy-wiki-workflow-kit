## 1. Change Setup

- [x] 1.1 Create OpenSpec proposal, design, spec deltas, tasks, and evaluation artifacts.
  <!-- 2026-05-07 — created proposal/design/tasks/evaluation plus spec deltas for learning-capture-routing, article-learning-capture, and readme-learning-skill -->
- [x] 1.2 Record RED baseline before skill edits.
  <!-- 2026-05-07 — evaluation.md records failing baseline for runtime trigger, repo scorecard, retrospective score, topic anchoring, weekly-review candidate path, and batch triage -->

## 2. Runtime Learning Skill Updates

- [x] 2.1 Update `learning-capture` to include runtime trigger, topic anchoring, batch triage, and weekly-review candidate path.
  <!-- 2026-05-07 — SKILL.md now includes batch triage, topic anchoring, weak-match weekly-review candidates, and promotion gate preservation -->
- [x] 2.2 Update learning-capture references and pressure scenarios.
  <!-- 2026-05-07 — routing/article/repo-readme references and pressure scenarios updated -->
- [x] 2.3 Update article learning guidance to forbid retrospective scores as score-first evidence.
  <!-- 2026-05-07 — article skill and scorecard now require retrospective marking and exclude it from score-first admission evidence -->
- [x] 2.4 Add repo/README admission gate and scorecard with a 75-point deep-read threshold.
  <!-- 2026-05-07 — readme-learning-capture now has scorecard and pressure scenario references -->

## 3. Repo Entry and Wiki Explanation

- [x] 3.1 Add `learning-capture` to repo `AGENTS.md` runtime skill routing.
  <!-- 2026-05-07 — AGENTS.md High-Frequency Skills includes external-source learning trigger -->
- [x] 3.2 Keep output routing separate from runtime trigger routing.
  <!-- 2026-05-07 — AGENTS.md keeps Output Routing as destination rules, not trigger rules -->
- [x] 3.3 Update `wiki/ops/learning-capture-routing.md` with the final runtime / routing / review split.
  <!-- 2026-05-07 — wiki records runtime/review priority table, directory mapping, and non-goals -->

## 4. Evaluation

- [x] 4.1 Record GREEN pressure scenario results.
  <!-- 2026-05-07 — evaluation.md records PASS for runtime trigger, repo scorecard, retrospective score, topic anchoring, weekly review candidate path, batch triage, and output routing separation -->
- [x] 4.2 Verify OpenSpec strict validation.
  <!-- 2026-05-07 — openspec validate harden-learning-capture-runtime --strict passed; PostHog DNS noise ignored -->
- [x] 4.3 Verify skill bodies remain compact and heavy details live in references.
  <!-- 2026-05-07 — SKILL.md line counts: learning-capture 87, article-learning-capture 81, readme-learning-capture 65; scorecards and pressure scenarios live in references -->
- [x] 4.4 Record residual risks and remaining non-goals.
  <!-- 2026-05-07 — evaluation.md records static/manual proof, no weekly-review automation, historical page risk, and no directory migration -->
