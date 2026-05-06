## 1. Reframe the Change

- [x] 1.1 Replace single-file line-count success language with progressive
  context governance language.
- [x] 1.2 Record why moving text to another file does not count as reduction if
  the moved file is still loaded on the default path.
- [x] 1.3 Confirm repo dirty tree unrelated files stay excluded from this
  change's commits.
  <!-- 2026-05-06 — unrelated report, IDE, inbox, Claude, and nested-path local files left unstaged -->

## 2. Harness Engineering Gate

- [x] 2.1 Add the RED scenario: move `Global Rule Routing` to
  `rule-routing.md`, then require non-trivial work to load it by default.
- [x] 2.2 Mark the RED scenario's expected result as FAIL because loaded context
  is not reduced for the dominant path.
- [x] 2.3 Define GREEN behavior: root keeps only always-on hard stops and
  routing principles; details load only after a concrete trigger.
- [x] 2.4 Record default loaded context and triggered loaded context as required
  evidence.
- [x] 2.5 Record the external article calibration as local target criteria:
  root `AGENTS.md` as map, stable source-of-record pointers, reviewable harness
  assumptions, and recovery artifacts.
  <!-- 2026-05-06 — captured in design.md §Progressive Context Strategy, evaluation.md §External Article Calibration, and wiki/ops/behavior-asset-governance-zh.md §Harness Engineering 学到什么 -->
- [x] 2.6 Record the evidence standard for adopted best practices: external
  documentation excerpt, local demo/fixture, or git-like project comparison.
  <!-- 2026-05-06 — captured in design.md §Require Evidence-Backed Best Practices, evaluation.md §Evidence Standard for Best Practices, and spec scenario Root context governance adopts external best practices -->

## 3. Root Context Implementation

- [ ] 3.1 Confirm target files before any root edit: `~/.codex/AGENTS.md` plus
  at most one trigger-gated root-local support file under `~/.codex/`.
- [ ] 3.2 Consolidate `Execution discipline` and `Git discipline` only if it
  preserves dirty-tree, commit, branch, resume, push, and truth-source behavior.
- [ ] 3.3 Do not extract routing detail into a default-loaded support file.
- [ ] 3.4 Keep deferred routing-table rows out of scope.

## 4. Validation

- [ ] 4.1 Record before/after line, word, and byte counts as supporting
  evidence.
- [ ] 4.2 Record before/after default loaded context.
- [ ] 4.3 Record before/after triggered loaded context.
- [ ] 4.4 Confirm no repo `AGENTS.md`, repo `.codex/skills/`, repo `wiki/`,
  repo `rules/`, or `~/.claude/CLAUDE.md` file was edited by root
  implementation.
- [ ] 4.5 Confirm the next agent can identify where to read, how to verify, and
  which artifact preserves recovery after interruption.
- [ ] 4.6 Confirm every adopted best practice has quantifiable or reproducible
  evidence, or is explicitly marked candidate-only.
- [x] 4.7 Run `openspec validate compress-root-agents-budget --strict`.
  <!-- PASS 2026-05-06 — validate returned "Change 'compress-root-agents-budget' is valid"; PostHog DNS noise only -->

## 5. Self-Check

- [x] 5.1 Structural: OpenSpec artifacts exist and validate.
- [x] 5.2 Semantic: target layer remains Root AGENTS; support files are
  trigger-gated references, not a new governance layer.
- [ ] 5.3 Evidence: loaded-context metrics, before/after counts, RED/GREEN,
  agent-legibility check, best-practice evidence table, and residual risks are
  recorded.
- [x] 5.4 Boundary: no new Pattern Catalog pattern, checklist item, skill, wiki
  method page, or repo policy is introduced.
