# Tasks

- [x] 1. Inspect the current wiki status command/skill packaging and identify
  the actual supported invocation surface.
  <!-- 2026-05-18: README, `tests/test_wiki_status_command.py`,
  `tests/test_wiki_runtime_skills.py`, `openspec/specs/wiki-status-skill/spec.md`,
  and `.codex/skills/wiki-status/SKILL.md` confirm the current supported
  surface is the repo-local `$wiki-status` skill, not a slash command. -->
- [x] 2. Add focused replay or static validation for the desired command surface
  and the existing status-only boundary.
  <!-- 2026-05-18: Existing static tests reject `/wiki:status` in active
  runtime skill/docs surfaces and preserve status-only boundaries. -->
- [x] 3. If `/wiki:status` is supported, add or rename the command surface while
  preserving the existing status-only behavior.
  <!-- 2026-05-18: Not applied. The current repo direction supersedes slash
  command runtime and keeps repo-local skills as the active surface. -->
- [x] 4. If `/wiki:status` is not supported, record the constraint and keep the
  prefixed invocation as the supported route.
  <!-- 2026-05-18: Recorded as closed without implementation. The active
  route is `$wiki-status`; no prefixed slash command is promoted. -->
- [x] 5. Validate OpenSpec strict mode and any focused command/skill checks.
  <!-- 2026-05-18: `python3 -m unittest tests.test_wiki_status_command
  tests.test_wiki_runtime_skills -v` passed; `openspec validate --specs
  --strict` passed. -->
- [x] 6. Update the medical case evidence for `detail-0118` after the decision
  is implemented or explicitly deferred.
  <!-- 2026-05-18: Medical case updated to record this change as closed without
  implementation. -->
