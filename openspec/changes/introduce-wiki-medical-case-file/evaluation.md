# Evaluation: introduce wiki medical case file

## Initial Evidence

This change was created after a live medical-loop drift:

- Surgery planning had generated a stage record from script output.
- The user challenged whether surgery should review the generated surgery
  record or the already-confirmed doctor/confirm content.
- The corrected model is that one canonical case file owns the current case,
  while stage records remain evidence attachments.

Repo-visible drift evidence:

- `wiki/ops/wiki-medical-case-file-drift-retro-2026-05-15.md`

Superpowers repair evidence:

- `docs/superpowers/specs/2026-05-15-wiki-medical-case-file-design.md`
- `docs/superpowers/plans/2026-05-15-wiki-medical-case-file.md`
- `docs/superpowers/specs/2026-05-15-wiki-medical-case-file-replay.md`

Proof boundary: these Superpowers files were added after the initial OpenSpec
proposal commit. They repair the missing support evidence; they do not claim
the original Superpowers brainstorming gate was completed before OpenSpec
editing.

## Superpowers Gate Repair

### What Failed

- `$superpowers` / Superpowers process pressure was present in the discussion.
- The case-file design was written directly into OpenSpec artifacts.
- No Superpowers design, plan, or replay artifact existed at the time of the
  initial commit.

### Corrected Route

The correct route for future equivalent work is:

```text
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.
```

After Superpowers design review, accepted lifecycle content can be copied into
OpenSpec.

### Current Repair

The current repair preserves the existing OpenSpec change and adds the missing
Superpowers support layer. It does not mark the case-file implementation tasks
as complete.

## Replay Summary

The replay file covers these cases:

- Doctor and confirm records exist; surgery is requested.
- Surgery script writes a generated surgery record.
- Human asks what to review.
- `relation_weak_evidence` appears.
- `drift_risk`, `adr_risk`, or `openspec_required` appears.
- Recovery runs after treatment or surgery.
- A later generated stage record disagrees with case decisions.

Expected result: the case file remains the authority; stage records remain
evidence attachments.

## Validation

### RED Baseline

Command:

```bash
python3 -m unittest tests.test_wiki_medical_case tests.test_wiki_surgery
```

Initial result before implementation:

```text
ModuleNotFoundError: No module named 'scripts.wiki_medical_case'
ImportError: cannot import name 'build_surgery_plan_from_case' from 'scripts.wiki_surgery'
```

Interpretation: the repo had no canonical case-file module and surgery could
not derive a plan from Confirmed Decisions.

### Implementation Replay

Implemented files:

- `.codex/skills/wiki-confirm/SKILL.md`
- `.codex/skills/wiki-surgery/SKILL.md`
- `scripts/wiki_medical_case.py`
- `scripts/build_wiki_medical_case.py`
- `scripts/wiki_surgery.py`
- `scripts/build_wiki_surgery.py`
- `tests/test_wiki_medical_case.py`
- `tests/test_wiki_surgery.py`

Replay coverage:

- A case file can be generated under `wiki/ops/wiki-medical-cases/`.
- The case file contains `Confirmed Decisions` and machine-readable case data.
- Surgery can read `--case-file` and build from confirmed surgery and OpenSpec
  decisions instead of raw adjudication details.
- `--update-case-file` writes the generated surgery plan back into the case
  file and preserves the surgery record path as an evidence attachment.
- No repo-local skill was updated; behavior-asset checks were therefore not
  required by the first implementation commit.

## Pressure Scenarios

Positive scenario:

- input or situation shape: user invokes `wiki-confirm` after `wiki-doctor`.
- trigger condition: confirmation writes a decision record and exposes
  treatment, surgery, and OpenSpec-required buckets.
- expected route: `wiki-confirm` runs `scripts/build_wiki_review_decisions.py`,
  then creates the canonical case file with
  `scripts/build_wiki_medical_case.py --confirm-record <decision_record_path>`.
- repo-visible artifact: `.codex/skills/wiki-confirm/SKILL.md` and the case
  file under `wiki/ops/wiki-medical-cases/`.
- expected output: the user receives both the confirmation record path and the
  medical case path.
- promotion or non-promotion boundary: confirmation remains draft routing, not
  human approval and not treatment or surgery execution.
- proof boundary: this does not write frontmatter, relation fields, MOC files,
  ADRs, AGENTS, skills beyond this repair, or OpenSpec lifecycle state.

Positive scenario:

- input or situation shape: user invokes `wiki-surgery` while a current case
  file exists.
- trigger condition: `wiki/ops/wiki-medical-cases/` contains the case file that
  owns the current Confirmed Decisions.
- expected route: `wiki-surgery` uses
  `scripts/build_wiki_surgery.py --case-file <case-file>`, and uses
  `--write-surgery-record --update-case-file` when a surgery record is
  requested.
- repo-visible artifact: `.codex/skills/wiki-surgery/SKILL.md`, the case file,
  and the surgery evidence attachment.
- expected output: the surgery plan cites confirmed case decisions and the
  updated case file links the surgery record as evidence.
- promotion or non-promotion boundary: the surgery record is not a new
  diagnosis and does not become the source of truth.
