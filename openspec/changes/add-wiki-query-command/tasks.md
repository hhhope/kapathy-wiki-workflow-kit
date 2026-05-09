# Tasks

## 1. Contract tests

- [ ] 1.1 Add failing command contract coverage for `/wiki:query`.
- [ ] 1.2 Verify the test fails before adding the command.

## 2. Command and docs

- [ ] 2.1 Add `commands/wiki-query.md`.
- [ ] 2.2 Update README command list with `/wiki:query`.
- [ ] 2.3 Ensure `/wiki:query` states proof boundaries and OpenSpec non-mutation boundaries.

## 3. Verification

- [ ] 3.1 Run targeted unittest coverage.
- [ ] 3.2 Run OpenSpec strict validation.
- [ ] 3.3 Run `git diff --check` on touched files.

## 4. Stop condition

- [ ] 4.1 Stop after the bounded query command is implemented; do not add vector search, embeddings, graph UI, or change queue automation in this change.
