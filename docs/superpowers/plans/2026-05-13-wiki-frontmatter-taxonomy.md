# Wiki Frontmatter Taxonomy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repo-local taxonomy contract and checker so wiki frontmatter cannot silently drift back to `domain: personal-ops`.

**Architecture:** OpenSpec owns the change boundary. `wiki/config/frontmatter-taxonomy.yaml` is the single vocabulary and policy source. `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` routes human/agent work through the contract, while `scripts/check_wiki_frontmatter.py` provides machine evidence for content drift, producer drift, and possible unregistered producers.

**Tech Stack:** Python 3, PyYAML, pytest, Markdown, repo-local Codex skills, OpenSpec artifacts.

---

## File Structure

- Create `openspec/changes/stabilize-wiki-frontmatter-taxonomy/proposal.md`: OpenSpec proposal and scope.
- Create `openspec/changes/stabilize-wiki-frontmatter-taxonomy/design.md`: implementation design and boundary decisions.
- Create `openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md`: execution checklist.
- Create `openspec/changes/stabilize-wiki-frontmatter-taxonomy/specs/wiki-frontmatter-taxonomy/spec.md`: behavior requirements.
- Create `openspec/changes/stabilize-wiki-frontmatter-taxonomy/evaluation.md`: RED/GREEN evidence for skill and behavior changes.
- Create `wiki/config/frontmatter-taxonomy.yaml`: single taxonomy contract.
- Create `scripts/check_wiki_frontmatter.py`: checker CLI and reusable functions.
- Create `tests/test_wiki_frontmatter_taxonomy.py`: checker tests.
- Create `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`: gate skill for frontmatter work.
- Modify `AGENTS.md`: route frontmatter changes through the taxonomy skill and checker.
- Modify `.codex/skills/article-learning-capture/references/wiki-template.md`: remove hardcoded `domain: personal-ops`.
- Modify `wiki/templates/*.md`: add `layer` and use contract-compatible placeholders.
- Modify `scripts/inbox_intake.py`: emit `layer`, `ops_area`, and `classification_needed` when needed.
- Modify `tests/test_inbox_intake.py`: cover new generated frontmatter.
- Modify five sample wiki pages listed in the design spec.

---

### Task 1: Create OpenSpec Change Boundary

**Files:**
- Create: `openspec/changes/stabilize-wiki-frontmatter-taxonomy/proposal.md`
- Create: `openspec/changes/stabilize-wiki-frontmatter-taxonomy/design.md`
- Create: `openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md`
- Create: `openspec/changes/stabilize-wiki-frontmatter-taxonomy/specs/wiki-frontmatter-taxonomy/spec.md`

- [ ] **Step 1: Create the OpenSpec directories**

Run:

```bash
mkdir -p openspec/changes/stabilize-wiki-frontmatter-taxonomy/specs/wiki-frontmatter-taxonomy
```

Expected: command exits `0`.

- [ ] **Step 2: Add `proposal.md`**

Write `openspec/changes/stabilize-wiki-frontmatter-taxonomy/proposal.md`:

```markdown
# stabilize-wiki-frontmatter-taxonomy

## Why

The repository currently allows `domain` to mean both real business or topic
domain and personal operations layer. This caused pages with
`domain: personal-ops` to look like business-domain records even though
`wiki/ops` is an operations and governance layer.

The drift is not limited to existing pages. Repo-local skills, templates,
scripts, and AI-authored markdown can each produce frontmatter differently.
The repository needs one contract, one gate skill, and one checker to stop new
drift and make legacy drift visible.

## What Changes

- Add `wiki/config/frontmatter-taxonomy.yaml` as the single taxonomy contract.
- Add `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` as the routing gate for
  wiki frontmatter work.
- Add `scripts/check_wiki_frontmatter.py` to report content drift, registered
  producer drift, and possible unregistered producer warnings.
- Add AGENTS routing so frontmatter changes must use the taxonomy skill and
  checker before completion claims.
- Update known producer templates and `scripts/inbox_intake.py` so they stop
  generating `domain: personal-ops`.
- Migrate five sample pages to prove `domain: none`, real domains, and
  `ops_area` behavior.
- Record RED/GREEN evidence in `evaluation.md`.

## Out of Scope

- Batch migration of all legacy ops pages.
- Full business domain taxonomy redesign.
- Scorecard scoring formula changes.
- Graph UI, query engine, or broad static analysis of arbitrary Python code.
- Global agent instruction changes.

## Source Design

- `docs/superpowers/specs/2026-05-13-wiki-frontmatter-taxonomy-design.md`
```

- [ ] **Step 3: Add `design.md`**

Write `openspec/changes/stabilize-wiki-frontmatter-taxonomy/design.md`:

```markdown
# Design

## Contract Boundary

`wiki/config/frontmatter-taxonomy.yaml` is the only source for allowed values,
forbidden values, path rules, severity, producer paths, and sample migration
paths. AGENTS and skills must not duplicate taxonomy vocabularies.

## Runtime Boundary

`.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` owns workflow only:

- when to load the taxonomy contract
- how to treat user and AI language as classification hints
- how to run the checker
- how to interpret drift

## Checker Boundary

`scripts/check_wiki_frontmatter.py` reads the YAML contract and emits:

- `/tmp/wiki-frontmatter-taxonomy-report.json`
- `/tmp/wiki-frontmatter-taxonomy-report.md`

The checker validates repository content and registered producers. It only emits
text-level warnings for possible unregistered producers and does not attempt
general Python static analysis.

## Producer Boundary

Repo-local templates and scripts that create wiki frontmatter must be registered
under `producer_paths`. External users and AI systems are not scanned; their
language becomes hints that must validate before being treated as final
frontmatter.

## Migration Boundary

Only pages in `sample_migration_paths` are required to pass the first rollout as
new-model pages. Legacy pages can continue to produce warnings until a later
migration change.
```