- proof boundary: this only repairs intent routing; it still does not apply
  relation, taxonomy, governance, MOC, ADR, AGENTS, skill, or OpenSpec edits.

Negative should-not-trigger scenario:

- input or situation shape: user invokes `wiki-surgery` and no case file exists.
- trigger condition: no current file is available under
  `wiki/ops/wiki-medical-cases/`.
- expected route: stop and route to `wiki-confirm` or
  `scripts/build_wiki_medical_case.py` instead of silently running raw
  adjudication.
- repo-visible artifact: `.codex/skills/wiki-surgery/SKILL.md`.
- expected output: the agent asks for or creates the case file before normal
  surgery planning.
- promotion or non-promotion boundary: raw adjudication remains a legacy/debug
  path, not the normal surgery intent path.
- proof boundary: the skill cannot automatically detect human approval; it
  only defines the required route judgment.

## RED Baseline

Command:

```bash
python3 -m unittest tests.test_wiki_runtime_skills.WikiRuntimeSkillsTest.test_wiki_runtime_skill_sources_exist_with_plain_wiki_names
```

Initial result before the skill repair:

```text
FAILED (failures=2)
AssertionError: 'scripts/build_wiki_medical_case.py' not found ... skill='wiki-confirm'
AssertionError: 'wiki/ops/wiki-medical-cases' not found ... skill='wiki-surgery'
```

Interpretation: the implemented CLI path existed, but the runtime skill entry
still lacked the intent judgment that turns confirmation into a case file and
turns surgery into case-file-based planning.

## GREEN Result

Command:

```bash
python3 -m unittest tests.test_wiki_runtime_skills.WikiRuntimeSkillsTest.test_wiki_runtime_skill_sources_exist_with_plain_wiki_names
```

Result:

```text
Ran 1 test in 0.162s
OK
```

The repaired skills now state the runtime route:

- `wiki-confirm` creates the case file after the confirmation record.
- `wiki-surgery` checks `wiki/ops/wiki-medical-cases/`, uses
  `--case-file`, and updates the same case with `--update-case-file` when a
  surgery record is requested.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md` Agent Intent Routing and Workflow Change Gate.
- `PROJECT.md` OpenSpec source-of-truth boundary.
- `openspec/changes/introduce-wiki-medical-case-file/design.md`.
- `openspec/changes/introduce-wiki-medical-case-file/specs/wiki-medical-loop-records/spec.md`.
- `.codex/skills/wiki-confirm/SKILL.md`.
- `.codex/skills/wiki-surgery/SKILL.md`.
- `tests/test_wiki_runtime_skills.py`.

Owns:

- The two stage skills own their local stage instructions: confirmation creates
  a case file, and surgery prefers the case file for normal surgery intent.

References:

- `AGENTS.md` still owns global intent classification and the high-frequency
  skill routing table.
- OpenSpec still owns the case-file lifecycle requirement.
- The surgery CLI still owns the concrete `--case-file` and
  `--update-case-file` behavior.

Rejects:

- No new broad route table was added to `AGENTS.md`.
- No generic intent framework was added.
- Raw surgery from adjudication was not promoted as the normal user-intent path.

## Residual Risks

- If multiple case files exist, the skill requires choosing the current case;
  automated latest-case selection is not implemented.
- The skill route depends on the agent reading the skill body after trigger.
- Historical surgery records remain evidence only; they are not migrated into
  case files by this repair.

### Focused Tests

Command:

```bash
python3 -m unittest tests.test_wiki_medical_case tests.test_wiki_surgery
```

Result:

```text
Ran 12 tests in 1.714s
OK
```

Command:

```bash
python3 -m unittest tests.test_wiki_medical_case tests.test_wiki_surgery tests.test_wiki_review_decisions tests.test_wiki_treatment tests.test_wiki_recovery
```

Result:

```text
Ran 29 tests in 3.836s
OK
```

### Generated Case Frontmatter Target Precheck

Command shape:

```bash
python3 scripts/wiki_gate_precheck.py --root "$tmpdir" --mode frontmatter --target wiki/ops/wiki-medical-cases/2026-05-15-061136-precheck-case.md --top 1
```

Result:

```text
passed: true
blocking_count: 0
target.entry_count: 0
```

### OpenSpec

Command:

```bash
openspec validate introduce-wiki-medical-case-file --strict
```

Result:

```text
Change 'introduce-wiki-medical-case-file' is valid
```

Residual note: the CLI attempted to flush PostHog telemetry and hit a network
resolution error for `edge.openspec.dev`. The local OpenSpec validation result
was already successful.

### Frontmatter Target Precheck

Command:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/wiki-medical-case-file-drift-retro-2026-05-15.md
```

Result:

```text
passed: false
blocking_count: 834
target.entry_count: 0
```

Interpretation:

- The whole-wiki strict gate still fails on existing legacy pages.
- The new target page has no target-level frontmatter blockers.

## Proof Boundary

This is proposal and design evidence only. It does not implement the case-file
builder, change surgery defaults, or approve any wiki repair. The Superpowers
artifacts repair process evidence only; they do not prove the original sequence
was followed.
