from __future__ import annotations

import shutil
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_frontmatter_repair import (
    apply_frontmatter_batch,
    build_repair_batch,
)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def strict_config() -> str:
    return """
version: 1
fields:
  layer:
    allowed:
      - ops
      - adr
  domain:
    known:
      - none
      - wiki
  ops_area:
    allowed:
      - wiki-runtime
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
severity:
  missing_required_field: error
  unexpected_field_value: error
scorecard:
  dimensions:
    completeness: 40
    taxonomy_validity: 25
    identity_coverage: 20
    relation_shape: 15
""".lstrip()


class WikiFrontmatterRepairTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-frontmatter-repair-test-"))
        write(self.tmpdir / "wiki/config/frontmatter-taxonomy.yaml", strict_config())
        write(
            self.tmpdir / "wiki/ops/broken.md",
            """---
title: Broken
---

# Broken
""",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_builds_explicit_batch_from_precheck_report(self) -> None:
        batch = build_repair_batch(self.tmpdir, limit=1)

        self.assertEqual(batch["mode"], "wiki_frontmatter_repair_batch")
        self.assertEqual(batch["summary"]["selected_count"], 1)
        item = batch["items"][0]
        self.assertEqual(item["path"], "wiki/ops/broken.md")
        self.assertGreater(item["blocking_entry_count"], 0)
        self.assertEqual(item["repair_hints"]["exact_frontmatter"], {"layer": "ops"})
        self.assertIn("domain", item["repair_hints"]["field_options"])
        self.assertEqual(item["decision"], "review_needed")

    def test_apply_batch_writes_only_approved_frontmatter_fields(self) -> None:
        batch = build_repair_batch(self.tmpdir, limit=1)

        result = apply_frontmatter_batch(
            self.tmpdir,
            batch,
            approved_frontmatter={
                "wiki/ops/broken.md": {
                    "layer": "ops",
                    "domain": "none",
                    "ops_area": "wiki-runtime",
                    "canonical_object": "broken",
                    "artifact_type": "method",
                    "related_objects": ["must-not-write"],
                }
            },
            apply=True,
        )

        text = (self.tmpdir / "wiki/ops/broken.md").read_text(encoding="utf-8")
        self.assertEqual(result["summary"]["applied_count"], 1)
        self.assertGreater(result["results"][0]["before"]["entry_count"], 0)
        self.assertEqual(result["results"][0]["after"]["entry_count"], 0)
        self.assertIn("layer: ops", text)
        self.assertIn("domain: none", text)
        self.assertIn("ops_area: wiki-runtime", text)
        self.assertIn("canonical_object: broken", text)
        self.assertIn("artifact_type: method", text)
        self.assertNotIn("related_objects", text)

    def test_cli_outputs_repair_batch(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_frontmatter_repair.py",
                "--root",
                str(self.tmpdir),
                "--limit",
                "1",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["batch"]["summary"]["selected_count"], 1)
        self.assertEqual(payload["batch"]["items"][0]["path"], "wiki/ops/broken.md")


if __name__ == "__main__":
    unittest.main()
