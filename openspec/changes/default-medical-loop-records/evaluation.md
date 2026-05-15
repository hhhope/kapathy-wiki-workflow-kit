# Evaluation: default medical loop records

## Behavior Replay

- Input or situation shape: user invokes `wiki-doctor` or `wiki-confirm` as a
  medical-loop stage.
- Trigger condition: diagnosis or confirmation is requested, including Chinese
  stage language such as `诊断` or `确诊`.
- Expected route or stop behavior: the stage writes a complete repo-visible
  record by default, then reports a compact stdout summary and path.
- Repo-visible artifact: diagnosis records under `wiki/ops/wiki-doctor-runs/`
  and confirmation records under `wiki/ops/wiki-review-decisions/`.
- Expected output or non-output: stdout is a summary, not the source of record;
  `--stdout-json-only` is required for non-writing JSON inspection.
- Promotion or non-promotion boundary: records do not approve treatment,
  surgery, frontmatter, taxonomy, relation, MOC, ADR, or OpenSpec changes.
- Residual risk or proof boundary: records are deterministic routing evidence;
  human confirmation is still needed before treatment or surgery.

## RED Baseline

- Command:
  `python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_review_decisions.py tests/test_wiki_medical_loop_skills.py tests/test_wiki_runtime_skills.py`
- Result: failed before implementation.
- Observed baseline failures:
  - default doctor CLI output had no `review_record_path`
  - default confirm CLI output had no `decision_record_path`
  - `--stdout-json-only` was an unknown CLI argument for both scripts
  - skill contracts still said records were written only when explicitly asked
  - written records used implementation-shaped titles and lacked the new
    medical-report section contract
- Baseline proved the old behavior could leave diagnosis and confirmation as
  transient stdout instead of durable repo-visible records.

## GREEN Result

- Command:
  `python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_review_decisions.py tests/test_wiki_medical_loop_skills.py tests/test_wiki_runtime_skills.py`
- Result: passed, 22 tests.
- Command: `python3 scripts/check_behavior_assets.py`
- Result: passed with no output.
- Command: `openspec validate default-medical-loop-records --strict`
- Result: change valid. The command later reported a PostHog telemetry DNS
  flush error for `edge.openspec.dev`; validation itself had already passed.
- Verified behavior:
  - default doctor CLI writes a full diagnosis record and returns compact
    summary JSON
  - default confirm CLI writes a full confirmation record and returns compact
    summary JSON
  - `--stdout-json-only` preserves non-writing JSON inspection
  - `--limit` does not truncate the written record in default mode
  - skill text now states default complete record behavior and stdout summary
  - generated medical-loop records remain excluded from adjudication candidates

## Prior-Art / Common-Rule Dedupe

- Owns: default record creation semantics for the `wiki-doctor` and
  `wiki-confirm` medical-loop stages.
- References: existing medical-loop boundaries from repo `AGENTS.md`,
  `wiki/ops/llm-wiki-self-evolution-medical-loop.md`, and archived
  review-decision / medical-loop OpenSpec changes.
- References: common behavior-asset evaluation and TDD rules from global
  development workflow and repo Skill Authoring Contract.
- Rejects: broadening doctor or confirm records into treatment, surgery,
  taxonomy, relation, MOC, ADR, or OpenSpec writes.
- Dedupe result: this change does not restate generic git, testing, or
  behavior-asset thresholds in skill files. It only updates the stage-specific
  default record behavior and preserves existing repair boundaries.
