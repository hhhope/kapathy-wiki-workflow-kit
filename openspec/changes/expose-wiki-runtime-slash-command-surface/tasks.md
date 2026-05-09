# Tasks

## 1. Contract tests

- [ ] 1.1 Add failing command-surface tests for the expected `/wiki:*` command files.
- [ ] 1.2 Verify the tests fail before adding the new command files.

## 2. Command surface

- [ ] 2.1 Add repo-local command files for `/wiki:manifest`, `/wiki:inbox`, `/wiki:graph`, `/wiki:scorecard`, `/wiki:route`, `/wiki:context`, and `/wiki:apply`.
- [ ] 2.2 Preserve `/wiki:status` and update its boundary wording if needed.
- [ ] 2.3 Update README with the command list and usage boundaries.

## 3. Verification

- [ ] 3.1 Run targeted unittest coverage for the wiki command surface.
- [ ] 3.2 Run OpenSpec strict validation for this change.
- [ ] 3.3 Run `git diff --check` on touched files.

## 4. Stop condition

- [ ] 4.1 Stop after the slash command surface is implemented and verified; do not add query engine, graph UI, score changes, or change queue automation in this change.
