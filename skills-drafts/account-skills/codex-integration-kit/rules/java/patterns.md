# Java Patterns

## Scope

The backend stack is Java 8+ with Spring-style REST controllers, service layers, and SQL or ORM-backed repositories.
Follow the target project's configured JDK and avoid language or library features that its runtime cannot support.

## Package and Class Structure

- Controllers should stay focused on HTTP binding, validation, and response mapping; business rules belong in service classes.
- Services should orchestrate use cases and transactions; repositories or mappers should stay responsible for persistence details.
- If a Java file exceeds 300 lines, evaluate extraction before adding more responsibilities.
- Do not let request DTOs, entities, and response DTOs collapse into one shared class unless the boundary is genuinely identical.

## Types and Domain Modeling

- Prefer explicit DTOs, value objects, enums, and typed result models over `Map<String, Object>` or loosely structured payloads.
- Use enums or named constant sets for semantic states; do not scatter magic strings through controller and service code.
- Keep nullable semantics explicit. Do not use empty strings, `0`, or sentinel values to hide "missing" input.
- Prefer immutable request/response models where the framework and serialization setup allow it cleanly.

## Request Validation and Normalization

- API request DTOs should use Bean Validation annotations such as `@NotNull`, `@NotBlank`, `@Size`, `@Pattern`, and `@Valid` instead of ad hoc controller checks.
- Enable validation on controller boundaries with `@Validated` and validate nested request objects with `@Valid`.
- Every externally provided string field should have a deliberate normalization rule. Default: trim leading and trailing whitespace before business logic.
- If a string field is meaningful with preserved whitespace, document that exception near the DTO or normalizer instead of relying on accidental behavior.
- Request parameters, path variables, and DTO fields that come from interfaces must define length limits. Do not accept unbounded strings for names, codes, remarks, search keys, or identifiers.
- Prefer placing trim and length rules close to the boundary DTO or a dedicated request normalizer so downstream code sees already-clean input.
- Validation failure messages should describe the business field and constraint clearly; do not leak internal class names or stack details.

## Controller and Service Boundaries

- Do not pass raw request objects deep into repositories. Convert them to command objects, typed parameters, or domain models first.
- Keep controller methods thin: bind input, validate, normalize, call the service, and map the response.
- Avoid mixing persistence branching, remote-call logic, and response formatting in one method.
- For bulk APIs, validate each item and enforce collection-size limits before entering business loops.

## Exceptions and Transactions

- Do not catch `Exception` just to return a success-like response. Preserve failure semantics and diagnostic context.
- Translate low-level exceptions at service boundaries into stable business exceptions or error codes.
- Keep transaction boundaries in service-layer use cases; avoid scattering transaction annotations across helper methods without intent.
- Avoid long blocking or remote work inside a transaction when the operation can be split safely.

## Data Handling

- Before mapping raw JSON or external fields, verify the real field names, nullability, enum values, and case conventions from actual payloads.
- Prefer small helper methods for complex list transformations instead of deep nested streams that hide business intent.
- When copying data between DTOs and entities, be explicit about which fields are allowed to cross the boundary.
