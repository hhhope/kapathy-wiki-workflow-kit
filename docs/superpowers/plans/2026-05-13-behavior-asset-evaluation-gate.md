# Behavior Asset Evaluation Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an executable behavior-asset evaluation gate for skill and runtime-routing changes.

**Architecture:** `AGENTS.md` keeps the hard rule, `wiki/config/behavior-asset-evaluation.yaml` owns detailed checker vocabulary, `scripts/check_behavior_assets.py` performs validation and report writing, and `scripts/repo_health_check.py` aggregates the result. The implementation follows the wiki frontmatter checker pattern and fixes the current Agent Intent Routing route-table drift as the first proven case.

**Tech Stack:** Python standard library, PyYAML already used by repo scripts, `unittest`, OpenSpec Markdown artifacts.

---

## Parallelization Map

Task 1 is a serial prerequisite because repo workflow changes require an active OpenSpec change before editing behavior assets.

After Task 1 lands, Tasks 2, 3, and 4 can run in parallel with disjoint write ownership:

- Task 2 owns `wiki/config/behavior-asset-evaluation.yaml`, `scripts/check_behavior_assets.py`, and `tests/test_behavior_asset_evaluation.py`.
- Task 3 owns `scripts/repo_health_check.py` and `tests/test_repo_health_check.py`.
- Task 4 owns `AGENTS.md` and `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`.

Task 5 is the integration and evaluation closeout after Tasks 2-4 land.

## File Structure

- Create `openspec/changes/harden-behavior-asset-evaluation-gate/proposal.md`: scope and rationale.
- Create `openspec/changes/harden-behavior-asset-evaluation-gate/design.md`: implementation design tied to the superpowers spec.
- Create `openspec/changes/harden-behavior-asset-evaluation-gate/tasks.md`: executable task checklist.
- Create `openspec/changes/harden-behavior-asset-evaluation-gate/specs/behavior-asset-evaluation-gate/spec.md`: formal requirements.
- Create `openspec/changes/harden-behavior-asset-evaluation-gate/evaluation.md`: RED/GREEN behavior evidence.
- Create `wiki/config/behavior-asset-evaluation.yaml`: source of truth for covered paths, required sections, replay fields, scenario markers, ownership rules, and severity.
- Create `scripts/check_behavior_assets.py`: behavior asset checker and report writer.
- Create `tests/test_behavior_asset_evaluation.py`: focused checker tests using temporary repositories.
- Modify `scripts/repo_health_check.py`: call the behavior asset checker as a named health result.
- Modify `tests/test_repo_health_check.py`: cover health-check integration.
- Modify `AGENTS.md`: compress Agent Intent Routing, route repo-public artifacts through High-Frequency Skills, and add the hard checker command.
- Modify `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`: add a drift replay case that fails when Agent Intent Routing duplicates the routing table.

---

### Task 1: OpenSpec Change Boundary

**Files:**
- Create: `openspec/changes/harden-behavior-asset-evaluation-gate/proposal.md`
- Create: `openspec/changes/harden-behavior-asset-evaluation-gate/design.md`
- Create: `openspec/changes/harden-behavior-asset-evaluation-gate/tasks.md`
- Create: `openspec/changes/harden-behavior-asset-evaluation-gate/specs/behavior-asset-evaluation-gate/spec.md`

- [ ] **Step 1: Create the OpenSpec directory**

Run:

```bash
mkdir -p openspec/changes/harden-behavior-asset-evaluation-gate/specs/behavior-asset-evaluation-gate
```

Expected: directory exists.

- [ ] **Step 2: Write `proposal.md`**

Create `openspec/changes/harden-behavior-asset-evaluation-gate/proposal.md` with:

```markdown
# harden-behavior-asset-evaluation-gate

## Why

The repo already requires `evaluation.md` for semantic skill changes, but the
current gate can pass shallow evidence. It checks for required section names but
does not prove positive and negative behavior, parent-gate preservation, or
non-overlapping routing ownership.

The Agent Intent Routing drift showed the gap: `High-Frequency Skills` already
owned the runtime skill routing map, while a new `Agent Intent Routing` section
introduced a second route table. Existing tests proved routing text existed but
did not detect duplicate ownership.

## What Changes

- Add `wiki/config/behavior-asset-evaluation.yaml` as the checker contract.
- Add `scripts/check_behavior_assets.py` for executable behavior-asset checks.
- Integrate the checker into `scripts/repo_health_check.py`.
- Compress `AGENTS.md` Agent Intent Routing so it references the single
  High-Frequency Skills route table instead of duplicating it.
- Strengthen pressure scenarios and evaluation evidence for skill and runtime
  routing changes.

## Non-Goals

- Do not scan archived OpenSpec changes by default.
- Do not build a general semantic static analyzer.
- Do not require multi-session rollout telemetry as the minimum gate.
```

