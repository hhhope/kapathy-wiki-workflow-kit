from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_wiki_frontmatter import build_report
from scripts.check_wiki_frontmatter import load_taxonomy
from scripts.check_wiki_frontmatter import check_content_drift
from scripts.check_wiki_frontmatter import check_possible_unregistered_producers
from scripts.check_wiki_frontmatter import check_registered_producer_drift
from scripts.check_wiki_frontmatter import render_markdown_report


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


def strict_config() -> str:
    return """
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
      - agent-governance
severity:
  missing_required_field: error
  unexpected_field_value: error
  forbidden_domain: error
  unclassified_without_flag: error
strict_gate:
  enabled: true
  minimum_pass_score: 100
  blocking_severities:
    - error
  rule_sets:
    whole_wiki:
      path_globs:
        - wiki/**/*.md
      required:
        - layer
        - domain
    ops_pages:
      path_globs:
        - wiki/ops/**/*.md
      required:
        - ops_area
        - canonical_object
        - artifact_type
      expected:
        layer: ops
    adr_pages:
      path_globs:
        - wiki/adr/**/*.md
      required:
        - canonical_object
        - artifact_type
      expected:
        layer: adr
        domain: none
scorecard:
  dimensions:
    completeness: 40
    taxonomy_validity: 25
    identity_coverage: 20
    relation_shape: 15
""".lstrip()


class StrictFrontmatterGateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="strict-frontmatter-test-"))
        write(self.tmpdir / "wiki/config/frontmatter-taxonomy.yaml", strict_config())

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_ops_page_missing_strict_fields_fails_gate(self) -> None:
        write(
            self.tmpdir / "wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md",
            """---
title: visual-output-routing / fix recheck
status: active
---

# Visual Output Routing Fix Recheck
""",
        )

        report = build_report(self.tmpdir)
        entries = [
            entry
            for entry in report["entries"]
            if entry["path"] == "wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md"
        ]

        self.assertFalse(report["strict_gate"]["passed"])
        self.assertEqual(report["scorecard"]["score"], 0)
        self.assertIn(
            ("missing_required_field", "layer"),
            {(entry["kind"], entry["field"]) for entry in entries},
        )
        self.assertIn(
            ("missing_required_field", "domain"),
            {(entry["kind"], entry["field"]) for entry in entries},
        )
        self.assertIn(
            ("missing_required_field", "ops_area"),
            {(entry["kind"], entry["field"]) for entry in entries},
        )

    def test_adr_page_missing_taxonomy_fields_fails_gate(self) -> None:
        write(
            self.tmpdir / "wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md",
            """---
canonical_object: wiki-runtime-context-source-integration
artifact_type: adr
---

# ADR
""",
        )

        report = build_report(self.tmpdir)
        entries = [
            entry
            for entry in report["entries"]
            if entry["path"]
            == "wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md"
        ]

        self.assertFalse(report["strict_gate"]["passed"])
        self.assertIn(
            ("missing_required_field", "layer"),
            {(entry["kind"], entry["field"]) for entry in entries},
        )
        self.assertIn(
            ("missing_required_field", "domain"),
            {(entry["kind"], entry["field"]) for entry in entries},
        )

    def test_compliant_ops_and_adr_pages_pass_strict_gate(self) -> None:
        write(
            self.tmpdir / "wiki/ops/compliant.md",
            """---
layer: ops
domain: none
ops_area: agent-governance
canonical_object: compliant
artifact_type: method
---

# Compliant
""",
        )
        write(
            self.tmpdir / "wiki/adr/0032-compliant.md",
            """---
layer: adr
domain: none
canonical_object: compliant
artifact_type: adr
---

# ADR
""",
        )

        report = build_report(self.tmpdir)

        self.assertTrue(report["strict_gate"]["passed"])
        self.assertEqual(report["scorecard"]["score"], 100)
        self.assertEqual(report["summary"]["error"], 0)
