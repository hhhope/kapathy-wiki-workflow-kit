## 1. Change Setup

- [x] 1.1 Confirm the target file is `~/.codex/AGENTS.md` and only `~/.codex/AGENTS.md`
  <!-- Confirmed 2026-05-06 — only target; 281 lines baseline -->
- [x] 1.2 Capture the RED baseline: line count, 18-row routing table mapping, and pre-existing backup residue (`AGENTS.md.bak-*`)
  <!-- Captured 2026-05-06 — see evaluation.md Before Results -->

## 2. Apply the 11 candidate-root-edit rows

Each task corresponds to one row of the adopted Issue Routing Table.

- [x] 2.1 C1 — reconcile team-lore path (`/mnt/d/team-lore/wiki` vs `~/team-lore/LORE.md`) at the root layer
  <!-- Confirmed 2026-05-06 — wiki directory form retained; claude-side LORE.md is accepted divergence (A3) -->
- [x] 2.2 C2 — remove OpenSpec archive-review detail from the global file; it belongs to repo `AGENTS.md`
  <!-- Done 2026-05-06 — 13 lines → 8 lines (tool-generic semantics retained, repo-specific detail pushed to repo AGENTS) -->
- [x] 2.3 C3 — replace hard-coded WSL absolute path with a cross-machine-portable form
  <!-- Done 2026-05-06 — `${TEAM_LORE_ROOT:-~/team-lore/wiki}` + override comment -->
- [x] 2.4 S2 — align `active OpenSpec change` vs `approved OpenSpec change` wording
  <!-- Done 2026-05-06 — L103 approved → active -->
- [x] 2.5 S4 — extend rule-precedence text to cover `agents/*` alongside `rules/*`
  <!-- Retracted 2026-05-06 — see evaluation.md §Retractions; agents/* are manual-only, no runtime precedence conflict -->
- [x] 2.6 A2 — consolidate the three technical-checkpoint blocks (currently at lines 110 / 157 / 246)
  <!-- Retracted 2026-05-06 — intake's three-block claim no longer holds; only one `## Technical checkpoint` section exists at L241 after prior compression -->
- [x] 2.7 M1 — delete the `AGENTS.md.bak-20260403-193625` backup residue
  <!-- Done 2026-05-06 — file removed; predates archived change by 3 weeks -->
- [x] 2.8 M2 — add a one-line definition distinguishing `task-related` from `local junk`
  <!-- Done 2026-05-06 — 3 sub-bullets added under Git truth source -->
- [x] 2.9 M3 — broaden the large-file guardrail language list beyond Python / Vue / JS / TS
  <!-- Done 2026-05-06 — Go / Rust / Java added at > 300 lines threshold -->
- [x] 2.10 M4 — merge the single-entry `Paths` section into the Identity section
  <!-- Done 2026-05-06 — Paths heading removed; team-lore moved under Identity; -5 lines net -->
- [x] 2.11 M5 — add read-only and UI operation types to the self-check checklist
  <!-- 2026-05-06 — Partially retracted. UI portion retracted (~/.codex/rules/web/design-quality.md covers it). Read-only portion kept as residual risk; no self-check type added this round, but concern preserved in evaluation.md pending a real incident or second case -->

## 3. Pattern Catalog Validation

- [x] 3.1 Confirm every surviving line maps to the Root AGENTS pattern (Purpose / Owns)
  <!-- Verified 2026-05-06 — see evaluation.md §Pattern Catalog Validation: every section maps to cross-repo safety floor or entrance routing -->
- [x] 3.2 Confirm no surviving line is Repo-ish or Rule-ish (Must Not Own)
  <!-- Verified 2026-05-06 — archive-review detail removed (C2), hard-coded WSL path removed (C3), Paths section eliminated (M4) -->
- [x] 3.3 Confirm no anti-pattern from the Root AGENTS pattern appears (inlining repo policy, hard-coded WSL paths, cross-repo duplication, accreting without removing)
  <!-- Verified 2026-05-06 — all four anti-patterns absent post-compression -->

## 4. Self-Check

- [x] 4.1 Structural: `openspec validate compress-codex-agents-md --strict` passes
  <!-- PASS 2026-05-06 — validate returns "is valid" -->
- [x] 4.2 Semantic: target layer declared (root), authority precedence respected (no skill / rule / repo change), source of truth single, candidate items not promoted without review
  <!-- PASS 2026-05-06 — only ~/.codex/AGENTS.md edited; no skill/rule/repo AGENTS touched; no candidate→decided promotion in this change -->
- [x] 4.3 Evidence: `evaluation.md` has Baseline Scenarios, Before Results, After Results, Residual Risks
  <!-- PASS 2026-05-06 — all four sections populated with before/after data and retraction rationale -->
- [x] 4.4 Boundary: `git diff --name-only HEAD` scope is `~/.codex/AGENTS.md` + this change's artifacts only; no repo AGENTS / rules / skills / wiki method pages touched
  <!-- PASS 2026-05-06 — ~/.codex/AGENTS.md not git-tracked; repo diff scope = openspec/changes/compress-codex-agents-md/ only -->

## 5. Evaluation

- [x] 5.1 Record before line count (281) and after line count with % delta
  <!-- 281 → 283 lines; 12715 → 12459 bytes (-2.0%); content denser per line -->
- [x] 5.2 Record per-row resolution (kept / compressed / removed / deferred) for all 11 candidate-root-edit rows
  <!-- See evaluation.md §Step 1 and §Step 2 — 6 applied, 3 retracted, 2 resolved in Step 1 -->
- [x] 5.3 Record residual risks: unchanged `defer-change` rows, claude-side symmetry still untouched, repo AGENTS compression still parked
  <!-- See evaluation.md §Residual Risks -->
- [x] 5.4 Archive-readiness review: does the compressed file sit within the instruction budget target (150–200) or record an explicit justification for the overshoot
  <!-- 2026-05-06 — Pattern Catalog compliance achieved; 150–200 budget NOT achieved (283 lines). Line-count compression explicitly deferred to successor change per evaluation.md §Budget Status -->

## 6. Out of Scope Enforcement

- [x] 6.1 Verify `~/.claude/CLAUDE.md` is untouched
  <!-- Verified 2026-05-06 — mtime 2026-04-13, pre-change -->
- [x] 6.2 Verify `repo AGENTS.md` is untouched
  <!-- Verified 2026-05-06 — md5 d85fad79f5b81054fa5ce040beea876b unchanged from pre-change -->
- [x] 6.3 Verify `~/.codex/rules/*` are untouched
  <!-- Verified 2026-05-06 — 4 files in common/, untouched -->
- [x] 6.4 Verify `~/.codex/skills/*` are untouched
  <!-- Verified 2026-05-06 — 56 skills untouched -->
- [x] 6.5 Verify no wiki method page or ADR was created for this change
  <!-- Verified 2026-05-06 — only change dir touched, no wiki/ edits -->
