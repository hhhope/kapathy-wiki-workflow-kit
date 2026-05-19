import unittest

from scripts.wiki_moc_temperature import (
    build_moc_admission_plan,
    build_relation_feature_packages,
    build_temperature_clue_board,
    temperature_band,
)


class WikiMocTemperatureTest(unittest.TestCase):
    def sample_graph(self) -> dict:
        return {
            "nodes": [
                {
                    "page_path": "wiki/ops/runtime-method.md",
                    "canonical_object": "runtime-method",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                    "domain": "wiki",
                },
                {
                    "page_path": "wiki/adr/001-runtime.md",
                    "canonical_object": "runtime-method",
                    "artifact_type": "adr",
                    "source_layer": "wiki/adr",
                    "domain": "wiki",
                },
                {
                    "page_path": "openspec/specs/runtime/spec.md",
                    "canonical_object": "runtime-spec",
                    "artifact_type": "spec",
                    "source_layer": "openspec/specs",
                    "domain": "wiki",
                },
            ],
            "edges": [
                {
                    "source_page_path": "wiki/adr/001-runtime.md",
                    "relation_type": "derived_from",
                    "target": "runtime-method",
                },
                {
                    "source_page_path": "openspec/specs/runtime/spec.md",
                    "relation_type": "validates",
                    "target": "runtime-method",
                },
            ],
        }

    def test_builds_relation_feature_packages_without_semantic_admission(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())

        self.assertEqual(
            [package["candidate_id"] for package in packages],
            [
                "relation:wiki/adr/001-runtime.md:derived_from:runtime-method",
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method",
            ],
        )
        first = packages[0]
        self.assertEqual(first["source_page"], "wiki/adr/001-runtime.md")
        self.assertEqual(first["source_object"], "runtime-method")
        self.assertEqual(first["relation_type"], "derived_from")
        self.assertEqual(first["target_object"], "runtime-method")
        self.assertEqual(first["source_layer"], "wiki/adr")
        self.assertEqual(first["target_layer"], "wiki/ops")
        self.assertEqual(
            first["evidence_refs"],
            ["wiki/adr/001-runtime.md", "wiki/ops/runtime-method.md"],
        )
        self.assertTrue(first["structural_features"]["mechanical_relation"])
        self.assertNotIn("moc_admission", first)

    def test_handles_malformed_top_level_graph_fields_as_empty(self) -> None:
        self.assertEqual(build_relation_feature_packages({"nodes": None}), [])
        self.assertEqual(build_relation_feature_packages({"edges": None}), [])
        self.assertEqual(
            build_relation_feature_packages({"nodes": None, "edges": None}),
            [],
        )

    def test_temperature_band_is_continuous_guidance(self) -> None:
        cases = {
            100: "strong",
            80: "strong",
            79: "supporting",
            60: "supporting",
            59: "weak",
            40: "weak",
            39: "noise",
            0: "noise",
        }

        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(temperature_band(value), expected)

    def test_reviewed_clue_board_blocks_mechanical_relation_without_explicit_admission(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:wiki/adr/001-runtime.md:derived_from:runtime-method": {
                    "temperature": 95,
                    "moc_admission": "needs_review",
                    "rationale": "Structural pointer only.",
                }
            },
        )
        derived_window = board["windows"][0]

        self.assertEqual(derived_window["status"], "blocked")
        self.assertEqual(derived_window["moc_admission"], "needs_review")
        self.assertEqual(derived_window["admission"], "block")
        self.assertEqual(derived_window["temperature"], 95)
        self.assertEqual(derived_window["temperature_band"], "strong")
        self.assertEqual(board["counts"]["blocked_count"], 1)
        self.assertEqual(board["counts"]["review_needed_count"], 1)
        self.assertEqual(board["counts"]["blocked"], 1)
        self.assertEqual(board["counts"]["needs_review"], 1)
        self.assertEqual(board["counts"]["admitted"], 0)
        self.assertEqual(board["counts"]["total"], 2)
        self.assertEqual(board["summary"]["blocked_count"], 1)
        self.assertEqual(board["summary"]["review_needed_count"], 1)
        self.assertIs(board["clue_windows"], board["windows"])

        plan = build_moc_admission_plan(board)

        self.assertEqual(plan["counts"]["blocked_count"], 1)
        self.assertEqual(plan["counts"]["blocked"], 1)
        self.assertEqual(plan["counts"]["needs_review"], 1)
        self.assertEqual(plan["counts"]["admitted"], 0)
        self.assertEqual(plan["counts"]["total"], 2)
        self.assertIs(plan["clue_windows"], plan["windows"])
        self.assertNotIn("derived_from", plan["admitted_relations"])
        self.assertIn("derived_from", plan["blocked_relations"])

    def test_legacy_admission_field_does_not_admit_relation(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 88,
                    "admission": "admit_relation",
                    "rationale": "Legacy field must not drive admission.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertEqual(validates_window["status"], "needs_review")
        self.assertEqual(validates_window["moc_admission"], "needs_review")
        self.assertEqual(board["counts"]["admitted"], 0)
        self.assertEqual(board["counts"]["needs_review"], 1)
        self.assertEqual(board["counts"]["total"], 2)
        self.assertNotIn("validates", plan["admitted_relations"])

    def test_invalid_moc_admission_admit_relation_does_not_admit(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 88,
                    "moc_admission": "admit_relation",
                    "rationale": "Invalid admission value must not drive admission.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertEqual(validates_window["status"], "needs_review")
        self.assertEqual(validates_window["moc_admission"], "needs_review")
        self.assertEqual(board["counts"]["admitted"], 0)
        self.assertEqual(board["counts"]["needs_review"], 1)
        self.assertNotIn("validates", plan["admitted_relations"])

    def test_temperature_80_with_admit_admits_relation(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 80,
                    "moc_admission": "admit",
                    "rationale": "Boundary temperature admits relation.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertEqual(validates_window["status"], "admitted")
        self.assertIn("validates", plan["admitted_relations"])

    def test_admit_below_temperature_80_stays_needs_review(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 79,
                    "moc_admission": "admit",
                    "rationale": "Below the admission boundary.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertEqual(validates_window["status"], "needs_review")
        self.assertNotIn("validates", plan["admitted_relations"])

    def test_temperature_over_100_does_not_admit(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 101,
                    "moc_admission": "admit",
                    "rationale": "Out of range temperature.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertIsNone(validates_window["temperature"])
        self.assertIsNone(validates_window["temperature_band"])
        self.assertEqual(validates_window["status"], "needs_review")
        self.assertNotIn("validates", plan["admitted_relations"])

    def test_non_int_temperature_does_not_admit(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": "80",
                    "moc_admission": "admit",
                    "rationale": "String temperature is invalid.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertIsNone(validates_window["temperature"])
        self.assertEqual(validates_window["status"], "needs_review")
        self.assertNotIn("validates", plan["admitted_relations"])

    def test_bool_temperature_does_not_admit(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": True,
                    "moc_admission": "admit",
                    "rationale": "Bool temperature is invalid.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        validates_window = board["clue_windows"][1]

        self.assertIsNone(validates_window["temperature"])
        self.assertEqual(validates_window["status"], "needs_review")
        self.assertNotIn("validates", plan["admitted_relations"])

    def test_moc_admission_block_preserves_blocked_status(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 92,
                    "moc_admission": "block",
                    "rationale": "Explicit review block.",
                }
            },
        )

        validates_window = board["clue_windows"][1]

        self.assertEqual(validates_window["moc_admission"], "block")
        self.assertEqual(validates_window["status"], "blocked")

    def test_admission_plan_trusts_clue_window_status(self) -> None:
        plan = build_moc_admission_plan(
            {
                "counts": {
                    "admitted": 1,
                    "blocked": 0,
                    "needs_review": 0,
                    "total": 1,
                },
                "clue_windows": [
                    {
                        "status": "admitted",
                        "relation_type": "validates",
                        "target_object": "runtime-method",
                    }
                ],
            }
        )

        self.assertIn("validates", plan["admitted_relations"])
        self.assertIn("runtime-method", plan["admitted_objects"])

    def test_admits_high_temperature_relation_when_review_says_admit(self) -> None:
        packages = build_relation_feature_packages(self.sample_graph())
        board = build_temperature_clue_board(
            packages,
            reviews={
                "relation:openspec/specs/runtime/spec.md:validates:runtime-method": {
                    "temperature": 88,
                    "moc_admission": "admit",
                    "rationale": "Spec validation is a strong reading clue.",
                }
            },
        )

        plan = build_moc_admission_plan(board)
        admitted_window = board["clue_windows"][1]

        self.assertEqual(admitted_window["status"], "admitted")
        self.assertEqual(admitted_window["moc_admission"], "admit")
        self.assertEqual(board["counts"]["admitted_count"], 1)
        self.assertEqual(board["counts"]["admitted"], 1)
        self.assertEqual(board["counts"]["blocked"], 1)
        self.assertEqual(board["counts"]["needs_review"], 0)
        self.assertEqual(board["counts"]["total"], 2)
        self.assertEqual(plan["counts"]["admitted_count"], 1)
        self.assertEqual(plan["counts"]["admitted"], 1)
        self.assertEqual(plan["counts"]["blocked"], 1)
        self.assertEqual(plan["counts"]["needs_review"], 0)
        self.assertEqual(plan["counts"]["total"], 2)
        self.assertIn("runtime-method", plan["admitted_objects"])
        self.assertIn("validates", plan["admitted_relations"])
        self.assertNotIn("derived_from", plan["admitted_relations"])


if __name__ == "__main__":
    unittest.main()
