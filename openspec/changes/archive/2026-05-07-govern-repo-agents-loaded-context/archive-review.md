## Archive Review: Structure Effectiveness Replay

Date: 2026-05-07

## Scope

This review checks whether the compressed repo `AGENTS.md` structure is
operationally effective. It does not introduce new rules and does not evaluate
unrelated dirty worktree files.

## Fresh Checks

- `wc -l -w -c AGENTS.md`: 215 lines / 1609 words / 14908 bytes.
- Baseline from `git show 9ac130f:AGENTS.md | wc -l -w -c`: 510 lines /
  3430 words / 23578 bytes.
- Unique explicit repo-visible proxy references in current `AGENTS.md`: 68.
- Missing proxy references: 0.
- `openspec validate govern-repo-agents-loaded-context --strict`: valid.
- `openspec list`: `govern-repo-agents-loaded-context` is complete.

## Post-Successor Fresh Check

After the successor change `harden-learning-capture-runtime` archived, repo
`AGENTS.md` gained one high-frequency skill row for `learning-capture`. The
loaded-context structure remains valid, but the raw size metric changed.

- `wc -l -w -c AGENTS.md`: 216 lines / 1626 words / 15055 bytes.
- Baseline from `git show 9ac130f:AGENTS.md | wc -l -w -c`: 510 lines /
  3430 words / 23578 bytes.
- The new `learning-capture` row is a runtime trigger correction, not a return
  to inline method expansion.
- `openspec validate govern-repo-agents-loaded-context --strict`: valid.

## Replay Matrix

| # | Trigger scenario | Expected decision from compressed `AGENTS.md` | Evidence | Result |
|---|---|---|---|---|
| 1 | User asks to change default repo behavior | Require active OpenSpec before editing guidance files. | `AGENTS.md` lines 20-30 | PASS |
| 2 | User asks to continue after all active-change tasks are checked | Stop implementation; default next action is archive review. | `AGENTS.md` line 63 | PASS |
| 3 | `$openspec-explore` is used | Create or update a lightweight `wiki/ops` trace before exploration continues; load the explore skill. | `AGENTS.md` lines 66 and 84 | PASS |
| 4 | Live conversation drifts from the last confirmed requirement | Stop continuation and re-anchor; update `wiki/ops` retro unless resolved in the active change. | `AGENTS.md` lines 67 and 152-159 | PASS |
| 5 | External article, README, repo, or in-chat example looks useful | Capture learning only with evidence; route extracted learning, not raw link presence. | `AGENTS.md` lines 68 and 126-139 | PASS |
| 6 | Semantic edit to `.codex/skills/*` | Require evaluation evidence and writing/TDD skill guidance; preserve delivery boundaries for sensitive skills. | `AGENTS.md` lines 69 and 91-112 | PASS |
| 7 | Material or meeting-note delivery work | Keep readable/review output and final-publication boundaries inline. | `AGENTS.md` lines 70-71 and 181-215 | PASS |
| 8 | Agent needs full wiki runtime details | Do not rely on repeated inline prose; follow the `Wiki Runtime Stack` source table. | `AGENTS.md` lines 161-179 | PASS |
| 9 | Public-facing repo artifact is the active target | Route README/docs/examples/templates to that target repo; keep this wiki for internal learning and evidence. | `AGENTS.md` lines 116-124 | PASS |

## Metrics

- Structural replay pass rate: 9 / 9 = 100%.
- Proxy existence hit rate: 68 / 68 = 100%.
- Baseline section coverage: 26 / 26 original sections mapped into retained
  inline sections, stable proxies, or delivery-sensitive inline sections.
- Direct stop visibility: all tested stop conditions were visible in
  `AGENTS.md` without opening a proxy.
- Post-successor size remains within the loaded-context target: 216 lines after
  the learning-capture trigger row, down from the 510-line baseline.

## Judgment

The current structure is effective as a loaded-context entrypoint. It preserves
the stop conditions and routing decisions needed for the next agent to decide
where to read, how to verify, and when to stop.

## Residual Risk

This is a replay-based structure test, not a multi-session production rollout.
The remaining risk is behavioral adoption: future agents must actually follow
the proxy links when they need details instead of treating the compact table as
the full method.

## Archive Readiness

PASS. No blocker found for archive review.
