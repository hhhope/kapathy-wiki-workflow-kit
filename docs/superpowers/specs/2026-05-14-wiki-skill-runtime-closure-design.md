# Wiki Skill Runtime Closure Design

Date: 2026-05-14

## Context

The wiki runtime surface drifted across several layers:

- `.codex/skills/wiki-status/SKILL.md` and the other repo-local wiki skills are
  the current skill sources.
- `commands/wiki-status.md` and
  `plugins/report-wiki-portfolio/commands/wiki-status.md` both describe a
  slash-style `/wiki:status` command.
- The `plugins/report-wiki-portfolio/commands/wiki-*.md` files describe a
  slash-command contract, while plugin metadata and plugin skill copies are
  absent.
- Tests still require the slash command files and require wiki skills to
  reference `plugins/report-wiki-portfolio/commands/wiki-*.md`.
- The generated page `wiki/status/wiki-status.md` is a status artifact, not a
  skill source and not a command definition.

This makes the runtime path ambiguous. Agents can read a wiki skill, then jump
to a slash-command contract that is not the active user-facing entrypoint in the
current repo-local skill surface.

## Goal

Close the wiki runtime loop around repo-local wiki skills only.

Supported user-facing skill sources are the concrete files under
`.codex/skills/`:

- `.codex/skills/wiki-status/SKILL.md`
- `.codex/skills/wiki-manifest/SKILL.md`
- `.codex/skills/wiki-inbox/SKILL.md`
- `.codex/skills/wiki-query/SKILL.md`
- `.codex/skills/wiki-explore/SKILL.md`
- `.codex/skills/wiki-graph/SKILL.md`
- `.codex/skills/wiki-scorecard/SKILL.md`
- `.codex/skills/wiki-route/SKILL.md`
- `.codex/skills/wiki-context/SKILL.md`
- `.codex/skills/wiki-apply/SKILL.md`
- `.codex/skills/wiki-queue/SKILL.md`
- `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`

The runtime should be understandable from those skill files plus the scripts
they name. It should not require opening a slash-command contract file.

## Non-Goals

- Do not restore plugin runtime.
- Do not define a general agent runtime framework.
- Do not migrate the existing whole-wiki frontmatter backlog.
- Do not treat `wiki/status/wiki-status.md` as a skill or command source.
- Do not rewrite archived OpenSpec history unless active tests or active docs
  depend on it.

## Runtime Shape

The closed loop is:

1. The user invokes a concrete repo-local wiki skill.
2. The skill itself names its scripts, artifacts, summary fields, and
   boundaries.
3. Scripts produce machine evidence under tracked wiki status files or bounded
   `/tmp` artifacts.
4. The skill summarizes the result and names the next inspection or repair
   route.
5. Repair routes use the same repo-local skill surface and scripts.
6. Completion claims require rerunning the relevant status or precheck command.

The core frontmatter repair loop is:

```text
wiki-status skill
-> python3 scripts/build_wiki_status.py
-> status shows strict frontmatter gate and scorecard
-> wiki-apply skill summarizes repair route
-> page-frontmatter-fix uses python3 scripts/wiki_gate_precheck.py --target PATH
-> target.repair_hints guides field repair
-> rerun precheck or status
```

## File Ownership

Keep:

- `.codex/skills/wiki-*/SKILL.md`
- `scripts/*.py` runtime helpers
- `wiki/status/manifest.json`
- `wiki/status/wiki-status.md`
- tests that validate repo-local wiki skills and runtime scripts

Remove from the active runtime surface:

- `commands/wiki-*.md`
- `plugins/report-wiki-portfolio/commands/wiki-*.md`

After removal, no active skill, README section, active spec, or active test
should require those command files or `/wiki:*` invocation text.

Historical references under `openspec/changes/archive/**` can remain as
history. They must not be used as current runtime truth.

## Skill Contracts

Each wiki skill should be self-contained enough for a future agent to execute
the workflow without opening a separate command contract.

Minimum fields per skill:

- purpose of the skill
- scripts to run or reference
- artifacts to read
- summary fields to report
- boundaries and forbidden actions
- next repair or inspection routes when applicable

The skills must not duplicate long generated output or taxonomy vocabulary.
They should name compact scripts and bounded artifacts instead.

## Frontmatter Gate Integration

The frontmatter taxonomy skill remains the specialized authority for wiki
frontmatter work. Routine checks use:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter
```

Targeted page repair uses:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH
```

Agents should use `target.repair_hints` before opening the full taxonomy YAML.
They should open `wiki/config/frontmatter-taxonomy.yaml` only when the repair
hints do not identify the needed rule or option.

## Status Integration

The status skill should remain the default health entrypoint. It should run or
reference:

```bash
python3 scripts/build_wiki_status.py
```

It should summarize:

- page and source counts
- inbox and OpenSpec counts
- identity and relation coverage
- graph parse health
- strict frontmatter gate result
- scorecard score and blocking count
- top frontmatter blockers when available

It must not create, modify, archive, or queue OpenSpec changes.

## Apply Integration

The apply skill remains a planning surface, not an executor. It should summarize
repair routes and explicitly distinguish:

- `page-frontmatter-fix`: bounded page frontmatter correction for explicit
  paths, using `wiki_gate_precheck.py --target`.
- `taxonomy-config-fix`: taxonomy vocabulary or scoring change; requires an
  OpenSpec change.
- `runtime-parser-fix`: parser/checker behavior change; requires an OpenSpec
  change.
- `readable-graph-fix`: graph/status readability change; requires an OpenSpec
  change.

The apply skill may recommend a route, but it must not execute queued work or
edit files by itself.

## Test Strategy

Update the active tests so they enforce the current runtime truth:

- `tests/test_wiki_runtime_skills.py` should validate that each wiki skill
  exists, has a plain `name: wiki-...`, names the scripts or artifacts it uses,
  preserves OpenSpec non-mutation boundaries, and does not reference
  `plugins/report-wiki-portfolio/commands`.
- `tests/test_wiki_runtime_commands.py` and `tests/test_wiki_status_command.py`
  should be removed or rewritten so they no longer require `/wiki:*` command
  files.
- Add a negative test that active docs and skill files do not reference
  `commands/wiki-*.md`, `plugins/report-wiki-portfolio/commands`, or `/wiki:`
  as current runtime entrypoints.
- Keep existing script tests for status, graph, scorecard, runtime context,
  frontmatter precheck, and behavior asset evaluation.

## Implementation Order

1. Create an OpenSpec change for wiki skill runtime closure.
2. Add failing tests that prove the current drift:
   slash command files exist, skills reference command contracts, and tests
   require `/wiki:*`.
3. Update wiki skill files to inline their runtime contracts.
4. Remove `commands/wiki-*.md` and
   `plugins/report-wiki-portfolio/commands/wiki-*.md`.
5. Update README and active specs to describe concrete repo-local wiki skills,
   not slash commands.
6. Update or remove command-surface tests.
7. Run focused wiki runtime, frontmatter, behavior asset, and OpenSpec checks.
8. Stop after tasks complete and perform archive review before archiving.

## Proof Boundary

This design closes the repo-local wiki skill runtime. It does not prove any
slash-style wiki entrypoint exists. It does not make wiki-apply autonomous. It
does not claim whole-wiki frontmatter compliance while the strict gate still
reports historical blockers.
