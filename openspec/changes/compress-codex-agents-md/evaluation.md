# Evaluation

## Baseline Scenarios

1. `~/.codex/AGENTS.md` has grown to 281 lines by 2026-04-25 and stayed there, while the `decide-root-governance-alignment` change accumulated one month of design work without touching the file itself.
2. A pre-existing backup residue `AGENTS.md.bak-20260403-193625` has been sitting in `~/.codex/` since 2026-04-03, outside any reviewed scope (intake finding M1).
3. The `Paths` section contains a single entry `team-lore:` and duplicates naming grammar that already belongs in `Identity` (intake finding M4).
4. Eleven of eighteen intake findings are labeled `candidate-root-edit` in the adopted Issue Routing Table and were deferred to this successor change.

## Before Results

- File: `~/.codex/AGENTS.md`, 281 lines, 12715 bytes (as of 2026-05-06 Step 1 start).
- Section headings at baseline: Identity (L6), Paths (L12), Project name (L18), Task size (L25), Pre-task health check (L37), Task start (L56), REQ identification (L85), Proceed signal (L101), OpenSpec boundary (L115), During execution (L131), Execution discipline (L161), Git discipline (L172), Task complete (L193), Long-step reporting (L207), Never (L218), Large-file guardrails (L230), Technical checkpoint (L246), Global Rule Routing (L252).
- Pre-existing backup: `~/.codex/AGENTS.md.bak-20260403-193625` (7801 bytes, 2026-04-03 19:36). Not under version control; not referenced by any active tooling; predates the archived `decide-root-governance-alignment` change by three weeks.
- Sibling file `~/.codex/AGENTS.account-team-efficiency.md` exists (4575 bytes); it is not in intake M1 scope and is not touched by this change.

## Step-by-Step Results

### Step 1 (2026-05-06): mechanical edits only

Four tasks from `tasks.md` were executed in Step 1. Each is zero-judgment.

- **1.1 Target confirmed.** Only `~/.codex/AGENTS.md`. No other file in scope.
- **1.2 RED baseline captured.** Line count 281. 18 intake findings mapped per archived Issue Routing Table. Backup residue identified.
- **2.7 M1 — backup deleted.** `~/.codex/AGENTS.md.bak-20260403-193625` removed.
- **2.10 M4 — Paths merged into Identity.** `Paths` heading removed; `team-lore:` line moved under `Identity`. Net line change: -4 (one heading, two blank lines around it, one horizontal rule absorbed).

Line count after Step 1: **276 lines** (was 281; -5 lines, -1.8%).
File size after Step 1: 12699 bytes (was 12715; -16 bytes).

### Step 2 (2026-05-06): resolved + retracted

- **2.1 C1** — team-lore path kept in `~/team-lore/wiki` directory form. Claude-side `~/team-lore/LORE.md` remains divergent under A3 (accept-as-divergence). No line change.
- **2.2 C2** — 13-line `## OpenSpec boundary` block compressed to 10 lines (heading + 8 bullets, some wrapping). Generic OpenSpec lifecycle semantics retained at root; repo-local archive-review detail pushed to each repo's AGENTS.md via an explicit pointer line. Content density increased: wordy run-on sentences ("natural next steps, automation follow-ups, refactors, helper scripts, or adjacent improvements") collapsed into short bullets.
- **2.3 C3** — L9 `team-lore:` value changed to `${TEAM_LORE_ROOT:-~/team-lore/wiki}` with an override comment. Local machine can `export TEAM_LORE_ROOT=/mnt/d/team-lore/wiki` to preserve current physical path without touching AGENTS.md.
- **2.4 S2** — L103 `approved` → `active` for wording consistency with the rest of the file.
- **2.8 M2** — three sub-bullets added under Git truth source defining `task-related` / `local junk` / tie-breaker.
- **2.9 M3** — Go / Rust / Java added at `> 300` line threshold.

### Retractions (intake findings judged to be overcalls after second review)

