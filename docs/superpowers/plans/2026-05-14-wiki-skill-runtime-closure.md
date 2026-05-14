# Wiki Skill Runtime Closure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the repo-local wiki runtime around `.codex/skills/wiki-*` and remove the active slash command contract surface.

**Architecture:** OpenSpec owns the change boundary. `.codex/skills/wiki-*` become self-contained runtime contracts that name scripts, artifacts, summary fields, and boundaries directly. Slash command files under `commands/` and `plugins/report-wiki-portfolio/commands/` are removed from the active runtime, while generated status artifacts and archived historical OpenSpec records remain.

**Tech Stack:** Markdown behavior assets, OpenSpec change artifacts, Python unittest tests, repo-local Python runtime scripts.

---

## File Structure

- Create: `openspec/changes/close-wiki-skill-runtime-loop/proposal.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/design.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/tasks.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/evaluation.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/specs/wiki-runtime-skill-surface/spec.md`
- Modify: `.codex/skills/wiki-status/SKILL.md`
- Modify: `.codex/skills/wiki-manifest/SKILL.md`
- Modify: `.codex/skills/wiki-inbox/SKILL.md`
- Modify: `.codex/skills/wiki-query/SKILL.md`
- Modify: `.codex/skills/wiki-explore/SKILL.md`
- Modify: `.codex/skills/wiki-graph/SKILL.md`
- Modify: `.codex/skills/wiki-scorecard/SKILL.md`
- Modify: `.codex/skills/wiki-route/SKILL.md`
- Modify: `.codex/skills/wiki-context/SKILL.md`
- Modify: `.codex/skills/wiki-apply/SKILL.md`
- Modify: `.codex/skills/wiki-queue/SKILL.md`
- Keep: `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`
- Modify: `README.md`
- Modify: `openspec/specs/wiki-runtime-slash-command-surface/spec.md`
- Modify: `openspec/specs/wiki-status-slash-command/spec.md`
- Modify: `tests/test_wiki_runtime_skills.py`
- Modify: `tests/test_wiki_status_command.py`
- Delete: `tests/test_wiki_runtime_commands.py`
- Delete: `commands/wiki-apply.md`
- Delete: `commands/wiki-context.md`
- Delete: `commands/wiki-graph.md`
- Delete: `commands/wiki-inbox.md`
- Delete: `commands/wiki-manifest.md`
- Delete: `commands/wiki-query.md`
- Delete: `commands/wiki-queue.md`
- Delete: `commands/wiki-route.md`
- Delete: `commands/wiki-scorecard.md`
- Delete: `commands/wiki-status.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-apply.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-context.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-explore.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-graph.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-inbox.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-manifest.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-query.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-queue.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-route.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-scorecard.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-status.md`

## Parallel Work Slices

- Slice A, skills: update `.codex/skills/wiki-*` to be self-contained and remove command contract references.
- Slice B, docs/specs/tests: update README, active specs, and tests to enforce skill runtime truth.
- Slice C, removal: delete active slash command files and ensure no active docs or tests require them.

These slices can run in parallel after Task 2 RED tests exist. Slice owners must not edit each other's files.

### Task 1: OpenSpec Boundary

**Files:**
- Create: `openspec/changes/close-wiki-skill-runtime-loop/proposal.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/design.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/tasks.md`
- Create: `openspec/changes/close-wiki-skill-runtime-loop/specs/wiki-runtime-skill-surface/spec.md`

- [ ] **Step 1: Create proposal**

Add `openspec/changes/close-wiki-skill-runtime-loop/proposal.md`:

```markdown
# Proposal

## Why

The active wiki runtime surface is split between repo-local skills and slash
command contract files. The current runtime should be closed around
`.codex/skills/wiki-*` so future agents can execute wiki workflows without
following stale `/wiki:*` command documents.

## What Changes

- Make repo-local `.codex/skills/wiki-*` files self-contained runtime contracts.
- Remove active slash command contract files under `commands/` and
  `plugins/report-wiki-portfolio/commands/`.
- Update README, active specs, and tests so the current runtime truth is the
  repo-local skill surface.
- Preserve generated status artifacts and archived historical OpenSpec records.

## Out of Scope

- Restoring plugin runtime.
- Defining a general agent runtime framework.
- Migrating historical frontmatter backlog.
- Editing archived OpenSpec history unless a current test imports it.
```

