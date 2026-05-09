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
        self.assertIn("structural graph evidence only", summary["proof_boundary_notes"][0])

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


if __name__ == "__main__":
    unittest.main()
