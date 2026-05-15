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
builder, change surgery defaults, or approve any wiki repair.