- [ ] **Step 2: Create design**

Add `openspec/changes/close-wiki-skill-runtime-loop/design.md`:

```markdown
# Design

## Source Of Truth

The current wiki runtime source of truth is `.codex/skills/wiki-*`.
Slash-style files under `commands/` and `plugins/report-wiki-portfolio/commands/`
are removed from active runtime ownership.

## Skill Contract Shape

Each wiki skill owns:

- trigger/purpose
- scripts to run or reference
- artifacts to read
- summary fields to report
- boundaries
- next repair or inspection route

Skills must not reference `plugins/report-wiki-portfolio/commands`.
Skills must not use `/wiki:` invocation text as current runtime guidance.

## Frontmatter Repair Loop

`wiki-status` surfaces strict frontmatter gate data from
`scripts/build_wiki_status.py`. `wiki-apply` routes explicit page frontmatter
fixes to `scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`.
`wiki-frontmatter-taxonomy` remains the specialized frontmatter authority.

## Historical Boundary

Archived OpenSpec records may still mention `/wiki:*`; they are historical
evidence and not current runtime truth.
```

- [ ] **Step 3: Create tasks ledger**

Add `openspec/changes/close-wiki-skill-runtime-loop/tasks.md`:

```markdown
# Tasks

- [ ] 1. Add RED tests for skill-runtime ownership and slash command removal.
- [ ] 2. Update wiki skill files to inline runtime contracts and remove command contract references.
- [ ] 3. Remove active slash command contract files.
- [ ] 4. Update README and active specs to describe repo-local skill runtime only.
- [ ] 5. Record behavior-asset evaluation evidence.
- [ ] 6. Run focused wiki runtime, frontmatter, behavior asset, and OpenSpec checks.
```

- [ ] **Step 4: Create spec delta**

Add `openspec/changes/close-wiki-skill-runtime-loop/specs/wiki-runtime-skill-surface/spec.md`:

```markdown
## Purpose

Define the current repo-local wiki runtime as a self-contained skill surface.

## ADDED Requirements

### Requirement: Wiki runtime SHALL be owned by repo-local skills

The current wiki runtime SHALL be discoverable and executable from
`.codex/skills/wiki-*` without opening slash command contract files.

#### Scenario: Agent reads a wiki skill

- **WHEN** an agent opens `.codex/skills/wiki-status/SKILL.md` or another
  repo-local wiki skill
- **THEN** the skill SHALL name the scripts, artifacts, summary fields, and
  boundaries needed to execute that runtime surface
- **AND** it SHALL NOT require `plugins/report-wiki-portfolio/commands`.

### Requirement: Active slash command contracts SHALL be removed

The repository SHALL remove active slash command contract files from
`commands/` and `plugins/report-wiki-portfolio/commands/`.

#### Scenario: Current runtime files are inspected

- **WHEN** active runtime docs, skills, and tests are inspected
- **THEN** they SHALL NOT present `/wiki:*` as a current executable entrypoint
- **AND** archived OpenSpec records MAY retain historical references.

### Requirement: Wiki apply SHALL route frontmatter repair through precheck hints

The wiki apply skill SHALL describe page frontmatter repair as a bounded route
through the compact frontmatter precheck.

#### Scenario: Page frontmatter repair is needed

- **WHEN** a page path is explicit
- **THEN** the repair route SHALL use
  `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`
- **AND** agents SHALL use `target.repair_hints` before opening full taxonomy
  configuration.
```

- [ ] **Step 5: Validate change shell**

Run:

```bash
openspec validate close-wiki-skill-runtime-loop --strict
```

Expected: validation passes. PostHog telemetry DNS errors after validation do not invalidate the OpenSpec result.

- [ ] **Step 6: Commit OpenSpec boundary**

Run:

```bash
git add openspec/changes/close-wiki-skill-runtime-loop
git commit -m "spec: propose wiki skill runtime closure"
```

