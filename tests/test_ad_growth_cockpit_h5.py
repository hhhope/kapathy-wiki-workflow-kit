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

        for target in ["money-flow", "optimization", "anomalies", "review"]:
            self.assertIn(f'data-jump-target="{target}"', self.html)

    def test_channel_view_toggle_controls_exist(self) -> None:
        for view in ["channel", "plan", "creative"]:
            self.assertIn(f'data-view="{view}"', self.html)
            self.assertIn(f'id="{view}-view"', self.html)

        self.assertIn("function switchView", self.html)
        self.assertIn("querySelectorAll(\"[data-view]\")", self.html)
        self.assertIn("querySelectorAll(\"[data-view-panel]\")", self.html)
        self.assertIn("data-view-panel=\"channel\"", self.html)
        self.assertIn("data-view-panel=\"plan\"", self.html)
        self.assertIn("data-view-panel=\"creative\"", self.html)
        for view, selected in [
            ("channel", "true"),
            ("plan", "false"),
            ("creative", "false"),
        ]:
            self.assertRegex(
                self.html,
                rf'<button id="{view}-tab"[^>]*data-view="{view}"[^>]*'
                rf'role="tab"[^>]*aria-selected="{selected}"[^>]*'
                rf'aria-controls="{view}-view"',
            )
            self.assertRegex(
                self.html,
                rf'<div id="{view}-view"[^>]*data-view-panel="{view}"[^>]*'
                rf'role="tabpanel"[^>]*aria-labelledby="{view}-tab"',
            )
        self.assertIn("tab.setAttribute(\"aria-selected\"", self.html)
        self.assertIn("panel.hidden =", self.html)
        self.assertIn("classList.add(\"is-active\")", self.html)

    def test_alert_expansion_controls_exist(self) -> None:
        self.assertGreaterEqual(len(re.findall(r'data-alert-card=', self.html)), 4)
        for alert_id, label in [
            ("alert-funnel-detail", "漏斗断崖"),
            ("alert-cpa-detail", "CPA 超标"),
            ("alert-traffic-detail", "流量异常"),
            ("alert-budget-detail", "预算超限"),
        ]:
            self.assertRegex(
                self.html,
                rf'<button[^>]*aria-expanded="false"[^>]*'
                rf'aria-controls="{alert_id}"[^>]*>[\s\S]*?'
                rf'<strong>{re.escape(label)}</strong>',
            )
            self.assertRegex(
                self.html,
                rf'<div id="{alert_id}" class="alert-detail" hidden>'
                rf'[\s\S]*?建议动作：[\s\S]*?自动化状态：[\s\S]*?</div>',
            )
        self.assertIn("querySelectorAll(\"[data-alert-card]\")", self.html)
        self.assertIn("querySelector(\".alert-detail\")", self.html)
        self.assertIn("button.setAttribute(\"aria-expanded\"", self.html)
        self.assertIn("button.setAttribute(\"aria-expanded\", \"false\")", self.html)
        self.assertIn("event.key === \"Escape\"", self.html)
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