- [ ] **Step 3: Write `design.md`**

Copy the accepted superpowers design into OpenSpec scope:

```bash
cp docs/superpowers/specs/2026-05-13-behavior-asset-evaluation-gate-design.md \
  openspec/changes/harden-behavior-asset-evaluation-gate/design.md
```

Expected: `design.md` contains the accepted Behavior Asset Evaluation Gate design.

- [ ] **Step 4: Write `tasks.md`**

Create `openspec/changes/harden-behavior-asset-evaluation-gate/tasks.md` with:

```markdown
# Tasks

- [ ] 1. Create OpenSpec change artifacts for behavior asset evaluation gate.
- [ ] 2. Add RED tests for behavior asset checker and current Agent Intent Routing drift.
- [ ] 3. Add behavior asset evaluation config and checker.
- [ ] 4. Integrate behavior asset checker into repo health check.
- [ ] 5. Compress Agent Intent Routing and strengthen skill pressure scenarios.
- [ ] 6. Record RED/GREEN evaluation evidence.
- [ ] 7. Run targeted tests, checker, repo health check, OpenSpec validation, and diff check.
```

- [ ] **Step 5: Write the spec**

Create `openspec/changes/harden-behavior-asset-evaluation-gate/specs/behavior-asset-evaluation-gate/spec.md` with:

```markdown
## Purpose

Define an executable behavior-asset evaluation gate for semantic skill changes
and repo runtime-routing changes.

## Requirements

### Requirement: Repository SHALL evaluate behavior-asset changes with executable evidence

Behavior-asset changes SHALL include evaluation evidence that proves more than
section presence.

#### Scenario: Active change edits a behavior asset

- **WHEN** an active OpenSpec change references or edits `.codex/skills/*`,
  `AGENTS.md` runtime routing, skill triggers, parent gates, hard stops,
  publish/sync behavior, or future runtime behavior
- **THEN** the change SHALL include `evaluation.md`
- **AND** the evaluation SHALL include pressure scenarios, RED baseline, GREEN
  result, residual risks, replay fields, positive and negative cases, and proof
  boundary

### Requirement: Repository SHALL expose a behavior asset checker

The repository SHALL provide a local checker that users and agents can run.

#### Scenario: User runs the checker

- **WHEN** `python3 scripts/check_behavior_assets.py` runs
- **THEN** it SHALL inspect active OpenSpec changes and current behavior assets
- **AND** it SHALL write JSON and Markdown reports under `/tmp`
- **AND** it SHALL exit non-zero when error-severity drift exists

### Requirement: Agent Intent Routing SHALL not duplicate the skill route table

Agent Intent Routing SHALL remain a pre-action classification rule and SHALL
not duplicate the High-Frequency Skills routing table.

#### Scenario: Agent Intent Routing contains a route table

- **WHEN** `AGENTS.md` has `High-Frequency Skills`
- **AND** `Agent Intent Routing` contains `Minimum routes` or a multi-row
  parent-gate route table
- **THEN** the behavior asset checker SHALL report error-severity route-table
  ownership drift

### Requirement: Repo health check SHALL aggregate behavior asset results

The repo health check SHALL expose behavior asset evaluation as a named check.

#### Scenario: Behavior asset checker fails

- **WHEN** `python3 scripts/repo_health_check.py` runs
- **AND** behavior asset evaluation has error-severity entries
- **THEN** repo health check SHALL report `FAIL behavior-asset-evaluation`
```

- [ ] **Step 6: Validate OpenSpec change**

Run:

```bash
openspec validate harden-behavior-asset-evaluation-gate --strict
```

Expected: change is valid. If `openspec` is unavailable, record the command and failure in the change evaluation.

- [ ] **Step 7: Commit Task 1**

Run:

```bash
git add openspec/changes/harden-behavior-asset-evaluation-gate
git commit -m "docs: propose behavior asset evaluation gate"
```

Expected: commit contains only the new OpenSpec change files.

---

### Task 2: Behavior Asset Checker

**Files:**
- Create: `wiki/config/behavior-asset-evaluation.yaml`
- Create: `scripts/check_behavior_assets.py`
- Create: `tests/test_behavior_asset_evaluation.py`

- [ ] **Step 1: Write failing checker tests**

Create `tests/test_behavior_asset_evaluation.py` with tests covering:

```python
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_behavior_assets import check_behavior_assets


class BehaviorAssetEvaluationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="behavior-assets-"))
        (self.tmpdir / "wiki/config").mkdir(parents=True)
        (self.tmpdir / "openspec/changes").mkdir(parents=True)
        (self.tmpdir / "AGENTS.md").write_text(
            "## High-Frequency Skills\n\n| Situation | Load |\n|---|---|\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def write_config(self) -> None:
        (self.tmpdir / "wiki/config/behavior-asset-evaluation.yaml").write_text(
            """
severity:
  missing_evaluation: error
  missing_required_section: error
  missing_negative_scenario: error
  missing_parent_gate_preservation: error
  route_table_ownership_drift: error
  weak_replay_evidence: warn
required_sections:
  - "## Pressure Scenarios"
  - "## RED Baseline"
  - "## GREEN Result"
  - "## Residual Risks"
required_replay_fields:
  - "input or situation shape"
  - "trigger condition"
  - "repo-visible artifact"
  - "expected output"
  - "proof boundary"
positive_markers:
  - "positive"
  - "trigger"
negative_markers:
  - "negative"
  - "should-not-trigger"
parent_gate_markers:
  - "parent gate"
  - "preserve"
covered_change_markers:
  - ".codex/skills/"
  - "AGENTS.md"
  - "runtime routing"
  - "parent gate"
ownership_rules:
  agent_intent_routing:
    owner_section: "High-Frequency Skills"
    classification_section: "Agent Intent Routing"
    forbidden_markers:
      - "Minimum routes"
      - "| Intent shape | Parent gate |"
""",
            encoding="utf-8",
        )

    def test_missing_evaluation_for_skill_change_is_error(self) -> None:
        self.write_config()
        change = self.tmpdir / "openspec/changes/skill-change"
        change.mkdir(parents=True)
        (change / "proposal.md").write_text("Change .codex/skills/example/SKILL.md\n", encoding="utf-8")

        entries = check_behavior_assets(self.tmpdir)

        self.assertTrue(any(entry.kind == "missing_evaluation" for entry in entries))

    def test_route_table_ownership_drift_is_error(self) -> None:
        self.write_config()
        (self.tmpdir / "AGENTS.md").write_text(
            "## High-Frequency Skills\n\n| Situation | Load |\n|---|---|\n\n"
            "## Agent Intent Routing\n\nMinimum routes:\n\n| Intent shape | Parent gate |\n|---|---|\n",
            encoding="utf-8",
        )

        entries = check_behavior_assets(self.tmpdir)

        self.assertTrue(any(entry.kind == "route_table_ownership_drift" for entry in entries))

    def test_valid_behavior_evaluation_passes(self) -> None:
        self.write_config()
        change = self.tmpdir / "openspec/changes/skill-change"
        change.mkdir(parents=True)
        (change / "proposal.md").write_text("Change .codex/skills/example/SKILL.md parent gate\n", encoding="utf-8")
        (change / "evaluation.md").write_text(
            """## Pressure Scenarios

| Case | Expected |
|---|---|
| positive trigger case | load skill |
| negative should-not-trigger case | do not load skill |
| parent gate preserve case | preserve parent gate blockers |

## Replay Evidence

- input or situation shape: semantic skill change
- trigger condition: `.codex/skills/*` edit
- repo-visible artifact: AGENTS.md and skill file
- expected output: route before edit
- proof boundary: local checker proof only

## RED Baseline

Observed failing command: `python3 scripts/check_behavior_assets.py` reported missing gate.

## GREEN Result

Manual replay record: file paths and expected observations are listed above.

## Residual Risks

Future agents must load repo guidance.
""",
            encoding="utf-8",
        )

        entries = check_behavior_assets(self.tmpdir)

        self.assertEqual([entry for entry in entries if entry.severity == "error"], [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_behavior_asset_evaluation -v
```

Expected: fail because `scripts.check_behavior_assets` does not exist.

- [ ] **Step 3: Add config**

Create `wiki/config/behavior-asset-evaluation.yaml` with the same keys used by the tests. Keep values focused on current requirements and current drift.

- [ ] **Step 4: Implement checker**

Create `scripts/check_behavior_assets.py` with:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path("wiki/config/behavior-asset-evaluation.yaml")
REPORT_JSON = Path("/tmp/behavior-asset-evaluation-report.json")
REPORT_MD = Path("/tmp/behavior-asset-evaluation-report.md")


@dataclass(frozen=True)
class BehaviorAssetEntry:
    kind: str
    severity: str
    path: str
    message: str


def load_config(repo_root: Path) -> dict[str, Any]:
    with (repo_root / CONFIG_PATH).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"config must be a mapping: {CONFIG_PATH}")
    return data


def severity(config: dict[str, Any], kind: str, default: str = "warn") -> str:
    return str(config.get("severity", {}).get(kind, default))


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def active_change_dirs(repo_root: Path) -> list[Path]:
    root = repo_root / "openspec/changes"
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and path.name != "archive")


def change_text(change_dir: Path) -> str:
    parts = []
    for path in sorted(change_dir.rglob("*.md")):
        if path.name == "evaluation.md":
            continue
        parts.append(read_text(path))
    return "\n".join(parts)


def change_is_behavior_asset_change(change_dir: Path, config: dict[str, Any]) -> bool:
    text = change_text(change_dir)
    markers = [str(value) for value in config.get("covered_change_markers", [])]
    return any(marker in text for marker in markers)


def check_evaluation(change_dir: Path, repo_root: Path, config: dict[str, Any]) -> list[BehaviorAssetEntry]:
    evaluation = change_dir / "evaluation.md"
    change_rel = rel(change_dir, repo_root)
    if not evaluation.exists():
        return [
            BehaviorAssetEntry(
                kind="missing_evaluation",
                severity=severity(config, "missing_evaluation", "error"),
                path=change_rel,
                message="Behavior-asset change requires evaluation.md.",
            )
        ]

    content = read_text(evaluation)
    entries: list[BehaviorAssetEntry] = []
    for section in config.get("required_sections", []):
        if str(section) not in content:
            entries.append(
                BehaviorAssetEntry(
                    kind="missing_required_section",
                    severity=severity(config, "missing_required_section", "error"),
                    path=rel(evaluation, repo_root),
                    message=f"Missing required evaluation section: {section}",
                )
            )

    lower = content.lower()
    if not any(str(marker).lower() in lower for marker in config.get("negative_markers", [])):
        entries.append(
            BehaviorAssetEntry(
                kind="missing_negative_scenario",
                severity=severity(config, "missing_negative_scenario", "error"),
                path=rel(evaluation, repo_root),
                message="Evaluation requires a negative or should-not-trigger scenario.",
            )
        )

    change_lower = change_text(change_dir).lower()
    parent_sensitive = any(marker in change_lower for marker in ["parent gate", "route", "publish", "sync", "reader-facing", "lightweight path", "full path"])
    if parent_sensitive and not any(str(marker).lower() in lower for marker in config.get("parent_gate_markers", [])):
        entries.append(
            BehaviorAssetEntry(
                kind="missing_parent_gate_preservation",
                severity=severity(config, "missing_parent_gate_preservation", "error"),
                path=rel(evaluation, repo_root),
                message="Parent-gate-sensitive behavior requires preservation evidence.",
            )
        )

    for field in config.get("required_replay_fields", []):
        if str(field).lower() not in lower:
            entries.append(
                BehaviorAssetEntry(
                    kind="weak_replay_evidence",
                    severity=severity(config, "weak_replay_evidence", "warn"),
                    path=rel(evaluation, repo_root),
                    message=f"Replay evidence does not mention: {field}",
                )
            )
    return entries


def section_between(text: str, start_heading: str, next_heading_prefix: str = "## ") -> str:
    start = text.find(start_heading)
    if start == -1:
        return ""
    next_start = text.find(next_heading_prefix, start + len(start_heading))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def check_agent_intent_ownership(repo_root: Path, config: dict[str, Any]) -> list[BehaviorAssetEntry]:
    agents = repo_root / "AGENTS.md"
    if not agents.exists():
        return []
    text = read_text(agents)
    rules = config.get("ownership_rules", {}).get("agent_intent_routing", {})
    owner = str(rules.get("owner_section", "High-Frequency Skills"))
    section_name = str(rules.get("classification_section", "Agent Intent Routing"))
    if f"## {owner}" not in text or f"## {section_name}" not in text:
        return []
    section = section_between(text, f"## {section_name}")
    forbidden = [str(value) for value in rules.get("forbidden_markers", [])]
    entries = []
    for marker in forbidden:
        if marker in section:
            entries.append(
                BehaviorAssetEntry(
                    kind="route_table_ownership_drift",
                    severity=severity(config, "route_table_ownership_drift", "error"),
                    path="AGENTS.md",
                    message=f"`{section_name}` duplicates route-table ownership via `{marker}`.",
                )
            )
    return entries


def check_behavior_assets(repo_root: Path | str) -> list[BehaviorAssetEntry]:
    root = Path(repo_root)
    config = load_config(root)
    entries: list[BehaviorAssetEntry] = []
    for change_dir in active_change_dirs(root):
        if change_is_behavior_asset_change(change_dir, config):
            entries.extend(check_evaluation(change_dir, root, config))
    entries.extend(check_agent_intent_ownership(root, config))
    return entries


def write_reports(entries: list[BehaviorAssetEntry]) -> None:
    REPORT_JSON.write_text(json.dumps([asdict(entry) for entry in entries], ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Behavior Asset Evaluation Report", ""]
    if not entries:
        lines.append("No behavior asset evaluation drift found.")
    else:
        for entry in entries:
            lines.append(f"- `{entry.severity}` `{entry.kind}` `{entry.path}`: {entry.message}")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check behavior asset evaluation evidence.")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    entries = check_behavior_assets(Path(args.repo_root).resolve())
    write_reports(entries)
    for entry in entries:
        print(f"{entry.severity.upper()} {entry.kind} {entry.path}: {entry.message}")
    return 1 if any(entry.severity == "error" for entry in entries) else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run checker tests**

Run:

```bash
python3 -m unittest tests.test_behavior_asset_evaluation -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit Task 2**

Run:

```bash
git add wiki/config/behavior-asset-evaluation.yaml scripts/check_behavior_assets.py tests/test_behavior_asset_evaluation.py
git commit -m "feat: add behavior asset evaluation checker"
```

---

### Task 3: Repo Health Check Integration

**Files:**
- Modify: `scripts/repo_health_check.py`
- Modify: `tests/test_repo_health_check.py`

- [ ] **Step 1: Add failing health-check tests**

Update `tests/test_repo_health_check.py` so clean repos report three checks and a temp repo with route ownership drift reports `FAIL behavior-asset-evaluation`. Add helper config creation matching Task 2's config keys.

- [ ] **Step 2: Run health-check tests and verify failure**

Run:

```bash
python3 -m unittest tests.test_repo_health_check -v
```

Expected: fail because the new health result is not integrated yet.

- [ ] **Step 3: Integrate checker**

Modify `scripts/repo_health_check.py`:

```python
from scripts.check_behavior_assets import check_behavior_assets
```

Inside `run_health_checks`, add:

```python
    behavior_asset_violations = [
        f"{entry.path}: {entry.kind}: {entry.message}"
        for entry in check_behavior_assets(repo_root)
        if entry.severity == "error"
    ]
```

Return a third result:

```python
        HealthCheckResult(
            name="behavior-asset-evaluation",
            passed=not behavior_asset_violations,
            details=behavior_asset_violations,
        ),
```

- [ ] **Step 4: Run health-check tests**

Run:

```bash
python3 -m unittest tests.test_repo_health_check tests.test_behavior_asset_evaluation -v
```

Expected: all tests pass.

- [ ] **Step 5: Commit Task 3**

Run:

```bash
git add scripts/repo_health_check.py tests/test_repo_health_check.py
git commit -m "feat: include behavior asset gate in health check"
```

---

### Task 4: Runtime Guidance Compression

**Files:**
- Modify: `AGENTS.md`
- Modify: `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`
- Test: existing `tests/test_agent_intent_routing.py` may need focused updates if it asserts the old duplicated table.

- [ ] **Step 1: Update RED test for route-table drift**

If `tests/test_agent_intent_routing.py` still expects `Minimum routes`, change it to expect the compressed shape:

```python
def test_agent_intent_routing_references_single_route_table(self) -> None:
    text = read(AGENTS)
    self.assertIn("## High-Frequency Skills", text)
    self.assertIn("## Agent Intent Routing", text)
    agent_intent = text.split("## Agent Intent Routing", 1)[1].split("\n## ", 1)[0]
    self.assertIn("High-Frequency Skills", agent_intent)
    self.assertNotIn("Minimum routes", agent_intent)
    self.assertNotIn("| Intent shape | Parent gate |", agent_intent)
```

- [ ] **Step 2: Run test and verify current drift fails**

Run:

```bash
python3 -m unittest tests.test_agent_intent_routing -v
```

Expected: fail while `AGENTS.md` still has `Minimum routes`.

- [ ] **Step 3: Compress `AGENTS.md`**

Change `High-Frequency Skills` to include repo-public artifacts in the public gate row. Replace the `Agent Intent Routing` `Minimum routes` table with short pre-action rules:

```markdown
## Agent Intent Routing

- Before acting, classify the user intent.
- Use `High-Frequency Skills` as the single repo-local skill routing table.
- If the request writes, rewrites, polishes, prepares, or updates an artifact
  that will be read outside the current chat or worklog, route through the
  applicable parent gate before editing.
- Repo-public artifact work, including `README.md`, `docs/*`, `examples/*`, and
  published templates, routes through `.codex/skills/public-report-quality-gate/SKILL.md`
  lightweight path.
- README work must scan relevant `README SHALL`, `README`, and `readme` hits in
  `AGENTS.md`, `PROJECT.md`, `openspec/specs`, `.codex/skills`, `wiki/adr`, and
  `wiki/ops` before drafting.
- Do not let the public gate replace specialized gates for frontmatter,
  semantic skill edits, OpenSpec lifecycle, or external learning.
- Do not add route tables, taxonomy vocabulary, report scorecards, or long
  examples here. Detailed behavior-asset evaluation rules live in
  `wiki/config/behavior-asset-evaluation.yaml`.
```

Add this hard checker command near the Skill Authoring Contract or Behavior Replay Gate:

```markdown
- Before claiming a behavior-asset change complete, run
  `python3 scripts/check_behavior_assets.py` and preserve any expected
  non-zero result in `evaluation.md`.
```

- [ ] **Step 4: Add pressure scenario**

Append or update `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md` with a case:

```markdown
| `Agent Intent Routing` adds a second parent-gate route table while `High-Frequency Skills` already owns runtime skill routes | Behavior Asset Evaluation Gate | FAIL; keep `High-Frequency Skills` as the single route table and keep Agent Intent Routing as pre-action classification |
```

- [ ] **Step 5: Run guidance tests**

Run:

```bash
python3 -m unittest tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit Task 4**

Run:

```bash
git add AGENTS.md .codex/skills/public-report-quality-gate/references/pressure-scenarios.md tests/test_agent_intent_routing.py
git commit -m "docs: compress behavior asset routing guidance"
```

---

### Task 5: Evaluation, Integration, and Completion

**Files:**
- Create: `openspec/changes/harden-behavior-asset-evaluation-gate/evaluation.md`
- Modify: `openspec/changes/harden-behavior-asset-evaluation-gate/tasks.md`

- [ ] **Step 1: Run the new checker on current repo**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected after Tasks 2-4: no error-severity drift. Warns are acceptable only if documented in `evaluation.md`.

- [ ] **Step 2: Run repo health check**

Run:

```bash
python3 scripts/repo_health_check.py
```

Expected: `PASS behavior-asset-evaluation`. If unrelated existing checks fail, record exact failures and classify them in `evaluation.md`.

- [ ] **Step 3: Run targeted tests**

Run:

```bash
python3 -m unittest tests.test_behavior_asset_evaluation tests.test_repo_health_check tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
```

Expected: all targeted tests pass.

- [ ] **Step 4: Validate OpenSpec**

Run:

```bash
openspec validate harden-behavior-asset-evaluation-gate --strict
```

Expected: valid.

- [ ] **Step 5: Run diff check**

Run:

```bash
git diff --check
```

Expected: no whitespace errors.

- [ ] **Step 6: Write `evaluation.md`**

Create `openspec/changes/harden-behavior-asset-evaluation-gate/evaluation.md` with:

```markdown
# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| Active skill change lacks `evaluation.md` | `check_behavior_assets.py` reports `missing_evaluation` error | `tests.test_behavior_asset_evaluation` |
| Active `AGENTS.md` runtime routing change lacks `evaluation.md` | Checker reports missing behavior proof | `tests.test_behavior_asset_evaluation` or `tests.test_repo_health_check` |
| `evaluation.md` has required headings but no negative scenario | Checker reports `missing_negative_scenario` error | `tests.test_behavior_asset_evaluation` |
| `Agent Intent Routing` duplicates High-Frequency Skills route table | Checker reports `route_table_ownership_drift` error | `tests.test_behavior_asset_evaluation` |
| Compressed Agent Intent Routing references High-Frequency Skills only | Checker reports no route-table ownership error | `python3 scripts/check_behavior_assets.py` |

## Replay Evidence

| Replay Field | Evidence |
|---|---|
| input or situation shape | Semantic skill edit, skill reference edit, or `AGENTS.md` runtime route/hard-stop/parent-gate change. |
| trigger condition | Active OpenSpec change references covered behavior-asset markers or current `AGENTS.md` contains known route ownership drift. |
| expected route, stop, refusal, or boundary behavior | Future agent runs `python3 scripts/check_behavior_assets.py` before claiming behavior-asset completion. |
| repo-visible artifact a future agent should read | `AGENTS.md`, `wiki/config/behavior-asset-evaluation.yaml`, `scripts/check_behavior_assets.py`, and this OpenSpec change. |
| expected output or non-output | Checker emits terminal output and `/tmp` reports; error-severity drift blocks completion claims. |
| promotion or non-promotion boundary | This is repo-local governance only; it does not promote rules to root AGENTS or team lore. |
| proof boundary | Tests and checker prove local structural and evidence requirements, not universal future-agent compliance. |

## RED Baseline

- Existing Agent Intent Routing contained a second route table under `Minimum routes`.
- Existing repo health check only verified `evaluation.md` section names for skill-touching changes.
- Initial checker tests failed before `scripts/check_behavior_assets.py` existed.

## GREEN Result

- `python3 -m unittest tests.test_behavior_asset_evaluation tests.test_repo_health_check tests.test_agent_intent_routing tests.test_public_report_quality_gate -v` passed.
- `python3 scripts/check_behavior_assets.py` completed with no error-severity behavior asset drift.
- `python3 scripts/repo_health_check.py` reported `PASS behavior-asset-evaluation`.
- `openspec validate harden-behavior-asset-evaluation-gate --strict` passed.
- `git diff --check` passed.

## Residual Risks

- Text-level checks can miss subtle semantic drift.
- Manual replay records can be incomplete.
- Archived changes are not scanned by default.
- Weak replay evidence remains warn-level in the first rollout.
```

- [ ] **Step 7: Mark tasks complete**

Update `tasks.md` checkboxes only after the evidence above is true. If a command cannot run, keep the relevant task unchecked and record the blocker.

- [ ] **Step 8: Commit Task 5**

Run:

```bash
git add openspec/changes/harden-behavior-asset-evaluation-gate/evaluation.md openspec/changes/harden-behavior-asset-evaluation-gate/tasks.md
git commit -m "docs: evaluate behavior asset gate"
```

---

## Final Verification

Run:

```bash
python3 -m unittest tests.test_behavior_asset_evaluation tests.test_repo_health_check tests.test_agent_intent_routing tests.test_public_report_quality_gate -v
python3 scripts/check_behavior_assets.py
python3 scripts/repo_health_check.py
openspec validate harden-behavior-asset-evaluation-gate --strict
git diff --check
git status --short
git log -1 --oneline
```

Expected:

- targeted tests pass
- behavior asset checker has no error-severity drift
- repo health check includes `PASS behavior-asset-evaluation`
- OpenSpec change validates
- diff check is clean
- only unrelated pre-existing dirty files remain outside task files
