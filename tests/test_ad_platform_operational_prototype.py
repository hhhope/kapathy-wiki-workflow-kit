import re
import unittest
from pathlib import Path


HTML = Path("wiki/reports/ad-platform-operational-prototype.html")
GATE_REVIEW = Path("wiki/ops/ad-platform-operational-prototype-report-gate-review.md")


class AdPlatformOperationalPrototypeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = HTML.read_text(encoding="utf-8")

    def test_shell_and_all_modules_exist(self) -> None:
        for label in [
            "总览",
            "投流方",
            "流量方",
            "平台运营",
            "广告核心",
            "规则引擎",
            "财务管理",
            "埋点与三方",
            "报表监控",
        ]:
            self.assertIn(label, self.html)

        for module_id in [
            "overview",
            "advertiser",
            "traffic",
            "platform",
            "core",
            "rules",
            "finance",
            "integration",
            "reports",
        ]:
            self.assertIn(f'data-module="{module_id}"', self.html)
            self.assertIn(f'id="module-{module_id}"', self.html)

        self.assertIn('id="roleSwitcher"', self.html)
        self.assertIn('id="stateRail"', self.html)
        self.assertIn('id="resetPrototype"', self.html)

    def test_requirement_mapping_is_operational_not_demo(self) -> None:
        required_phrases = [
            "日预算",
            "总预算",
            "时段预算",
            "成本控制",
            "量级优先",
            "ROI 最优",
            "广告位",
            "CPM",
            "CPC",
            "CPA",
            "CPS",
            "跨媒体复制",
            "自动调价",
            "预算分配",
            "创意轮播",
            "多维度归因",
            "LTV 回传",
            "无代码",
            "商户充值",
            "退款",
            "开票",
            "AppKey",
            "AppSecret",
            "SDK",
            "API",
            "实时监控",
            "自定义报表",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, self.html)

        forbidden_phrases = [
            "客户演示驾驶舱",
            "投放增长驾驶舱",
            "查看本周投放复盘",
            "营销落地页",
        ]
        for phrase in forbidden_phrases:
            self.assertNotIn(phrase, self.html)

    def test_state_contract_and_persistence_hooks_exist(self) -> None:
        for state_key in [
            "advertisers",
            "trafficSources",
            "mediaAccounts",
            "campaigns",
            "budgets",
            "strategies",
            "rules",
            "alerts",
            "financeLedger",
            "trackingEvents",
            "reports",
            "operationsLog",
        ]:
            self.assertIn(state_key, self.html)

        for function_name in [
            "seedState",
            "loadState",
            "saveState",
            "resetState",
            "setActiveModule",
            "switchRole",
            "updateLog",
            "render",
        ]:
            self.assertIn(f"function {function_name}", self.html)

        self.assertIn("localStorage", self.html)
        self.assertIn("ad-platform-operational-prototype-state", self.html)
        self.assertIn("window.AdPrototype", self.html)

    def test_operational_actions_are_wired(self) -> None:
        action_contracts = {
            "budgetForm": "submitBudget",
            "strategyForm": "submitStrategy",
            "trafficPlacementForm": "createTrafficPlacement",
            "handleFunnelAlert": "handleFunnelAlert",
            "copyCampaignAcrossMedia": "copyCampaignAcrossMedia",
            "runAutoBidSimulation": "runAutoBidSimulation",
            "redistributeBudget": "redistributeBudget",
            "sendLtvCallback": "sendLtvCallback",
            "testRule": "testRule",
            "publishRule": "publishRule",
            "rechargeForm": "rechargeMerchant",
            "refundForm": "submitRefund",
            "invoiceForm": "submitInvoice",
            "generateCredentials": "generateCredentials",
            "sendTestEvent": "sendTestEvent",
            "saveReportTemplate": "saveReportTemplate",
            "confirmMonitoringAlert": "confirmMonitoringAlert",
            "generateReviewReport": "generateReviewReport",
        }
        for element_id, function_name in action_contracts.items():
            self.assertIn(element_id, self.html)
            self.assertIn(f"function {function_name}", self.html)

    def test_architecture_and_sequence_surfaces_exist(self) -> None:
        for diagram in [
            "overall-architecture",
            "advertiser-architecture",
            "traffic-architecture",
            "platform-architecture",
            "core-architecture",
            "rules-architecture",
            "finance-architecture",
            "integration-architecture",
            "reports-architecture",
        ]:
            self.assertIn(f'data-diagram="{diagram}"', self.html)

        for sequence in [
            "budget-sequence",
            "traffic-placement-sequence",
            "revenue-evaluation-sequence",
            "funnel-alert-sequence",
            "cross-media-copy-sequence",
            "auto-bid-sequence",
            "rule-execution-sequence",
            "finance-sequence",
            "tracking-sequence",
            "realtime-report-sequence",
        ]:
            self.assertIn(f'data-sequence="{sequence}"', self.html)

    def test_gate_review_artifact_exists(self) -> None:
        content = GATE_REVIEW.read_text(encoding="utf-8")
        for phrase in [
            "Article Intent Contract",
            "operable advertising delivery system prototype",
            "not a customer demo",
            "No Feishu sync",
            "local prototype",
        ]:
            self.assertIn(phrase, content)


if __name__ == "__main__":
    unittest.main()
