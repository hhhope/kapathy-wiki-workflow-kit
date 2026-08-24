import json
import re
import unittest
from pathlib import Path

SOURCE_SUMMARY = Path("wiki/sources/baocaitong-2-3-plan-source-2026-08-24.md")
SOURCE_ASSETS = [
    Path("wiki/sources/assets/baocaitong-2-3/01-main-comparison.png"),
    Path("wiki/sources/assets/baocaitong-2-3/02-mode-options.png"),
]
CONTENT = Path("wiki/reports/assets/baocaitong-2-3-review-h5/content.json")
REPORT = Path("wiki/reports/baocaitong-2-3-review-h5.html")
STYLES = Path("wiki/reports/assets/baocaitong-2-3-review-h5/styles.css")
SCRIPT = Path("wiki/reports/assets/baocaitong-2-3-review-h5/app.js")
GATE_REVIEW = Path("wiki/ops/baocaitong-2-3-h5-report-gate-review-2026-08-24.md")


class BaocaitongSourceContractTest(unittest.TestCase):
    def test_source_assets_and_summary_are_persisted(self) -> None:
        for asset in SOURCE_ASSETS:
            self.assertTrue(asset.is_file(), asset)
            self.assertGreater(asset.stat().st_size, 10_000, asset)

        text = SOURCE_SUMMARY.read_text(encoding="utf-8")
        for heading in [
            "## 来源范围", "## 2.0 现状", "## 3.0 目标", "## 业务规则",
            "## 改造项", "## 风险与待确认",
        ]:
            self.assertIn(heading, text)
        self.assertRegex(text, r"F-\d{3}")
        for phrase in ["收单", "分账", "退款", "提现", "余额调账", "待原文确认"]:
            self.assertIn(phrase, text)


class BaocaitongBuildContractTest(unittest.TestCase):
    def test_content_model_has_required_shape(self) -> None:
        data = json.loads(CONTENT.read_text(encoding="utf-8"))
        self.assertEqual("baocaitong-2-3-review", data["report_id"])
        self.assertEqual(["2.0", "3.0"], list(data["versions"]))
        self.assertEqual(7, len(data["change_areas"]))
        self.assertEqual(7, len(data["business_rules"]))
        self.assertTrue(data["open_questions"])
        for fact in data["facts"]:
            self.assertRegex(fact["id"], r"^F-\d{3}$")
            self.assertIn(fact["confidence"], {"confirmed", "transcribed", "needs_confirmation"})

    def test_generated_report_contains_required_sections_and_copy(self) -> None:
        html = REPORT.read_text(encoding="utf-8")
        for section_id in [
            "hero", "core-changes", "flow-2", "flow-3", "difference-matrix",
            "change-areas", "business-rules", "open-questions", "review-decision",
        ]:
            self.assertIn(f'id="{section_id}"', html)
        for phrase in [
            "宝财通收单与分账方案演进", "内部评审稿", "宝财通 2.0",
            "宝财通 3.0", "收单", "分账", "退款", "提现", "待原文确认",
        ]:
            self.assertIn(phrase, html)


class BaocaitongVisualContractTest(unittest.TestCase):
    def test_styles_and_flow_semantics_are_wired(self) -> None:
        html = REPORT.read_text(encoding="utf-8")
        css = STYLES.read_text(encoding="utf-8")
        for token in ["--navy", "--blue-2", "--blue-3", "--success", "--warning"]:
            self.assertIn(token, css)
        for kind in ["fund", "relation", "upgrade", "withdrawal"]:
            self.assertIn(f'data-flow-kind="{kind}"', html)
        self.assertIn("@media (max-width: 760px)", css)
        self.assertIn("@media (prefers-reduced-motion: reduce)", css)

    def test_report_has_no_external_loading_dependency(self) -> None:
        combined = REPORT.read_text(encoding="utf-8") + STYLES.read_text(encoding="utf-8")
        self.assertNotRegex(combined, r"(?i)(src|href)=[\"']https?://")
        self.assertNotRegex(combined, r"(?i)url\([\"']?https?://")
        self.assertNotIn("file://", combined)


class BaocaitongInteractionContractTest(unittest.TestCase):
    def test_compare_and_owner_filter_controls_are_accessible(self) -> None:
        html = REPORT.read_text(encoding="utf-8")
        js = SCRIPT.read_text(encoding="utf-8")
        for mode in ["2", "3", "compare"]:
            self.assertIn(f'data-compare-mode="{mode}"', html)
        for owner in ["all", "product", "engineering", "qa-compliance"]:
            self.assertIn(f'data-owner-filter="{owner}"', html)
        for function_name in ["setCompareMode", "setOwnerFilter", "updateProgress", "activateSection"]:
            self.assertIn(f"function {function_name}", js)
        self.assertIn('setAttribute("aria-pressed"', js)
        self.assertIn("panel.hidden", js)

    def test_core_content_is_present_without_javascript(self) -> None:
        html = REPORT.read_text(encoding="utf-8")
        self.assertIn('data-version-panel="2"', html)
        self.assertIn('data-version-panel="3"', html)
        self.assertGreaterEqual(html.count("<details"), 7)
        self.assertNotIn("document.write", html)


class BaocaitongReviewGateTest(unittest.TestCase):
    def test_gate_review_records_required_boundaries(self) -> None:
        text = GATE_REVIEW.read_text(encoding="utf-8")
        for phrase in [
            "Article Intent Contract", "Source-to-Screen Map",
            "Section And Paragraph Drift Review", "Visual QA",
            "Judgment Ownership", "No Feishu sync", "Residual Risks",
        ]:
            self.assertIn(phrase, text)

    def test_every_fact_is_rendered_or_explained_as_not_rendered(self) -> None:
        data = json.loads(CONTENT.read_text(encoding="utf-8"))
        html = REPORT.read_text(encoding="utf-8")
        gate = GATE_REVIEW.read_text(encoding="utf-8")
        for fact in data["facts"]:
            self.assertTrue(fact["id"] in html or f'{fact["id"]}: not rendered' in gate, fact["id"])


if __name__ == "__main__":
    unittest.main()