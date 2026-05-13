import re
import unittest
from pathlib import Path


HTML = Path("wiki/reports/ad-growth-cockpit-h5.html")
GATE_REVIEW = Path("wiki/ops/ad-growth-cockpit-h5-report-gate-review.md")


class AdGrowthCockpitH5Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = HTML.read_text(encoding="utf-8")

    def test_required_customer_sections_exist(self) -> None:
        for section_id in [
            "hero",
            "money-flow",
            "optimization",
            "anomalies",
            "review",
        ]:
            self.assertIn(f'id="{section_id}"', self.html)

        for label in [
            "投放增长驾驶舱",
            "钱花在哪",
            "为什么效果变好",
            "异常怎么处理",
            "复盘与下一轮投放",
        ]:
            self.assertIn(label, self.html)

    def test_navigation_and_jump_targets_exist(self) -> None:
        for anchor in [
            "#hero",
            "#money-flow",
            "#optimization",
            "#anomalies",
            "#review",
        ]:
            self.assertIn(f'href="{anchor}"', self.html)

        self.assertIn("data-jump-target=\"optimization\"", self.html)
        self.assertIn("data-jump-target=\"anomalies\"", self.html)
        self.assertIn("data-jump-target=\"review\"", self.html)

    def test_channel_view_toggle_controls_exist(self) -> None:
        for view in ["channel", "plan", "creative"]:
            self.assertIn(f'data-view="{view}"', self.html)
            self.assertIn(f'id="{view}-view"', self.html)

        self.assertIn("function switchView", self.html)
        self.assertIn("classList.add(\"is-active\")", self.html)

    def test_alert_expansion_controls_exist(self) -> None:
        self.assertGreaterEqual(len(re.findall(r'data-alert-card=', self.html)), 4)
        self.assertIn("function toggleAlert", self.html)
        self.assertIn("漏斗断崖", self.html)
        self.assertIn("CPA 超标", self.html)
        self.assertIn("流量异常", self.html)
        self.assertIn("预算超限", self.html)

    def test_customer_facing_mapping_not_prd_dump(self) -> None:
        for phrase in [
            "巨量引擎",
            "腾讯广告",
            "Google Ads",
            "自动调价",
            "预算分配",
            "创意优选",
            "规则引擎",
            "归因",
            "LTV",
        ]:
            self.assertIn(phrase, self.html)

        self.assertNotIn("2.1.1", self.html)
        self.assertNotIn("详细设计PRD", self.html)

    def test_gate_review_artifact_exists(self) -> None:
        content = GATE_REVIEW.read_text(encoding="utf-8")

        self.assertIn("Article Intent Contract", content)
        self.assertIn("advertisers", content)
        self.assertIn("Growth Cockpit", content)
        self.assertIn("No Feishu sync", content)
        self.assertIn("prototype", content)


if __name__ == "__main__":
    unittest.main()