- **S4** — intake called for extending rule-precedence to `agents/*`. Retracted: `~/.codex/agents/*` are manual-only templates; `~/.codex/AGENTS.md` L274 already states they do not auto-trigger. No runtime precedence conflict exists. Adding them to the rules/* precedence chain would imply they auto-load, which contradicts the manual-only declaration.
- **A2** — intake called for consolidating three technical-checkpoint blocks at lines 110 / 157 / 246. Retracted: prior compression (including M4 Paths merge) has already reduced the file structure to a single `## Technical checkpoint` section (now at L241). The intake observation is stale; there is nothing left to consolidate.
- **M5** — intake called for adding `read-only` and `UI` operation types to the self-check checklist. **Partially retracted.**
  - *UI — retracted.* `~/.codex/rules/web/design-quality.md` already governs UI / visual regression; adding a UI type to the AGENTS self-check would duplicate it.
  - *Read-only — not retracted, kept as residual risk.* This change does not add a `read-only` self-check type, but the concern is not dismissed. Read-only operations can still carry side effects (log emission, cache invalidation, heartbeat, rate counter). The three-category (Write / External call / DB) split is retained for now; if a real read-only incident or a second recurring case surfaces, a successor change should reopen the M5 finding with that case as evidence. Recorded as residual risk below.

### Step 2 line count

File: 283 lines (was 276; +7). The +7 reflects structural additions (M2 definitions +3, M3 language +1, C3 comment +1, C2 net +2) offsetting a net zero compression from C2 alone. Content quality improved — wordy C2 text replaced with denser bullets — but raw line count is not the success metric for this step. Pattern Catalog compliance (Root Must Not Own: archive-review detail) is the metric: the repo-specific archive-review detail is out.

File size after Step 2: 12459 bytes (was 12715 baseline; -256 bytes, -2.0%). Lines 281 → 283 (+2), bytes 12715 → 12459 (-256) — text became denser per line.

## After Results

Final state of `~/.codex/AGENTS.md` after Step 1 + Step 2:

- Lines: 281 → 283 (+2, +0.7%)
- Bytes: 12715 → 12459 (-256, -2.0%)
- Sections: 18 → 17 (`## Paths` merged into `## Identity` per M4)
- Candidate-root-edit rows: 11 → 0 (6 applied, 3 retracted, 2 done in Step 1)

### Pattern Catalog Validation (Step 3)

Checked every surviving section against the Root AGENTS pattern:

| Section | Maps to Root pattern? | Why |
|---|---|---|
| Identity | ✓ | cross-repo entrance card (member, team-lore) |
| Project name | ✓ | cross-repo lookup convention |
| Task size | ✓ | session entry-card sizing hint |
| Pre-task health check | ✓ | hard stops before substantial work (cross-repo) |
| Task start | ✓ | cross-repo source-order routing |
| REQ identification | ✓ | cross-repo intent routing |
| Proceed signal | ✓ | cross-repo session gate |
| OpenSpec boundary | ✓ | OpenSpec tool semantics (cross-repo); archive-review *detail* pushed to repo |
| During execution | ✓ | operation-type self-check (cross-repo) |
| Execution discipline | ✓ | git/branch hard stops (cross-repo) |
| Git discipline | ✓ | git truth-source rules (cross-repo) |
| Task complete | ✓ | cross-repo task-end convention |
| Long-step reporting | ✓ | reporting discipline (cross-repo) |
| Never | ✓ | cross-repo hard stops |
| Large-file guardrails | ✓ | refactor discipline (cross-repo) |
| Technical checkpoint | ✓ | safety rule for dangerous shell content |
| Global Rule Routing | ✓ | cross-repo layer map |

No section is repo-local, personal-preference, or method-body-like after compression.

Anti-patterns checked and absent:
- inlining repo policy: removed via C2 (archive-review detail pushed to repo)
- hard-coded WSL paths: removed via C3 (`${TEAM_LORE_ROOT:-...}` form)
- cross-repo rule duplication: no section duplicates repo AGENTS
- accreting without removing: this change is net-byte-negative

### Budget Status

Instruction budget target per skyzyx/Humanlayer class B evidence is 150–200 instructions. The compressed file is 283 lines, **not within that target**.

This change achieves Pattern Catalog compliance (3 anti-patterns removed) but does not achieve the 150–200 budget. Line-count compression is explicitly deferred to a successor change to keep this change's scope confined to the 11 candidate-root-edit rows.

Known further compression vectors, not attempted here:

- Consolidate Execution discipline + Git discipline sections (potential ~10 lines).
- Extract Global Rule Routing table (~30 lines) into a separate `~/.codex/rule-routing.md` referenced from a single line in AGENTS.md.

Opening either vector inside this change would expand scope from "apply 11 routing rows" into a structural migration — a drift pattern this governance thread has repeatedly warned against. The honest position is: **Pattern Catalog compliance achieved this round; instruction-budget compliance is a separate, successor-change decision**.

## Residual Risks

- `defer-change` rows from the routing table (S1 progressive disclosure, S5 lore navigation, A5 graphify parity, Q1/Q2/Q4 open questions) are not resolved. Each opens its own change when prioritized.
- `~/.claude/CLAUDE.md` (claude-side symmetry) is intentionally untouched. Scope is deferred per the archived change's task 2.7. Claude-side `team-lore: ~/team-lore/LORE.md` remains divergent per A3.
- `phase1-repo-agents-compression` remains parked; repo AGENTS compression is not attempted in this change.
- 283 lines is above the 150–200 aspirational budget; line-count compression is explicitly deferred to a successor change (see §Budget Status).
- **M5 read-only side-effect risk is preserved, not closed.** This change retracted the UI portion of M5 (covered by `~/.codex/rules/web/design-quality.md`) but kept the read-only concern open as residual risk. A read-only operation can still emit logs, mutate cache, bump a rate counter, or reset a heartbeat — side effects that the current Write/External/DB self-check does not prompt for. No `read-only` self-check type is added in this change. Trigger for reopening M5: one real production-ish incident caused by an unanticipated read-only side effect, OR a second recurring case where the existing three categories miss the risk. Either trigger justifies a successor change; neither is present today.
- The `${TEAM_LORE_ROOT:-~/team-lore/wiki}` form requires the user to `export TEAM_LORE_ROOT=/mnt/d/team-lore/wiki` on this machine, or create a `~/team-lore/wiki` symlink. Failure to do either will make codex look for a non-existent path. An override comment at L10 documents this.
- `~/.codex/` is not under version control; if a future edit corrupts `~/.codex/AGENTS.md`, the only recovery is the Step N backup snapshots (`~/.codex/AGENTS.md.stepN-backup-20260506`). A follow-up change should consider `git init` on `~/.codex/`.
- 3 intake findings (S4 / A2 / M5) were retracted. If these were wrong retractions (the underlying concerns are real), a successor change would need to raise them again with stronger evidence than the original intake provided.

## Residual Risks

- `defer-change` rows from the routing table (S1 progressive disclosure, S5 lore navigation, A5 graphify parity, Q1/Q2/Q4 open questions) are not resolved here. Each opens its own change when prioritized.
- `~/.claude/CLAUDE.md` (claude-side symmetry) is intentionally untouched. Scope is deferred per the archived change's task 2.7.
- `phase1-repo-agents-compression` remains parked; repo AGENTS compression is not attempted in this change.
- The 150–200 instruction-budget target is aspirational; if the compressed file lands above 200 lines, the excess must be justified per root-pattern Purpose / Owns, not defended by appeal to past content.
- C3 (WSL hard-coded path) is handled in Step 2, not Step 1; until Step 2 runs, the merged `Identity.team-lore` line still carries the hard-coded `/mnt/d/team-lore/wiki` value.
