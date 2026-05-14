import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAYER_CONTRACT = ROOT / "wiki/ops/wiki-runtime-layer-contract.md"
README = ROOT / "README.md"
SPECS = ROOT / "openspec/specs"


class WikiRuntimeLayerContractTest(unittest.TestCase):
    def test_layer_contract_defines_all_runtime_layers(self) -> None:
        self.assertTrue(LAYER_CONTRACT.exists(), LAYER_CONTRACT)
        text = LAYER_CONTRACT.read_text(encoding="utf-8")

        for marker in [
            "Core loop",
            "Skill entrypoints",
            "Decision contract",
            "Observation tools",
            "Boundaries",
            "Eval and lifecycle gates",
        ]:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_layer_contract_separates_eval_scorecard_and_lifecycle_gates(self) -> None:
        text = LAYER_CONTRACT.read_text(encoding="utf-8")

        self.assertIn("scorecard is an observation", text)
        self.assertIn("trace eval validates agent-produced decision traces", text)
        self.assertIn("behavior asset checker validates behavior-change evidence", text)
        self.assertIn("OpenSpec owns workflow/runtime change lifecycle", text)

    def test_readme_explains_wiki_react_without_replacing_domain_skills(self) -> None:
        text = README.read_text(encoding="utf-8")

        self.assertIn("wiki-react is the explicit router", text)
        self.assertIn("does not replace domain skills", text)
        self.assertIn("status -> wiki-status", text)
        self.assertIn("repair -> wiki-apply", text)
        self.assertIn("uncertain/high-risk -> wiki-react", text)
        self.assertIn("scorecard/evidence strength -> wiki-scorecard", text)

    def test_active_specs_do_not_use_obsolete_slash_command_names(self) -> None:
        offending = [
            path.relative_to(ROOT).as_posix()
            for path in SPECS.rglob("*")
            if "slash-command" in path.as_posix()
        ]

        self.assertEqual(offending, [])


if __name__ == "__main__":
    unittest.main()
