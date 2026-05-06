## 1. Rename / Rescope

- [x] 1.1 Rename the change away from `phase1-repo-agents-compression`.
  <!-- 2026-05-06 — renamed to govern-repo-agents-loaded-context to avoid the old Phase 1 naming collision -->
- [x] 1.2 Reframe the target from line-count compression to repo AGENTS loaded-context governance.
  <!-- 2026-05-06 — proposal/design now define map + hard stops + stable proxies -->
- [x] 1.3 Confirm Phase 1 preconditions are no longer blocked by root sequencing or commit-hook ambiguity.
  <!-- 2026-05-06 — root successor archived; ADR-0030 says repo-local commit hooks are not the default governance path -->

## 2. Planning Evidence

- [ ] 2.1 Record baseline repo `AGENTS.md` line, word, and byte counts.
- [ ] 2.2 Classify each repo `AGENTS.md` section as inline hard stop, stable proxy, delivery-sensitive inline, or deferred candidate.
- [ ] 2.3 Define proxy acceptance checks and hard-stop preservation checks.

## 3. Implementation

- [ ] 3.1 Update repo `AGENTS.md` to the accepted compressed entrypoint structure.
- [ ] 3.2 Verify every proxy points to a stable repo-visible source.
- [ ] 3.3 Verify repo-only delivery boundaries still remain explicit.

## 4. Evaluation

- [ ] 4.1 Record before/after line, word, and byte counts.
- [ ] 4.2 Record before/after proxy coverage.
- [ ] 4.3 Record agent-legibility result: where to read, how to verify, and when to stop.
- [ ] 4.4 Record residual risks after migration.