### Task 2: RED Runtime Ownership Tests

**Files:**
- Modify: `tests/test_wiki_runtime_skills.py`
- Modify: `tests/test_wiki_status_command.py`
- Delete: `tests/test_wiki_runtime_commands.py`

- [ ] **Step 1: Rewrite runtime skill expectations**

Replace `WIKI_SKILLS` in `tests/test_wiki_runtime_skills.py` with script/artifact requirements:

```python
WIKI_SKILLS = {
    "wiki-status": ("scripts/build_wiki_status.py", "wiki/status/wiki-status.md"),
    "wiki-manifest": ("scripts/build_wiki_status.py", "wiki/status/manifest.json"),
    "wiki-inbox": ("scripts/build_wiki_status.py", "inbox/"),
    "wiki-query": (
        "scripts/build_wiki_status.py",
        "scripts/derive_runtime_auto_routing.py",
        "scripts/build_runtime_context_injection.py",
        "rg -n",
    ),
    "wiki-explore": ("wiki-query", "Evidence surface", "Enoughness judgment"),
    "wiki-graph": (
        "scripts/extract_wiki_graph.py",
        "scripts/analyze_wiki_relations.py",
        "scripts/summarize_wiki_graph.py",
    ),
    "wiki-scorecard": (
        "scripts/score_wiki_semantics.py",
        "scripts/derive_wiki_utilization.py",
        "scripts/summarize_wiki_scorecard.py",
    ),
    "wiki-route": (
        "scripts/resolve_runtime_context_sources.py",
        "scripts/derive_runtime_auto_routing.py",
    ),
    "wiki-context": (
        "scripts/build_wiki_runtime_context.py",
        "scripts/build_runtime_context_injection.py",
    ),
    "wiki-apply": (
        "scripts/build_runtime_context_injection.py",
        "scripts/derive_self_directed_execution.py",
        "scripts/wiki_gate_precheck.py",
        "page-frontmatter-fix",
    ),
    "wiki-queue": ("scripts/build_wiki_change_queue_preview.py",),
}
```

- [ ] **Step 2: Assert skill self-contained runtime contracts**

In `test_wiki_runtime_skill_sources_exist_with_plain_wiki_names`, replace the
command path assertion with:

```python
for marker in command_path:
    self.assertIn(marker, content)
self.assertNotIn("Command contract:", content)
self.assertNotIn("plugins/report-wiki-portfolio/commands", content)
self.assertNotIn("/wiki:", content)
```

Use the variable name `required_markers` instead of `command_path`.

- [ ] **Step 3: Add active doc negative test**

Add this test to `tests/test_wiki_runtime_skills.py`:

```python
def test_active_runtime_docs_do_not_reference_slash_command_surface(self) -> None:
    active_paths = [
        Path("README.md"),
        Path("openspec/specs/wiki-runtime-slash-command-surface/spec.md"),
        Path("openspec/specs/wiki-status-slash-command/spec.md"),
    ]
    active_paths.extend(sorted(Path(".codex/skills").glob("wiki-*/SKILL.md")))
    for path in active_paths:
        with self.subTest(path=path.as_posix()):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("plugins/report-wiki-portfolio/commands", text)
            self.assertNotIn("commands/wiki-", text)
            self.assertNotIn("/wiki:", text)
```

- [ ] **Step 4: Rewrite status command test to status skill test**

Replace `tests/test_wiki_status_command.py` with:

