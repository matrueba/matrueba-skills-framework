# Quality Checklist for Requirements Documents

Apply this checklist to every reviewed requirements document. Each unfulfilled item is a candidate for a proposed improvement.

## Document Metadata

- [ ] Has a clear project or product name
- [ ] Includes version number
- [ ] Includes date (creation or last updated)
- [ ] Lists author(s) or responsible team
- [ ] Status is indicated (Draft / Under Review / Approved)

## 1. Introduction

- [ ] **Purpose**: Document objective and intended audience are defined
- [ ] **Product Vision**: Describes what the product is, the problem it solves, and its core value proposition
- [ ] **Scope**: Explicitly lists what is included in this phase
- [ ] **Out of Scope**: Explicitly states what is NOT included
- [ ] **Glossary**: Technical or business terms are defined to avoid confusion

## 2. User Profiles (User Personas)

- [ ] **Roles**: Different types of users are identified (e.g., Admin, Guest, Premium)
- [ ] **Needs**: What each profile aims to achieve is described

## 3. Functional Requirements

- [ ] **User Stories / Use Cases**: Described in format "As a [user], I want to [action] so that [benefit]"
- [ ] **Business Logic**: Specific rules the system must follow are documented
- [ ] **Data Management**: Input data, processing, and output are defined
- [ ] **Prioritization**: Requirements are prioritized using a clear framework (e.g., MoSCoW: Must, Should, Could, Won't)

## 4. Workflows

- [ ] **Main Processes**: Key interactions described step by step (registration, purchase, recovery, etc.)
- [ ] **Diagrams**: Flowcharts or sequence diagrams are included (or noted as needed)

## 5. Quality Attributes (Non-Functional Requirements)

- [ ] **Performance**: Expected response times and processing capacity defined
- [ ] **Scalability**: Concurrent user targets specified
- [ ] **Security**: Authentication, encryption, and regulatory compliance addressed (GDPR, HIPAA, etc.)
- [ ] **Usability**: Accessibility criteria (WCAG 2.1) and UX standards defined
- [ ] **Availability**: Uptime percentage specified (e.g., 99.9%)
- [ ] **Observability and Monitoring**: Error reporting and metrics tools identified (Sentry, Datadog, etc.)
- [ ] **Testing Strategy**: Minimum code coverage or testing requirements defined

## 6. Interface Requirements (UI)

- [ ] **Theming and States**: Dark/Light mode strategy defined
- [ ] **Color Palette**: Primary, secondary, and accent colors specified
- [ ] **Typography**: Selected fonts documented
- [ ] **Responsive Behavior**: Mobile-first or Desktop-first approach stated
- [ ] **Interface States**: Loading, empty, and error states defined (spinners vs. skeletons, 404/500 pages)

## 7. Constraints

- [ ] **Technological**: Languages, frameworks, databases, and legacy integrations documented with rationale
- [ ] **Third-Party Services**: External services listed (payment, email, analytics, auth)
- [ ] **Regulatory/Legal**: Applicable laws and compliance requirements identified
- [ ] **Resources and Time**: Budget limits and delivery deadlines stated

## 8. Dependencies and Assumptions

- [ ] **Dependencies**: External elements required for success are listed
- [ ] **Assumptions**: Facts taken for granted that could affect the project are documented

## 9. Acceptance Criteria

- [ ] Each requirement has testable acceptance criteria
- [ ] Criteria follow a clear format (Given/When/Then or equivalent)
- [ ] Definition of Done is unambiguously defined

---

## 10. Consistency & Clarity

- [ ] Technical terms are defined or consistent with project glossary
- [ ] No ambiguities that allow multiple interpretations
- [ ] Examples illustrate complex scenarios
- [ ] File paths, endpoints, and component names are specific
- [ ] Entity names match other project specifications

## 11. Delivery & Operations

- [ ] Testing strategy is outlined (unit, integration, E2E)
- [ ] Rollout plan is defined (feature flags, phased release, rollback)
- [ ] Success metrics or telemetry are identified
- [ ] Monitoring and alerting considerations are addressed
