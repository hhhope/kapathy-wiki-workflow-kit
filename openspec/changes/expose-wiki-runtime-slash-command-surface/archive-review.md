# Archive Review: expose-wiki-runtime-slash-command-surface

## Decision

Archive-ready.

## Scope Check

This change exposed the existing LLM Wiki runtime layers as repo-local
`/wiki:*` command files. It did not add a query engine, graph UI, score formula
change, change queue automation, or new runtime semantics.

Implemented command surface:

- `/wiki:status`
- `/wiki:manifest`
- `/wiki:inbox`
- `/wiki:graph`
- `/wiki:scorecard`
- `/wiki:route`
- `/wiki:context`
- `/wiki:apply`

## Evidence

| Check | Result |
|---|---|
| Artifacts complete | PASS — proposal, design, spec delta, and tasks are present |
| Tasks complete | PASS — `tasks.md` has 9/9 complete |
| Command files present | PASS — `commands/wiki-*.md` contains all eight command files |
| README updated | PASS — README lists the wiki runtime command surface |
| Contract tests | PASS — `python3 -m unittest tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed |
| OpenSpec validation | PASS — `openspec validate expose-wiki-runtime-slash-command-surface --strict` passed |
| Diff hygiene | PASS — `git diff --check` passed |

## Boundary Review

The command files preserve the intended proof boundary:

- they are thin wrappers over existing scripts and artifacts
- they do not create, modify, archive, or queue OpenSpec changes
- they do not mark OpenSpec tasks complete
- `/wiki:apply` summarizes bounded execution guidance but does not execute it

## Residual Risk

The command surface is still documentation-driven. The Codex slash picker was
not exercised interactively in this archive review. This is the same proof
boundary as the prior `/wiki:status` command work: repository command shape,
tests, and local artifacts are validated; interactive Codex UI discovery remains
a manual runtime check.

## Next Action

Archive this change and sync its spec delta into main specs.
