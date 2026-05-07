## 1. Setup

- [x] 1.1 Create proposal, design, tasks, evaluation, and spec deltas.
  <!-- 2026-05-07 — created OpenSpec artifacts plus deltas for principle-skills-layer and repo-agents-loaded-context -->
- [x] 1.2 Record RED baseline for the ownership gap.
  <!-- 2026-05-07 — evaluation.md records missing ownership-status classification in repo High-Frequency Skills -->

## 2. Durable Records

- [x] 2.1 Add wiki retro describing the gap root cause.
  <!-- 2026-05-07 — added wiki/ops/root-capability-extraction-retro.md -->
- [x] 2.2 Add ADR for root-capability extraction boundary.
  <!-- 2026-05-07 — added wiki/adr/0031-root-capability-extraction-boundary.md -->
- [x] 2.3 Update ADR index.
  <!-- 2026-05-07 — linked ADR-0031 from wiki/adr/index.md -->

## 3. Spec and Runtime Map

- [x] 3.1 Update `principle-skills-layer` spec with ownership-status classification.
  <!-- 2026-05-07 — spec delta requires repo guidance to declare repo-owned/root-candidate/root-owned-reference/shared -->
- [x] 3.2 Update `repo-agents-loaded-context` spec so runtime maps do not imply ownership.
  <!-- 2026-05-07 — spec delta requires runtime skill routes to state routing does not imply ownership -->
- [x] 3.3 Update repo `AGENTS.md` High-Frequency Skills to include ownership status.
  <!-- 2026-05-07 — AGENTS.md table now has Ownership column for repo-owned/shared/root-candidate rows -->

## 4. Evaluation

- [x] 4.1 Record GREEN replay results.
  <!-- 2026-05-07 — evaluation.md records PASS for ownership column, root-candidate labels, repo-owned labels, shared skills, ADR gate, and retro evidence -->
- [x] 4.2 Run `openspec validate decide-root-capability-extraction-boundary --strict`.
  <!-- 2026-05-07 — strict validation passed; PostHog DNS flush noise ignored -->
- [x] 4.3 Confirm no root dotfiles or skill bodies were edited.
  <!-- 2026-05-07 — task diff touches repo AGENTS, OpenSpec change artifacts, ADR/index, and wiki ops; no ~/.codex, ~/.claude, or .codex/skills body edits -->
- [x] 4.4 Record residual risks.
  <!-- 2026-05-07 — evaluation.md records documentation-level proof, no root runtime change, and physical repo skill location as residual risks -->