```python
import unittest
from pathlib import Path


class WikiStatusSkillTest(unittest.TestCase):
    def test_wiki_status_skill_is_self_contained(self) -> None:
        skill_path = Path(".codex/skills/wiki-status/SKILL.md")

        self.assertTrue(skill_path.exists())
        skill = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: wiki-status", skill)
        self.assertIn("python3 scripts/build_wiki_status.py", skill)
        self.assertIn("wiki/status/manifest.json", skill)
        self.assertIn("wiki/status/wiki-status.md", skill)
        self.assertIn("strict frontmatter gate", skill)
        self.assertIn("Do not mark OpenSpec tasks complete", skill)
        self.assertNotIn("Command contract:", skill)
        self.assertNotIn("/wiki:status", skill)
        self.assertNotIn("plugins/report-wiki-portfolio/commands", skill)

    def test_no_claude_only_wiki_status_command_remains(self) -> None:
        self.assertFalse(Path(".claude/commands/wiki/status.md").exists())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 5: Remove slash command test file**

Run:

```bash
git rm tests/test_wiki_runtime_commands.py
```

- [ ] **Step 6: Run RED tests**

Run:

```bash
python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command
```

Expected: fail because skills still reference `Command contract:` and slash command files still exist.

- [ ] **Step 7: Commit RED tests**

Run:

```bash
git add tests/test_wiki_runtime_skills.py tests/test_wiki_status_command.py
git add -u tests/test_wiki_runtime_commands.py
git commit -m "test: require wiki skill runtime closure"
```

### Task 3: Inline Wiki Skill Runtime Contracts

**Files:**
- Modify: `.codex/skills/wiki-status/SKILL.md`
- Modify: `.codex/skills/wiki-manifest/SKILL.md`
- Modify: `.codex/skills/wiki-inbox/SKILL.md`
- Modify: `.codex/skills/wiki-query/SKILL.md`
- Modify: `.codex/skills/wiki-explore/SKILL.md`
- Modify: `.codex/skills/wiki-graph/SKILL.md`
- Modify: `.codex/skills/wiki-scorecard/SKILL.md`
- Modify: `.codex/skills/wiki-route/SKILL.md`
- Modify: `.codex/skills/wiki-context/SKILL.md`
- Modify: `.codex/skills/wiki-apply/SKILL.md`
- Modify: `.codex/skills/wiki-queue/SKILL.md`

- [ ] **Step 1: Update wiki-status skill**

Replace the body after frontmatter in `.codex/skills/wiki-status/SKILL.md` with:

```markdown
Use the wiki status runtime surface for the report wiki repository.

When triggered:

1. Confirm the current repository has `scripts/build_wiki_status.py`.
2. Run or reference `python3 scripts/build_wiki_status.py`.
3. Read `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.
4. Summarize page and source counts, inbox and OpenSpec counts, identity and
   relation coverage, graph parse health, strict frontmatter gate status,
   scorecard score, blocking count, and top blockers when present.
5. Name next inspection routes such as `wiki-graph`, `wiki-scorecard`,
   `wiki-apply`, or `wiki-frontmatter-taxonomy` when the status shows drift.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not implement a query engine, graph UI, scorecard, or change queue from
  this skill.
```

- [ ] **Step 2: Update wiki-manifest skill**

Replace command-contract lines with:

```markdown
When triggered:

1. Confirm the current repository has `scripts/build_wiki_status.py`.
2. Run or reference `python3 scripts/build_wiki_status.py`.
3. Read `wiki/status/manifest.json`.
4. Summarize manifest counts, source coverage, stale inputs, route pressure,
   missing generated artifacts, and proof boundaries.
```

- [ ] **Step 3: Update wiki-inbox skill**

Replace command-contract lines with:

```markdown
When triggered:

1. Confirm the current repository has `inbox/` or `wiki/status/manifest.json`.
2. Run or reference `python3 scripts/build_wiki_status.py` when status needs
   refreshing.
3. Read `wiki/status/manifest.json`, `wiki/status/wiki-status.md`, and relevant
   `inbox/` filenames.
4. Summarize pending intake items and route them as candidate work only.
```

- [ ] **Step 4: Update wiki-query skill**

Replace command-contract lines with:

```markdown
When triggered:

1. Confirm the current repository has wiki runtime scripts and `wiki/`.
2. Run or reference `python3 scripts/build_wiki_status.py`,
   `python3 scripts/derive_runtime_auto_routing.py`, and
   `python3 scripts/build_runtime_context_injection.py` as needed.
3. Use explicit `rg -n` text search for the user's query terms.
4. Read `wiki/status/manifest.json`, `wiki/status/wiki-status.md`,
   `/tmp/wiki-runtime-auto-routing.json`, `/tmp/wiki-context-injection.json`,
   and explicit text matches when available.
5. Summarize bounded context using `open_first`, `open_next`, `do_not_anchor`,
   explicit matches, caution notes, and proof boundaries.
```

