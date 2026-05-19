# Tasks

## 1. Change Setup

- [x] 1.1 Create OpenSpec proposal, design, tasks, evaluation, and spec delta artifacts.
  <!-- 2026-05-19 — created proposal/design/tasks/evaluation plus interview-deep-reading-board and public-report-quality-gate spec deltas -->
- [x] 1.2 Record RED baseline evidence for the original compression failure.
  <!-- 2026-05-19 — evaluation.md records word-cloud compression, timeline/evidence gap, dropped Coworker/Feishu/stable Agent/MCP passage, missing public-gate route, missing AGENTS route, and missing H5 reference/example -->
- [x] 1.3 Record prior-art/common-rule dedupe for `AGENTS.md`, `PROJECT.md`, relevant specs, wiki ADR/ops, existing skills, and common/global skill-authoring guidance.
  <!-- 2026-05-19 — evaluation.md records scanned assets, ownership, references, and rejected promotions -->

## 2. Skill and References

- [ ] 2.1 Add `.codex/skills/interview-deep-reading-board/SKILL.md` as an English-first repo-local module.
- [ ] 2.2 Add `.codex/skills/interview-deep-reading-board/references/h5-output-shape.md`.
- [ ] 2.3 Add `.codex/skills/interview-deep-reading-board/evaluation.md` with local pressure-test evidence.
- [ ] 2.4 Keep the main `SKILL.md` compact; move H5 details and long examples into references.

## 3. Output Gate and Repo Routing

- [ ] 3.1 Update `.codex/skills/public-report-quality-gate/SKILL.md` to delegate interview deep-reading, word-cloud, timeline, temperature-axis, and draggable-evidence H5 outputs to `interview-deep-reading-board`.
- [ ] 3.2 Update `AGENTS.md` High-Frequency Skills / Agent Intent Routing with a lightweight route to the new skill.
- [ ] 3.3 Preserve `public-report-quality-gate` as the parent gate for reader-facing H5/share/report outputs.

## 4. H5 Reference Example

- [ ] 4.1 Add `wiki/examples/interview-deep-reading-board-lixiang-luoyonghao.md`.
- [ ] 4.2 Link the validated H5, data file, source note, and old word-cloud counterexample.
- [ ] 4.3 State the copyright-safe reference boundary: short evidence plus paraphrase and source position, not full verbatim transcript storage.

## 5. Evaluation and Replay

- [ ] 5.1 Record RED baseline: interview word cloud compresses source order, hides speaker-turn logic, and drops the Coworker / Feishu / stable Agent / subagent / MCP section.
- [ ] 5.2 Record GREEN result: trigger asks the full-window reading-board fork question and requires enough source-order windows, temperature-axis evidence, and user-highlighted passage protection.
- [ ] 5.3 Record public-gate replay: reader-facing interview H5 routes through `public-report-quality-gate` before the interview module.
- [ ] 5.4 Record AGENTS route replay: interview-like source plus compression-sensitive output loads the new skill.
- [ ] 5.5 Record H5 reference replay: future agents can find the Li Xiang H5 example and distinguish the old word-cloud artifact as a counterexample.

## 6. Validation and Commit Discipline

- [ ] 6.1 Run `python3 scripts/check_behavior_assets.py`.
- [ ] 6.2 Run `rg -n 'interview-deep-reading-board|访谈|temperature|full-window|全文窗口' AGENTS.md .codex/skills openspec/changes/add-interview-deep-reading-board wiki/examples`.
- [ ] 6.3 Run `python3 -m html.parser wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html`.
- [ ] 6.4 If wiki frontmatter is added or modified, run `python3 scripts/check_wiki_frontmatter.py`.
- [ ] 6.5 Commit only task-related files after verified implementation steps; do not stage unrelated dirty worktree files.
