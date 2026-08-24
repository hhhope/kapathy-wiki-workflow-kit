from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTENT_PATH = ROOT / "wiki/reports/assets/baocaitong-2-3-review-h5/content.json"
OUTPUT_PATH = ROOT / "wiki/reports/baocaitong-2-3-review-h5.html"

NAV = [
    ("hero", "评审目标"), ("core-changes", "核心变化"), ("flow-2", "2.0 现状"),
    ("flow-3", "3.0 目标"), ("difference-matrix", "差异矩阵"),
    ("change-areas", "七项改造"), ("business-rules", "业务规则"),
    ("open-questions", "风险与待确认"), ("review-decision", "评审结论"),
]


def load_content(path: Path = CONTENT_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def fact_badge(fact_id: str, pending: bool = False) -> str:
    klass = "fact pending" if pending else "fact"
    return f'<span class="{klass}">{esc(fact_id)}</span>'


def render_navigation(title: str) -> str:
    links = "".join(
        f'<a href="#{section_id}"><b>{index:02d}</b><span>{esc(label)}</span></a>'
        for index, (section_id, label) in enumerate(NAV, 1)
    )
    return f'''<aside class="rail" aria-label="章节导航"><div class="rail-brand">
<strong>{esc(title)}</strong><span>产品 × 研发联合评审</span></div><nav class="nav">{links}</nav></aside>'''


def render_hero(data: dict[str, Any]) -> str:
    return f'''<section id="hero" class="section hero"><div class="inner hero-grid"><div>
<p class="eyebrow">BAOCAITONG · REVIEW 2026</p><h1>{esc(data["title"])}</h1>
<p class="hero-copy">{esc(data["summary"])}</p><div class="hero-meta">
<span class="pill">{esc(data["status"])}</span><span class="pill">产品 × 研发</span>
<span class="pill">离线可审阅</span><span class="pill">事实可追溯</span></div></div>
<div class="evolution" aria-label="方案演进"><div class="evolution-row">
<div class="evo-card"><b>2.0</b><span>收单商户号</span><small>二级户升级与分账</small></div>
<div class="evo-arrow" aria-hidden="true">→</div>
<div class="evo-card v3"><b>3.0</b><span>代付商户号</span><small>批量开通、模式切换、调账</small></div>
</div><small>阅读顺序：现状 → 目标 → 差异 → 改造 → 风险 → 决策</small></div>
</div></section>'''


def section_head(kicker: str, title: str, copy: str) -> str:
    return f'''<div class="section-head"><div><p class="section-kicker">{esc(kicker)}</p>
<h2>{esc(title)}</h2></div><p class="section-copy">{esc(copy)}</p></div>'''


def render_core_changes(data: dict[str, Any]) -> str:
    cards = "".join(
        f'''<article class="summary-card" data-index="{esc(item["index"])}" data-fact="{esc(item["fact"])}">
{fact_badge(item["fact"])}<h3>{esc(item["title"])}</h3><p>{esc(item["summary"])}</p></article>'''
        for item in data["core_changes"]
    )
    return f'''<section id="core-changes" class="section"><div class="inner">
{section_head("01 · CORE CHANGES", "一分钟看懂核心变化", "先建立共同判断，再进入接口与规则细节；收益不预设，事实与待确认项分开呈现。")}
<div class="cards">{cards}</div></div></section>'''


def render_flow_panel(version: str, info: dict[str, Any]) -> str:
    nodes = {node["id"]: node for node in info["nodes"]}
    first = info["nodes"][:2]
    targets = info["nodes"][2:]

    def node_button(node: dict[str, str]) -> str:
        return f'''<button class="flow-node" type="button" data-node-button aria-expanded="false" data-fact="{esc(node["fact"])}">
<strong>{esc(node["label"])}</strong><span>{esc(node["role"])}</span>
<span class="node-detail" hidden>{esc(node["detail"])}</span></button>'''

    edges = "".join(
        f'''<div class="edge" data-flow-kind="{esc(edge["kind"])}" data-fact="{esc(edge["fact"])}">
<b>{esc(edge["label"])}</b><span>{esc(edge["from"])} → {esc(edge["to"])}</span>{fact_badge(edge["fact"])}</div>'''
        for edge in info["edges"]
    )
    cls = "version-2" if version == "2.0" else "version-3"
    panel_value = version.split(".")[0]
    return f'''<article class="flow-panel {cls}" data-version-panel="{panel_value}">
<div class="flow-title"><div><h3>宝财通 {esc(version)}</h3><p>{esc(info["tagline"])}</p></div>{fact_badge("F-001" if version == "2.0" else "F-002")}</div>
<div class="hub">{esc(info["hub"])}</div><div class="flow-bridge"><span>下挂账户</span></div>
<div class="flow-step">{''.join(node_button(node) for node in first)}</div>
<div class="flow-bridge"><span>升级</span></div><div class="flow-step">{''.join(node_button(node) for node in targets)}</div>
<div class="money-strip"><span>未结算资金</span><i></i><span>收单商户 A</span><i></i><span>分账接收方 B</span></div>
<div class="card-row"><div class="bank-card">二级户 b → {esc(info["cards"][0])}</div><div class="bank-card">分账接收方 B → {esc(info["cards"][1])}</div></div>
<div class="edge-list">{edges}</div></article>'''


def render_flows(data: dict[str, Any]) -> str:
    controls = '''<div class="controls" role="group" aria-label="版本显示方式">
<button class="control" type="button" data-compare-mode="2" aria-pressed="false">只看 2.0</button>
<button class="control" type="button" data-compare-mode="3" aria-pressed="false">只看 3.0</button>
<button class="control" type="button" data-compare-mode="compare" aria-pressed="true">并排对照</button></div>'''
    v2 = render_flow_panel("2.0", data["versions"]["2.0"])
    v3 = render_flow_panel("3.0", data["versions"]["3.0"])
    return f'''<section id="flow-2" class="section"><div class="inner">
{section_head("02 · CURRENT STATE", "现状：宝财通 2.0", "先看账户主体、升级关系，再看收单、分账与提现出口。点击节点可展开解释。")}
{controls}<div class="compare-grid">{v2}{v3}</div></div></section>
<section id="flow-3" class="section"><div class="inner">
{section_head("03 · TARGET STATE", "目标：宝财通 3.0", "3.0 是本次评审的推荐方向；推荐不等于业务收益已经验证，待确认边界仍需在后文决策。")}
<div class="evolution"><div class="evolution-row"><div class="evo-card"><b>2.0</b><span>单点升级</span></div><div class="evo-arrow">→</div><div class="evo-card v3"><b>3.0</b><span>批量开通 · 状态留痕 · 模式切换</span></div></div>
<small>备选的“保留电子户 + 平台”模式仅作为历史/过渡背景，不默认为最终路径。 {fact_badge("F-023")}</small></div>
</div></section>'''


def render_difference(data: dict[str, Any]) -> str:
    rows = "".join(
        f'''<tr data-fact="{esc(row["fact"])}"><td><strong>{esc(row["dimension"])}</strong></td>
<td>{esc(row["v2"])}</td><td>{esc(row["v3"])}</td><td>{esc(row["impact"])}</td>
<td class="status">{esc(row["status"])}</td><td>{fact_badge(row["fact"], row["status"] == "待确认")}</td></tr>'''
        for row in data["difference_rows"]
    )
    return f'''<section id="difference-matrix" class="section"><div class="inner">
{section_head("04 · DIFFERENCE MATRIX", "2.0 / 3.0 差异矩阵", "每一行同时回答：方案差在哪里、研发受什么影响、当前结论是否足够明确。")}
<div class="table-wrap"><table class="matrix"><thead><tr><th>维度</th><th>2.0</th><th>3.0</th><th>研发影响</th><th>状态</th><th>来源</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>'''


def render_change_areas(data: dict[str, Any]) -> str:
    blocks = "".join(
        f'''<details data-fact="{esc(item["fact"])}"><summary><span class="num">{esc(item["number"])}</span>
<span>{esc(item["title"])}</span>{fact_badge(item["fact"])}</summary><div class="detail-body"><p>{esc(item["summary"])}</p>
<ul>{''.join(f'<li>{esc(entry)}</li>' for entry in item["items"])}</ul></div></details>'''
        for item in data["change_areas"]
    )
    return f'''<section id="change-areas" class="section"><div class="inner">
{section_head("05 · CHANGE SCOPE", "七个业务环节的改造", "评审时先确认范围，再下钻字段和接口；所有小字号字段仍以权威文档复核。")}
<div class="accordion-grid">{blocks}</div></div></section>'''


def render_rules(data: dict[str, Any]) -> str:
    blocks = "".join(
        f'''<details data-fact="{esc(item["fact"])}"><summary><span class="num">{index:02d}</span><span>{esc(item["title"])}</span>{fact_badge(item["fact"])}</summary>
<div class="detail-body"><p><strong>{esc(item["conclusion"])}</strong></p><ul>{''.join(f'<li>{esc(entry)}</li>' for entry in item["conditions"])}</ul></div></details>'''
        for index, item in enumerate(data["business_rules"], 1)
    )
    return f'''<section id="business-rules" class="section"><div class="inner">
{section_head("06 · BUSINESS RULES", "关键规则与异常路径", "默认只看结论；展开后核对触发条件、主体边界与兼容路径。")}
<div class="rule-grid">{blocks}</div></div></section>'''


def render_questions(data: dict[str, Any]) -> str:
    cards = "".join(
        f'''<article class="question" data-question-owner="{esc(item["owner"])}" data-fact="{esc(item["fact"])}">
<span class="owner">{esc(item["owner_label"])}</span><h3>{esc(item["id"])} · {esc(item["title"])}</h3>
<p>{esc(item["detail"])}</p>{fact_badge(item["fact"], True)}</article>'''
        for item in data["open_questions"]
    )
    controls = '''<div class="controls" role="group" aria-label="按负责人筛选待确认项">
<button class="control" type="button" data-owner-filter="all" aria-pressed="true">全部</button>
<button class="control" type="button" data-owner-filter="product" aria-pressed="false">产品</button>
<button class="control" type="button" data-owner-filter="engineering" aria-pressed="false">研发</button>
<button class="control" type="button" data-owner-filter="qa-compliance" aria-pressed="false">测试 / 合规</button></div>'''
    return f'''<section id="open-questions" class="section"><div class="inner">
{section_head("07 · OPEN QUESTIONS", "风险、依赖与待确认事项", "这些问题不阻塞内部评审稿，但会阻塞最终业务结论。评审需要为每项指定负责人和权威依据。")}
{controls}<div class="question-grid">{cards}</div></div></section>'''


def render_decision(data: dict[str, Any]) -> str:
    facts = "".join(
        fact_badge(item["id"], item["confidence"] == "needs_confirmation")
        for item in data["facts"]
    )
    return f'''<section id="review-decision" class="section"><div class="inner">
{section_head("08 · REVIEW DECISION", "把评审结果落到可执行动作", "H5 不替评审会做业务判断；会中只需要把结论、负责人、时间和证据补齐。")}
<div class="decision"><article class="decision-card"><b>已确认项</b><span>会中填写：范围、规则与接口结论</span></article>
<article class="decision-card"><b>待确认项</b><span>会中填写：问题编号和权威依据</span></article>
<article class="decision-card"><b>负责人</b><span>产品 / 研发 / 测试 / 合规</span></article>
<article class="decision-card"><b>下一步</b><span>动作、目标时间、回查方式</span></article></div>
<div class="ledger" aria-label="来源事实台账">{facts}</div></div></section>'''


def render_report(data: dict[str, Any]) -> str:
    sections = "".join([
        render_hero(data), render_core_changes(data), render_flows(data),
        render_difference(data), render_change_areas(data), render_rules(data),
        render_questions(data), render_decision(data),
    ])
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light">
<title>{esc(data["title"])}</title><link rel="stylesheet" href="assets/baocaitong-2-3-review-h5/styles.css"></head>
<body><div class="progress" aria-hidden="true"></div><div class="draft">{esc(data["status"])}</div>
<div class="shell">{render_navigation(data["title"])}<main class="main">{sections}
<footer class="footer"><div class="inner"><strong>{esc(data["title"])}</strong><span>No Feishu sync · 本地评审材料</span></div></footer>
</main></div><script src="assets/baocaitong-2-3-review-h5/app.js"></script></body></html>'''


def main() -> int:
    OUTPUT_PATH.write_text(render_report(load_content()), encoding="utf-8")
    print(f"built: {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())