import re
import unittest
from pathlib import Path


COMMANDS = {
    "status": {
        "file": "commands/wiki-status.md",
        "references": (
            "scripts/build_wiki_status.py",
            "wiki/status/manifest.json",
            "wiki/status/wiki-status.md",
        ),
    },
    "manifest": {
        "file": "commands/wiki-manifest.md",
        "references": (
            "scripts/build_wiki_status.py",
            "wiki/status/manifest.json",
        ),
    },
    "inbox": {
        "file": "commands/wiki-inbox.md",
        "references": (
            "scripts/build_wiki_status.py",
            "wiki/status/manifest.json",
            "inbox/",
        ),
    },
    "graph": {
        "file": "commands/wiki-graph.md",
        "references": (
            "scripts/extract_wiki_graph.py",
            "scripts/analyze_wiki_relations.py",
            "scripts/examples/agent_readable_wiki_graph_sample.json",
            "scripts/examples/agent_readable_wiki_relation_analysis_sample.json",
        ),
    },
    "scorecard": {
        "file": "commands/wiki-scorecard.md",
        "references": (
            "scripts/score_wiki_semantics.py",
            "scripts/derive_wiki_utilization.py",
            "scripts/examples/agent_readable_wiki_semantic_scoring_sample.json",
            "scripts/examples/agent_readable_wiki_utilization_sample.json",
        ),
    },
    "route": {
        "file": "commands/wiki-route.md",
        "references": (
            "scripts/resolve_runtime_context_sources.py",
            "scripts/derive_runtime_auto_routing.py",
            "scripts/examples/agent_readable_wiki_runtime_context_source_integration_sample.json",
            "scripts/examples/agent_readable_wiki_runtime_auto_routing_sample.json",
        ),
    },
    "context": {
        "file": "commands/wiki-context.md",
        "references": (
            "scripts/build_wiki_runtime_context.py",
            "scripts/build_runtime_context_injection.py",
            "scripts/examples/agent_readable_wiki_runtime_context_sample.json",
            "scripts/examples/agent_readable_wiki_context_injection_sample.json",
        ),
    },
    "apply": {
        "file": "commands/wiki-apply.md",
        "references": (
            "scripts/build_runtime_context_injection.py",
            "scripts/derive_self_directed_execution.py",
            "scripts/examples/agent_readable_wiki_self_directed_execution_sample.json",
            "execute_now",
            "defer_for_followup",
            "do_not_execute",
        ),
    },
}


class WikiRuntimeCommandsTest(unittest.TestCase):
    def test_expected_wiki_runtime_command_files_exist(self) -> None:
        for command_name, command in COMMANDS.items():
            with self.subTest(command=command_name):
                self.assertTrue(Path(command["file"]).exists(), command["file"])

    def test_wiki_runtime_commands_use_wiki_namespace(self) -> None:
        for command_name, command in COMMANDS.items():
            with self.subTest(command=command_name):
                content = self.read_command(command["file"])
                self.assertIn(f"/wiki:{command_name}", content)
                self.assertNotIn("/report-wiki-portfolio:", content)

    def test_wiki_runtime_commands_name_their_runtime_inputs(self) -> None:
        for command_name, command in COMMANDS.items():
            with self.subTest(command=command_name):
                content = self.read_command(command["file"])
                for reference in command["references"]:
                    self.assertIn(reference, content)

    def test_wiki_runtime_commands_preserve_openspec_boundaries(self) -> None:
        for command_name, command in COMMANDS.items():
            with self.subTest(command=command_name):
                content = self.read_command(command["file"])
                normalized = self._normalize(content)

                self.assertRegex(
                    normalized,
                    re.compile(r"do not [^.]*openspec changes"),
                )
                self.assert_boundary_terms(
                    normalized,
                    ("create", "modify", "archive"),
                    boundary="OpenSpec lifecycle mutation",
                )
                self.assertRegex(normalized, re.compile(r"mark [^.]*tasks complete"))
                self.assertIn("change queue", normalized)

    def test_wiki_runtime_commands_reject_out_of_scope_product_surfaces(self) -> None:
        for command_name, command in COMMANDS.items():
            with self.subTest(command=command_name):
                normalized = self._normalize(self.read_command(command["file"]))

                self.assertIn("do not implement", normalized)
                self.assertIn("graph ui", normalized)
                self.assertIn("query engine", normalized)
                self.assertIn("change queue", normalized)

    def assert_boundary_terms(
        self,
        content: str,
        terms: tuple[str, ...],
        *,
        boundary: str,
    ) -> None:
        boundary_lines = [
            line
            for line in content.splitlines()
            if "do not" in line and ("openspec" in line or "implement" in line)
        ]
        self.assertTrue(boundary_lines, boundary)
        joined = "\n".join(boundary_lines)
        for term in terms:
            self.assertIn(term, joined, boundary)

    def read_command(self, command_file: str) -> str:
        path = Path(command_file)
        self.assertTrue(path.exists(), command_file)
        return path.read_text(encoding="utf-8")

    def _normalize(self, content: str) -> str:
        return content.replace("`", "").lower()


if __name__ == "__main__":
    unittest.main()
