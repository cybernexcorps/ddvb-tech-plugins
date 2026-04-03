# Blueprint Template — 14 Sections

Use this template for every technical blueprint. Each section is required. Write as if the reader (a developer or AI coding agent) will build the product from this document alone.

## Section Guide

### 1. Product Design Requirements (PDR)
- Project Vision: problem it solves, 2-3 sentences
- Current Context (if enhancing existing system): what exists, what's missing
- Target Users: persona table (name, role, usage)
- Core Features: P0 (must-have), P1 (should-have), P2 (nice-to-have) with IDs (F-XXX-01)
- Functional Requirements: user stories, integration points
- Non-Functional Requirements: performance (response times), scalability, reliability (uptime SLA), security, accessibility

### 2. Design Decisions
For every major choice, use ADR format:
- **Decision**: what we chose
- **Rationale**: why (numbered reasons)
- **Alternatives Considered**: at least 2, with honest rejection reasons
- **Trade-offs**: what downsides we accept and why
- **Reversibility**: how hard to change later (High/Medium/Low)

Cover at minimum: framework, database, hosting, auth, state management, LLM provider, agent framework.

### 3. Tech Stack
Table with: Layer | Technology | Version | Decision Ref
Separate runtime dependencies from development dependencies.

### 4. App Flowchart
Mermaid diagrams:
- System architecture (components + connections)
- User journey (step by step with decision points)
- State machine (if applicable)

### 5. Technical Design
- Core Components: key interfaces/types with TypeScript or Python code blocks
- Data Models: full SQL schema with constraints, indexes, RLS policies
- Integration Points: table with protocol, auth, rate limits, error handling
- File Structure: explicit directory tree with NEW/MODIFIED/EXISTING annotations

### 6. Project Rules
- Coding standards, naming conventions
- Branch strategy, commit conventions, PR requirements
- Code quality tools (linters, formatters)
- Documentation standards

### 7. Frontend Guidelines
- Design principles (dark mode default, component library)
- Component architecture (tree showing Server vs Client components)
- Styling (Tailwind, shadcn/ui, design tokens)
- Error/loading/empty states

### 8. Backend Guidelines
- API design (endpoints table)
- Job queue architecture (if applicable)
- Security measures
- Scalability patterns

### 9. Optimised Code Guidelines
- Good vs bad code examples (with comments)
- Common pitfalls for this specific stack
- Performance patterns

### 10. Implementation Plan
Phased with milestones:
- Phase 1: Foundation [timeline] — checklist of tasks
- Phase 2: Core Features [timeline]
- Phase 3: Enhancement [timeline]
- Phase 4: Production Readiness [timeline]
Total estimated timeline at the end.

### 11. Testing Strategy
- Unit tests: coverage target, mocking strategy
- Integration tests: scenarios, environment requirements
- E2E tests: critical user journeys, tools
- Performance tests: load testing approach, thresholds

### 12. Observability
- Logging: key points, structured format, correlation IDs
- Metrics: table with metric name, collection method, alert threshold
- Alerting: channels, thresholds, escalation

### 13. Rollout Strategy
5 stages: Development → Testing → Staging → Production → Post-Launch Monitoring
Include success criteria checklist.

### 14. Security Checklist
Table with 13 checks (auth, endpoints, secrets, git-ignore, errors, middleware, RBAC, DB, hosting, HTTPS, uploads, CSP, dependency scanning). Each with implementation detail.

## Appendix Sections (optional)
- Future Considerations: v2 enhancements, known limitations, competitive analysis
- References: links to source documents, external docs, related blueprints
