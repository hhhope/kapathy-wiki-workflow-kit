# SVG 一图流模板参考

本文件包含生成标准 Apple 风格信息流+资金流 SVG 所需的所有代码片段。

---

## 目录

1. [完整 defs 块](#1-完整-defs-块)
2. [背景与标题结构](#2-背景与标题结构)
3. [节点卡片模板（4种角色）](#3-节点卡片模板)
4. [箭头类型模板](#4-箭头类型模板)
5. [标签 Pill 模板](#5-标签-pill-模板)
6. [图例模板](#6-图例模板)
7. [完整骨架（4节点版）](#7-完整骨架)

---

## 1. 完整 defs 块

每张 SVG 必须包含此 defs，不可删减：

```svg
<defs>
  <!-- 卡片阴影 -->
  <filter id="fs" x="-40%" y="-60%" width="180%" height="220%">
    <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#000" flood-opacity="0.07"/>
  </filter>
  <!-- 标签阴影 -->
  <filter id="fp" x="-40%" y="-80%" width="180%" height="360%">
    <feDropShadow dx="0" dy="2" stdDeviation="5" flood-color="#000" flood-opacity="0.06"/>
  </filter>

  <!-- 信息流箭头 markers（开口V形，非实心） -->
  <marker id="m-blue" markerWidth="13" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L11,5 L1,8.5" fill="none" stroke="#007AFF" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>
  <marker id="m-purple" markerWidth="13" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L11,5 L1,8.5" fill="none" stroke="#5856D6" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>
  <marker id="m-orange" markerWidth="13" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L11,5 L1,8.5" fill="none" stroke="#FF9500" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>
  <marker id="m-gray" markerWidth="13" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L11,5 L1,8.5" fill="none" stroke="#8E8E93" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>

  <!-- 资金流箭头 markers -->
  <marker id="m-green" markerWidth="13" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L11,5 L1,8.5" fill="none" stroke="#30D158" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>
  <marker id="m-orange2" markerWidth="13" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L11,5 L1,8.5" fill="none" stroke="#FF9500" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>
  <marker id="m-blue-sm" markerWidth="11" markerHeight="9" refX="9" refY="4.5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M1,1.5 L9,4.5 L1,7.5" fill="none" stroke="#007AFF" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>
  </marker>
</defs>
```

---

## 2. 背景与标题结构

```svg
<!-- 背景 -->
<rect width="900" height="1040" fill="#F2F2F7"/>

<!-- 分隔线（两图之间） -->
<line x1="60" y1="524" x2="840" y2="524" stroke="#D1D1D6" stroke-width="0.75" stroke-dasharray="6,4"/>

<!-- ── 信息流标题（上半） ── -->
<text x="450" y="46" text-anchor="middle"
      font-family="-apple-system,'PingFang SC','Noto Sans SC',sans-serif"
      font-size="22" font-weight="700" fill="#1C1C1E" letter-spacing="-0.3">信息流</text>
<text x="450" y="68" text-anchor="middle"
      font-family="-apple-system,'PingFang SC',sans-serif"
      font-size="13" fill="#8E8E93">[业务流程名称]</text>
<line x1="60" y1="84" x2="840" y2="84" stroke="#D1D1D6" stroke-width="0.75"/>

<!-- ── 资金流标题（下半） ── -->
<text x="450" y="566" text-anchor="middle"
      font-family="-apple-system,'PingFang SC','Noto Sans SC',sans-serif"
      font-size="22" font-weight="700" fill="#1C1C1E" letter-spacing="-0.3">资金流</text>
<text x="450" y="588" text-anchor="middle"
      font-family="-apple-system,'PingFang SC',sans-serif"
      font-size="13" fill="#8E8E93">[业务流程名称]</text>
<line x1="60" y1="604" x2="840" y2="604" stroke="#D1D1D6" stroke-width="0.75"/>
```

---

## 3. 节点卡片模板

### 客户节点（蓝色 #007AFF）
```svg
<g transform="translate(62, [Y])">
  <rect width="142" height="68" rx="18" fill="white" filter="url(#fs)"/>
  <circle cx="35" cy="34" r="21" fill="#007AFF"/>
  <text x="35" y="34" text-anchor="middle" dominant-baseline="central"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="16" font-weight="700" fill="white">客</text>
  <text x="100" y="28" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="15" font-weight="600" fill="#1C1C1E">客户</text>
  <text x="100" y="49" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="11" fill="#8E8E93">付款方</text>
</g>
<!-- 信息流 Y=206，资金流 Y=726 -->
```

### 支付机构节点（紫色 #5856D6）
```svg
<g transform="translate(376, [Y])">
  <rect width="148" height="68" rx="18" fill="white" filter="url(#fs)"/>
  <circle cx="35" cy="34" r="21" fill="#5856D6"/>
  <text x="35" y="34" text-anchor="middle" dominant-baseline="central"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="16" font-weight="700" fill="white">[图标字]</text>
  <text x="104" y="27" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="15" font-weight="600" fill="#1C1C1E">[机构名]</text>
  <text x="104" y="48" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="10.5" fill="#8E8E93">第三方支付机构</text>
</g>
<!-- 信息流 Y=206，资金流 Y=726 -->
```

### 银行节点（绿色 #34C759）
```svg
<g transform="translate(692, [Y])">
  <rect width="144" height="68" rx="18" fill="white" filter="url(#fs)"/>
  <circle cx="35" cy="34" r="21" fill="#34C759"/>
  <text x="35" y="34" text-anchor="middle" dominant-baseline="central"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="16" font-weight="700" fill="white">银</text>
  <text x="101" y="28" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="15" font-weight="600" fill="#1C1C1E">银行</text>
  <text x="101" y="49" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="11" fill="#8E8E93">[具体银行名]</text>
</g>
<!-- 信息流 Y=206，资金流 Y=726 -->
```

### 清算机构节点（橙色 #FF9500）—— 垂直方向
```svg
<g transform="translate(376, [Y])">
  <rect width="148" height="68" rx="18" fill="white" filter="url(#fs)"/>
  <circle cx="35" cy="34" r="21" fill="#FF9500"/>
  <text x="35" y="34" text-anchor="middle" dominant-baseline="central"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="16" font-weight="700" fill="white">联</text>
  <text x="104" y="28" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="15" font-weight="600" fill="#1C1C1E">[清算机构名]</text>
  <text x="104" y="49" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="11" fill="#8E8E93">清算组织</text>
</g>
<!-- 信息流 Y=406，资金流 Y=910 -->
```

---

## 4. 箭头类型模板

### 水平正向请求（实线）
```svg
<!-- 客户 → 支付机构：y = 节点中Y - 15 = 225 -->
<line x1="207" y1="225" x2="372" y2="225"
      stroke="#007AFF" stroke-width="2" marker-end="url(#m-blue)"/>
```

### 水平返回响应（虚线）
```svg
<!-- 支付机构 → 客户：y = 节点中Y + 15 = 255 -->
<line x1="372" y1="255" x2="207" y2="255"
      stroke="#8E8E93" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#m-gray)"/>
```

### 垂直向下（支付机构 → 清算机构）
```svg
<!-- 退款路径，左偏x=432 -->
<line x1="432" y1="278" x2="432" y2="400"
      stroke="#FF9500" stroke-width="2" marker-end="url(#m-orange)"/>
```

### 垂直向上（清算机构 → 支付机构，返回）
```svg
<!-- 右偏x=468，与下行错开 -->
<line x1="468" y1="400" x2="468" y2="278"
      stroke="#8E8E93" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#m-gray)"/>
```

### 斜向（清算机构 → 银行，退款清算）
```svg
<!-- 网联右边缘 → 银行底部中心 -->
<line x1="526" y1="[网联Y+54]" x2="760" y2="[银行Y+68]"
      stroke="#FF9500" stroke-width="2.5" marker-end="url(#m-orange2)"/>
```

### 资金流：代付资金（粗绿线）
```svg
<line x1="528" y1="738" x2="690" y2="738"
      stroke="#30D158" stroke-width="3" marker-end="url(#m-green)"/>
```

### 资金流：授权委托（细蓝虚线）
```svg
<line x1="207" y1="760" x2="372" y2="760"
      stroke="#007AFF" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#m-blue-sm)"/>
```

---

## 5. 标签 Pill 模板

正向请求 pill（白底）：
```svg
<rect x="[中点X-35]" y="[箭头Y-18]" width="70" height="19" rx="9.5" fill="white" filter="url(#fp)"/>
<text x="[中点X]" y="[箭头Y-5]" text-anchor="middle"
      font-family="-apple-system,'PingFang SC',sans-serif"
      font-size="11" font-weight="500" fill="[箭头颜色]">[标签文字]</text>
```

退款路径 pill（浅橙底）：
```svg
<rect x="[X]" y="[Y]" width="[W]" height="19" rx="9.5" fill="#FFF4E0" filter="url(#fp)"/>
<text ... fill="#FF9500">[退款路径标签]</text>
```

成功路径 pill（浅绿底，资金流用）：
```svg
<rect x="[X]" y="[Y]" width="72" height="19" rx="9.5" fill="#E8F9EE" filter="url(#fp)"/>
<text ... fill="#30D158">代付资金</text>
```

---

## 6. 图例模板

### 信息流图例
```svg
<g transform="translate(644, 398)">
  <rect width="218" height="100" rx="16" fill="white" filter="url(#fs)"/>
  <text x="109" y="22" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="12" font-weight="600" fill="#1C1C1E">图例</text>
  <!-- 正常信息流 -->
  <line x1="16" y1="41" x2="52" y2="41" stroke="#007AFF" stroke-width="2" marker-end="url(#m-blue)"/>
  <text x="60" y="45" font-family="-apple-system,'PingFang SC',sans-serif" font-size="11" fill="#3C3C43">请求 / 正常信息流</text>
  <!-- 退款路径 -->
  <line x1="16" y1="63" x2="52" y2="63" stroke="#FF9500" stroke-width="2" marker-end="url(#m-orange)"/>
  <text x="60" y="67" font-family="-apple-system,'PingFang SC',sans-serif" font-size="11" fill="#3C3C43">退款路径（失败时触发）</text>
  <!-- 响应虚线 -->
  <line x1="16" y1="85" x2="52" y2="85" stroke="#8E8E93" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#m-gray)"/>
  <text x="60" y="89" font-family="-apple-system,'PingFang SC',sans-serif" font-size="11" fill="#3C3C43">返回 / 响应</text>
</g>
```

### 资金流图例
```svg
<g transform="translate(62, [下半图例Y])">
  <rect width="256" height="82" rx="16" fill="white" filter="url(#fs)"/>
  <text x="128" y="22" text-anchor="middle"
        font-family="-apple-system,'PingFang SC',sans-serif"
        font-size="12" font-weight="600" fill="#1C1C1E">图例</text>
  <!-- 代付资金 -->
  <line x1="16" y1="41" x2="54" y2="41" stroke="#30D158" stroke-width="3" marker-end="url(#m-green)"/>
  <text x="64" y="45" font-family="-apple-system,'PingFang SC',sans-serif" font-size="11" fill="#3C3C43">代付资金流向（成功路径）</text>
  <!-- 退款资金 -->
  <line x1="16" y1="63" x2="54" y2="63" stroke="#FF9500" stroke-width="2.5" marker-end="url(#m-orange2)"/>
  <text x="64" y="67" font-family="-apple-system,'PingFang SC',sans-serif" font-size="11" fill="#3C3C43">退款资金流向（失败路径）</text>
</g>
```

---

## 7. 完整骨架（4节点标准版）

```svg
<svg width="900" height="1040" viewBox="0 0 900 1040" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- [粘贴第1节完整defs] -->
  </defs>

  <!-- 背景 + 分隔线 -->
  <!-- [粘贴第2节] -->

  <!-- ═══════════ 信息流（上半）═══════════ -->
  <!-- 箭头（先画，在节点下方） -->
  <!-- 水平箭头：客户↔支付机构（Y=225/255），支付机构↔银行（Y=225/255） -->
  <!-- 垂直箭头：支付机构↕清算机构（X=432/468） -->

  <!-- 箭头标签 pills -->

  <!-- 节点（后画，压在箭头上方） -->
  <!-- 客户 Y=206，支付机构 Y=206，银行 Y=206，清算机构 Y=406 -->

  <!-- 图例（右下角，Y=398） -->

  <!-- ═══════════ 资金流（下半）Y偏移+520 ═══════════ -->
  <!-- 路径标识 chips -->
  <!-- 箭头 -->
  <!-- 箭头标签 pills -->
  <!-- 节点（Y各+520） -->
  <!-- 图例（左下角） -->
</svg>
```

---

## 坐标速查表

| 元素 | 信息流 Y | 资金流 Y |
|------|---------|---------|
| 上行节点（客/支付/银行）| 206 | 726 |
| 下方节点（清算机构）| 406 | 910 |
| 水平正向箭头 Y | 225 | 745 |
| 水平返回箭头 Y | 255 | 760 |
| 竖向下行 X | 432 | 432 |
| 竖向上行 X | 468 | 468 |
| 图例（右） X | 644 | 644 |
| 图例（左） X | 62 | 62 |

| 节点 | X 起点 | 中心 X | 右边缘 X |
|------|--------|--------|---------|
| 客户（142宽）| 62 | 133 | 204 |
| 支付机构（148宽）| 376 | 450 | 524 |
| 银行（144宽）| 692 | 764 | 836 |
| 清算机构（148宽）| 376 | 450 | 524 |