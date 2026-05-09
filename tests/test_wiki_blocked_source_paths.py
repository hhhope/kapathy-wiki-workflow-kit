import unittest
import sys
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from scripts.build_runtime_context_injection import build_context_injection
from scripts.build_wiki_change_queue_preview import build_queue_preview
from scripts.derive_runtime_auto_routing import build_runtime_auto_routing
from scripts.derive_self_directed_execution import build_self_directed_execution
from scripts.resolve_runtime_context_sources import build_integrated_runtime


class WikiBlockedSourcePathsTest(unittest.TestCase):
    def test_blocked_source_refs_survive_runtime_chain_to_queue_preview(self) -> None:
        source_ref = {
            "page_path": "wiki/ops/blocked-object.md",
            "artifact_type": "method",
            "source_layer": "wiki/ops",
        }
        runtime_context = {
            "summary": {"caution_active": False},
            "runtime_caution": {"direct_source_inspection_required": True},
            "preferred_context": [],
            "supporting_context": [],
            "blocked_context": [
                {
                    "canonical_object": "blocked-object",
                    "usage_guidance": "Do not anchor first-pass execution.",
                    "reasons": ["single-layer evidence only"],
                    "source_utilization_band": "blocked",
                    "source_semantic_score": 2,
                }
            ],
        }

        with patch(
            "scripts.resolve_runtime_context_sources.build_source_index",
            return_value={"blocked-object": [source_ref]},
        ):
            source_runtime = build_integrated_runtime(runtime_context)

        blocked_source_runtime = source_runtime["blocked_objects"][0]
        self.assertEqual(blocked_source_runtime["blocked_source_refs"], [source_ref])
        self.assertNotIn("resolved_sources", blocked_source_runtime)

        routing = build_runtime_auto_routing(source_runtime)
        blocked_routing = routing["do_not_open_first"][0]
        self.assertEqual(blocked_routing["blocked_source_refs"], [source_ref])
        self.assertNotIn("route_sources", blocked_routing)

        injection = build_context_injection(routing)
        excluded_object = injection["excluded_objects"][0]
        self.assertEqual(excluded_object["excluded_source_refs"], [source_ref])
        self.assertNotIn("injected_sources", excluded_object)

        execution = build_self_directed_execution(injection)
        blocked_execution = execution["do_not_execute"][0]
        self.assertEqual(
            blocked_execution["action_sources"],
            [
                {
                    "page_path": "wiki/ops/blocked-object.md",
                    "artifact_type": "method",
                    "source_layer": "wiki/ops",
                }
            ],
        )
        self.assertEqual(blocked_execution["action_type"], "blocked_from_first_pass_execution")

        queue = build_queue_preview(execution)
        self.assertEqual(queue["blocked"][0]["source_paths"], ["wiki/ops/blocked-object.md"])


if __name__ == "__main__":
    unittest.main()
