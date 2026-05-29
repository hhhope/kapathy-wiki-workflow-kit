# Proposal: Repair Account H5 Headings And Roadmap

## Why

The current account-group onboarding H5 still exposes process-oriented and
overly colloquial section titles. It also presents technical planning as a
card grid rather than a route-level plan, which fails the user's expectation
for a real technical-planning route diagram.

## What Changes

- Remove the process section titled `这版先看重绘图，再看说明`.
- Restore stable training-section titles:
  - `你加入的是什么小组`
  - `账户体系能力地图`
  - `核心业务链路`
  - `我们支撑的对象`
  - `正在做的项目`
  - `技术规划路线`
  - `AI 如何与我们协作`
  - `AI Coding 成熟度：当前站在哪一层`
- Rewrite the `你加入的是什么小组` copy to describe the account technical group
  in formal onboarding language.
- Rename `典型业务对象` to `我们支撑的对象`.
- Rename `正在做的项目入口` to `正在做的项目`.
- Replace `技术规划看什么` with a source-backed fishbone roadmap visual and
  route-oriented planning text.
- Update the gate review with this drift and repair evidence.

## Out of Scope

- Feishu sync or image insertion.
- Changing source evidence outside the account onboarding H5.
- Reopening completed OpenSpec changes.
- Introducing credentials, internal URLs, personal contacts, QR codes, or
  access instructions.

## Impact

- The existing H5 is edited in place.
- A new editable SVG and exported PNG for the technical roadmap fishbone are
  added under `wiki/reports/assets/account-group-onboarding-h5/`.
- The gate review records that earlier process-title and roadmap-shape choices
  were not acceptable.
