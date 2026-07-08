import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def read_visual_agent(path: str = "SKILL.md") -> str:
    return (SKILLS / "visual-agent" / path).read_text(encoding="utf-8")


class VisualAgentSkillPackageTest(unittest.TestCase):
    def test_reference_image_requests_are_image_mode_pressure(self):
        skill = read_visual_agent()
        evaluation = read_visual_agent("evaluation.md")

        for marker in [
            "reference PNG",
            "similar image",
            "image-mode pressure",
            "start HTML/CSS/SVG/browser-screenshot production",
            "explicitly chooses deterministic output",
        ]:
            self.assertIn(marker, skill)

        for marker in [
            "H5 source plus reference PNG / similar-image target",
            "`image_model` or `hybrid` as active route pressure",
            "do not start HTML/CSS/SVG/browser-screenshot production",
            "2026-06-23 Image Reference Mode Ownership",
        ]:
            self.assertIn(marker, evaluation)


if __name__ == "__main__":
    unittest.main()
