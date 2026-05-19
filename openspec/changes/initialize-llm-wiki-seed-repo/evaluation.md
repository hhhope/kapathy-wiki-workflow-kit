# Evaluation: initialize LLM-WIKI seed repo

## Source Repository

- `PYTHONPATH=. .venv-taxonomy/bin/pytest -q tests/test_llm_wiki_seed_manifest.py tests/test_llm_wiki_seed_builder.py`: 14 passed.
- `python3 -m py_compile scripts/llm_wiki_seed_manifest.py scripts/build_llm_wiki_seed.py scripts/verify_llm_wiki_seed.py`: passed.
- `python3 scripts/build_llm_wiki_seed.py --target-dir /tmp/llm-wiki-seed-dryrun --force`: passed.
- `python3 scripts/verify_llm_wiki_seed.py --target-dir /tmp/llm-wiki-seed-dryrun`: passed.

## Target Repository

Target path: `/mnt/d/cloud/LLM-WIKI`.

Initial commit:

- `3dbb953 feat: initialize llm wiki seed`

Committed seed surface:

- `AGENTS.md`, `PROJECT.md`, `README.md`, `.gitignore`
- `.codex/skills/` real wiki, learning, public-output, OpenSpec, and medical-loop skills
- `wiki/config/` frontmatter and behavior-asset config
- `scripts/` wiki runtime, graph, scorecard, status, and medical-loop scripts
- sanitized seed pages for LLM-Wiki method notes, Li Xiang interview shape, examples, ops, ADR, status, and generated medical-loop examples

Target verification:

- `python3 scripts/verify_llm_wiki_seed.py --target-dir /mnt/d/cloud/LLM-WIKI`: passed.
- `python3 scripts/check_wiki_frontmatter.py`: passed in target repository.
- `python3 scripts/build_wiki_status.py`: wrote `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.
- `python3 scripts/extract_wiki_graph.py`: passed with 3 nodes and 1 unresolved example warning.
- `python3 scripts/analyze_wiki_relations.py`: passed with 3 canonical objects.
- `python3 scripts/score_wiki_semantics.py`: passed with 3 weak-band objects, as expected for a thin seed.
- `python3 scripts/derive_wiki_utilization.py /tmp/llm-wiki-seed-scorecard.json`: passed.
- `python3 scripts/build_wiki_medical_case.py`: wrote a seed medical case under `wiki/ops/wiki-medical-cases/`.
- `python3 scripts/build_wiki_review_decisions.py`: wrote a seed review decision under `wiki/ops/wiki-review-decisions/`.
- `python3 scripts/build_wiki_medical_agent.py --intent-text status`: passed with `allowed_action: report_status`.

Git hygiene:

- Target repository status after commit: clean.
- Target `scripts/__pycache__/` is ignored by `.gitignore` and is not committed.
- Source repository task-related commits were made separately from the target seed commit.

## README Follow-Up

README polish remains intentionally deferred. This change only proves the seed
repository skeleton, copied runtime surface, sanitized examples, and minimal
runtime commands. A later README pass should explain the system and future
roadmap after this seed is pushed and reviewed.

## Residual Risks

- The seed graph has thin objects and one unresolved example warning; this is
  expected for a minimal seed and should not be treated as retrieval proof.
- Runtime commands are script-level checks only, not multi-agent rollout proof.
- The target commit is local only until explicitly pushed.