- [ ] **Step 4: Add `tasks.md`**

Write `openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md`:

```markdown
# Tasks

- [ ] 1. Create OpenSpec change artifacts for taxonomy drift control.
- [ ] 2. Add taxonomy contract config and config-loading tests.
- [ ] 3. Add content drift checker and tests.
- [ ] 4. Add registered producer drift and possible producer warning checks.
- [ ] 5. Add checker CLI report output.
- [ ] 6. Add taxonomy gate skill and AGENTS routing.
- [ ] 7. Update known producer templates and inbox intake generation.
- [ ] 8. Migrate sample pages listed in the taxonomy contract.
- [ ] 9. Add evaluation evidence and run verification.
```

- [ ] **Step 5: Add spec requirements**

Write `openspec/changes/stabilize-wiki-frontmatter-taxonomy/specs/wiki-frontmatter-taxonomy/spec.md`:

```markdown
## Purpose

Define a repo-local wiki frontmatter taxonomy contract that prevents operations
layer metadata from masquerading as business-domain metadata.

## Requirements

### Requirement: Repository SHALL provide a single frontmatter taxonomy contract

The repository SHALL define wiki frontmatter taxonomy values and validation
policies in `wiki/config/frontmatter-taxonomy.yaml`.

#### Scenario: Agent needs taxonomy values

- **WHEN** an agent, skill, or script needs allowed domains, forbidden domains,
  `ops_area` values, path rules, producer paths, or severity
- **THEN** it SHALL read `wiki/config/frontmatter-taxonomy.yaml`
- **AND** it SHALL NOT duplicate those vocabularies in AGENTS or skill bodies

### Requirement: Repository SHALL distinguish domain from operations area

The repository SHALL reserve `domain` for real business or topic domains and use
`ops_area` for operations or governance workflow categories.

#### Scenario: Pure operations page has no business domain

- **WHEN** a pure `wiki/ops` governance page is migrated under the new contract
- **THEN** it SHALL use `layer: ops`
- **AND** it SHALL use `domain: none`
- **AND** it SHALL use a valid `ops_area`

#### Scenario: Business intake page lives in ops

- **WHEN** a `wiki/ops` intake page records business-related source intake
- **THEN** it SHALL use `layer: ops`
- **AND** it SHALL use the real domain when known
- **AND** it SHALL use `domain: unclassified` with `classification_needed: true`
  when the real domain is not known
- **AND** it SHALL use `ops_area: source-intake`

### Requirement: Repository SHALL reject forbidden domain drift

The repository SHALL treat `domain: personal-ops` as forbidden for new or
touched frontmatter.

#### Scenario: Content uses forbidden domain

- **WHEN** the checker scans a wiki page with `domain: personal-ops`
- **THEN** it SHALL report `forbidden_domain`
- **AND** the severity SHALL be `error`

#### Scenario: Producer hardcodes forbidden domain

- **WHEN** the checker scans a registered producer template containing
  `domain: personal-ops`
- **THEN** it SHALL report `producer_hardcoded_forbidden_domain`
- **AND** the severity SHALL be `error`

### Requirement: Repository SHALL expose taxonomy drift reports

The checker SHALL emit both JSON and Markdown reports.

#### Scenario: Checker runs

- **WHEN** `python3 scripts/check_wiki_frontmatter.py` runs
- **THEN** it SHALL write `/tmp/wiki-frontmatter-taxonomy-report.json`
- **AND** it SHALL write `/tmp/wiki-frontmatter-taxonomy-report.md`
- **AND** the reports SHALL include content drift, producer drift, possible
  unregistered producer warnings, and summary counts by severity

### Requirement: AGENTS SHALL route frontmatter changes through the taxonomy gate

Repo AGENTS SHALL not duplicate taxonomy vocabulary, but SHALL require the
taxonomy skill and checker for frontmatter work.

#### Scenario: Agent creates or modifies wiki frontmatter

- **WHEN** an agent creates or modifies wiki frontmatter, wiki templates, or
  repo-local frontmatter producers
- **THEN** it SHALL load `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`
- **AND** it SHALL run the taxonomy checker before claiming taxonomy compliance
  or completion
```

- [ ] **Step 6: Commit OpenSpec artifacts**

Run:

```bash
git add openspec/changes/stabilize-wiki-frontmatter-taxonomy
git commit -m "docs: propose wiki frontmatter taxonomy gate"
```

Expected: commit succeeds with only the OpenSpec change artifacts staged.

---

### Task 2: Add Taxonomy Config and Loader Tests

**Files:**
- Create: `wiki/config/frontmatter-taxonomy.yaml`
- Create: `scripts/check_wiki_frontmatter.py`
- Create: `tests/test_wiki_frontmatter_taxonomy.py`

- [ ] **Step 1: Write failing config-load test**

Create `tests/test_wiki_frontmatter_taxonomy.py`:

```python
from __future__ import annotations

from pathlib import Path

from scripts.check_wiki_frontmatter import load_taxonomy


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_load_taxonomy_reads_contract(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/config/frontmatter-taxonomy.yaml",
        """
version: 1
fields:
  domain:
    forbidden:
      - personal-ops
    known:
      - none
      - unclassified
  ops_area:
    allowed:
      - source-intake
path_rules:
  wiki/ops:
    required:
      - layer
      - domain
      - ops_area
    layer: ops
severity:
  forbidden_domain: error
producer_paths:
  templates:
    - wiki/templates/*.md
  scripts:
    - scripts/inbox_intake.py
sample_migration_paths:
  - wiki/ops/example-intake.md
""".lstrip(),
    )

    config = load_taxonomy(tmp_path)

    assert config["version"] == 1
    assert config["fields"]["domain"]["forbidden"] == ["personal-ops"]
    assert config["producer_paths"]["scripts"] == ["scripts/inbox_intake.py"]
```

