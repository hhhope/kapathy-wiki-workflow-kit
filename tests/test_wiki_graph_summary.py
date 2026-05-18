import unittest

from scripts.summarize_wiki_graph import summarize_graph


class WikiGraphSummaryTest(unittest.TestCase):
    def test_summarizes_object_view_without_semantic_claims(self) -> None:
        graph = {
            "summary": {"node_count": 2, "edge_count": 1, "warning_count": 1},
            "nodes": [
                {
                    "page_path": "wiki/ops/example.md",
                    "canonical_object": "wiki-runtime",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                },
                {
                    "page_path": "openspec/specs/wiki-runtime/spec.md",
                    "canonical_object": "wiki-runtime",
                    "artifact_type": "spec",
                    "source_layer": "openspec/specs",
                },
            ],
            "edges": [
                {
                    "source_page_path": "wiki/ops/example.md",
                    "relation_type": "formalizes",
                    "target": "wiki-runtime",
                }
            ],
            "warnings": ["unresolved_identity:wiki/ops/loose.md"],
        }
        relation_analysis = {
            "summary": {
                "canonical_object_count": 1,
                "cross_layer_object_count": 1,
            },
            "object_coverage": [
                {
                    "canonical_object": "wiki-runtime",
                    "node_count": 2,
                    "source_layers": ["openspec/specs", "wiki/ops"],
                    "artifact_types": ["method", "spec"],
                    "relation_count": 1,
                    "cross_layer": True,
                }
            ],
        }

        summary = summarize_graph(graph, relation_analysis)

        self.assertEqual(summary["summary"]["displayed_object_count"], 1)
        self.assertEqual(summary["object_view"][0]["canonical_object"], "wiki-runtime")
        self.assertEqual(summary["object_view"][0]["relation_types"], {"formalizes": 1})
        self.assertEqual(summary["warning_view"]["by_layer"], {"wiki/ops": 1})
        self.assertEqual(summary["moc_candidates"]["summary"]["object_count"], 1)
        self.assertEqual(summary["moc_candidates"]["summary"]["relation_count"], 1)
        self.assertIn("structural graph evidence only", summary["proof_boundary_notes"][0])
        self.assertIn("does not write files", summary["proof_boundary_notes"][-1])

    def test_focus_filters_by_explicit_object_text(self) -> None:
        graph = {
            "summary": {},
            "nodes": [
                {
                    "page_path": "wiki/ops/a.md",
                    "canonical_object": "alpha-object",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                },
                {
                    "page_path": "wiki/ops/b.md",
                    "canonical_object": "beta-object",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                },
            ],
            "edges": [],
            "warnings": [],
        }

        summary = summarize_graph(graph, {"summary": {}, "object_coverage": []}, "alpha")

        self.assertEqual(
            [item["canonical_object"] for item in summary["object_view"]],
            ["alpha-object"],
        )

    def test_default_representative_pages_collapse_specs_but_retain_spec_evidence(self) -> None:
        graph = {
            "summary": {"node_count": 3, "edge_count": 1, "warning_count": 0},
            "nodes": [
                {
                    "page_path": "openspec/specs/wiki-runtime/spec.md",
                    "canonical_object": "wiki-runtime",
                    "artifact_type": "spec",
                    "source_layer": "openspec/specs",
                },
                {
                    "page_path": "wiki/adr/0001-wiki-runtime.md",
                    "canonical_object": "wiki-runtime",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                },
                {
                    "page_path": "wiki/ops/wiki-runtime.md",
                    "canonical_object": "wiki-runtime",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                },
            ],
            "edges": [
                {
                    "source_page_path": "wiki/ops/wiki-runtime.md",
                    "relation_type": "formalizes",
                    "target": "wiki-runtime",
                }
            ],
            "warnings": [],
        }
        relation_analysis = {
            "summary": {
                "canonical_object_count": 1,
                "cross_layer_object_count": 1,
            },
            "object_coverage": [
                {
                    "canonical_object": "wiki-runtime",
                    "node_count": 3,
                    "source_layers": ["openspec/specs", "wiki/adr", "wiki/ops"],
                    "artifact_types": ["adr", "method", "spec"],
                    "relation_count": 1,
                    "cross_layer": True,
                }
            ],
        }

        summary = summarize_graph(graph, relation_analysis)
        object_view = summary["object_view"][0]

        self.assertEqual(object_view["node_count"], 3)
        self.assertIn("openspec/specs", object_view["source_layers"])
        self.assertIn("spec", object_view["artifact_types"])
        self.assertEqual(object_view["relation_count"], 1)
        self.assertNotIn(
            "openspec/specs/wiki-runtime/spec.md",
            [page["page_path"] for page in object_view["representative_pages"]],
        )


if __name__ == "__main__":
    unittest.main()
