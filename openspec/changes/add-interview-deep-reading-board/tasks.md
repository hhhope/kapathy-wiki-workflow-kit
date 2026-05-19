# Tasks

## 1. Change Setup

- [x] 1.1 Create OpenSpec proposal, design, tasks, evaluation, and spec delta artifacts.
  <!-- 2026-05-19 — created proposal/design/tasks/evaluation plus interview-deep-reading-board and public-report-quality-gate spec deltas -->
- [x] 1.2 Record RED baseline evidence for the original compression failure.
  <!-- 2026-05-19 — evaluation.md records word-cloud compression, timeline/evidence gap, dropped Coworker/Feishu/stable Agent/MCP passage, missing public-gate route, missing AGENTS route, and missing H5 reference/example -->
- [x] 1.3 Record prior-art/common-rule dedupe for `AGENTS.md`, `PROJECT.md`, relevant specs, wiki ADR/ops, existing skills, and common/global skill-authoring guidance.
  <!-- 2026-05-19 — evaluation.md records scanned assets, ownership, references, and rejected promotions -->

## 2. Skill and References

- [x] 2.1 Add `.codex/skills/interview-deep-reading-board/SKILL.md` as an English-first repo-local module.
  <!-- 2026-05-19 — added compact English-first skill with Chinese-facing fork question and parent-gate boundaries -->
- [x] 2.2 Add `.codex/skills/interview-deep-reading-board/references/h5-output-shape.md`.
  <!-- 2026-05-19 — added H5 shape reference covering source windows, timeline, temperature axis, word-cloud index, evidence panel, Li Xiang reference, and copyright boundary -->
- [x] 2.3 Add `.codex/skills/interview-deep-reading-board/evaluation.md` with local pressure-test evidence.
  <!-- 2026-05-19 — added pressure scenarios, RED baseline command evidence, expected GREEN evidence, prior-art/common-rule dedupe, and residual risks -->
- [x] 2.4 Keep the main `SKILL.md` compact; move H5 details and long examples into references.
  <!-- 2026-05-19 — SKILL.md is 77 lines; H5 details live in references/h5-output-shape.md -->

## 3. Output Gate and Repo Routing

- [x] 3.1 Update `.codex/skills/public-report-quality-gate/SKILL.md` to delegate interview deep-reading, word-cloud, timeline, temperature-axis, and draggable-evidence H5 outputs to `interview-deep-reading-board`.
  <!-- 2026-05-19 — added delegation row, hard route check, and common mistake while preserving public gate ownership -->
- [x] 3.2 Update `AGENTS.md` High-Frequency Skills / Agent Intent Routing with a lightweight route to the new skill.
  <!-- 2026-05-19 — added one routing row without copying detailed interview-window rules -->
- [x] 3.3 Preserve `public-report-quality-gate` as the parent gate for reader-facing H5/share/report outputs.
  <!-- 2026-05-19 — public gate wording states the interview route does not replace reader intent, reference, visual, judgment, publish, or sync blockers -->

## 4. H5 Reference Example

- [x] 4.1 Add `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`.
  <!-- 2026-05-19 — added validated output-shape example under wiki/examples and linked it from the examples index -->
- [x] 4.2 Link the validated H5, data file, source note, and old word-cloud counterexample.
  <!-- 2026-05-19 — example links reading-board HTML, data JS, source record, and word-cloud counterexample -->
- [x] 4.3 State the copyright-safe reference boundary: short evidence plus paraphrase and source position, not full verbatim transcript storage.
  <!-- 2026-05-19 — example records the copyright boundary and avoids full transcript storage -->

## 5. Evaluation and Replay

- [x] 5.1 Record RED baseline: interview word cloud compresses source order, hides speaker-turn logic, and drops the Coworker / Feishu / stable Agent / subagent / MCP section.
  <!-- 2026-05-19 — OpenSpec and skill evaluations record the baseline failure and absence of runtime skill/route/example -->
- [x] 5.2 Record GREEN result: trigger asks the full-window reading-board fork question and requires enough source-order windows, temperature-axis evidence, and user-highlighted passage protection.
  <!-- 2026-05-19 — evaluations record implemented trigger, fork question, window/evidence structure, and named-passage protection -->
- [x] 5.3 Record public-gate replay: reader-facing interview H5 routes through `public-report-quality-gate` before the interview module.
  <!-- 2026-05-19 — OpenSpec evaluation records public gate parent route and non-replacement boundary -->
- [x] 5.4 Record AGENTS route replay: interview-like source plus compression-sensitive output loads the new skill.
  <!-- 2026-05-19 — AGENTS route and rg verification evidence recorded -->
- [x] 5.5 Record H5 reference replay: future agents can find the Li Xiang H5 example and distinguish the old word-cloud artifact as a counterexample.
  <!-- 2026-05-19 — wiki example and H5 reference record positive H5, source/data links, and word-cloud counterexample -->

## 6. Validation and Commit Discipline

- [x] 6.1 Run `python3 scripts/check_behavior_assets.py`.
  <!-- 2026-05-19 — initially failed on missing exact "Scanned:" prior-art label; after evaluation wording fix, passed -->
- [x] 6.2 Run `rg -n 'interview-deep-reading-board|访谈|temperature|full-window|全文窗口' AGENTS.md .codex/skills openspec/changes/add-interview-deep-reading-board wiki/examples`.
  <!-- 2026-05-19 — passed; route, skill, public gate, OpenSpec, and wiki example hits found -->
- [x] 6.3 Run `python3 -m html.parser wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html`.
  <!-- 2026-05-19 — passed with no parser output -->
- [x] 6.4 If wiki frontmatter is added or modified, run `python3 scripts/check_wiki_frontmatter.py`.
  <!-- 2026-05-19 — passed with no checker output; target precheck also had blocking_count 0 -->
- [x] 6.5 Commit only task-related files after verified implementation steps; do not stage unrelated dirty worktree files.
  <!-- 2026-05-19 — final validation/evaluation files staged separately from unrelated dirty worktree files -->
