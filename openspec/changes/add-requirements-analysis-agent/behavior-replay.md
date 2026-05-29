# Behavior Replay Evidence

Generated: 2026-05-29

## Scope

This record covers runtime behavior introduced by
`add-requirements-analysis-agent`:

- intent routing
- domain candidate routing
- requirements hard-gate blocking
- wiki-independent requirements gating
- OpenSpec draft collision blocking

The evidence boundary is focused local replay through unit tests and CLI probes.
It proves deterministic behavior in this repository; it is not evidence of LLM
semantic judgment.

## Replay Matrix

### Intent Routing

Input shape: user asks `请跑一下需求门禁，校验这份需求`.

Trigger condition: material contains `需求门禁`, `校验需求`, or `需求校验`.

Expected behavior: `classify_intent` returns `check_requirements_ready` and
`next_action: run_requirements_checker`.

Evidence:

- `tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTests.test_classify_intent_detects_requirements_ready_check_requests`
- CLI probe:
  `python3 scripts/build_requirements_analysis_agent.py "请跑一下需求门禁，校验这份需求"`

Residual risk: heuristic phrase coverage is intentionally bounded; new wording
requires taxonomy/test expansion.

### Domain Candidates

Input shape: `embedded wallet account balance reservation before wallet payment
capture`.

Trigger condition: wallet-like vocabulary appears even when `account` also
appears.

Expected behavior: domain status remains `candidate_pending`, candidates include
`embedded_wallet` or `wallet_payment`, and seeded domains are not forced.

Evidence:

- `tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTests.test_wallet_material_with_account_word_is_not_forced_to_seeded_domain`

Residual risk: candidate generation is deterministic and conservative; it is not
a complete domain ontology.

### Hard-Gate Blocking

Input shape: requirements case with a user story missing
`acceptance_function_ids`.

Trigger condition: `create_openspec_draft_from_case` is requested before
requirements readiness.

Expected behavior: draft creation returns `status: blocked`,
`reason: requirements_not_ready`, includes checker blockers naming `US-1`, and
does not create `openspec/changes/<change-id>`.

Evidence:

- `tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTests.test_create_openspec_draft_blocks_unready_case_without_creating_files`
- `tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_missing_acceptance_mapping_fails_naming_user_story`

Residual risk: hard-gate completeness is limited to first-version requirement
readiness fields, not API, DDL, release, or architecture correctness.

### Wiki-Independent Gating

Input shape: requirements case stored under `wiki/ops/requirements-cases` in a
temporary repo root without `wiki/config/frontmatter-taxonomy.yaml`.

Trigger condition: checker evaluates a wiki-stored case.

Expected behavior: checker uses
`requirements/config/requirements-taxonomy.yaml`, returns
`requirements_ready`, and does not require wiki frontmatter taxonomy.

Evidence:

- `tests.test_requirements_checker_gate.RequirementsCheckerGateTests.test_wiki_stored_case_does_not_need_wiki_frontmatter_taxonomy`

Residual risk: wiki frontmatter still governs wiki page identity when files are
committed into wiki; requirements readiness remains separate.

### Draft Collision Blocking

Input shape: target `openspec/changes/draft-existing` already exists with
`proposal.md`.

Trigger condition: ready case requests draft creation with existing change id.

Expected behavior: draft creation returns `status: blocked`,
`reason: change_id_collision`, preserves existing `proposal.md`, and asks for a
different change id or explicit selection.

Evidence:

- `tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTests.test_create_openspec_draft_blocks_existing_change_id_without_overwrite`

Residual risk: collision detection is directory-based. It intentionally blocks
reuse instead of merging into existing OpenSpec changes.

### Draft Path Safety

Input shape: ready case with `capability: ../outside`.

Trigger condition: caller attempts to use a capability value that is not a
single path segment.

Expected behavior: draft creation returns `status: blocked`,
`reason: invalid_capability`, and does not create the change directory.

Evidence:

- `tests.test_requirements_analysis_agent.RequirementsAnalysisAgentTests.test_create_openspec_draft_blocks_invalid_capability_path`

Residual risk: this prevents path traversal for the public helper parameters;
callers still own choosing meaningful capability names.

## Verification Commands

```text
python3 -m unittest tests.test_requirements_case tests.test_requirements_checker tests.test_requirements_checker_gate tests.test_requirements_analysis_agent
openspec validate add-requirements-analysis-agent --strict
python3 scripts/check_wiki_frontmatter.py
python3 scripts/build_requirements_analysis_agent.py "请跑一下需求门禁，校验这份需求"
```

## Verification Results

- `python3 -m unittest tests.test_requirements_case tests.test_requirements_checker tests.test_requirements_checker_gate tests.test_requirements_analysis_agent`
  - Exit status: 0
  - Result: `Ran 30 tests ... OK`
- `openspec validate add-requirements-analysis-agent --strict`
  - Exit status: 0
  - Result: `Change 'add-requirements-analysis-agent' is valid`
  - Caveat: PostHog telemetry DNS flush produced `EAI_AGAIN edge.openspec.dev`
    after validation; this did not change the OpenSpec validation exit status.
- `python3 scripts/check_wiki_frontmatter.py`
  - Exit status: 0
  - Result: no output
- `python3 scripts/build_requirements_analysis_agent.py "请跑一下需求门禁，校验这份需求"`
  - Exit status: 0
  - Result: JSON output returned `intent: check_requirements_ready` and
    `next_action: run_requirements_checker`.
