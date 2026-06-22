#!/usr/bin/env bash
set -euo pipefail

svg="codex-integration-kit/docs/assets/account-harness-system-map.svg"
share="codex-integration-kit/docs/feishu-codex-governance-share.md"

required_svg=(
  "1. 你掌握方向盘"
  "2. 控制层"
  "AI 必须先过这些门禁"
  "3. 知识与规划层"
  "让 AI 先知道在做什么"
  "skills/ + agents/"
  "OpenSpec"
  "proposal / design / tasks"
  "Lore"
  "wiki / logs / weekly review"
  "默认读取：index -&gt; overview -&gt; domain / pitfall / principle"
  "Graphify"
  "graphify-out / report / query"
  "行为资产"
  "AGENTS / rules / skills / agents"
  "OpenSpec 资产"
  "Lore 资产"
  "分享与发布"
)

forbidden=(
  "高密度版本"
  "恢复成"
  "不再试图"
  "不是继续堆工具"
)

for item in "${required_svg[@]}"; do
  rg -Fq "$item" "$svg" || { echo "missing required svg text: $item" >&2; exit 1; }
done

for item in "${forbidden[@]}"; do
  if rg -Fq "$item" "$svg" "$share"; then
    echo "forbidden wording still present: $item" >&2
    exit 1
  fi
done

if rg -Fq 'class="small"' "$svg"; then
  echo 'unexpected small-font text remains in svg' >&2
  exit 1
fi

echo "PASS: account harness map wording and typography checks"
