# Evaluation

## Pressure Scenarios

1. Positive trigger scenario: a trace for article weight/temperature can use
   `exploratory_scoring` or `article_learning` and still pass when it keeps the
   boundary at `candidate_judgment_only`.
2. Positive trigger scenario: a frontmatter repair trace can require
   `run_static_precheck` and static facts without requiring Python to infer the
   user intent.
3. Negative should-not-trigger scenario: an article weight/temperature trace
   fails when it includes `frontmatter_repair`.
4. Negative should-not-trigger scenario: a trace fails when it does not record
   that forbidden actions were checked.

## Behavior Replay

- Input or situation shape: a user asks a repo-local wiki skill to inspect,
  repair, learn, score, explore relations, execute queued work, or promote a
  behavior rule.
- Trigger condition: the wiki request is high-risk or ambiguous enough to need
  a decision boundary before action.
- Expected route: agent classifies intent and emits a `decision_trace`; Python
  evaluates that trace against `wiki/evals/wiki-react-trace-cases.json`.
- Repo-visible artifact: `wiki/ops/wiki-react-decision-trace-runtime.md`,
  `wiki/evals/wiki-react-trace-cases.json`,
  `scripts/eval_wiki_decision_trace.py`, high-risk wiki skills, and this
  OpenSpec change.
- Expected output: a pass/fail trace evaluation that validates allowed intents,
  required actions, forbidden actions, observation class, and boundary.
- Promotion or non-promotion boundary: the eval harness does not promote
  candidate learning, article temperature, relation strength, or scorecard
  bands into hard gates.
- Proof boundary: this proves deterministic trace validation for first-version
  wiki ReAct replay, not live LLM intent accuracy or autonomous execution.

## RED Baseline

Before implementation:

- `python3 -m unittest tests.test_wiki_decision_trace_eval` failed with
  `ModuleNotFoundError: No module named 'scripts.eval_wiki_decision_trace'`.
- High-risk wiki skills did not reference a shared decision-trace contract.
- The new wiki ops method page initially failed target frontmatter precheck for
  missing `layer`, `domain`, and `ops_area`.

## GREEN Result

After implementation:

- `scripts/eval_wiki_decision_trace.py` validates agent-produced traces without
  natural-language intent classification.
- `.codex/skills/wiki-react/SKILL.md` provides the direct repo-local skill
  entrypoint for decision-trace creation, replay, and onward wiki routing.
- `wiki/evals/wiki-react-trace-cases.json` covers status, query, frontmatter
  repair, article learning, article weight/temperature, relation exploration,
  execution request, and promotion-to-ADR scenarios.
- `wiki-query`, `wiki-apply`, `wiki-explore`, and `wiki-scorecard` reference the
  shared decision-trace contract.
- The new wiki ops method page has target precheck `entry_count: 0`; the whole
  wiki gate still fails on historical pages outside this change.

## Verification

- `python3 -m unittest tests.test_wiki_decision_trace_eval`
- `python3 -m unittest tests.test_wiki_runtime_skills tests.test_wiki_status_command`
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/wiki-react-decision-trace-runtime.md`
- `rg -n "plugins/report-wiki-portfolio/commands|commands/wiki-|/wiki:" README.md .codex/skills tests openspec/specs`
- `python3 scripts/check_behavior_assets.py`
- `openspec validate introduce-wiki-react-decision-trace-eval --strict`

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`, active wiki runtime skills, existing
  wiki runtime specs, behavior asset evaluation rules, and recent wiki skill
  runtime closure change.
- Owns: first-version wiki decision-trace contract and deterministic trace
  evaluation.
- References: existing agent intent routing remains the repo-level parent
  classifier; existing scorecard remains an observation source.
- Rejects: Python natural-language intent classification, plugin/slash runtime,
  autonomous execution, scorecard-as-behavior-judge, and hard-gating
  exploratory article weight or temperature.

## Parent Gate Preservation

- Parent gate preserved: repo `AGENTS.md` still owns intent classification
  before acting, OpenSpec still owns workflow behavior changes, and specialized
  material/meeting/public/frontmatter gates are not bypassed.
- The ReAct decision trace narrows action by recording boundary and forbidden
  actions; it does not grant permission to write pages, mutate taxonomy,
  publish output, sync external systems, mark OpenSpec tasks done, or archive.

## Residual Risks

- This version validates trace shape and boundaries, not live LLM judgment
  quality.
- Trace cases are deliberately small; future work should add live replay traces
  after the first version is reviewed.
- Whole-wiki frontmatter remains blocked by historical pages outside this
  change, even though the new method page passes target precheck.