- [ ] **Step 5: Update wiki-explore skill**

Delete the `Command contract:` line. Keep the existing depth-gate content.
Ensure the body still contains `wiki-query`, `Evidence surface`, and
`Enoughness judgment`.

- [ ] **Step 6: Update graph, scorecard, route, context, and queue skills**

Remove `Command contract:` and `Follow the command contract when present.` from:

```text
.codex/skills/wiki-graph/SKILL.md
.codex/skills/wiki-scorecard/SKILL.md
.codex/skills/wiki-route/SKILL.md
.codex/skills/wiki-context/SKILL.md
.codex/skills/wiki-queue/SKILL.md
```

Keep their existing script lists and boundaries.

- [ ] **Step 7: Update wiki-apply skill**

Replace the `When triggered:` block in `.codex/skills/wiki-apply/SKILL.md` with:

```markdown
When triggered:

1. Confirm the current repository has `scripts/derive_self_directed_execution.py`.
2. Run or reference `python3 scripts/build_runtime_context_injection.py` and
   `python3 scripts/derive_self_directed_execution.py`.
3. Read self-directed execution JSON when available.
4. Summarize `execute_now`, `defer_for_followup`, and `do_not_execute` as
   suggestions only.
5. For explicit page frontmatter repairs, route to
   `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target PATH`
   and use `target.repair_hints` before opening full taxonomy config.
6. Distinguish `page-frontmatter-fix`, `taxonomy-config-fix`,
   `runtime-parser-fix`, and `readable-graph-fix`; only page-frontmatter-fix
   can be bounded to an explicit page without a new runtime behavior change.
```

- [ ] **Step 8: Run GREEN skill tests**

Run:

```bash
python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command
```

Expected: remaining failures only from docs/specs or command files, not from skill command-contract references.

- [ ] **Step 9: Commit skill closure**

Run:

```bash
git add .codex/skills/wiki-status/SKILL.md .codex/skills/wiki-manifest/SKILL.md .codex/skills/wiki-inbox/SKILL.md .codex/skills/wiki-query/SKILL.md .codex/skills/wiki-explore/SKILL.md .codex/skills/wiki-graph/SKILL.md .codex/skills/wiki-scorecard/SKILL.md .codex/skills/wiki-route/SKILL.md .codex/skills/wiki-context/SKILL.md .codex/skills/wiki-apply/SKILL.md .codex/skills/wiki-queue/SKILL.md
git commit -m "feat: inline wiki skill runtime contracts"
```

### Task 4: Remove Slash Command Contract Files

**Files:**
- Delete: `commands/wiki-*.md`
- Delete: `plugins/report-wiki-portfolio/commands/wiki-*.md`

- [ ] **Step 1: Remove command files**

Run:

```bash
git rm commands/wiki-apply.md commands/wiki-context.md commands/wiki-graph.md commands/wiki-inbox.md commands/wiki-manifest.md commands/wiki-query.md commands/wiki-queue.md commands/wiki-route.md commands/wiki-scorecard.md commands/wiki-status.md
git rm plugins/report-wiki-portfolio/commands/wiki-apply.md plugins/report-wiki-portfolio/commands/wiki-context.md plugins/report-wiki-portfolio/commands/wiki-explore.md plugins/report-wiki-portfolio/commands/wiki-graph.md plugins/report-wiki-portfolio/commands/wiki-inbox.md plugins/report-wiki-portfolio/commands/wiki-manifest.md plugins/report-wiki-portfolio/commands/wiki-query.md plugins/report-wiki-portfolio/commands/wiki-queue.md plugins/report-wiki-portfolio/commands/wiki-route.md plugins/report-wiki-portfolio/commands/wiki-scorecard.md plugins/report-wiki-portfolio/commands/wiki-status.md
```

- [ ] **Step 2: Verify no active command files remain**

Run:

```bash
find commands plugins/report-wiki-portfolio/commands -maxdepth 1 -type f 2>/dev/null | sort
```

