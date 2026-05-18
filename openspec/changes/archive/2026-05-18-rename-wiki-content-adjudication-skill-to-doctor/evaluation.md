# Evaluation: wiki-doctor skill rename

## Evidence

- `python3 -m unittest tests/test_wiki_runtime_skills.py`
  - RED baseline: failed because `.codex/skills/wiki-doctor/SKILL.md` did not
    exist.
  - GREEN result: passed, 5 tests.
- `python3 scripts/check_behavior_assets.py`
  - Result: passed.
- `openspec validate rename-wiki-content-adjudication-skill-to-doctor --strict`
  - Result: passed.
  - Concern: OpenSpec printed PostHog network flush warnings for
    `edge.openspec.dev`, but the validation command exited successfully.

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: user invokes wiki-doctor | Direct skill references adjudication script and review sections | Passed |
| Negative: user expects doctor to apply fixes | Skill keeps review-only boundary | Passed |

## RED Baseline

Input or situation shape: the direct skill exists as
`wiki-content-adjudication`, which is long and internal.

Trigger condition: user says the name is too long and asks for doctor.

Observed failure before this change: there is no `wiki-doctor` skill entry.

## GREEN Result

Expected route:

```text
wiki-doctor -> build_wiki_content_adjudication.py -> review package summary
```

Repo-visible artifact: `.codex/skills/wiki-doctor/SKILL.md` and
`tests/test_wiki_runtime_skills.py`.

Expected output: a short direct skill entry that diagnoses review package
risks without applying structure.

Promotion or non-promotion boundary: the rename does not change adjudication
runtime behavior or approve writes.

Proof boundary: this is a naming and routing ergonomics change only.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `.codex/skills/wiki-content-adjudication/SKILL.md`
- `tests/test_wiki_runtime_skills.py`
- `openspec/changes/add-wiki-content-adjudication-skill/design.md`

Owns:

- User-facing skill name `wiki-doctor`.

References:

- Existing content adjudication runtime and review-only boundary.

Rejects:

- Renaming scripts just for surface ergonomics.
- Treating doctor as an apply/fix command.

## Parent Gate Preservation

Parent gate: `wiki-doctor` remains a review-package inspection wrapper.

## Residual Risks

- The doctor metaphor may still imply repairs to some users; the skill body
  keeps diagnosis-only wording explicit.
