import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.bootstrap_wiki_workflow_kit import main as bootstrap_main
from scripts.verify_wiki_workflow_kit import verify_installation


class BootstrapWikiWorkflowKitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="bootstrap-wiki-workflow-kit-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_bootstrap_installs_inbox_entrypoints_and_intake_script(self) -> None:
        target_dir = self.tmpdir / "kit"

        exit_code = bootstrap_main(
            [
                "--project-name",
                "Example Kit",
                "--target-dir",
                str(target_dir),
                "--owner",
                "yan",
            ]
        )

        self.assertEqual(exit_code, 0)
        self.assertTrue((target_dir / "README.md").exists())
        self.assertTrue((target_dir / "README.en.md").exists())
        self.assertTrue((target_dir / "inbox" / "README.md").exists())
        self.assertTrue((target_dir / "scripts" / "inbox_intake.py").exists())
        self.assertTrue((target_dir / "wiki" / "sources" / "index.md").exists())
        readme = (target_dir / "README.md").read_text(encoding="utf-8")
        readme_en = (target_dir / "README.en.md").read_text(encoding="utf-8")
        self.assertIn("[中文](README.md) | [English](README.en.md)", readme)
        self.assertIn("[中文](README.md) | [English](README.en.md)", readme_en)
        self.assertIn("## 快速开始", readme)
        self.assertNotIn("## English Guide", readme)
        self.assertNotIn("This repository is", readme)
        self.assertIn("[PROJECT.md]", readme)
        self.assertIn("## Quick Start", readme_en)
        self.assertNotIn("## 中文入口", readme_en)

    def test_verify_accepts_install_without_obsidian_when_mode_disables_it(self) -> None:
        target_dir = self.tmpdir / "kit-no-obsidian"

        exit_code = bootstrap_main(
            [
                "--project-name",
                "Example Kit",
                "--target-dir",
                str(target_dir),
                "--owner",
                "yan",
                "--without-obsidian",
            ]
        )

        self.assertEqual(exit_code, 0)
        result = verify_installation(
            target_dir,
            with_openspec=True,
            with_obsidian=False,
            with_examples=True,
        )

        self.assertEqual(result.missing_required, [])
        self.assertEqual(result.missing_optional, [".obsidian/core-plugins.json"])


if __name__ == "__main__":
    unittest.main()