Expected: no output. Empty directories may remain if Git ignores them.

- [ ] **Step 3: Commit removal**

Run:

```bash
git add -u commands plugins/report-wiki-portfolio/commands
git commit -m "chore: remove wiki slash command contracts"
```

### Task 5: README And Active Spec Cleanup

**Files:**
- Modify: `README.md`
- Modify: `openspec/specs/wiki-runtime-slash-command-surface/spec.md`
- Modify: `openspec/specs/wiki-status-slash-command/spec.md`

- [ ] **Step 1: Update README skill section**

In `README.md`, keep the `## Codex Skills` section but ensure it says:

```markdown
Use repo-local skills under `.codex/skills/`. Do not install this repo's
`wiki-*` or `openspec-*` skills into root/user scope; duplicate registrations
can surface obsolete namespaces.

The current wiki runtime is the repo-local skill surface. Do not document or
invoke `/wiki:*` as the active runtime entrypoint.
```

Keep the concrete `$wiki-status`, `$wiki-query`, and other `$wiki-...` entries.
Do not add wildcard command examples.

- [ ] **Step 2: Rename active runtime spec purpose text**

In `openspec/specs/wiki-runtime-slash-command-surface/spec.md`, change the title
and purpose to skill runtime wording:

```markdown
# wiki-runtime-skill-surface Specification

## Purpose

Define the current repo-local wiki skill runtime surface and keep obsolete
slash command contracts out of active runtime documentation.
```

Replace active `/wiki:*` requirements with requirements that `.codex/skills/wiki-*`
exist, are self-contained, and do not reference command contract files. Keep
requirements about not duplicating user/root skill installs and not publishing
plugin marketplace metadata.

- [ ] **Step 3: Rename active status spec wording**

In `openspec/specs/wiki-status-slash-command/spec.md`, change title and
requirements from slash command language to skill language:

```markdown
# wiki-status-skill Specification

## Purpose

Define the repo-local `wiki-status` skill as the current status entrypoint.
```

Ensure the spec requires `.codex/skills/wiki-status/SKILL.md`, `python3 scripts/build_wiki_status.py`, `wiki/status/manifest.json`, and `wiki/status/wiki-status.md`.
Ensure it does not mention `/wiki:status`.

- [ ] **Step 4: Run active reference scan**

Run:

```bash
rg -n "plugins/report-wiki-portfolio/commands|commands/wiki-|/wiki:" README.md .codex/skills tests openspec/specs
```

Expected: no output.

- [ ] **Step 5: Commit docs/spec cleanup**

Run:

```bash
git add README.md openspec/specs/wiki-runtime-slash-command-surface/spec.md openspec/specs/wiki-status-slash-command/spec.md
git commit -m "docs: document wiki skill runtime surface"
```

### Task 6: Evaluation And Final Verification

**Files:**
- Create: `openspec/changes/close-wiki-skill-runtime-loop/evaluation.md`
- Modify: `openspec/changes/close-wiki-skill-runtime-loop/tasks.md`

- [ ] **Step 1: Add evaluation evidence**

Create `openspec/changes/close-wiki-skill-runtime-loop/evaluation.md`:

```markdown
# Evaluation

## Pressure Scenarios

1. Positive trigger scenario: an agent opens `wiki-status` and can execute the
   status runtime without opening a slash command contract file.
2. Positive trigger scenario: `wiki-apply` can route explicit page frontmatter
   repair to `wiki_gate_precheck.py --target PATH` and `target.repair_hints`.
3. Negative should-not-trigger scenario: active docs and skills must not present
   `/wiki:*` as the current runtime entrypoint.
4. Negative should-not-trigger scenario: archived OpenSpec history can retain
   historical slash references and should not be rewritten.

## Behavior Replay

- Input or situation shape: a user invokes a repo-local wiki skill such as
  `wiki-status`, `wiki-query`, or `wiki-apply`.
- Trigger condition: the task is a wiki runtime inspection or bounded repair
  route, not plugin installation and not general agent runtime work.
- Expected route: open `.codex/skills/wiki-*/SKILL.md`, run the scripts named
  there, read bounded artifacts, and summarize within the skill boundary.
- Repo-visible artifact: `.codex/skills/wiki-*`, README, active OpenSpec specs,
  and this OpenSpec change.
- Expected output: status, query, graph, scorecard, route, context, apply, or
  queue summaries grounded in named script artifacts.
- Promotion or non-promotion boundary: plugin/slash runtime is not promoted by
  this change; archived slash references remain historical only.
- Proof boundary: this proves repo-local skill runtime closure, not plugin
  slash command availability or autonomous execution.

## RED Baseline

Before implementation:

- Wiki skills referenced `plugins/report-wiki-portfolio/commands/wiki-*.md`.
- Active tests required `/wiki:*` command files.
- `commands/wiki-*.md` and `plugins/report-wiki-portfolio/commands/wiki-*.md`
  existed as active slash command contracts.

## GREEN Result

After implementation:

- Wiki skills are self-contained runtime contracts.
- Active slash command contract files are removed.
- README and active specs describe repo-local wiki skills as current runtime.
- Tests enforce no active `/wiki:` or command-contract references.

## Verification

- `python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_wiki_frontmatter_taxonomy_skill tests.test_wiki_gate_precheck`
- `python3 -m unittest tests.test_wiki_status tests.test_wiki_graph_summary tests.test_wiki_scorecard_summary tests.test_wiki_queue_preview`
- `python3 scripts/check_behavior_assets.py`
- `openspec validate close-wiki-skill-runtime-loop --strict`

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`, README, `.codex/skills/wiki-*`,
  active `openspec/specs`, previous runtime command archive changes, and the
  wiki skill runtime closure design.
- Owns: current repo-local wiki skill runtime surface and active docs/tests.
- References: historical archive records remain historical evidence.
- Rejects: restoring plugin runtime, generic agent runtime, slash command
  contracts as current runtime truth, and migrating historical frontmatter debt.

## Residual Risks

- The current skill invocation display may vary by host UI, but the repo-local
  source of truth is `.codex/skills/wiki-*`.
- Whole-wiki frontmatter still fails until historical pages are migrated.
```

- [ ] **Step 2: Mark tasks complete after verification**

Only after all verification commands pass or expected failures are documented,
update `openspec/changes/close-wiki-skill-runtime-loop/tasks.md` to mark all
tasks complete.

- [ ] **Step 3: Run focused tests**

Run:

```bash
python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_wiki_frontmatter_taxonomy_skill tests.test_wiki_gate_precheck
python3 -m unittest tests.test_wiki_status tests.test_wiki_graph_summary tests.test_wiki_scorecard_summary tests.test_wiki_queue_preview
```

Expected: all tests pass.

- [ ] **Step 4: Run active reference scan**

Run:

```bash
rg -n "plugins/report-wiki-portfolio/commands|commands/wiki-|/wiki:" README.md .codex/skills tests openspec/specs
```

Expected: no output.

- [ ] **Step 5: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: exit code 0.

- [ ] **Step 6: Validate OpenSpec**

Run:

```bash
openspec validate close-wiki-skill-runtime-loop --strict
```

Expected: validation passes. PostHog telemetry DNS errors after validation do not invalidate the OpenSpec result.

- [ ] **Step 7: Commit final verification**

Run:

```bash
git add openspec/changes/close-wiki-skill-runtime-loop/evaluation.md openspec/changes/close-wiki-skill-runtime-loop/tasks.md
git commit -m "test: verify wiki skill runtime closure"
```

## Execution Notes

- Use subagent-driven execution because the user requested parallel work.
- Suggested parallel assignment after Task 2:
  - Worker A owns `.codex/skills/wiki-*`.
  - Worker B owns README and active specs.
  - Worker C owns slash command file deletion and test updates.
- Workers are not alone in the codebase. They must not revert unrelated dirty
  files and must not edit outside their assigned write set.
- Do not touch `openspec/changes/archive/**` unless a current test directly
  imports an archived file.
- Stop implementation when all OpenSpec tasks are complete. The next action is
  archive review, not automatic archive.
