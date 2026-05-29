# account-group-onboarding-h5 Spec Delta

## ADDED Requirements

### Requirement: Stable Training Section Titles

The H5 SHALL use stable onboarding section titles rather than process-oriented
or colloquial draft narration.

#### Scenario: section titles are reviewable

- **WHEN** a reviewer scans the H5 headings
- **THEN** the H5 includes `你加入的是什么小组`, `账户体系能力地图`,
  `核心业务链路`, `我们支撑的对象`, `正在做的项目`, `技术规划路线`,
  `AI 如何与我们协作`, and `AI Coding 成熟度：当前站在哪一层`
- **AND** it does not include `这版先看重绘图，再看说明`.

### Requirement: Technical Planning Fishbone Roadmap

The H5 SHALL present technical planning as a fishbone roadmap visual rather
than only as a card grid.

#### Scenario: roadmap has planning structure

- **WHEN** a reviewer reads the technical planning section
- **THEN** they can see the main planning spine and branches for account model,
  balance service, accounting standardization, settlement/reconciliation
  convergence, observability/risk, and technology/knowledge reuse.
