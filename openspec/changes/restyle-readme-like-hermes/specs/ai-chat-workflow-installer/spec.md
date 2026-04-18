## MODIFIED Requirements

### Requirement: Repository SHALL provide a shareable explainer for the installer model

The repository SHALL provide a shareable explanation artifact for the installer model so that the installation logic, platform mapping, and scope boundaries can be communicated outside the repository chat history.

#### Scenario: Reader starts from the repository root

- **WHEN** a contributor first encounters the installer model from the root README
- **THEN** the repository SHALL guide that reader from the README into the deeper installer documentation
- **AND** the README SHALL summarize the runtime boundary truthfully without claiming unsupported adapters as already shipped
