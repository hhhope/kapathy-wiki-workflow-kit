# wiki-doctor Review Records Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an explicit review-only `wiki-doctor` review-record path that can persist diagnosis artifacts under `wiki/ops` without applying wiki structure changes.

**Architecture:** Keep `scripts/wiki_content_adjudication.py` focused on building the adjudication package because it is already over the Python large-file threshold. Add a small `scripts/wiki_doctor_review_records.py` module that renders Markdown and writes non-overwriting records. Wire `scripts/build_wiki_content_adjudication.py` to the new module behind an explicit CLI flag, and update the `wiki-doctor` skill contract plus OpenSpec evidence.

**Tech Stack:** Python 3 standard library, `unittest`, repo-local OpenSpec markdown, repo-local Codex skill markdown.

---

## File Structure

- Create: `openspec/changes/add-wiki-doctor-review-records/proposal.md`
  - Owns the change summary, scope, out-of-scope boundaries, and success criteria.
- Create: `openspec/changes/add-wiki-doctor-review-records/design.md`
  - Owns architecture and review-record boundary decisions.
- Create: `openspec/changes/add-wiki-doctor-review-records/tasks.md`
  - Owns task checklist and implementation progress.
- Create: `openspec/changes/add-wiki-doctor-review-records/specs/wiki-doctor-review-records/spec.md`
  - Owns the formal `SHALL` requirements.
- Create: `openspec/changes/add-wiki-doctor-review-records/evaluation.md`
  - Owns RED/GREEN evidence, behavior replay evidence, prior-art dedupe, and residual risk.
- Create: `scripts/wiki_doctor_review_records.py`
  - Owns Markdown rendering, non-overwrite path generation, and review-record writes.
- Modify: `scripts/build_wiki_content_adjudication.py`
  - Owns CLI flags only: default stdout, optional `--write-review-record`, optional `--review-record-dir`.
- Modify: `tests/test_wiki_content_adjudication.py`
  - Adds focused tests for review-record rendering and CLI write behavior.
- Modify: `tests/test_wiki_runtime_skills.py`
  - Adds runtime skill markers for explicit review-record capability and boundaries.
- Modify: `.codex/skills/wiki-doctor/SKILL.md`
  - Updates the skill contract while preserving review-only boundaries.
- Optional generated evidence: `wiki/ops/wiki-doctor-runs/<timestamp>-review.md`
  - Include only if the OpenSpec evaluation intentionally uses a real generated review record as evidence.

## Parallel Execution Boundaries

- Worker A owns OpenSpec files only under `openspec/changes/add-wiki-doctor-review-records/`.
- Worker B owns Python implementation and content-adjudication tests only: `scripts/wiki_doctor_review_records.py`, `scripts/build_wiki_content_adjudication.py`, and `tests/test_wiki_content_adjudication.py`.
- Worker C owns skill contract and runtime skill tests only: `.codex/skills/wiki-doctor/SKILL.md` and `tests/test_wiki_runtime_skills.py`.
- The lead integrator owns final evidence updates in `evaluation.md`, final generated review-record evidence, validation commands, and commits.

## Task 1: Create OpenSpec Change Skeleton

**Files:**
- Create: `openspec/changes/add-wiki-doctor-review-records/proposal.md`
- Create: `openspec/changes/add-wiki-doctor-review-records/design.md`
- Create: `openspec/changes/add-wiki-doctor-review-records/tasks.md`
- Create: `openspec/changes/add-wiki-doctor-review-records/specs/wiki-doctor-review-records/spec.md`
- Create: `openspec/changes/add-wiki-doctor-review-records/evaluation.md`

- [ ] **Step 1: Create proposal**

Write `openspec/changes/add-wiki-doctor-review-records/proposal.md`:

```markdown
# Proposal: wiki-doctor review records

## Summary

Add an explicit repo-visible review-record path for `wiki-doctor` diagnosis.

## Problem

`wiki-doctor` can inspect and summarize the content adjudication review package,
but the diagnosis can disappear into stdout or chat. The repository needs a
durable, review-only artifact that preserves scan scope, summary counts,
taxonomy candidates, drift traces, eval warnings, proof boundary, and next
review actions for later human review.

## Scope

In scope:

- Add `wiki-doctor` review-record requirements.
- Add a non-overwriting Markdown review-record writer under `wiki/ops`.
- Add an explicit CLI flag for review-record generation.
- Update the `wiki-doctor` skill contract and runtime skill tests.
- Preserve behavior replay and skill evaluation evidence.

Out of scope:

- Applying frontmatter writes.
- Mutating `wiki/config/frontmatter-taxonomy.yaml`.
- Writing `wiki/moc` pages.
- Marking OpenSpec tasks complete from doctor output.
- Reopening `rename-wiki-content-adjudication-skill-to-doctor`.

## Success Criteria

- Default adjudication CLI behavior remains stdout-only.
- Explicit review-record generation writes a Markdown diagnosis under
  `wiki/ops/wiki-doctor-runs/`.
- Generated records include proof boundary and next review actions.
- `wiki-doctor` says review records are diagnosis evidence, not repair approval.
- Tests, behavior-asset checks, and OpenSpec validation pass or record bounded
  expected failures in `evaluation.md`.
```

- [ ] **Step 2: Create design**

Write `openspec/changes/add-wiki-doctor-review-records/design.md`:

```markdown
# Design: wiki-doctor review records

## Architecture

Keep adjudication package construction in `scripts/wiki_content_adjudication.py`.
Add `scripts/wiki_doctor_review_records.py` for review-record rendering and
write safety. Wire `scripts/build_wiki_content_adjudication.py` to the new
module with explicit CLI flags.

## Data Flow

```text
build_adjudication_package(root)
  -> optional limit applied by CLI
  -> stdout JSON
  -> optional write_review_record(package, root, output_dir)
  -> wiki/ops/wiki-doctor-runs/YYYY-MM-DD-HHMMSS-review.md
```

## Review Record Contract

The Markdown record includes:

- scan scope and generated time
- summary counts
- taxonomy candidates as candidates only
- drift trace summary
- eval result summary
- proof boundary
- next review actions

## Boundaries

The review record is diagnosis evidence only. It does not apply structure,
approve taxonomy, write MOC pages, mark OpenSpec tasks complete, or execute
queued work.

## Large-File Boundary

`scripts/wiki_content_adjudication.py` is already above the Python large-file
threshold. This change adds a new helper module instead of adding rendering and
filesystem responsibilities to that file.
```

- [ ] **Step 3: Create tasks**

Write `openspec/changes/add-wiki-doctor-review-records/tasks.md`:

```markdown
# Tasks

- [ ] 1. Create OpenSpec change artifacts for wiki-doctor review records.
- [ ] 2. Add RED tests for Markdown review-record rendering and explicit CLI write behavior.
- [ ] 3. Implement non-overwriting review-record rendering and CLI write flag.
- [ ] 4. Update `wiki-doctor` skill contract and runtime skill coverage.
- [ ] 5. Generate or inspect review-record evidence and update `evaluation.md`.
- [ ] 6. Run tests, behavior asset checks, OpenSpec validation, and record results.
```

- [ ] **Step 4: Create spec**

Write `openspec/changes/add-wiki-doctor-review-records/specs/wiki-doctor-review-records/spec.md`:

