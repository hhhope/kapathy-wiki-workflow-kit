# Evaluation: repair wiki frontmatter recovery blocker

## RED Baseline

Command:

```bash
python3 -m unittest tests.test_wiki_frontmatter_repair tests.test_wiki_recovery -v
```

Initial result:

- `tests.test_wiki_frontmatter_repair` failed to import because
  `scripts.wiki_frontmatter_repair` did not exist.
- `tests.test_wiki_recovery.WikiRecoveryTest.test_frontmatter_status_separates_clean_targets_from_repo_debt`
  failed because `build_recovery_package()` did not accept
  `frontmatter_targets`.
- After the module existed, the before/after target evidence assertion failed
  because apply results did not include target precheck evidence.

## GREEN Result

Command:

```bash
python3 -m unittest tests.test_wiki_frontmatter_repair tests.test_wiki_recovery tests.test_wiki_medical_agent -v
```

Result: PASS, 27 tests.

Covered behavior:

- Repair planner groups frontmatter blockers into explicit page batches.
- Repair apply writes only approved frontmatter fields and ignores relation
  fields.
- Repair apply emits target-level before/after precheck evidence.
- Recovery separates treatment-target frontmatter cleanliness from
  repository-wide strict-gate debt.
- Medical-agent treatment apply passes treatment target paths into recovery.

## Runtime Evidence

Planner dry-run:

```bash
python3 scripts/build_wiki_frontmatter_repair.py --root /mnt/d/cloud/account-meeting-lore --limit 3
```

Result:

- `source_blocking_count: 910`
- `selected_count: 3`
- `review_needed_count: 3`
- selected paths:
  - `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`
  - `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`
  - `wiki/adr/0003-retros-stay-separate-from-adrs.md`

Whole-wiki frontmatter precheck:

```bash
python3 scripts/wiki_gate_precheck.py --root /mnt/d/cloud/account-meeting-lore --mode frontmatter --full-json-output /tmp/wiki-frontmatter-repair-verify.json --full-markdown-output /tmp/wiki-frontmatter-repair-verify.md
```

Result: expected non-zero.

- `passed: false`
- `blocking_count: 910`
- top blockers remain missing or invalid `layer`, missing `domain`, missing
  `ops_area`, and missing `canonical_object`.

OpenSpec validation:

```bash
openspec validate repair-wiki-frontmatter-recovery-blocker --strict
```

Result: PASS, reported `Change 'repair-wiki-frontmatter-recovery-blocker' is valid`.
PostHog telemetry flush printed DNS warnings for `edge.openspec.dev`; the
command exited 0 after validation passed.

## Residual Risks

- This change intentionally does not batch-apply repairs to legacy pages.
- Whole-wiki frontmatter recovery remains blocked until explicit repair batches
  are selected and applied.
- Existing unrelated worktree changes were not included in this implementation
  boundary.
