import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path


from scripts.inbox_intake import generate_intake_draft, generate_source_draft, process_inbox


class InboxIntakeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="inbox-intake-test-"))
        self.inbox_dir = self.tmpdir / "inbox"
        self.wiki_sources_dir = self.tmpdir / "wiki" / "sources"
        self.inbox_dir.mkdir(parents=True)
        self.wiki_sources_dir.mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _write_docx(self, path: Path, text: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr(
                "[Content_Types].xml",
                """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>""",
            )
            archive.writestr(
                "_rels/.rels",
                """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>""",
            )
            archive.writestr(
                "word/document.xml",
                f"""<?xml version="1.0" encoding="UTF-8"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:r><w:t>{text}</w:t></w:r></w:p>
  </w:body>
</w:document>""",
            )

    def test_generates_chinese_summary_for_english_source(self) -> None:
        source_file = self.inbox_dir / "weekly_update.txt"
        source_file.write_text(
            "Weekly clearing update\nRisks are tracked and owners are assigned.\n",
            encoding="utf-8",
        )

        output_path = generate_source_draft(source_file, self.wiki_sources_dir, self.inbox_dir)

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

        output_path = generate_source_draft(source_file, self.wiki_sources_dir, self.inbox_dir)

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

    def test_generates_intake_draft_linked_to_source(self) -> None:
        source_file = self.inbox_dir / "routing_note.txt"
        source_file.write_text("Need to route engineering todos to codex", encoding="utf-8")
        wiki_ops_dir = self.tmpdir / "wiki" / "ops"
        wiki_ops_dir.mkdir(parents=True)

        output_path = generate_intake_draft(source_file, wiki_ops_dir, self.inbox_dir)

        self.assertEqual(output_path, wiki_ops_dir / "routing-note-intake.md")
        content = output_path.read_text(encoding="utf-8")
        self.assertIn("type: intake", content)
        self.assertIn("related_sources:", content)
        self.assertIn("../sources/routing-note.md", content)
        self.assertIn("## 输入摘要", content)

    def test_detects_meeting_note_from_name_and_content(self) -> None:
        source_file = self.inbox_dir / "nirvana-weekly-sync.txt"
        source_file.write_text(
            "项目周会纪要\n结论：本周先补 intake 路由，再整理管理周报。\n",
            encoding="utf-8",
        )

        output_path = generate_source_draft(source_file, self.wiki_sources_dir, self.inbox_dir)

        content = output_path.read_text(encoding="utf-8")
        self.assertIn("source_type: meeting-note", content)
        self.assertIn("Source class: meeting note", content)
        self.assertIn("Intake confidence: high", content)

    def test_process_inbox_recurses_and_uses_folder_as_domain_hint(self) -> None:
        nested_dir = self.inbox_dir / "nirvana"
        nested_dir.mkdir(parents=True)
        source_file = nested_dir / "meeting-note.md"
        source_file.write_text("会议纪要\n需要跟进排期偏差。", encoding="utf-8")
        wiki_ops_dir = self.tmpdir / "wiki" / "ops"
        wiki_ops_dir.mkdir(parents=True)

        output_paths = process_inbox(self.inbox_dir, self.wiki_sources_dir, wiki_ops_dir)

        self.assertEqual(
            [path.name for path in output_paths],
            ["nirvana-meeting-note.md", "nirvana-meeting-note-intake.md"],
        )
        source_content = (self.wiki_sources_dir / "nirvana-meeting-note.md").read_text(encoding="utf-8")
        intake_content = (wiki_ops_dir / "nirvana-meeting-note-intake.md").read_text(encoding="utf-8")
        self.assertIn("source_path: inbox/nirvana/meeting-note.md", source_content)
        self.assertIn("domain: nirvana", source_content)
        self.assertIn("source_type: meeting-note", source_content)
        self.assertIn("source_path: inbox/nirvana/meeting-note.md", intake_content)
        self.assertIn("domain: nirvana", intake_content)

    def test_process_inbox_reads_docx_content_and_classifies_meeting_note(self) -> None:
        source_file = self.inbox_dir / "project-sync.docx"
        self._write_docx(source_file, "项目周会纪要 需要跟进对齐和风险")

        output_paths = process_inbox(self.inbox_dir, self.wiki_sources_dir)

        self.assertEqual([path.name for path in output_paths], ["project-sync.md"])
        content = (self.wiki_sources_dir / "project-sync.md").read_text(encoding="utf-8")
        self.assertIn("source_type: meeting-note", content)
        self.assertIn("Intake confidence: high", content)

    def test_process_inbox_skips_existing_source_path(self) -> None:
        source_file = self.inbox_dir / "nirvana" / "meeting-note.md"
        source_file.parent.mkdir(parents=True)
        source_file.write_text("会议纪要\n已经整理过。", encoding="utf-8")
        (self.wiki_sources_dir / "existing.md").write_text(
            """---
title: Existing
source_path: inbox/nirvana/meeting-note.md
---
""",
            encoding="utf-8",
        )

        output_paths = process_inbox(self.inbox_dir, self.wiki_sources_dir)

        self.assertEqual(output_paths, [])

    def test_process_inbox_preserves_non_ascii_names_to_avoid_slug_collisions(self) -> None:
        file_a = self.inbox_dir / "转写-会议纪要.docx"
        file_b = self.inbox_dir / "转写-逐字稿.docx"
        self._write_docx(file_a, "会议纪要 结论整理")
        self._write_docx(file_b, "逐字稿 原始记录")

        output_paths = process_inbox(self.inbox_dir, self.wiki_sources_dir)

        self.assertEqual(
            [path.name for path in output_paths],
            ["转写-会议纪要.md", "转写-逐字稿.md"],
        )

    def test_process_inbox_links_new_intake_to_existing_source_file(self) -> None:
        source_file = self.inbox_dir / "nirvana" / "preview .html"
        source_file.parent.mkdir(parents=True)
        source_file.write_text("<html><body>周视图会议材料</body></html>", encoding="utf-8")
        (self.wiki_sources_dir / "nirvana-weekly-view-2026-04-13.md").write_text(
            """---
title: Existing View
source_path: inbox/nirvana/preview .html
---
""",
            encoding="utf-8",
        )
        wiki_ops_dir = self.tmpdir / "wiki" / "ops"
        wiki_ops_dir.mkdir(parents=True)

        output_paths = process_inbox(self.inbox_dir, self.wiki_sources_dir, wiki_ops_dir)

        self.assertEqual([path.name for path in output_paths], ["nirvana-preview-intake.md"])
        intake_content = (wiki_ops_dir / "nirvana-preview-intake.md").read_text(encoding="utf-8")
        self.assertIn("../sources/nirvana-weekly-view-2026-04-13.md", intake_content)


if __name__ == "__main__":
    unittest.main()
