# Ad Growth Cockpit H5 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone customer-facing H5 prototype demo for an advertising growth cockpit based on `inbox/ad-desgin.md`.

**Architecture:** The implementation is a static HTML prototype at `wiki/reports/ad-growth-cockpit-h5.html`, backed by a focused unittest that checks required sections, anchors, interaction hooks, and customer-facing content mapping. A repo-visible gate review artifact records the public report quality boundary without claiming Feishu sync or production readiness.

**Tech Stack:** Static HTML/CSS/JavaScript, inline SVG/CSS charts, Python `unittest`, no backend, no external dependencies.

---

## File Structure

- Create `wiki/reports/ad-growth-cockpit-h5.html`: standalone H5 prototype with five customer-facing sections, mock dashboard data, and real click interactions.
- Create `tests/test_ad_growth_cockpit_h5.py`: static checks for anchors, controls, content mapping, and JavaScript hooks.
- Create `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md`: public report quality gate evidence for this prototype.

## Public Gate Boundary

This is reader-facing H5 output, so the implementation must preserve the public report quality gate:

- Audience: advertisers and customer-side decision makers.
- User-owned judgment: the selected direction is Growth Cockpit.
- Agent-allowed work: compress source PRD into a customer-facing prototype with mock data and demo interactions.
- Non-goal: no Feishu sync, no production claim, no real media API or backend.
- Verification: test coverage, static checks, and browser/manual visual review.

---

### Task 1: H5 Contract Test

**Files:**
- Create: `tests/test_ad_growth_cockpit_h5.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_ad_growth_cockpit_h5.py`:

```python
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
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```bash
python3 -m unittest tests.test_ad_growth_cockpit_h5 -v
```

Expected: fail because `wiki/reports/ad-growth-cockpit-h5.html` and the gate review artifact do not exist yet.

- [ ] **Step 3: Commit the RED test**

Run:

```bash
git add tests/test_ad_growth_cockpit_h5.py
git commit -m "test: cover ad growth cockpit h5"
```

---

### Task 2: Static H5 Prototype

**Files:**
- Create: `wiki/reports/ad-growth-cockpit-h5.html`

- [ ] **Step 1: Create the standalone HTML**

Create `wiki/reports/ad-growth-cockpit-h5.html` as a full HTML document with:

- `<!DOCTYPE html>`
- `<html lang="zh-CN">`
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- embedded `<style>`
- embedded `<script>`

Required section IDs:

```html
<section id="hero" class="hero-section">...</section>
<section id="money-flow" class="section">...</section>
<section id="optimization" class="section">...</section>
<section id="anomalies" class="section">...</section>
<section id="review" class="section">...</section>
```

Required navigation:

```html
<nav class="top-nav" aria-label="H5 sections">
  <a href="#hero">驾驶舱</a>
  <a href="#money-flow">钱花在哪</a>
  <a href="#optimization">效果优化</a>
  <a href="#anomalies">异常处理</a>
  <a href="#review">复盘</a>
</nav>
```

Required hero KPI cards:

```html
<button class="kpi-card" data-jump-target="money-flow">
  <span>今日消耗</span>
  <strong>¥128,420</strong>
  <em>预算利用率 73%</em>
</button>
<button class="kpi-card" data-jump-target="review">
  <span>转化数</span>
  <strong>6,842</strong>
  <em>较昨日 +18%</em>
</button>
<button class="kpi-card" data-jump-target="optimization">
  <span>ROAS</span>
  <strong>3.8</strong>
  <em>优于目标 26%</em>
</button>
<button class="kpi-card" data-jump-target="anomalies">
  <span>CPA</span>
  <strong>18.6</strong>
  <em>自动降价中</em>
</button>
```

Required money-flow view controls:

```html
<div class="view-tabs" role="tablist" aria-label="Spend views">
  <button class="view-tab is-active" data-view="channel" type="button">渠道</button>
  <button class="view-tab" data-view="plan" type="button">计划</button>
  <button class="view-tab" data-view="creative" type="button">素材</button>
</div>
<div id="channel-view" class="view-panel is-active">...</div>
<div id="plan-view" class="view-panel">...</div>
<div id="creative-view" class="view-panel">...</div>
```

Required alert cards:

```html
<article class="alert-card" data-alert-card>
  <button type="button" onclick="toggleAlert(this)">漏斗断崖</button>
  <div class="alert-detail">建议动作：暂停低转化计划，切换备用素材，通知优化师确认落地页。</div>
