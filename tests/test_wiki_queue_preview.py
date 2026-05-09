import unittest

from scripts.build_wiki_change_queue_preview import build_queue_preview


class WikiQueuePreviewTest(unittest.TestCase):
    def test_groups_execution_output_without_mutation_claims(self) -> None:
        execution = {
            "summary": {
                "caution_active": True,
                "direct_source_inspection_required": True,
            },
            "execute_now": [
                {
                    "canonical_object": "ready-object",
                    "action_type": "inspect_and_apply_context",
                    "reasons": ["first-pass candidate"],
                    "action_sources": [{"page_path": "wiki/ops/ready.md"}],
                }
            ],
            "defer_for_followup": [
                {
                    "canonical_object": "decision-object",
                    "action_type": "inspect_before_followup",
                    "reasons": ["follow-up candidate"],
                    "action_sources": [{"page_path": "wiki/ops/decision.md"}],
                }
            ],
            "do_not_execute": [
                {
                    "canonical_object": "blocked-object",
                    "action_type": "blocked_from_first_pass_execution",
                    "reasons": ["single-layer evidence only"],
                }
            ],
        }

        preview = build_queue_preview(execution)

        self.assertEqual(preview["summary"]["ready_count"], 1)
        self.assertEqual(preview["summary"]["needs_user_decision_count"], 1)
        self.assertEqual(preview["summary"]["blocked_count"], 1)
        self.assertEqual(preview["ready"][0]["source_paths"], ["wiki/ops/ready.md"])
        self.assertEqual(preview["needs_user_decision"][0]["queue_state"], "needs_user_decision")
        self.assertIn("does not create, modify, archive, or queue OpenSpec changes", preview["proof_boundary_notes"][1])


if __name__ == "__main__":
    unittest.main()