```markdown
## Purpose

Define explicit repo-visible `wiki-doctor` review records as diagnosis artifacts
that preserve adjudication review output without applying wiki structure changes.

## ADDED Requirements

### Requirement: Repository SHALL generate explicit wiki-doctor review records

The repository SHALL provide an explicit, non-default path for generating
Markdown `wiki-doctor` review records under `wiki/ops/wiki-doctor-runs/`.

#### Scenario: User requests a review record

- **WHEN** the user explicitly asks `wiki-doctor` to generate a diagnosis record
- **THEN** the repository SHALL build the adjudication package
- **AND** it SHALL write a Markdown review record under `wiki/ops/wiki-doctor-runs/`
- **AND** it SHALL preserve stdout diagnosis behavior for the package.

### Requirement: Review records SHALL preserve diagnosis boundaries

Review records SHALL be diagnosis evidence only and SHALL NOT approve or apply
structural wiki changes.

#### Scenario: Review record contains taxonomy candidates

- **WHEN** a review record includes taxonomy candidates
- **THEN** it SHALL label them as candidates only
- **AND** it SHALL NOT mutate `wiki/config/frontmatter-taxonomy.yaml`.

#### Scenario: Review record contains accepted or likely judgments

- **WHEN** a review record includes adjudication judgments
- **THEN** it SHALL NOT write page frontmatter
- **AND** it SHALL NOT write MOC pages
- **AND** it SHALL NOT mark OpenSpec tasks complete.

### Requirement: Default doctor diagnosis SHALL remain non-writing

The default adjudication CLI and `wiki-doctor` diagnosis path SHALL remain
review-only and non-writing unless review-record generation is explicitly
requested.

#### Scenario: User asks for ordinary doctor diagnosis

- **WHEN** the user asks for `wiki-doctor` diagnosis without asking for a record
- **THEN** the repository SHALL show or summarize the review package
- **AND** it SHALL NOT create files under `wiki/ops/wiki-doctor-runs/`.
```

- [ ] **Step 5: Create initial evaluation**

Write `openspec/changes/add-wiki-doctor-review-records/evaluation.md`:

