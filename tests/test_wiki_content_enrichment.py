import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_content_enrichment import build_enrichment_preview


class WikiContentEnrichmentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-enrichment-test-"))
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)
        (self.tmpdir / "wiki" / "adr").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config").mkdir(parents=True)
        (self.tmpdir / "openspec" / "specs" / "wiki-runtime-layer-boundary").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").write_text(
            """version: 1
fields:
  domain:
    known:
      - none
      - unclassified
      - wiki
      - report-workflow
  ops_area:
    allowed:
      - agent-governance
      - learning-capture
      - wiki-runtime
      - report-quality
      - workflow-trace
strict_gate:
  enabled: true
  rule_sets: {}
""",
            encoding="utf-8",
        )
        (self.tmpdir / "openspec" / "specs" / "wiki-runtime-layer-boundary" / "spec.md").write_text(
            "# wiki-runtime-layer-boundary Specification\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_suggests_ops_frontmatter_from_content_and_existing_objects(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "runtime-boundary-drift-retro.md").write_text(
            """# Runtime Boundary Drift

This retro explains wiki-react decision_trace, eval, apply preview, and
wiki-runtime-layer-boundary.
""",
            encoding="utf-8",
        )

        preview = build_enrichment_preview(self.tmpdir)
        entry = preview["entries"][0]

        self.assertEqual(entry["path"], "wiki/ops/runtime-boundary-drift-retro.md")
        self.assertEqual(entry["suggested_frontmatter"]["layer"], "ops")
        self.assertEqual(entry["suggested_frontmatter"]["domain"], "wiki")
        self.assertEqual(entry["suggested_frontmatter"]["ops_area"], "wiki-runtime")
        self.assertEqual(entry["suggested_frontmatter"]["canonical_object"], "runtime-boundary-drift")
        self.assertEqual(entry["suggested_frontmatter"]["artifact_type"], "retro")
        self.assertIn("wiki-runtime-layer-boundary", entry["suggested_relations"]["related_objects"])
        self.assertTrue(entry["needs_review"])
        self.assertTrue(entry["evidence"])

    def test_adr_defaults_to_domain_none_and_artifact_type_adr(self) -> None:
        (self.tmpdir / "wiki" / "adr" / "0034-readme-capability-map-is-project-description.md").write_text(
            """# ADR-0034 README Capability Map Is Project Description

README is project description, not runtime authority.
""",
            encoding="utf-8",
        )

        preview = build_enrichment_preview(self.tmpdir)
        entry = preview["entries"][0]

        self.assertEqual(entry["path"], "wiki/adr/0034-readme-capability-map-is-project-description.md")
        self.assertEqual(entry["suggested_frontmatter"]["layer"], "adr")
        self.assertEqual(entry["suggested_frontmatter"]["domain"], "none")
        self.assertEqual(entry["suggested_frontmatter"]["artifact_type"], "adr")
        self.assertEqual(
            entry["suggested_frontmatter"]["canonical_object"],
            "readme-capability-map-is-project-description",
        )

    def test_preserves_existing_valid_frontmatter(self) -> None:
        (self.tmpdir / "wiki" / "ops" / "existing.md").write_text(
            """---
layer: ops
domain: report-workflow
ops_area: report-quality
canonical_object: existing-object
artifact_type: method
---

# Existing
""",
            encoding="utf-8",
        )

        preview = build_enrichment_preview(self.tmpdir)
        entry = preview["entries"][0]

        self.assertEqual(entry["suggested_frontmatter"]["domain"], "report-workflow")
        self.assertEqual(entry["suggested_frontmatter"]["ops_area"], "report-quality")
        self.assertEqual(entry["suggested_frontmatter"]["canonical_object"], "existing-object")
        self.assertEqual(entry["confidence"], "high")
        self.assertFalse(entry["needs_review"])


if __name__ == "__main__":
    unittest.main()