- [ ] **Step 2: Run test and verify failure**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py::test_load_taxonomy_reads_contract -q
```

Expected: FAIL with `ModuleNotFoundError` or import error for
`scripts.check_wiki_frontmatter`.

- [ ] **Step 3: Add taxonomy config**

Create `wiki/config/frontmatter-taxonomy.yaml`:

```yaml
version: 1

fields:
  layer:
    allowed:
      - sources
      - domains
      - timeline
      - reports
      - ops
      - adr
      - spec
      - examples

  domain:
    meaning: business_or_topic_only
    allow_none: true
    require_classification_flag_for_unclassified: true
    forbidden:
      - personal-ops
    known:
      - none
      - unclassified
      - nirvana
      - nirvana-project
      - account-clearing
      - agentic-collaboration
      - report-workflow
      - wiki
      - agent-harness

  ops_area:
    allowed:
      - agent-governance
      - learning-capture
      - wiki-runtime
      - report-quality
      - meeting-notes
      - source-intake
      - workflow-trace

path_rules:
  wiki/ops:
    required:
      - layer
      - domain
      - ops_area
    layer: ops
    domain_policy: none_or_real_domain_or_unclassified

  wiki/domains:
    required:
      - layer
      - domain
    layer: domains
    domain_policy: required_real_domain

  wiki/sources:
    required:
      - layer
      - domain
    layer: sources
    domain_policy: real_domain_or_unclassified

severity:
  forbidden_domain: error
  missing_ops_area_on_ops_page: error
  missing_domain_on_sample_ops_page: error
  producer_hardcoded_forbidden_domain: error
  unclassified_without_flag: error
  unknown_domain: warn
  missing_layer_on_legacy_page: warn
  possible_unregistered_producer: warn

