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
