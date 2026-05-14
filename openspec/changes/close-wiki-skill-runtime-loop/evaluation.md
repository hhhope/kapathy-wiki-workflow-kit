# Evaluation

## Pressure Scenarios

1. Positive trigger scenario: an agent opens `wiki-status` and can execute the
   status runtime without opening a slash command contract file.
2. Positive trigger scenario: `wiki-apply` can route explicit page frontmatter
   repair to `wiki_gate_precheck.py --target PATH` and `target.repair_hints`.
3. Negative should-not-trigger scenario: active docs and skills must not present
   the old wiki slash namespace as the current runtime entrypoint.
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

- Wiki skills referenced old plugin command contract paths.
- Active tests required wiki slash command files.
- Active slash command contracts existed under `commands/` and under the
  report-wiki-portfolio plugin command directory.
- `python3 scripts/check_behavior_assets.py` reported
  `missing_evaluation` before this file existed.

## GREEN Result

After implementation:

- Wiki skills are self-contained runtime contracts.
- Active slash command contract files are removed.
- README and active specs describe repo-local wiki skills as current runtime.
- Tests enforce no active wiki slash namespace or command-contract references.

## Verification

- `python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command tests.test_wiki_frontmatter_taxonomy_skill tests.test_wiki_gate_precheck`
- `python3 -m unittest tests.test_wiki_status tests.test_wiki_graph_summary tests.test_wiki_scorecard_summary tests.test_wiki_queue_preview`
- `rg -n "plugins/report-wiki-portfolio/commands|commands/wiki-|/wiki:" README.md .codex/skills tests openspec/specs`
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

## Parent Gate Preservation

- Parent gate preserved: the repo `AGENTS.md` high-frequency skill routing and
  behavior replay gate still own when wiki skills are loaded and when behavior
  changes require OpenSpec.
- This change does not promote wiki skills above material, meeting-note,
  public-report, frontmatter taxonomy, or OpenSpec lifecycle gates.
- The runtime surface is narrower after this change: wiki skills inspect and
  summarize named artifacts, while implementation, archive, sync, publication,
  and queued execution still require their existing parent gate.

## Residual Risks

- The current skill invocation display may vary by host UI, but the repo-local
  source of truth is `.codex/skills/wiki-*`.
- Whole-wiki frontmatter still fails until historical pages are migrated.
