## ADDED Requirements

### Requirement: Direct-sales phase1 PM brief SHALL use management framing
The system SHALL provide a direct-sales phase1 PM brief that uses project-management framing instead of generic analysis framing. The brief MUST organize content around committed interface scope, minimum customer delivery path, current delivery coverage, key time nodes, current delivery constraints, resource asks, and decisions requiring management approval.

#### Scenario: Reader needs a management-ready briefing structure
- **WHEN** a user opens the direct-sales phase1 PM brief
- **THEN** the document SHALL present the direct-sales phase1 scope in management language
- **AND** the document SHALL avoid using generic `gap` framing as the primary structure

### Requirement: Direct-sales phase1 PM brief SHALL define the minimum customer delivery path
The system SHALL describe the minimum customer delivery path for direct-sales phase1 in a way that states what can currently be delivered, what can be partially supported, and what is not yet closed.

#### Scenario: Reader asks what phase1 can currently deliver to customers
- **WHEN** a user reviews the minimum customer delivery path section
- **THEN** the document SHALL show the ordered path from product enablement through payment, result feedback, refund baseline, and operating closure
- **AND** each step SHALL include what can be done now and what is still missing

### Requirement: Direct-sales phase1 PM brief SHALL map committed interfaces to current delivery state
The system SHALL include a committed-interface view that groups product-promised interfaces into management-relevant bundles and states the current delivery maturity of each bundle.

#### Scenario: Reader asks what was committed versus what is currently carried by engineering
- **WHEN** a user reviews the committed interface section
- **THEN** the document SHALL group interfaces into bundles such as payment mainline, result feedback, binding, refund baseline, BM operations, split-account coupling, and extensions
- **AND** each bundle SHALL show whether it is in committed scope, current state, and management meaning

### Requirement: Direct-sales phase1 PM brief SHALL include dated control points
The system SHALL show key milestone and feature dates using explicit calendar dates and SHALL identify where current status conflicts with the original plan or current reporting.

#### Scenario: Reader asks whether current progress still supports the committed milestone
- **WHEN** a user reviews the time-control section
- **THEN** the document SHALL show original committed dates and the current status as of the reporting date
- **AND** the document SHALL mark whether the item still supports the phase1 milestone

### Requirement: Direct-sales phase1 PM brief SHALL end in actions and asks
The system SHALL translate current constraints into concrete management actions, resource asks, and decision items instead of leaving them as passive observations.

#### Scenario: Reader asks what support is needed next
- **WHEN** a user reviews the final sections of the PM brief
- **THEN** the document SHALL list resource constraints, requested support, and decision items with explicit business impact

### Requirement: Direct-sales phase1 PM brief SHALL show distance from resale capability
The system SHALL include a management-facing comparison that explains how far direct-sales phase1 currently is from resale target capability by major domain.

#### Scenario: Reader asks how far direct-sales is from resale
- **WHEN** a user reviews the comparison section of the PM brief
- **THEN** the document SHALL show by domain the current direct-sales capability, the resale target capability, the current difference, customer-facing impact, and whether phase1 handles that difference
