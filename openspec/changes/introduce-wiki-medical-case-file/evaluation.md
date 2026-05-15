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
  required by this change.

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
