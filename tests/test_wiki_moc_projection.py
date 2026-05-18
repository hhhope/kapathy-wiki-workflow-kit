import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_moc_projection import (
    apply_moc_plan,
    build_moc_candidates,
    build_moc_health,
    build_moc_plan,
)


class WikiMocProjectionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-moc-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def sample_graph(self) -> dict:
        return {
            "nodes": [
                {
                    "page_path": "wiki/ops/agent-readable-wiki-frontmatter.md",
                    "canonical_object": "wiki-frontmatter-model",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                },
                {
                    "page_path": "wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md",
                    "canonical_object": "wiki-frontmatter-model",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                    "domain": "wiki",
                },
            ],
            "edges": [
                {
                    "source_page_path": "wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md",
                    "relation_type": "formalizes",
                    "target": "wiki-frontmatter-model",
                }
            ],
        }

    def test_builds_domain_object_and_relation_candidates(self) -> None:
        candidates = build_moc_candidates(self.sample_graph())
        paths = {candidate.path for candidate in candidates}

        self.assertIn("wiki/moc/domain-wiki.md", paths)
        self.assertIn("wiki/moc/object-wiki-frontmatter-model.md", paths)
        self.assertIn("wiki/moc/relation-formalizes.md", paths)

    def test_object_preview_groups_pages_by_lifecycle_not_ops_area(self) -> None:
        graph = {
            "nodes": [
                {
                    "page_path": "wiki/ops/karpathy-llm-wiki-reading-notes.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "reading-notes",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                    "ops_area": "learning-capture",
                },
                {
                    "page_path": "openspec/specs/wiki-runtime-context/spec.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "spec",
                    "source_layer": "openspec/specs",
                    "domain": "wiki",
                },
                {
                    "page_path": "wiki/adr/0019-agent-readable-wiki-runtime-context-after-utilization.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                    "domain": "none",
                },
                {
                    "page_path": "wiki/ops/wiki-runtime-layer-contract.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                    "ops_area": "wiki-runtime",
                },
                {
                    "page_path": "wiki/ops/wiki-readable-views-validation-harness.md",
                    "canonical_object": "llm-wiki",
                    "artifact_type": "replay-harness",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                    "ops_area": "workflow-trace",
                },
            ],
            "edges": [],
        }

        plan = build_moc_plan(self.tmpdir, graph)
        object_entry = next(
            entry
            for entry in plan["entries"]
            if entry["path"] == "wiki/moc/object-llm-wiki.md"
        )
        preview = object_entry["preview"]

        for heading in [
            "## Sources / Learning",
            "## Specification",
            "## Decisions",
            "## Methods / Runtime",
            "## Evidence / Replay",
        ]:
            self.assertIn(heading, preview)

        self.assertNotIn("## learning-capture", preview)
        self.assertNotIn("## workflow-trace", preview)
        self.assertEqual(object_entry["link_count"], 5)

    def test_dry_run_plan_does_not_write_files(self) -> None:
        plan = build_moc_plan(self.tmpdir, self.sample_graph())

        self.assertEqual(plan["summary"]["create_count"], 3)
        self.assertFalse((self.tmpdir / "wiki" / "moc").exists())

    def test_apply_writes_generated_moc_files(self) -> None:
        plan = apply_moc_plan(self.tmpdir, self.sample_graph())
        domain_path = self.tmpdir / "wiki" / "moc" / "domain-wiki.md"

        self.assertEqual(plan["summary"]["create_count"], 3)
        self.assertTrue(domain_path.exists())
        text = domain_path.read_text(encoding="utf-8")
        self.assertIn("<!-- BEGIN GENERATED MOC: domain=wiki -->", text)
        self.assertIn("[[agent-readable-wiki-frontmatter]]", text)

    def test_update_preserves_manual_content_outside_generated_block(self) -> None:
        apply_moc_plan(self.tmpdir, self.sample_graph())
        object_path = self.tmpdir / "wiki" / "moc" / "object-wiki-frontmatter-model.md"
        original = object_path.read_text(encoding="utf-8")
        object_path.write_text(f"Manual note\n\n{original}", encoding="utf-8")

        graph = self.sample_graph()
        graph["nodes"].append(
            {
                "page_path": "openspec/specs/wiki-frontmatter-model/spec.md",
                "canonical_object": "wiki-frontmatter-model",
                "artifact_type": "spec",
                "source_layer": "openspec/specs",
                "domain": "wiki",
            }
        )
        apply_moc_plan(self.tmpdir, graph)

        updated = object_path.read_text(encoding="utf-8")
        self.assertIn("Manual note", updated)
        self.assertIn("[[spec]]", updated)

    def test_health_reports_missing_and_then_passes_after_apply(self) -> None:
        missing = build_moc_health(self.tmpdir, self.sample_graph())
        self.assertEqual(missing["status"], "drift")
        self.assertEqual(missing["summary"]["create_count"], 3)

        apply_moc_plan(self.tmpdir, self.sample_graph())
        clean = build_moc_health(self.tmpdir, self.sample_graph())

        self.assertEqual(clean["status"], "pass")
        self.assertEqual(clean["summary"]["noop_count"], 3)


if __name__ == "__main__":
    unittest.main()
