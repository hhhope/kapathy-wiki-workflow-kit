from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_gate_precheck import build_precheck_report


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def strict_config() -> str:
    return """
version: 1
fields:
  domain:
    forbidden:
      - personal-ops
    known:
      - none
  ops_area:
    allowed:
      - agent-governance
severity:
  missing_required_field: error
  unexpected_field_value: error
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
scorecard:
  dimensions:
    completeness: 40
    taxonomy_validity: 25
    identity_coverage: 20
    relation_shape: 15
""".lstrip()


class WikiGatePrecheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-gate-precheck-test-"))
        write(self.tmpdir / "wiki/config/frontmatter-taxonomy.yaml", strict_config())

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_precheck_reports_compact_failure_without_full_entries(self) -> None:
        write(
            self.tmpdir / "wiki/ops/broken.md",
            """---
title: Broken
---

# Broken
""",
        )

        report = build_precheck_report(
            root=self.tmpdir,
            mode="frontmatter",
            target="wiki/ops/broken.md",
            top=2,
            json_output=self.tmpdir / "full.json",
            markdown_output=self.tmpdir / "full.md",
        )

        self.assertEqual(report["gate"], "wiki-frontmatter-taxonomy")
        self.assertFalse(report["passed"])
        self.assertEqual(report["score"], 0)
        self.assertEqual(report["minimum_pass_score"], 100)
        self.assertGreater(report["blocking_count"], 0)
        self.assertLessEqual(len(report["top_blockers"]), 2)
        self.assertGreaterEqual(len(report["top_blockers"]), 1)
        self.assertNotIn("entries", report)
        self.assertEqual(report["target"]["path"], "wiki/ops/broken.md")
        self.assertLessEqual(len(report["target"]["entries"]), 2)
        self.assertGreaterEqual(len(report["target"]["entries"]), 1)
        self.assertEqual(
            report["target"]["repair_hints"]["exact_frontmatter"],
            {"layer": "ops"},
        )
        self.assertEqual(
            report["target"]["repair_hints"]["required_fields"],
            ["layer", "domain", "ops_area", "canonical_object", "artifact_type"],
        )
        self.assertEqual(
            report["target"]["repair_hints"]["field_options"]["ops_area"],
            ["agent-governance"],
        )
        self.assertEqual(
            report["target"]["repair_hints"]["field_options"]["domain"],
            ["none"],
        )
        self.assertTrue(report["full_report"]["json"].endswith("full.json"))
        self.assertTrue(report["full_report"]["markdown"].endswith("full.md"))


    def test_precheck_preserves_whole_gate_result_for_clean_target(self) -> None:
        write(
            self.tmpdir / "wiki/ops/broken.md",
            """---
title: Broken
---

# Broken
""",
        )
        write(
            self.tmpdir / "wiki/ops/clean.md",
            """---
layer: ops
domain: none
ops_area: agent-governance
canonical_object: clean
artifact_type: method
---

# Clean
""",
        )

        report = build_precheck_report(
            root=self.tmpdir,
            mode="frontmatter",
            target="wiki/ops/clean.md",
            top=3,
            json_output=self.tmpdir / "full.json",
            markdown_output=self.tmpdir / "full.md",
        )

        self.assertFalse(report["passed"])
        self.assertEqual(report["target"]["path"], "wiki/ops/clean.md")
        self.assertEqual(report["target"]["entry_count"], 0)
        self.assertEqual(report["target"]["entries"], [])
