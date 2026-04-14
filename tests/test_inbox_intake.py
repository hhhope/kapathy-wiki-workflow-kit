import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.inbox_intake import generate_source_draft, process_inbox


class InboxIntakeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="inbox-intake-test-"))
        self.inbox_dir = self.tmpdir / "inbox"
        self.wiki_sources_dir = self.tmpdir / "wiki" / "sources"
        self.inbox_dir.mkdir(parents=True)
        self.wiki_sources_dir.mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_generates_chinese_summary_for_english_source(self) -> None:
        source_file = self.inbox_dir / "weekly_update.txt"
        source_file.write_text(
            "Weekly clearing update\nRisks are tracked and owners are assigned.\n",
            encoding="utf-8",
        )

        output_path = generate_source_draft(source_file, self.wiki_sources_dir)

        self.assertEqual(output_path, self.wiki_sources_dir / "weekly-update.md")
        self.assertTrue(output_path.exists())
        content = output_path.read_text(encoding="utf-8")
        self.assertIn("language: en", content)
        self.assertIn("## 中文摘要", content)
        self.assertIn("待补充：请基于英文原文整理中文摘要。", content)
        self.assertIn("## English Notes", content)
        self.assertIn("Weekly clearing update", content)

    def test_generates_chinese_language_source_for_chinese_input(self) -> None:
        source_file = self.inbox_dir / "meeting_note.txt"
        source_file.write_text(
            "清结算周会纪要\n本周需要补齐自动分类规则。\n",
            encoding="utf-8",
        )

        output_path = generate_source_draft(source_file, self.wiki_sources_dir)

        content = output_path.read_text(encoding="utf-8")
        self.assertIn("language: zh-CN", content)
        self.assertIn("待补充：请基于原始输入整理中文摘要。", content)
        self.assertIn("## English Notes", content)

    def test_process_inbox_generates_drafts_for_supported_files(self) -> None:
        (self.inbox_dir / "README.md").write_text("ignore me", encoding="utf-8")
        (self.inbox_dir / "todo.txt").write_text("Need a codex handoff", encoding="utf-8")
        (self.inbox_dir / "notes.md").write_text("清结算记录", encoding="utf-8")

        output_paths = process_inbox(self.inbox_dir, self.wiki_sources_dir)

        self.assertEqual(
            [path.name for path in output_paths],
            ["notes.md", "todo.md"],
        )
        self.assertTrue((self.wiki_sources_dir / "todo.md").exists())
        self.assertTrue((self.wiki_sources_dir / "notes.md").exists())


if __name__ == "__main__":
    unittest.main()