</article>
```

Include four cards: `漏斗断崖`, `CPA 超标`, `流量异常`, `预算超限`.

Required JavaScript:

```html
<script>
  function scrollToSection(id) {
    const target = document.getElementById(id);
    if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  document.querySelectorAll("[data-jump-target]").forEach((button) => {
    button.addEventListener("click", () => scrollToSection(button.dataset.jumpTarget));
  });

  function switchView(view) {
    document.querySelectorAll(".view-tab").forEach((tab) => {
      tab.classList.toggle("is-active", tab.dataset.view === view);
    });
    document.querySelectorAll(".view-panel").forEach((panel) => {
      panel.classList.toggle("is-active", panel.id === `${view}-view`);
    });
  }

  document.querySelectorAll("[data-view]").forEach((button) => {
    button.addEventListener("click", () => switchView(button.dataset.view));
  });

  function toggleAlert(button) {
    const card = button.closest("[data-alert-card]");
    if (card) card.classList.toggle("is-open");
  }
</script>
```

Design constraints:

- Use a deep neutral background, but avoid a single-hue blue/purple look.
- Use cyan for live data, green for healthy performance, amber for warnings, and violet only as a supporting accent.
- Keep cards at `border-radius: 8px` or less unless the chart shape requires a circle.
- Make desktop and mobile responsive with CSS grid and media queries.
- Do not include internal production notes, prompts, or tool instructions in the H5.

- [ ] **Step 2: Run the H5 test**

Run:

```bash
python3 -m unittest tests.test_ad_growth_cockpit_h5 -v
```

Expected: fail only because the gate review artifact does not exist yet.

- [ ] **Step 3: Commit the H5 prototype**

Run:

```bash
git add wiki/reports/ad-growth-cockpit-h5.html
git commit -m "feat: add ad growth cockpit h5 prototype"
```

---

### Task 3: Public Gate Review Artifact

**Files:**
- Create: `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md`

- [ ] **Step 1: Create the gate review artifact**

Create `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md`:

```markdown
---
layer: ops
domain: none
ops_area: public-output-gate
canonical_object: ad-growth-cockpit-h5
artifact_type: report-gate-review
---

# Ad Growth Cockpit H5 Report Gate Review

## Article Intent Contract

| Field | Decision |
|---|---|
| Reader | advertisers and customer-side decision makers |
| Reader job | Understand how the advertising platform helps control spend, see performance, react to anomalies, and improve future campaigns |
| Main line | Growth Cockpit: one real-time cockpit for delivery, monitoring, optimization, anomaly handling, and review |
| Non-goals | No Feishu sync, no production claim, no login, no backend, no real media API calls |
| User-owned judgments | Audience C and Growth Cockpit direction |
| Agent-allowed work | Compress `inbox/ad-desgin.md` into a customer-facing H5 prototype with mock data and demo interactions |

## Reference Output Shape Gate

Selected output shape: polished operational SaaS H5 dashboard.

Rejected output shapes:

- module-by-module PRD dump
- pure architecture diagram
- backend implementation document

## Visual Gate

The H5 uses dashboard cards, spend distribution views, optimization action
panels, anomaly cards, and review loop panels. Each visual carries spend,
performance, optimization, or risk-handling meaning.

## Judgment Ownership Gate

The prototype does not claim real performance lift or production readiness.
Mock metrics are labeled by context as demo cockpit data.

## Hard Gate Results

| Gate | Result | Evidence |
|---|---|---|
| Article Intent Contract | PASS | This artifact |
| Reference Output Shape | PASS | `wiki/reports/ad-growth-cockpit-h5.html` |
| Visual Gate | PASS | Dashboard, channel, optimization, alert, and review sections |
| Publish Gate | NOT REQUESTED | Local prototype only |
| Feishu Sync | NOT REQUESTED | No Feishu write |

## Verification Plan

- `python3 -m unittest tests.test_ad_growth_cockpit_h5 -v`
- Browser open: `wiki/reports/ad-growth-cockpit-h5.html`
- Check section navigation, KPI jump, view toggles, alert expansion, and review CTA.
```

- [ ] **Step 2: Run H5 test**

Run:

```bash
python3 -m unittest tests.test_ad_growth_cockpit_h5 -v
```

Expected: pass.

- [ ] **Step 3: Run taxonomy checker**

Run:

```bash
python3 scripts/check_wiki_frontmatter.py
```

Expected: may exit non-zero because legacy wiki drift exists, but the new gate review page must not appear as a new taxonomy error.

- [ ] **Step 4: Commit gate review**

Run:

```bash
git add wiki/ops/ad-growth-cockpit-h5-report-gate-review.md
git commit -m "docs: gate review ad growth cockpit h5"
```

---

### Task 4: Final Verification

**Files:**
- Verify: `wiki/reports/ad-growth-cockpit-h5.html`
- Verify: `tests/test_ad_growth_cockpit_h5.py`
- Verify: `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md`

- [ ] **Step 1: Run targeted tests**

Run:

```bash
python3 -m unittest tests.test_ad_growth_cockpit_h5 tests.test_public_report_quality_gate -v
```

Expected: all tests pass.

- [ ] **Step 2: Run behavior and diff checks**

Run:

```bash
python3 scripts/check_behavior_assets.py
git diff --check
```

Expected: behavior checker passes with no error output; diff check has no whitespace errors.

- [ ] **Step 3: Manually open the HTML**

Open this file in a browser:

```text
wiki/reports/ad-growth-cockpit-h5.html
```

Check:

- Top navigation jumps to five sections.
- KPI cards jump to related sections.
- 渠道/计划/素材 tabs switch visible content.
- Four alert cards expand/collapse.
- “查看本周投放复盘” jumps to review.
- Mobile width remains readable and no text overlaps.

- [ ] **Step 4: Commit any verification-only updates**

If manual verification requires text or layout fixes, commit them:

```bash
git add wiki/reports/ad-growth-cockpit-h5.html tests/test_ad_growth_cockpit_h5.py wiki/ops/ad-growth-cockpit-h5-report-gate-review.md
git commit -m "fix: verify ad growth cockpit h5 interactions"
```

If no fixes are needed, do not create an empty commit.

## Final Expected State

- `wiki/reports/ad-growth-cockpit-h5.html` is a standalone customer-facing H5 prototype.
- `tests/test_ad_growth_cockpit_h5.py` passes.
- `wiki/ops/ad-growth-cockpit-h5-report-gate-review.md` records the public gate boundary.
- No Feishu sync or publish-ready claim is made.
