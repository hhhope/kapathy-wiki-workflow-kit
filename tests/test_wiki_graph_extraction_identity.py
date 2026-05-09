import unittest

from scripts.extract_wiki_graph import ROOT, collect_pages, derive_object_and_type


class WikiGraphExtractionIdentityTest(unittest.TestCase):
    def test_derives_openspec_spec_identity_from_path(self) -> None:
        path = ROOT / "openspec/specs/wiki-runtime-slash-command-surface/spec.md"

        canonical_object, artifact_type = derive_object_and_type(path, {})

        self.assertEqual(canonical_object, "wiki-runtime-slash-command-surface")
        self.assertEqual(artifact_type, "spec")

    def test_derives_known_runtime_adr_identity_from_filename(self) -> None:
        path = ROOT / "wiki/adr/0017-agent-readable-wiki-semantic-scoring-after-relation-analysis.md"

        canonical_object, artifact_type = derive_object_and_type(path, {})

        self.assertEqual(canonical_object, "wiki-semantic-scoring")
        self.assertEqual(artifact_type, "adr")

    def test_derives_numbered_adr_identity_from_path(self) -> None:
        path = ROOT / "wiki/adr/0007-archive-review-before-archive.md"

        canonical_object, artifact_type = derive_object_and_type(path, {})

        self.assertEqual(canonical_object, "archive-review-before-archive")
        self.assertEqual(artifact_type, "adr")

    def test_derives_example_identity_from_path(self) -> None:
        path = ROOT / "wiki/examples/meeting-note-example.md"

        canonical_object, artifact_type = derive_object_and_type(path, {})

        self.assertEqual(canonical_object, "meeting-note")
        self.assertEqual(artifact_type, "example")

    def test_does_not_infer_identity_from_unmapped_ops_page(self) -> None:
        path = ROOT / "wiki/ops/reminders.md"

        canonical_object, artifact_type = derive_object_and_type(path, {})

        self.assertIsNone(canonical_object)
        self.assertIsNone(artifact_type)

    def test_live_extraction_resolves_target_runtime_pages(self) -> None:
        nodes, _edges, warnings = collect_pages()
        warning_text = "\n".join(warnings)
        node_paths = {node["page_path"] for node in nodes}

        self.assertNotIn(
            "unresolved_identity:openspec/specs/wiki-runtime-slash-command-surface/spec.md",
            warning_text,
        )
        self.assertNotIn(
            "unresolved_identity:wiki/adr/0007-archive-review-before-archive.md",
            warning_text,
        )
        self.assertNotIn(
            "unresolved_identity:wiki/examples/meeting-note-example.md",
            warning_text,
        )
        self.assertIn(
            "wiki/ops/agent-readable-wiki-graph-extraction.md",
            node_paths,
        )
        self.assertLess(len(warnings), 49)


if __name__ == "__main__":
    unittest.main()