```markdown
# Evaluation: wiki-doctor review records

## Evidence

- Skeleton creation evidence: this file records the expected RED baseline before
  implementation commands are run.

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: explicit review-record request | Build adjudication package and write Markdown diagnosis under `wiki/ops/wiki-doctor-runs/` | Not run in skeleton stage |
| Negative: ordinary doctor diagnosis | Preserve stdout-only behavior and create no review-record file | Not run in skeleton stage |
| Negative: taxonomy candidates appear | Record candidates without mutating taxonomy YAML | Not run in skeleton stage |
| Negative: accepted judgments appear | Record diagnosis without frontmatter, MOC, or OpenSpec task writes | Not run in skeleton stage |

## RED Baseline

Input or situation shape: the adjudication package exists and `wiki-doctor`
can summarize it.

Trigger condition: user asks for a durable diagnosis record or doctor run
record.

Observed failure before this change: `scripts/build_wiki_content_adjudication.py`
only prints JSON and has no explicit review-record write path.

## GREEN Result

Expected route:

```text
wiki-doctor -> build adjudication package -> explicit review record ->
human review -> later explicit fix or OpenSpec
```

Repo-visible artifact: this change will add `scripts/wiki_doctor_review_records.py`,
`scripts/build_wiki_content_adjudication.py`, `.codex/skills/wiki-doctor/SKILL.md`,
targeted tests, and optional `wiki/ops/wiki-doctor-runs/*-review.md` evidence.

Expected output: a Markdown diagnosis record with scan scope, summary, taxonomy
candidates, drift traces, eval result, proof boundary, and next review actions.

Promotion or non-promotion boundary: the review record does not become approved
frontmatter, taxonomy config, MOC pages, or OpenSpec task completion.

Proof boundary: this proves deterministic record generation and boundary text,
not semantic correctness of every candidate or multi-session enforcement.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/specs/behavior-replay-gate/spec.md`
- `wiki/ops/behavior-replay-gate.md`
- `openspec/changes/add-wiki-content-adjudication-eval/design.md`
- `openspec/changes/add-wiki-content-adjudication-eval/evaluation.md`
- `openspec/changes/rename-wiki-content-adjudication-skill-to-doctor/design.md`
- `.codex/skills/wiki-doctor/SKILL.md`

Owns:

- Explicit `wiki-doctor` diagnosis record generation.

References:

- Existing content adjudication package and eval.
- Existing behavior replay and skill evaluation gates.
- Existing review-only doctor boundary.

Rejects:

- Default file writes during ordinary diagnosis.
- Direct frontmatter writes from doctor output.
- Silent taxonomy mutation.
- Treating a diagnosis record as repair approval.

## Parent Gate Preservation

Parent gate: `wiki-doctor` remains a review-only diagnostic wrapper around the
content adjudication package. The new record is a persisted diagnosis, not an
apply or repair command.

## Residual Risks

- Human review remains required for taxonomy expansion and structure writes.
- A Markdown record can become stale after wiki content changes.
- This evidence does not prove future agents will always choose record
  generation unless the trigger is explicit.
```

- [ ] **Step 6: Validate OpenSpec skeleton**

Run:

```bash
openspec validate add-wiki-doctor-review-records --strict
```

Expected: PASS. If PostHog network flush warnings appear while the command exits
successfully, record that as a warning in `evaluation.md`.

- [ ] **Step 7: Commit OpenSpec skeleton**

Run:

```bash
git add openspec/changes/add-wiki-doctor-review-records
git commit -m "spec: add wiki-doctor review records change"
```

Expected: commit includes only the new OpenSpec change directory.

## Task 2: Add RED Tests for Review Records

**Files:**
- Modify: `tests/test_wiki_content_adjudication.py`

- [ ] **Step 1: Add imports for subprocess and json**

Patch the imports at the top of `tests/test_wiki_content_adjudication.py`:

```python
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
```

- [ ] **Step 2: Add failing test for Markdown rendering**

Add this test method to `WikiContentAdjudicationTest`:

```python
    def test_renders_wiki_doctor_review_record_markdown(self) -> None:
        from scripts.wiki_doctor_review_records import render_review_record_markdown

        package = {
            "generated_at": "2026-05-14T12:46:28+00:00",
            "summary": {
                "candidate_count": 2,
                "full_detail_count": 2,
                "review_focus_count": 1,
                "taxonomy_candidate_count": 1,
                "drift_trace_count": 1,
            },
            "taxonomy_candidate_set": [
                {
                    "field": "domain",
                    "value": "agent-runtime",
                    "detail_refs": ["detail-0001"],
                    "reason": "value absent from wiki/config/frontmatter-taxonomy.yaml",
                }
            ],
            "drift_trace_set": [
                {
                    "detail_ref": "detail-0002",
                    "path": "wiki/ops/runtime-drift-retro.md",
                    "risk_flags": ["drift_risk"],
                    "reason": "governance or drift signal requires explicit review",
                }
            ],
            "eval_result": {
                "passed": True,
                "errors": [],
                "warnings": ["detail-0002: relation candidate needs reviewed evidence"],
            },
            "proof_boundary_notes": [
                "Content adjudication is deterministic review output only.",
                "It does not write frontmatter.",
                "It does not mutate taxonomy config.",
            ],
        }

        markdown = render_review_record_markdown(package, scan_root=self.tmpdir, limit=50)

        self.assertIn("# wiki-doctor Review Record", markdown)
        self.assertIn("Scan root:", markdown)
        self.assertIn("candidate_count: 2", markdown)
        self.assertIn("agent-runtime", markdown)
        self.assertIn("detail-0002", markdown)
        self.assertIn("This record is diagnosis only.", markdown)
        self.assertIn("Human review", markdown)
        self.assertIn("OpenSpec candidate", markdown)
        self.assertNotIn("Approved frontmatter write", markdown)
```

- [ ] **Step 3: Add failing test for non-overwriting writes**

Add this test method:

```python
    def test_writes_review_record_without_overwriting_existing_file(self) -> None:
        from scripts.wiki_doctor_review_records import write_review_record

        package = {
            "generated_at": "2026-05-14T12:46:28+00:00",
            "summary": {
                "candidate_count": 0,
                "full_detail_count": 0,
                "review_focus_count": 0,
                "taxonomy_candidate_count": 0,
                "drift_trace_count": 0,
            },
            "taxonomy_candidate_set": [],
            "drift_trace_set": [],
            "eval_result": {"passed": True, "errors": [], "warnings": []},
            "proof_boundary_notes": ["It does not write frontmatter."],
        }
        output_dir = self.tmpdir / "wiki" / "ops" / "wiki-doctor-runs"

        first = write_review_record(
            package,
            root=self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-14T12:46:28+00:00",
        )
        second = write_review_record(
            package,
            root=self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-14T12:46:28+00:00",
        )

        self.assertTrue(first.exists())
        self.assertTrue(second.exists())
        self.assertNotEqual(first, second)
        self.assertEqual(first.name, "2026-05-14-124628-review.md")
        self.assertEqual(second.name, "2026-05-14-124628-review-2.md")
```

- [ ] **Step 4: Add failing test for explicit CLI write flag**

Add this test method:

```python
    def test_cli_writes_review_record_only_when_explicitly_requested(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "runtime-boundary-drift-retro.md").write_text(
            "# Runtime Boundary Drift\n\nThis drift retro records a runtime boundary.\n",
            encoding="utf-8",
        )
        output_dir = self.tmpdir / "wiki" / "ops" / "wiki-doctor-runs"

        default_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_content_adjudication.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "0",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(default_result.stdout)
        self.assertEqual(payload["mode"], "review_package")
        self.assertFalse(output_dir.exists())

        write_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_content_adjudication.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "0",
                "--write-review-record",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(write_result.stdout)
        self.assertEqual(payload["mode"], "review_package")
        self.assertIn("review_record_path", payload)
        record_path = Path(payload["review_record_path"])
        self.assertTrue(record_path.exists())
        self.assertEqual(record_path.parent, output_dir)
        self.assertIn("This record is diagnosis only.", record_path.read_text(encoding="utf-8"))
```

- [ ] **Step 5: Run RED tests**

Run:

```bash
python3 -m unittest tests/test_wiki_content_adjudication.py
```

Expected: FAIL because `scripts.wiki_doctor_review_records` does not exist and
the CLI does not recognize `--write-review-record`.

## Task 3: Implement Review Record Module and CLI Flag

**Files:**
- Create: `scripts/wiki_doctor_review_records.py`
- Modify: `scripts/build_wiki_content_adjudication.py`
- Modify: `tests/test_wiki_content_adjudication.py`

- [ ] **Step 1: Create review-record module**

Create `scripts/wiki_doctor_review_records.py`:

```python
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REVIEW_RECORD_DIR = Path("wiki/ops/wiki-doctor-runs")


def _parse_timestamp(value: str | None = None) -> datetime:
    if value:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    return datetime.now(timezone.utc)


def _record_name(timestamp: datetime, suffix: int | None = None) -> str:
    base = timestamp.astimezone(timezone.utc).strftime("%Y-%m-%d-%H%M%S-review")
    if suffix is not None:
        return f"{base}-{suffix}.md"
    return f"{base}.md"


def _limited(items: Any, count: int = 20) -> list[Any]:
    if not isinstance(items, list):
        return []
    return items[:count]


def _summary_lines(summary: dict[str, Any]) -> list[str]:
    keys = [
        "candidate_count",
        "full_detail_count",
        "review_focus_count",
        "taxonomy_candidate_count",
        "drift_trace_count",
    ]
    return [f"- {key}: {summary.get(key, 0)}" for key in keys]


def _bullet_lines(items: list[Any], empty: str) -> list[str]:
    if not items:
        return [f"- {empty}"]
    lines: list[str] = []
    for item in items:
        if isinstance(item, dict):
            detail = item.get("detail_ref") or ", ".join(item.get("detail_refs", []))
            path = item.get("path", "")
            label = item.get("value") or item.get("reason") or item.get("field") or "item"
            suffix = f" ({path})" if path else ""
            ref = f" [{detail}]" if detail else ""
            lines.append(f"- {label}{ref}{suffix}")
        else:
            lines.append(f"- {item}")
    return lines


def render_review_record_markdown(package: dict[str, Any], scan_root: Path | str, limit: int) -> str:
    summary = package.get("summary", {})
    eval_result = package.get("eval_result", {})
    warnings = eval_result.get("warnings", [])
    errors = eval_result.get("errors", [])
    generated_at = str(package.get("generated_at", "unknown"))
    lines = [
        "# wiki-doctor Review Record",
        "",
        "## Scan",
        "",
        f"- Generated at: {generated_at}",
        f"- Scan root: {Path(scan_root)}",
        f"- Detail limit: {limit}",
        "- Source: scripts/build_wiki_content_adjudication.py",
        "",
        "## Summary",
        "",
        *_summary_lines(summary),
        f"- eval_passed: {bool(eval_result.get('passed', False))}",
        f"- eval_error_count: {len(errors) if isinstance(errors, list) else 0}",
        f"- eval_warning_count: {len(warnings) if isinstance(warnings, list) else 0}",
        "",
        "## Taxonomy Candidates",
        "",
        *_bullet_lines(
            _limited(package.get("taxonomy_candidate_set"), 20),
            "No taxonomy candidates in this limited package.",
        ),
        "",
        "## Drift Traces",
        "",
        *_bullet_lines(
            _limited(package.get("drift_trace_set"), 20),
            "No drift traces in this limited package.",
        ),
        "",
        "## Eval Result",
        "",
        "### Errors",
        "",
        *_bullet_lines(_limited(errors, 20), "No eval errors."),
        "",
        "### Warnings",
        "",
        *_bullet_lines(_limited(warnings, 20), "No eval warnings."),
        "",
        "## Proof Boundary",
        "",
        "- This record is diagnosis only.",
        "- It does not approve frontmatter writes.",
        "- It does not mutate taxonomy config.",
        "- It does not write MOC pages.",
        "- It does not mark OpenSpec tasks complete.",
        *_bullet_lines(_limited(package.get("proof_boundary_notes"), 20), "No additional proof boundary notes."),
        "",
        "## Next Review Actions",
        "",
        "- Human review: inspect review focus and detail refs before accepting any structure change.",
        "- Discard: ignore candidates that lack evidence or repeat historical drift only.",
        "- OpenSpec candidate: create or select a change for taxonomy or workflow behavior changes.",
        "- Later explicit repair: apply frontmatter, taxonomy, or MOC changes only after approval.",
        "",
    ]
    return "\n".join(lines)


def next_review_record_path(output_dir: Path, timestamp: str | None = None) -> Path:
    parsed = _parse_timestamp(timestamp)
    candidate = output_dir / _record_name(parsed)
    if not candidate.exists():
        return candidate
    suffix = 2
    while True:
        candidate = output_dir / _record_name(parsed, suffix)
        if not candidate.exists():
            return candidate
        suffix += 1


def write_review_record(
    package: dict[str, Any],
    root: Path | str,
    output_dir: Path | str | None = None,
    timestamp: str | None = None,
    limit: int = 50,
) -> Path:
    root_path = Path(root)
    target_dir = Path(output_dir) if output_dir is not None else root_path / DEFAULT_REVIEW_RECORD_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    target = next_review_record_path(target_dir, timestamp)
    markdown = render_review_record_markdown(package, scan_root=root_path, limit=limit)
    target.write_text(markdown, encoding="utf-8")
    return target
```

- [ ] **Step 2: Wire CLI flags**

Patch `scripts/build_wiki_content_adjudication.py`:

```python
from scripts.wiki_content_adjudication import build_adjudication_package
from scripts.wiki_doctor_review_records import write_review_record
```

Add parser arguments after `--limit`:

```python
    parser.add_argument(
        "--write-review-record",
        action="store_true",
        help="Write a Markdown wiki-doctor review record under wiki/ops/wiki-doctor-runs.",
    )
    parser.add_argument(
        "--review-record-dir",
        default=None,
        help="Override the review-record output directory.",
    )
```

After limiting payload sets and before printing JSON, add:

```python
    if args.write_review_record:
        record_path = write_review_record(
            payload,
            root=Path(args.root).resolve(),
            output_dir=Path(args.review_record_dir).resolve() if args.review_record_dir else None,
            limit=limit,
        )
        payload["review_record_path"] = record_path.as_posix()
```

- [ ] **Step 3: Run targeted tests**

Run:

```bash
python3 -m unittest tests/test_wiki_content_adjudication.py
```

Expected: PASS.

- [ ] **Step 4: Run CLI smoke checks**

Run default non-writing mode:

```bash
python3 scripts/build_wiki_content_adjudication.py --limit 0
```

Expected: JSON includes `"mode": "review_package"` and does not include
`review_record_path`.

Run explicit write mode to `/tmp` first:

```bash
python3 scripts/build_wiki_content_adjudication.py --limit 0 --write-review-record --review-record-dir /tmp/wiki-doctor-review-record-check
```

Expected: JSON includes `review_record_path` under
`/tmp/wiki-doctor-review-record-check` and the file contains
`This record is diagnosis only.`

- [ ] **Step 5: Commit Python implementation**

Run:

```bash
git add scripts/wiki_doctor_review_records.py scripts/build_wiki_content_adjudication.py tests/test_wiki_content_adjudication.py
git commit -m "feat: add wiki-doctor review records"
```

Expected: commit includes only Python implementation and focused tests.

## Task 4: Update wiki-doctor Skill Contract

**Files:**
- Modify: `.codex/skills/wiki-doctor/SKILL.md`
- Modify: `tests/test_wiki_runtime_skills.py`
- Modify: `openspec/changes/add-wiki-doctor-review-records/evaluation.md`

- [ ] **Step 1: Update runtime skill markers**

In `tests/test_wiki_runtime_skills.py`, update the `wiki-doctor` marker tuple:

```python
    "wiki-doctor": (
        "scripts/build_wiki_content_adjudication.py",
        "--write-review-record",
        "wiki/ops/wiki-doctor-runs",
        "full_detail_set",
        "review_focus_set",
        "taxonomy_candidate_set",
        "drift_trace_set",
        "eval_result",
        "review-only",
    ),
```

- [ ] **Step 2: Run RED skill test**

Run:

```bash
python3 -m unittest tests/test_wiki_runtime_skills.py
```

Expected: FAIL because `.codex/skills/wiki-doctor/SKILL.md` does not yet mention
`--write-review-record` or `wiki/ops/wiki-doctor-runs`.

- [ ] **Step 3: Update skill body**

Patch `.codex/skills/wiki-doctor/SKILL.md` so the trigger list includes this
explicit record path after the package summary step:

```markdown
5. If the user explicitly asks to generate a diagnosis record, run
   `python3 scripts/build_wiki_content_adjudication.py --write-review-record`
   or the same command with `--review-record-dir`.
6. Treat generated files under `wiki/ops/wiki-doctor-runs/` as diagnosis
   records only. They are review evidence, not approval to apply repairs.
```

Add these boundaries:

```markdown
- Do not generate a review record unless the user explicitly asks for one.
- Do not treat a review record as approval to apply frontmatter, taxonomy, MOC,
  OpenSpec, or queued-work changes.
```

- [ ] **Step 4: Run GREEN skill test**

Run:

```bash
python3 -m unittest tests/test_wiki_runtime_skills.py
```

Expected: PASS.

- [ ] **Step 5: Commit skill contract**

Run:

```bash
git add .codex/skills/wiki-doctor/SKILL.md tests/test_wiki_runtime_skills.py
git commit -m "docs: define wiki-doctor review record contract"
```

Expected: commit includes only skill contract and runtime skill test changes.

## Task 5: Generate Evidence and Complete Evaluation

**Files:**
- Modify: `openspec/changes/add-wiki-doctor-review-records/evaluation.md`
- Modify: `openspec/changes/add-wiki-doctor-review-records/tasks.md`
- Optional create: `wiki/ops/wiki-doctor-runs/<timestamp>-review.md`

- [ ] **Step 1: Run full targeted test set**

Run:

```bash
python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_runtime_skills.py
```

Expected: PASS.

- [ ] **Step 2: Generate repo-visible review-record evidence**

Run:

```bash
python3 scripts/build_wiki_content_adjudication.py --limit 0 --write-review-record
```

Expected: JSON includes `review_record_path` under `wiki/ops/wiki-doctor-runs/`.
Inspect the generated file and confirm it includes:

```text
This record is diagnosis only.
Next Review Actions
```

- [ ] **Step 3: Run behavior asset check**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: PASS. If it fails because unrelated active behavior-asset changes are
already incomplete, record the exact non-zero result and unrelated paths in
`evaluation.md`.

- [ ] **Step 4: Validate OpenSpec**

Run:

```bash
openspec validate add-wiki-doctor-review-records --strict
```

Expected: PASS.

- [ ] **Step 5: Update evaluation evidence**

Replace the pending evidence table in
`openspec/changes/add-wiki-doctor-review-records/evaluation.md` with concrete
results:

```markdown
## Evidence

- `python3 -m unittest tests/test_wiki_content_adjudication.py`
  - RED baseline: failed before implementation because
    `scripts.wiki_doctor_review_records` did not exist and the CLI lacked
    `--write-review-record`.
  - GREEN result: passed after implementation.
- `python3 -m unittest tests/test_wiki_runtime_skills.py`
  - RED baseline: failed after adding markers because `wiki-doctor` did not
    mention explicit review-record generation.
  - GREEN result: passed after skill contract update.
- `python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_runtime_skills.py`
  - Result: passed.
- `python3 scripts/build_wiki_content_adjudication.py --limit 0`
  - Result: completed without `review_record_path`.
- `python3 scripts/build_wiki_content_adjudication.py --limit 0 --write-review-record`
  - Result: wrote a Markdown diagnosis record under `wiki/ops/wiki-doctor-runs/`.
- `python3 scripts/check_behavior_assets.py`
  - Result: passed.
- `openspec validate add-wiki-doctor-review-records --strict`
  - Result: passed.
```

Update each `Pressure Scenarios` row from `Not run in skeleton stage` to
`Passed` when confirmed.

- [ ] **Step 6: Mark tasks complete**

Update `openspec/changes/add-wiki-doctor-review-records/tasks.md` so all six
items are checked only after their corresponding evidence exists.

- [ ] **Step 7: Commit evidence**

Run:

```bash
git add openspec/changes/add-wiki-doctor-review-records wiki/ops/wiki-doctor-runs
git commit -m "test: record wiki-doctor review evidence"
```

Expected: commit includes OpenSpec evidence and the intentionally generated
review record, if generated.

## Task 6: Final Verification

**Files:**
- No new source edits expected.

- [ ] **Step 1: Re-run final commands**

Run:

```bash
python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_runtime_skills.py
python3 scripts/check_behavior_assets.py
openspec validate add-wiki-doctor-review-records --strict
```

Expected: all pass, except any known unrelated behavior-asset failure must
already be documented in `evaluation.md`.

- [ ] **Step 2: Verify git state and latest commit**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: task-related files are either committed or intentionally staged for a
final commit. Unrelated pre-existing modified/untracked files remain excluded.

- [ ] **Step 3: Stop at OpenSpec completion boundary**

If `openspec/changes/add-wiki-doctor-review-records/tasks.md` is fully checked,
stop implementation. The default next action is archive review, not additional
automation or adjacent wiki repair.