producer_paths:
  templates:
    - wiki/templates/*.md
    - .codex/skills/**/references/*template*.md
  scripts:
    - scripts/inbox_intake.py

sample_migration_paths:
  - wiki/ops/behavior-replay-gate.md
  - wiki/ops/learning-capture-routing.md
  - wiki/ops/agent-readable-wiki-semantic-scoring.md
  - wiki/ops/nirvana-协议支付涅槃需求文档-intake.md
  - wiki/ops/nirvana-preview-intake.md
```

- [ ] **Step 4: Add minimal checker loader**

Create `scripts/check_wiki_frontmatter.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = Path("wiki/config/frontmatter-taxonomy.yaml")


@dataclass(frozen=True)
class DriftEntry:
    kind: str
    severity: str
    path: str
    message: str
    field: str | None = None
    value: str | None = None


def load_taxonomy(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config_file = root_path / CONFIG_PATH
    with config_file.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"taxonomy config must be a mapping: {config_file}")
    return data


def build_report(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config = load_taxonomy(root_path)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": root_path.resolve().as_posix(),
        "config_path": CONFIG_PATH.as_posix(),
        "summary": {"error": 0, "warn": 0, "info": 0, "total": 0},
        "entries": [],
        "taxonomy_version": config.get("version"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check wiki frontmatter taxonomy drift.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--json-output", default="/tmp/wiki-frontmatter-taxonomy-report.json")
    parser.add_argument("--markdown-output", default="/tmp/wiki-frontmatter-taxonomy-report.md")
    args = parser.parse_args()

    report = build_report(Path(args.root))
    Path(args.json_output).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    Path(args.markdown_output).write_text("# Wiki Frontmatter Taxonomy Report\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run config test and verify pass**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py::test_load_taxonomy_reads_contract -q
```

Expected: PASS.

- [ ] **Step 6: Commit config and loader**

Run:

```bash
git add wiki/config/frontmatter-taxonomy.yaml scripts/check_wiki_frontmatter.py tests/test_wiki_frontmatter_taxonomy.py
git commit -m "feat: add wiki frontmatter taxonomy contract"
```

Expected: commit succeeds with only these three paths staged.

---

### Task 3: Add Content Drift Checks

**Files:**
- Modify: `scripts/check_wiki_frontmatter.py`
- Modify: `tests/test_wiki_frontmatter_taxonomy.py`

- [ ] **Step 1: Add failing content drift tests**

Append to `tests/test_wiki_frontmatter_taxonomy.py`:

```python
from scripts.check_wiki_frontmatter import check_content_drift


def minimal_config() -> dict:
    return {
        "fields": {
            "domain": {
                "forbidden": ["personal-ops"],
                "known": ["none", "unclassified", "nirvana"],
            },
            "ops_area": {"allowed": ["agent-governance", "source-intake"]},
        },
        "path_rules": {
            "wiki/ops": {"required": ["layer", "domain", "ops_area"], "layer": "ops"},
        },
        "severity": {
            "forbidden_domain": "error",
            "missing_ops_area_on_ops_page": "error",
            "missing_domain_on_sample_ops_page": "error",
            "unclassified_without_flag": "error",
            "unknown_domain": "warn",
            "missing_layer_on_legacy_page": "warn",
        },
        "sample_migration_paths": ["wiki/ops/sample.md"],
    }


def test_content_drift_reports_forbidden_personal_ops(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/ops/sample.md",
        """
---
layer: ops
domain: personal-ops
ops_area: agent-governance
---
# Sample
""".lstrip(),
    )

    entries = check_content_drift(tmp_path, minimal_config())

    assert [(entry.kind, entry.severity, entry.value) for entry in entries] == [
        ("forbidden_domain", "error", "personal-ops")
    ]


def test_content_drift_requires_ops_area_for_sample_path(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/ops/sample.md",
        """
---
layer: ops
domain: none
---
# Sample
""".lstrip(),
    )

    entries = check_content_drift(tmp_path, minimal_config())

    assert any(entry.kind == "missing_ops_area_on_ops_page" for entry in entries)


def test_unclassified_domain_requires_classification_flag(tmp_path: Path) -> None:
    write(
        tmp_path / "wiki/ops/sample.md",
        """
---
layer: ops
domain: unclassified
ops_area: source-intake
---
# Sample
""".lstrip(),
    )

    entries = check_content_drift(tmp_path, minimal_config())

    assert any(entry.kind == "unclassified_without_flag" for entry in entries)
```

- [ ] **Step 2: Run tests and verify failure**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py -q
```

Expected: FAIL because `check_content_drift` is not implemented.

- [ ] **Step 3: Implement content drift helpers**

Modify `scripts/check_wiki_frontmatter.py` by importing the existing parser and
adding these functions above `build_report`:

```python
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.extract_wiki_graph import parse_frontmatter


def severity(config: dict[str, Any], kind: str, default: str = "warn") -> str:
    value = config.get("severity", {}).get(kind, default)
    return str(value)


def rel_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_under(rel: str, prefix: str) -> bool:
    normalized = prefix.rstrip("/") + "/"
    return rel.startswith(normalized)


def check_content_drift(root: Path | str, config: dict[str, Any]) -> list[DriftEntry]:
    root_path = Path(root)
    wiki_dir = root_path / "wiki"
    if not wiki_dir.exists():
        return []

    forbidden_domains = set(config.get("fields", {}).get("domain", {}).get("forbidden", []))
    known_domains = set(config.get("fields", {}).get("domain", {}).get("known", []))
    sample_paths = set(config.get("sample_migration_paths", []))
    entries: list[DriftEntry] = []

    for path in sorted(wiki_dir.rglob("*.md")):
        rel = rel_path(path, root_path)
        text = path.read_text(encoding="utf-8")
        meta, _body = parse_frontmatter(text)
        domain = meta.get("domain")
        layer = meta.get("layer")
        ops_area = meta.get("ops_area")

        if isinstance(domain, str) and domain in forbidden_domains:
            entries.append(
                DriftEntry(
                    kind="forbidden_domain",
                    severity=severity(config, "forbidden_domain", "error"),
                    path=rel,
                    field="domain",
                    value=domain,
                    message=f"`domain: {domain}` is forbidden by taxonomy contract.",
                )
            )

        if isinstance(domain, str) and domain not in known_domains and rel in sample_paths:
            entries.append(
                DriftEntry(
                    kind="unknown_domain",
                    severity=severity(config, "unknown_domain", "warn"),
                    path=rel,
                    field="domain",
                    value=domain,
                    message=f"`domain: {domain}` is not listed in taxonomy known domains.",
                )
            )

        if domain == "unclassified" and meta.get("classification_needed") != "true":
            entries.append(
                DriftEntry(
                    kind="unclassified_without_flag",
                    severity=severity(config, "unclassified_without_flag", "error"),
                    path=rel,
                    field="classification_needed",
                    value=str(meta.get("classification_needed")),
                    message="`domain: unclassified` requires `classification_needed: true`.",
                )
            )

        if is_under(rel, "wiki/ops") and rel in sample_paths:
            if not domain:
                entries.append(
                    DriftEntry(
                        kind="missing_domain_on_sample_ops_page",
                        severity=severity(config, "missing_domain_on_sample_ops_page", "error"),
                        path=rel,
                        field="domain",
                        value=None,
                        message="Sample migration ops page must declare `domain`.",
                    )
                )
            if not ops_area:
                entries.append(
                    DriftEntry(
                        kind="missing_ops_area_on_ops_page",
                        severity=severity(config, "missing_ops_area_on_ops_page", "error"),
                        path=rel,
                        field="ops_area",
                        value=None,
                        message="Sample migration ops page must declare `ops_area`.",
                    )
                )
            if layer != "ops":
                entries.append(
                    DriftEntry(
                        kind="missing_layer_on_legacy_page",
                        severity=severity(config, "missing_layer_on_legacy_page", "warn"),
                        path=rel,
                        field="layer",
                        value=str(layer),
                        message="Sample migration ops page should declare `layer: ops`.",
                    )
                )

    return entries
```

- [ ] **Step 4: Wire content drift into report**

Replace `build_report` in `scripts/check_wiki_frontmatter.py` with:

```python
def summarize(entries: list[DriftEntry]) -> dict[str, int]:
    summary = {"error": 0, "warn": 0, "info": 0, "total": len(entries)}
    for entry in entries:
        if entry.severity not in summary:
            summary[entry.severity] = 0
        summary[entry.severity] += 1
    return summary


def build_report(root: Path | str = ROOT) -> dict[str, Any]:
    root_path = Path(root)
    config = load_taxonomy(root_path)
    entries = check_content_drift(root_path, config)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": root_path.resolve().as_posix(),
        "config_path": CONFIG_PATH.as_posix(),
        "summary": summarize(entries),
        "entries": [asdict(entry) for entry in entries],
        "taxonomy_version": config.get("version"),
    }
```

- [ ] **Step 5: Run content drift tests**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py -q
```

Expected: PASS.

- [ ] **Step 6: Commit content drift checker**

Run:

```bash
git add scripts/check_wiki_frontmatter.py tests/test_wiki_frontmatter_taxonomy.py
git commit -m "feat: check wiki frontmatter content drift"
```

Expected: commit succeeds with only these two files staged.

---

### Task 4: Add Producer Drift Checks

**Files:**
- Modify: `scripts/check_wiki_frontmatter.py`
- Modify: `tests/test_wiki_frontmatter_taxonomy.py`

- [ ] **Step 1: Add failing producer drift tests**

Append to `tests/test_wiki_frontmatter_taxonomy.py`:

```python
from scripts.check_wiki_frontmatter import (
    check_possible_unregistered_producers,
    check_registered_producer_drift,
)


def producer_config() -> dict:
    config = minimal_config()
    config["producer_paths"] = {
        "templates": [".codex/skills/**/references/*template*.md"],
        "scripts": ["scripts/inbox_intake.py"],
    }
    config["severity"]["producer_hardcoded_forbidden_domain"] = "error"
    config["severity"]["possible_unregistered_producer"] = "warn"
    return config


def test_registered_template_reports_hardcoded_forbidden_domain(tmp_path: Path) -> None:
    write(
        tmp_path / ".codex/skills/article-learning-capture/references/wiki-template.md",
        """
```markdown
---
domain: personal-ops
---
```
""".lstrip(),
    )

    entries = check_registered_producer_drift(tmp_path, producer_config())

    assert [(entry.kind, entry.severity, entry.value) for entry in entries] == [
        ("producer_hardcoded_forbidden_domain", "error", "personal-ops")
    ]


def test_unregistered_frontmatter_producer_warns(tmp_path: Path) -> None:
    write(
        tmp_path / "scripts/other_writer.py",
        'CONTENT = "---\\ndomain: personal-ops\\n---\\n"',
    )

    entries = check_possible_unregistered_producers(tmp_path, producer_config())

    assert [(entry.kind, entry.severity, entry.path) for entry in entries] == [
        ("possible_unregistered_producer", "warn", "scripts/other_writer.py")
    ]
```

- [ ] **Step 2: Run producer tests and verify failure**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py -q
```

Expected: FAIL because producer check functions are missing.

- [ ] **Step 3: Implement producer path expansion and checks**

Add to `scripts/check_wiki_frontmatter.py` above `build_report`:

```python
def configured_producer_paths(config: dict[str, Any]) -> set[str]:
    producer_paths = config.get("producer_paths", {})
    paths: set[str] = set()
    for values in producer_paths.values():
        if isinstance(values, list):
            paths.update(str(value) for value in values)
    return paths


def expand_registered_producers(root: Path, config: dict[str, Any]) -> list[Path]:
    producer_paths = config.get("producer_paths", {})
    paths: list[Path] = []
    for values in producer_paths.values():
        if not isinstance(values, list):
            continue
        for pattern in values:
            paths.extend(sorted(root.glob(str(pattern))))
    return sorted(path for path in paths if path.is_file())


def check_registered_producer_drift(root: Path | str, config: dict[str, Any]) -> list[DriftEntry]:
    root_path = Path(root)
    forbidden_domains = set(config.get("fields", {}).get("domain", {}).get("forbidden", []))
    entries: list[DriftEntry] = []
    for path in expand_registered_producers(root_path, config):
        rel = rel_path(path, root_path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for domain in sorted(forbidden_domains):
            if f"domain: {domain}" in text:
                entries.append(
                    DriftEntry(
                        kind="producer_hardcoded_forbidden_domain",
                        severity=severity(config, "producer_hardcoded_forbidden_domain", "error"),
                        path=rel,
                        field="domain",
                        value=domain,
                        message=f"Registered producer hardcodes forbidden `domain: {domain}`.",
                    )
                )
    return entries


def is_registered_path(rel: str, config: dict[str, Any], root: Path) -> bool:
    return any((root / rel) in expand_registered_producers(root, config) for _ in [None])


def check_possible_unregistered_producers(root: Path | str, config: dict[str, Any]) -> list[DriftEntry]:
    root_path = Path(root)
    registered = {rel_path(path, root_path) for path in expand_registered_producers(root_path, config)}
    candidate_roots = [root_path / "scripts", root_path / ".codex/skills"]
    entries: list[DriftEntry] = []
    for candidate_root in candidate_roots:
        if not candidate_root.exists():
            continue
        for path in sorted(candidate_root.rglob("*")):
            if not path.is_file() or path.suffix not in {".py", ".md"}:
                continue
            rel = rel_path(path, root_path)
            if rel in registered:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "---" in text and "domain:" in text:
                entries.append(
                    DriftEntry(
                        kind="possible_unregistered_producer",
                        severity=severity(config, "possible_unregistered_producer", "warn"),
                        path=rel,
                        message="File contains frontmatter-looking text but is not registered in producer_paths.",
                    )
                )
    return entries
```

- [ ] **Step 4: Wire producer checks into report**

Modify `build_report` so the `entries` assignment is:

```python
    entries = [
        *check_content_drift(root_path, config),
        *check_registered_producer_drift(root_path, config),
        *check_possible_unregistered_producers(root_path, config),
    ]
```

- [ ] **Step 5: Remove unused helper if present**

If `is_registered_path` is not called after tests pass, delete it from
`scripts/check_wiki_frontmatter.py`. The implementation does not need it because
`registered` is computed once in `check_possible_unregistered_producers`.

- [ ] **Step 6: Run producer tests**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py -q
```

Expected: PASS.

- [ ] **Step 7: Commit producer drift checks**

Run:

```bash
git add scripts/check_wiki_frontmatter.py tests/test_wiki_frontmatter_taxonomy.py
git commit -m "feat: check wiki frontmatter producer drift"
```

Expected: commit succeeds with only these two files staged.

---

### Task 5: Add Checker Markdown Report and CLI Exit Behavior

**Files:**
- Modify: `scripts/check_wiki_frontmatter.py`
- Modify: `tests/test_wiki_frontmatter_taxonomy.py`

- [ ] **Step 1: Add failing report rendering test**

Append to `tests/test_wiki_frontmatter_taxonomy.py`:

```python
from scripts.check_wiki_frontmatter import render_markdown_report


def test_render_markdown_report_includes_summary_and_entries() -> None:
    report = {
        "generated_at": "2026-05-13T00:00:00+00:00",
        "root": "/repo",
        "config_path": "wiki/config/frontmatter-taxonomy.yaml",
        "taxonomy_version": 1,
        "summary": {"error": 1, "warn": 1, "info": 0, "total": 2},
        "entries": [
            {
                "kind": "forbidden_domain",
                "severity": "error",
                "path": "wiki/ops/sample.md",
                "field": "domain",
                "value": "personal-ops",
                "message": "`domain: personal-ops` is forbidden by taxonomy contract.",
            },
            {
                "kind": "possible_unregistered_producer",
                "severity": "warn",
                "path": "scripts/other_writer.py",
                "field": None,
                "value": None,
                "message": "File contains frontmatter-looking text but is not registered in producer_paths.",
            },
        ],
    }

    markdown = render_markdown_report(report)

    assert "# Wiki Frontmatter Taxonomy Report" in markdown
    assert "| error | 1 |" in markdown
    assert "`wiki/ops/sample.md`" in markdown
    assert "`scripts/other_writer.py`" in markdown
```

- [ ] **Step 2: Run report test and verify failure**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py::test_render_markdown_report_includes_summary_and_entries -q
```

Expected: FAIL because `render_markdown_report` is missing.

- [ ] **Step 3: Implement Markdown rendering**

Add to `scripts/check_wiki_frontmatter.py` above `main`:

```python
def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Wiki Frontmatter Taxonomy Report",
        "",
        f"Generated at: `{report['generated_at']}`",
        f"Root: `{report['root']}`",
        f"Config: `{report['config_path']}`",
        f"Taxonomy version: `{report['taxonomy_version']}`",
        "",
        "## Summary",
        "",
        "| Severity | Count |",
        "| --- | --- |",
    ]
    for key in ["error", "warn", "info", "total"]:
        lines.append(f"| {key} | {report['summary'].get(key, 0)} |")

    lines.extend(["", "## Drift Entries", ""])
    entries = report.get("entries", [])
    if not entries:
        lines.append("- None")
    else:
        for entry in entries:
            field = entry.get("field") or "-"
            value = entry.get("value") or "-"
            lines.append(
                f"- `{entry['path']}` `{entry['severity']}` `{entry['kind']}` "
                f"field=`{field}` value=`{value}`: {entry['message']}"
            )
    lines.append("")
    return "\n".join(lines)
```

- [ ] **Step 4: Update CLI to write Markdown report and fail on errors**

Replace the body of `main` after argument parsing with:

```python
    report = build_report(Path(args.root))
    Path(args.json_output).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    Path(args.markdown_output).write_text(
        render_markdown_report(report),
        encoding="utf-8",
    )
    return 1 if report["summary"].get("error", 0) else 0
```

- [ ] **Step 5: Run report tests**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py -q
```

Expected: PASS.

- [ ] **Step 6: Run checker against repo and capture expected current failure**

Run:

```bash
python3 scripts/check_wiki_frontmatter.py
```

Expected: non-zero exit because the current repo still has known
`domain: personal-ops` drift and producer drift. Confirm both files exist:

```bash
test -s /tmp/wiki-frontmatter-taxonomy-report.json
test -s /tmp/wiki-frontmatter-taxonomy-report.md
```

Expected: both commands exit `0`.

- [ ] **Step 7: Commit report rendering**

Run:

```bash
git add scripts/check_wiki_frontmatter.py tests/test_wiki_frontmatter_taxonomy.py
git commit -m "feat: render wiki frontmatter taxonomy report"
```

Expected: commit succeeds with only these two files staged.

---

### Task 6: Add Taxonomy Skill and AGENTS Route

**Files:**
- Create: `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`
- Modify: `AGENTS.md`
- Modify: `tests/test_wiki_runtime_skills.py` or create `tests/test_wiki_frontmatter_taxonomy_skill.py`

- [ ] **Step 1: Add failing skill test**

Create `tests/test_wiki_frontmatter_taxonomy_skill.py`:

```python
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_taxonomy_skill_references_contract_without_vocab_duplication() -> None:
    skill = ROOT / ".codex/skills/wiki-frontmatter-taxonomy/SKILL.md"
    text = skill.read_text(encoding="utf-8")

    assert "wiki/config/frontmatter-taxonomy.yaml" in text
    assert "scripts/check_wiki_frontmatter.py" in text
    assert "Do not duplicate taxonomy vocabulary" in text
    assert "agent-governance" not in text
    assert "source-intake" not in text


def test_agents_routes_frontmatter_changes_to_taxonomy_skill() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert ".codex/skills/wiki-frontmatter-taxonomy/SKILL.md" in text
    assert "run the repo frontmatter taxonomy checker" in text
```

- [ ] **Step 2: Run skill test and verify failure**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy_skill.py -q
```

Expected: FAIL because skill and AGENTS route are missing.

- [ ] **Step 3: Create taxonomy skill**

Create `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`:

```markdown
---
name: wiki-frontmatter-taxonomy
description: Use when creating or modifying report wiki frontmatter, wiki templates, or repo-local scripts that generate wiki frontmatter.
---

Use the repo-local wiki frontmatter taxonomy gate.

Load:

- `wiki/config/frontmatter-taxonomy.yaml`
- `scripts/check_wiki_frontmatter.py`
- `docs/superpowers/specs/2026-05-13-wiki-frontmatter-taxonomy-design.md` when design context is needed

Hard rules:

- Do not duplicate taxonomy vocabulary in this skill.
- Treat user language, AI drafts, folder names, and script guesses as hints until validated.
- Do not use local skill templates or ad hoc agent judgment as final taxonomy authority.
- Run `python3 scripts/check_wiki_frontmatter.py` before claiming taxonomy compliance or completion.
- If the checker reports errors, do not claim the taxonomy work is complete.

When creating or modifying frontmatter:

1. Read `wiki/config/frontmatter-taxonomy.yaml`.
2. Determine whether the page is content, operations, source, report, timeline, ADR, spec, or example by path and task.
3. Apply the path rule from the taxonomy contract.
4. Use explicit uncertainty fields when classification is not known.
5. Run the checker and summarize remaining drift.

Boundaries:

- Do not batch-migrate legacy pages unless the active OpenSpec change lists them.
- Do not edit global agent instructions.
- Do not change scorecard scoring formulas from this skill.
- Do not treat checker warnings as proof that all legacy drift has been resolved.
```

- [ ] **Step 4: Add AGENTS route**

Modify repo `AGENTS.md` by adding this under `## High-Frequency Skills` or the nearest repo workflow routing section:

```markdown
## Wiki Frontmatter Taxonomy Gate

- When creating or modifying wiki frontmatter, wiki templates, or repo-local
  scripts that generate wiki frontmatter, load
  `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`.
- `AGENTS.md` must not duplicate the taxonomy vocabulary. The source of truth is
  `wiki/config/frontmatter-taxonomy.yaml`.
- Before claiming taxonomy compliance or completion, run the repo frontmatter
  taxonomy checker: `python3 scripts/check_wiki_frontmatter.py`.
- Do not claim taxonomy compliance from memory.
```

- [ ] **Step 5: Run skill route tests**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy_skill.py -q
```

Expected: PASS.

- [ ] **Step 6: Commit skill and AGENTS route**

Run:

```bash
git add .codex/skills/wiki-frontmatter-taxonomy/SKILL.md AGENTS.md tests/test_wiki_frontmatter_taxonomy_skill.py
git commit -m "feat: add wiki frontmatter taxonomy gate skill"
```

Expected: commit succeeds with only these three files staged.

---

### Task 7: Update Known Producers

**Files:**
- Modify: `.codex/skills/article-learning-capture/references/wiki-template.md`
- Modify: `wiki/templates/*.md`
- Modify: `scripts/inbox_intake.py`
- Modify: `tests/test_inbox_intake.py`

- [ ] **Step 1: Add failing inbox intake assertions**

Open `tests/test_inbox_intake.py` and add assertions to the existing generated
source and intake tests. If the file has separate tests for source and intake
drafts, add these exact expectations to the relevant assertions:

```python
assert "layer: sources" in source_content
assert "domain: unclassified" in source_content
assert "classification_needed: true" in source_content
assert "layer: ops" in intake_content
assert "ops_area: source-intake" in intake_content
assert "domain: unclassified" in intake_content
assert "classification_needed: true" in intake_content
```

For an inbox path under `inbox/nirvana/`, assert:

```python
assert "domain: nirvana" in source_content
assert "classification_needed: true" not in source_content
assert "domain: nirvana" in intake_content
assert "classification_needed: true" not in intake_content
```

- [ ] **Step 2: Run inbox tests and verify failure**

Run:

```bash
pytest tests/test_inbox_intake.py -q
```

Expected: FAIL because generated drafts do not yet include `layer`, `ops_area`,
or `classification_needed`.

- [ ] **Step 3: Update article learning wiki template**

Modify `.codex/skills/article-learning-capture/references/wiki-template.md` so
the frontmatter block uses:

```yaml
layer: ops
domain: <real-topic-domain-or-none>
ops_area: learning-capture
classification_needed: true
```

Remove this line:

```yaml
domain: personal-ops
```

- [ ] **Step 4: Update wiki templates**

For `wiki/templates/source-template.md`, add:

```yaml
layer: sources
classification_needed: true
```

For `wiki/templates/intake-record-template.md`, add:

```yaml
layer: ops
ops_area: source-intake
classification_needed: true
```

For `wiki/templates/domain-template.md`, add:

```yaml
layer: domains
```

For `wiki/templates/report-template.md`, add:

```yaml
layer: reports
```

For `wiki/templates/timeline-template.md`, add:

```yaml
layer: timeline
```

For `wiki/templates/meeting-note-source-template.md`, add:

```yaml
layer: sources
classification_needed: true
```

For `wiki/templates/focus-thread-template.md`,
`wiki/templates/reminder-item-template.md`, and
`wiki/templates/codex-handoff-template.md`, add:

```yaml
layer: ops
domain: <real-topic-domain-or-none>
ops_area: workflow-trace
classification_needed: true
```

- [ ] **Step 5: Update inbox intake generation**

Modify `scripts/inbox_intake.py` by adding this helper after `_infer_domain`:

```python
def _domain_fields(domain: str) -> str:
    if domain == "unclassified":
        return "domain: unclassified\nclassification_needed: true"
    return f"domain: {domain}"
```

In `generate_source_draft`, replace:

```python
domain: {domain}
```

with:

```python
layer: sources
{_domain_fields(domain)}
```

In `generate_intake_draft`, replace:

```python
domain: {domain}
```

with:

```python
layer: ops
{_domain_fields(domain)}
ops_area: source-intake
```

- [ ] **Step 6: Run producer-related tests**

Run:

```bash
pytest tests/test_inbox_intake.py tests/test_wiki_frontmatter_taxonomy.py -q
```

Expected: PASS for the targeted tests. The checker may still fail on the full
repo until sample pages are migrated in Task 8.

- [ ] **Step 7: Commit producer updates**

Run:

```bash
git add .codex/skills/article-learning-capture/references/wiki-template.md wiki/templates scripts/inbox_intake.py tests/test_inbox_intake.py
git commit -m "feat: align wiki frontmatter producers with taxonomy"
```

Expected: commit succeeds with only listed producer and test paths staged.

---

### Task 8: Migrate Sample Pages

**Files:**
- Modify: `wiki/ops/behavior-replay-gate.md`
- Modify: `wiki/ops/learning-capture-routing.md`
- Modify: `wiki/ops/agent-readable-wiki-semantic-scoring.md`
- Modify: `wiki/ops/nirvana-协议支付涅槃需求文档-intake.md`
- Modify: `wiki/ops/nirvana-preview-intake.md`

- [ ] **Step 1: Update pure governance sample**

In `wiki/ops/behavior-replay-gate.md`, ensure frontmatter contains:

```yaml
layer: ops
domain: none
ops_area: agent-governance
```

Keep existing `canonical_object`, `artifact_type`, and relation fields.

- [ ] **Step 2: Update learning routing sample**

In `wiki/ops/learning-capture-routing.md`, ensure frontmatter contains:

```yaml
layer: ops
domain: none
ops_area: learning-capture
```

Keep existing `canonical_object`, `artifact_type`, and relation fields.

- [ ] **Step 3: Update wiki runtime sample**

In `wiki/ops/agent-readable-wiki-semantic-scoring.md`, ensure frontmatter contains:

```yaml
layer: ops
domain: none
ops_area: wiki-runtime
```

Keep existing `canonical_object`, `artifact_type`, and relation fields.

- [ ] **Step 4: Update Nirvana intake samples**

In both `wiki/ops/nirvana-协议支付涅槃需求文档-intake.md` and
`wiki/ops/nirvana-preview-intake.md`, ensure frontmatter contains:

```yaml
layer: ops
domain: nirvana
ops_area: source-intake
```

Do not add `classification_needed: true` because `nirvana` is known.

- [ ] **Step 5: Run checker and targeted tests**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_frontmatter_taxonomy_skill.py -q
python3 scripts/check_wiki_frontmatter.py
```

Expected: pytest PASS. Checker may still exit non-zero if legacy
`domain: personal-ops` remains outside sample paths. Confirm the five sample
paths do not appear as error entries in `/tmp/wiki-frontmatter-taxonomy-report.md`.

- [ ] **Step 6: Commit sample migration**

Run:

```bash
git add wiki/ops/behavior-replay-gate.md wiki/ops/learning-capture-routing.md wiki/ops/agent-readable-wiki-semantic-scoring.md wiki/ops/nirvana-协议支付涅槃需求文档-intake.md wiki/ops/nirvana-preview-intake.md
git commit -m "docs: migrate sample wiki frontmatter taxonomy"
```

Expected: commit succeeds with only the five sample pages staged.

---

### Task 9: Add Evaluation Evidence and Final Verification

**Files:**
- Create: `openspec/changes/stabilize-wiki-frontmatter-taxonomy/evaluation.md`
- Modify: `openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md`

- [ ] **Step 1: Run verification commands**

Run:

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_frontmatter_taxonomy_skill.py tests/test_inbox_intake.py -q
python3 scripts/check_wiki_frontmatter.py
```

Expected:

- pytest exits `0`.
- checker writes `/tmp/wiki-frontmatter-taxonomy-report.json`.
- checker writes `/tmp/wiki-frontmatter-taxonomy-report.md`.
- checker may exit `1` if legacy errors remain, and the evaluation must record
  that residual risk explicitly.

- [ ] **Step 2: Add evaluation evidence**

Create `openspec/changes/stabilize-wiki-frontmatter-taxonomy/evaluation.md`:

```markdown
# Evaluation

## Pressure Scenarios

| Scenario | Expected Result |
|---|---|
| Registered producer template hardcodes `domain: personal-ops` | Checker reports `producer_hardcoded_forbidden_domain` as `error` |
| Sample ops governance page uses `domain: personal-ops` | Checker reports `forbidden_domain` as `error` |
| Sample pure governance page uses `domain: none` and valid `ops_area` | Checker reports no sample error for that page |
| Sample business intake uses `domain: nirvana` and `ops_area: source-intake` | Checker reports no sample error for that page |
| `domain: unclassified` appears without `classification_needed: true` | Checker reports `unclassified_without_flag` as `error` |
| Repo-local file contains frontmatter-like `domain:` but is not registered | Checker reports `possible_unregistered_producer` as `warn` |

## RED Baseline

- Existing article learning template contained `domain: personal-ops`.
- Existing ops pages contained `domain: personal-ops`.
- Existing inbox intake generator wrote `domain` directly from folder inference.

## GREEN Result

- Taxonomy contract exists at `wiki/config/frontmatter-taxonomy.yaml`.
- Taxonomy skill exists at `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`.
- AGENTS routes wiki frontmatter changes through the taxonomy skill and checker.
- Checker emits JSON and Markdown reports.
- Producer templates no longer hardcode `domain: personal-ops`.
- Sample migration pages use `layer`, `domain`, and `ops_area` according to the contract.

## Verification Commands

```bash
pytest tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_frontmatter_taxonomy_skill.py tests/test_inbox_intake.py -q
python3 scripts/check_wiki_frontmatter.py
```

## Residual Risks

- Legacy pages outside `sample_migration_paths` may still contain drift.
- The checker intentionally does not perform broad Python static analysis.
- Business domain taxonomy remains thin and should be strengthened in a later change.
```

- [ ] **Step 3: Mark OpenSpec tasks complete**

Update `openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md` by changing
each checklist item from `[ ]` to `[x]` only after the corresponding task is
completed and verified.

- [ ] **Step 4: Commit evaluation**

Run:

```bash
git add openspec/changes/stabilize-wiki-frontmatter-taxonomy/evaluation.md openspec/changes/stabilize-wiki-frontmatter-taxonomy/tasks.md
git commit -m "docs: evaluate wiki frontmatter taxonomy gate"
```

Expected: commit succeeds with only evaluation and task status staged.

---

## Final Review

- [ ] Run `git status --short` and confirm no task-related files are unstaged.
- [ ] Run `git log -1 --oneline` and confirm the latest commit is task-related.
- [ ] Confirm the active OpenSpec change is complete but not archived.
- [ ] Stop implementation at OpenSpec completion. Archive review is the next action, not immediate archive.
