# Evaluation

## RED Baseline

Command:

```bash
PYTHONPATH=. .venv-taxonomy/bin/pytest -q tests/test_learning_capture_consolidation.py
```

Observed RED result before implementation:

- `test_readme_learning_is_not_a_separate_active_skill` failed because
  `.codex/skills/readme-learning-capture/SKILL.md` existed.
- `test_repo_readme_module_is_self_contained_under_learning_capture` failed
  because `learning-capture/references/repo-readme.md` delegated to
  `.codex/skills/readme-learning-capture/SKILL.md`.
- `test_active_manifests_do_not_require_retired_readme_skill` failed because
  `scripts/llm_wiki_seed_manifest.py` and
  `tests/test_llm_wiki_seed_manifest.py` still required the old skill path.

Result: RED. The current repo exposed two active runtime entry surfaces for
repo/README learning.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `.codex/skills/learning-capture/SKILL.md`
- `.codex/skills/learning-capture/references/repo-readme.md`
- `.codex/skills/readme-learning-capture/SKILL.md`
- `openspec/specs/readme-learning-skill/spec.md`
- `openspec/specs/learning-capture-routing/spec.md`
- `wiki/ops/learning-capture-routing.md`
- `openspec/changes/archive/2026-04-18-formalize-readme-learning-skill/*`
- `openspec/changes/retire-article-learning-skill-surface/*`

Owns:

- This change owns retirement of the active
  `.codex/skills/readme-learning-capture/` runtime surface.
- This change owns migration of repo/README scorecard and pressure scenarios
  into `learning-capture` references.
- This change owns active manifest/test cleanup for the retired skill path.

References:

- `learning-capture` remains the parent gate for external-source learning.
- `learning-capture-routing` continues to own evidence-object routing.
- Repo behavior-asset gates continue to own promotion into `AGENTS.md`, specs,
  skill hard rules, or archive-ready claims.

Rejects:

- Do not recreate a standalone active `readme-learning-capture` skill surface.
- Do not rewrite historical wiki records only because they mention the old
  skill name.
- Do not weaken repo/README admission, score-first, or adaptation-boundary
  gates while consolidating the entry point.

## Pressure Scenarios

Positive scenario:

- input or situation shape: user provides a GitHub repo or README and asks
  "这个方案能不能复用".
- trigger condition: external-source learning with repo/README evidence object.
- expected route: load `learning-capture`, then use
  `references/repo-readme.md`.
- repo-visible artifact: `.codex/skills/learning-capture/SKILL.md` and
  `.codex/skills/learning-capture/references/repo-readme.md`.
- expected output: admission gate, score-first decision, reused / modified /
  rejected / adoption-boundary record.
- promotion or non-promotion boundary: no promotion into `AGENTS.md`, specs, or
  skill hard rules without the behavior-asset/OpenSpec gate.
- proof boundary: this validates routing and module availability, not quality of
  a future source analysis.

Negative should-not-trigger scenario:

- input or situation shape: user asks only for latest repo stars, facts, or a
  generic repository code review.
- trigger condition: no local learning, reuse, wiki, or method-calibration
  intent.
- expected route: do not use durable repo/README learning capture; use lookup or
  review workflow instead.
- repo-visible artifact: no new durable wiki learning page required.
- expected output: answer the narrow request or route to code review.
- promotion or non-promotion boundary: no behavior-asset promotion from a raw
  lookup.
- proof boundary: this validates non-trigger behavior, not external fact
  freshness.

Parent gate preservation:

- The parent gate remains `learning-capture`.
- The repo/README module preserves admission, score-first triage, adaptation
  boundary, output routing, and promotion boundaries.
- The consolidation removes only the duplicate active entry surface.

## GREEN Result

Command:

```bash
PYTHONPATH=. .venv-taxonomy/bin/pytest -q tests/test_learning_capture_consolidation.py
```

Observed GREEN result:

```text
3 passed in 1.06s
```

Additional active-surface scan:

```bash
find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'readme-learning-capture|learning-capture'
```

Observed result:

```text
.codex/skills/learning-capture/SKILL.md
```

Active reference scan:

```bash
rg -n "readme-learning-capture" .codex/skills scripts tests AGENTS.md PROJECT.md openspec/specs/readme-learning-skill openspec/specs/learning-capture-routing
```

Observed result after implementation: only the new regression test and this
OpenSpec change mention the retired name. Active skills, scripts, current specs,
and repo entrypoints no longer expose it.

## Validation Evidence

Commands:

```bash
PYTHONPATH=. .venv-taxonomy/bin/pytest -q tests/test_learning_capture_consolidation.py tests/test_llm_wiki_seed_manifest.py
python3 -m py_compile scripts/llm_wiki_seed_manifest.py
openspec validate consolidate-readme-learning-capture --strict
python3 scripts/check_behavior_assets.py
```

Observed results:

- `pytest`: `7 passed in 1.55s`.
- `py_compile`: passed.
- `openspec validate`: `Change 'consolidate-readme-learning-capture' is valid`
  with PostHog network flush warnings after the valid result.
- `check_behavior_assets.py`: non-zero. The reported errors are for
  `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`, not for this
  change. The user explicitly scoped the current request away from LLM-WIKI, so
  that earlier change is left untouched here.

## Residual Risks

- Archived OpenSpec changes and historical wiki records still mention
  `readme-learning-capture`; those are historical evidence and were left intact.
- Full behavior-asset checker is still blocked by the separate active
  `initialize-llm-wiki-seed-repo` evaluation artifact.
- The global/user skill inventory may still contain a similarly named external
  skill outside this repo; this change only governs the current repository.
- This does not prove future source-analysis quality; it proves active routing
  dedupe and preserved module gates.
