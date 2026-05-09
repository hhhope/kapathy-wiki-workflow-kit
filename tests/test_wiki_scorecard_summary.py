import unittest

from scripts.summarize_wiki_scorecard import summarize_scorecard


class WikiScorecardSummaryTest(unittest.TestCase):
    def test_builds_actionable_diagnostics_with_boundaries(self) -> None:
        scores = {
            "summary": {
                "scored_object_count": 2,
                "band_counts": {"strong": 1, "moderate": 0, "weak": 1},
            },
            "object_scores": [
                {
                    "canonical_object": "wiki-context",
                    "semantic_score": 8,
                    "score_band": "strong",
                    "factor_breakdown": {"cross_layer_presence": 3},
                    "coverage_snapshot": {
                        "source_layers": ["wiki/ops", "openspec/specs"],
                        "artifact_types": ["method", "spec"],
                    },
                },
                {
                    "canonical_object": "loose-note",
                    "semantic_score": 1,
                    "score_band": "weak",
                    "factor_breakdown": {"cross_layer_presence": 0},
                    "coverage_snapshot": {
                        "source_layers": ["wiki/ops"],
                        "artifact_types": ["intake"],
                    },
                },
            ],
        }
        utilization = {
            "summary": {
                "band_counts": {"preferred": 1, "cautious": 0, "blocked": 1}
            },
            "repository_caution": {"caution_active": True},
            "object_utilization": [
                {
                    "canonical_object": "wiki-context",
                    "utilization_band": "preferred",
                    "reasons": ["strong bounded semantic score"],
                },
                {
                    "canonical_object": "loose-note",
                    "utilization_band": "blocked",
                    "reasons": ["single-layer evidence only"],
                },
            ],
        }

        summary = summarize_scorecard(scores, utilization)

        self.assertEqual(summary["summary"]["displayed_diagnostic_count"], 2)
        self.assertEqual(summary["diagnostics"][0]["canonical_object"], "wiki-context")
        self.assertIn("Inspect explicit source layers", summary["diagnostics"][0]["next_inspection_actions"][0])
        self.assertIn("no embeddings", summary["proof_boundary_notes"][1])
        self.assertTrue(summary["summary"]["caution_active"])

    def test_focus_filters_by_explicit_object_text(self) -> None:
        scores = {
            "summary": {},
            "object_scores": [
                {
                    "canonical_object": "alpha-object",
                    "semantic_score": 7,
                    "score_band": "strong",
                    "factor_breakdown": {},
                    "coverage_snapshot": {"source_layers": [], "artifact_types": []},
                },
                {
                    "canonical_object": "beta-object",
                    "semantic_score": 7,
                    "score_band": "strong",
                    "factor_breakdown": {},
                    "coverage_snapshot": {"source_layers": [], "artifact_types": []},
                },
            ],
        }

        summary = summarize_scorecard(
            scores,
            {"summary": {}, "repository_caution": {}, "object_utilization": []},
            "beta",
        )

        self.assertEqual(
            [item["canonical_object"] for item in summary["diagnostics"]],
            ["beta-object"],
        )


if __name__ == "__main__":
    unittest.main()
