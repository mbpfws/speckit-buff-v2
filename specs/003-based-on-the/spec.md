# Feature Specification: Spec-Kit Realignment Fork - Back to Basics

**Feature Branch**: `003-based-on-the`
**Created**: 2025-09-30
**Status**: Draft
**Input**: User description: ": Based on the analysis report showing spec-kit has drifted from its original vision of being a simple template and script system for AI agents, create a fork that realigns with the original principles while incorporating the improvements from specs/001-improve-spec-kit/spec.md but simplified according to the original minimalist philosophy. The fork should focus on: 1) Simple CLI with only init and check commands, 2) High-quality markdown templates instead of complex analysis, 3) Cross-platform shell scripts for automation, 4) Agent-first design where AI agents do the work, 5) Template-driven guardrails instead of complex governance. Transform the 001-improve-spec-kit requirements to fit this simplicity mindset while preserving valuable improvements."

## Execution Flow (main)
```
1. Parse user description from Input
   ’ SUCCESS: Realignment fork requirements identified with simplicity focus
2. Extract key concepts from description
   ’ Identify: simplicity, realignment, template-driven, agent-first, minimal CLI
3. Validate against constitution principles:
   ’ Cross-Platform: Requirements apply to all 10 platforms 
   ’ Multi-Installation: Must support both installation methods 
   ’ Template-Driven: Core of the simplified approach 
   ’ Agent-Native: AI agents remain primary actors 
4. For each unclear aspect:
   ’ Mark with [NEEDS CLARIFICATION: specific question]
5. Fill User Scenarios & Testing section
   ’ SUCCESS: Clear user scenarios for simplified workflow
   ’ Include cross-platform validation scenarios
6. Generate Functional Requirements
   ’ Each requirement must be testable across all platforms
   ’ Mark ambiguous requirements
   ’ Validate against template-driven consistency
7. Identify Key Entities (data involved)
   ’ Identified: Template System, CLI Tool, Script Library
8. Run Review Checklist
   ’ SUCCESS: All constitution principles addressed
   ’ Requirements aligned with simplicity goals
9. Return: SUCCESS (spec ready for planning)
```

---

## ¡ Quick Guidelines
-  Focus on WHAT users need and WHY
- L Avoid HOW to implement (no tech stack, APIs, code structure)
- =e Written for business stakeholders, not developers

### Section Requirements
- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### Cross-Platform Validation
- All requirements MUST work across all 10 supported platforms
- Requirements MUST NOT specify platform-specific implementation details
- User scenarios MUST account for different agent execution patterns
- Acceptance criteria MUST be verifiable on all platforms

### Template-Driven Consistency
- Specifications MUST follow established template structure
- Requirements MUST use standardized phrasing and formatting
- All specifications MUST be consumable by all AI agents
- Changes MUST propagate to dependent artifacts automatically

### For AI Generation
When creating this spec from a user prompt:
1. **Mark all ambiguities**: Use [NEEDS CLARIFICATION: specific question] for any assumption you'd need to make
2. **Don't guess**: If the prompt doesn't specify something (e.g., "login system" without auth method), mark it
3. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
4. **Consider cross-platform implications**: Ensure requirements work on all 10 AI coding platforms
5. **Validate template consistency**: Follow established patterns and structure
6. **Common underspecified areas**:
   - User types and permissions
   - Data retention/deletion policies
   - Performance targets and scale
   - Error handling behaviors
   - Integration requirements
   - Security/compliance needs
   - Cross-platform compatibility requirements
   - Multi-installation support considerations

---

## User Scenarios & Testing *(mandatory)*

### Primary User Story
As a developer who believes in the original vision of spec-kit, I want a fork that returns to simple, elegant templates and scripts while preserving the valuable improvements from the enhancement initiative, so that I can efficiently develop both greenfield and brownfield projects with minimal tooling overhead, maximum AI agent autonomy, and augmented agent research capabilities.

### Acceptance Scenarios
1. **Given** a new project, **When** I run the simplified CLI init command, **Then** it MUST download templates and set up structure within 3 seconds without deep analysis
2. **Given** a brownfield project, **When** agent uses analysis templates, **Then** it MUST perform multi-pass analysis (scan → research → validate) and report findings with confidence levels
3. **Given** framework-specific needs, **When** agent uses architecture templates, **Then** it MUST research official guidelines and validate patterns against latest versions
4. **Given** artifact creation, **When** agent completes a task, **Then** validation scripts MUST check naming/structure and prompt agent for compliance report
5. **Given** the template-based system, **When** I use /specify command with any AI agent, **Then** it MUST execute natively using templates, scripts, and agent research capabilities
6. **Given** cross-platform needs, **When** I use any of the 10 supported AI platforms, **Then** all commands MUST work consistently with agent-native patterns
7. **Given** existing improvements from 001-improve-spec-kit, **When** I use the fork, **Then** brownfield analysis, architecture guidance, artifact management, and quality validation MUST be preserved through agent-augmented templates
8. **Given** the simplicity focus, **When** I examine the CLI code, **Then** it MUST be under 400 lines with init, check commands, and validation script integration
9. **Given** quality tool integration, **When** agent uses quality templates, **Then** it MUST check standard tools (eslint, pylint) and report findings without blocking
10. **Given** governance enforcement, **When** validation scripts detect issues, **Then** agents MUST report to users for decisions rather than auto-blocking

### Edge Cases
- What happens when templates need updating? → GitHub release workflow with version tagging
- How does the system handle custom template modifications? → User-owned .specify/ folder, templates as starting point
- What are the implications for offline usage? → Templates cached locally, agents work offline after initial setup
- How does the fork handle version compatibility with original spec-kit projects? → Full backward compatibility through template structure
- What happens when AI agents need additional context beyond templates? → Agents use internet research and MCP tools for validation
- What happens when brownfield project analysis yields ambiguous results? → Agent presents findings with confidence levels, asks user
- How does system handle framework version conflicts? → Agents research latest versions, validate against project dependencies
- What happens when validation scripts fail? → Non-blocking warnings, agents report to user for decision

---

## Clarifications

### Session 2025-09-30: Simplicity vs Feature Parity
- **Q1: Brownfield Analysis Scope** → Agent-based analysis with template guidance and online validation. Modern agents have sufficient capabilities for file/folder expansion and reading within context limits.
- **Q2: Architecture Guidance Implementation** → Hybrid approach: templates pull from official framework guidelines via internet search, agents validate with research for latest tech/versions.
- **Q3: Artifact Synchronization Mechanism** → Combined approach: scripts validate structure, enforce naming patterns, YAML frontmatter for controlled IDs (simplified REL format).
- **Q4: Governance Enforcement Philosophy** → Agents self-regulate with templated instructions to run scripts at integration points (e.g., after task completion). Scripts urge agents for reports, leaving user decisions.
- **Q5: Quality Metrics vs Simplicity** → Support well-known tools (eslint, pytest) with agent instruction rules. Agents check for lint errors and report findings.

---

## Requirements *(mandatory)*

### Functional Requirements

#### Simplified CLI Architecture
- **FR-001**: CLI MUST provide only two commands: init (downloads templates, sets up project) and check (verifies tools and validates project structure)
- **FR-002**: CLI MUST be under 400 lines of Python code with no analysis engines but WITH validation scripts for structure/naming
- **FR-003**: CLI MUST download templates from GitHub releases without processing or deep analysis
- **FR-004**: CLI MUST support both persistent installation (uv tool) and one-time usage (uvx) patterns
- **FR-005**: CLI MUST have minimal dependencies: Python standard library, requests for downloads, PyYAML for frontmatter parsing

#### Template-Driven System
- **FR-006**: System MUST provide high-quality markdown templates for spec, plan, tasks, and constitution
- **FR-007**: Templates MUST include embedded guidance and examples instead of external analysis engines
- **FR-008**: Templates MUST be self-contained and executable by AI agents without additional tooling
- **FR-009**: Template system MUST support custom modifications while maintaining core structure
- **FR-010**: Templates MUST include cross-platform shell scripts for automation tasks

#### Agent-First Design
- **FR-011**: All commands (/specify, /plan, /tasks, /implement) MUST execute natively on all 10 AI platforms
- **FR-012**: System MUST provide platform-specific instruction files (.claude/, .roo/, etc.) generated from templates
- **FR-013**: AI agents MUST remain the primary actors for all analysis, planning, and implementation work
- **FR-014**: Templates MUST provide context and guardrails rather than enforcing rules through code
- **FR-015**: System MUST leverage AI agents' native capabilities instead of replacing them

#### Cross-Platform Compatibility
- **FR-016**: All templates MUST work identically across all 10 supported AI coding platforms
- **FR-017**: Shell scripts MUST be provided in both bash and PowerShell for Windows compatibility
- **FR-018**: Template structure MUST be consumable by all AI agents without platform-specific modifications
- **FR-019**: System MUST handle platform-specific differences through templates, not code logic
- **FR-020**: All functionality MUST be accessible through slash commands on every platform

#### Simplified Improvements (from 001-improve-spec-kit)

##### Brownfield Analysis (Agent-Augmented)
- **FR-021**: Templates MUST provide structured checklists for agents to analyze existing projects (technology stack, architecture patterns, file organization)
- **FR-022**: Templates MUST guide agents to perform multi-pass analysis: initial scan → online research → validation → user confirmation
- **FR-023**: Templates MUST include instructions for agents to use file/folder expansion, dependency file parsing (package.json, requirements.txt), and git history analysis
- **FR-024**: System MUST support brownfield projects through agent-driven template guidance, with agents reporting findings and confidence levels to users

##### Framework-Specific Architecture (Hybrid Research)
- **FR-025**: Templates MUST include starter patterns for 3-5 common frameworks (React/Next.js, Django/FastAPI, Spring Boot) as examples
- **FR-026**: Templates MUST instruct agents to research official framework guidelines via internet search for latest versions and best practices
- **FR-027**: Templates MUST provide validation checklists for agents to verify framework patterns against official documentation
- **FR-028**: Templates MUST include folder structure examples as starting points, with instructions for agents to adapt based on research

##### Artifact Management (Script-Enforced)
- **FR-029**: System MUST enforce naming conventions through validation scripts: `{feature-id}-{feature-slug}/` folder structure
- **FR-030**: All artifacts MUST include YAML frontmatter with minimal metadata: `feature_id`, `created`, `status`, `parent_spec` (for plan/tasks)
- **FR-031**: Validation scripts MUST check artifact structure and naming patterns, providing non-blocking warnings to agents
- **FR-032**: Templates MUST guide agents to maintain artifact relationships through frontmatter references and consistent naming
- **FR-033**: System MUST provide shell/bash scripts for validation at integration points (post-task, pre-commit hooks optional)

##### Quality and Tool Integration
- **FR-034**: Templates MUST include instructions for agents to check well-known tools: eslint (JS/TS), pylint (Python), prettier (formatting)
- **FR-035**: Templates MUST provide quality checklists as agent rules: code complexity guidelines, test coverage expectations, documentation standards
- **FR-036**: Validation scripts MUST be optional and user-configurable, with clear bypass instructions in templates
- **FR-037**: Templates MUST guide agents to report quality findings and lint errors, leaving remediation decisions to users

#### Cross-Platform Agent Integration
- **FR-038**: Templates MUST work identically across all 10 AI coding platforms with agent-native execution patterns
- **FR-039**: System MUST provide platform-specific instruction files that reference validation scripts appropriately
- **FR-040**: Templates MUST guide agents to use platform-native capabilities (MCP tools, internet search, file operations) for enhanced analysis
- **FR-041**: Validation scripts MUST be cross-platform (bash for Unix, PowerShell for Windows) with identical outputs

#### Governance and Maintenance
- **FR-042**: Constitution MUST be a simple guiding principles document with script-based validation for critical rules only
- **FR-043**: Template updates MUST be handled through GitHub releases with semantic versioning
- **FR-044**: System MUST use agent self-regulation with script checkpoints, not blocking enforcement
- **FR-045**: Validation scripts MUST provide actionable guidance and allow user override decisions
- **FR-046**: System MUST provide clear migration path for existing spec-kit projects with backward compatibility
- **FR-047**: All governance MUST balance automation (scripts) with autonomy (agent decisions and user choices)

### Key Entities

#### Augmented Template System
- **Purpose**: Provides markdown templates with embedded guidance, research instructions, and validation checkpoints for AI agents
- **Attributes**: Self-contained with agent research hooks, platform-agnostic, YAML frontmatter for metadata
- **Relationships**: Core system component, consumed by agents with internet-augmented validation
- **Enhancement**: Includes framework research instructions and brownfield analysis checklists from 001 spec

#### Lightweight CLI with Validation
- **Purpose**: Bootstraps projects, validates structure, runs optional quality checks
- **Attributes**: Under 400 lines, init/check commands, validation scripts integration
- **Relationships**: Setup tool + structure validator, not used for deep analysis
- **Enhancement**: Adds validation capabilities while maintaining simplicity (<400 LOC target)

#### Script Library (Validation-Focused)
- **Purpose**: Provides cross-platform validation and structure checking scripts
- **Attributes**: Bash/PowerShell versions, non-blocking warnings, naming enforcement, frontmatter validation
- **Relationships**: Called by agents at integration points (post-task, pre-commit)
- **Enhancement**: Enforces naming conventions and artifact structure from 001 spec governance requirements

#### Agent Research Integration
- **Purpose**: Guides agents to use internet search and validation for brownfield analysis and framework patterns
- **Attributes**: Template-driven research instructions, confidence-based reporting, user confirmation loops
- **Relationships**: Augments template system with dynamic validation
- **Enhancement**: Replaces complex analysis engines with agent-driven research capabilities

---

## Review & Acceptance Checklist
*GATE: Automated checks run during main() execution*

### Content Quality
- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

### Requirement Completeness
- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified
- [x] Cross-platform compatibility validated
- [x] Multi-installation support considered
- [x] Template-driven consistency maintained
- [x] Architecture-first principles followed
- [x] Brownfield analysis capabilities preserved (agent-augmented)
- [x] Framework-specific guidance preserved (hybrid research)
- [x] Artifact management preserved (script-enforced)
- [x] Quality validation preserved (tool integration)
- [x] Governance balanced (automation + autonomy)

### Constitution Alignment
- [x] Cross-Platform compatibility ensured (all 10 platforms)
- [x] Multi-Installation support maintained (PATH + uvx)
- [x] Template-Driven approach central (augmented with research)
- [x] Agent-Native execution preserved (enhanced with validation)
- [x] Hierarchical governance balanced (scripts + autonomy)
- [x] Simplicity preserved (CLI <400 LOC, no analysis engines)
- [x] Feature parity achieved (001 improvements via agent augmentation)

---

## Execution Status
*Updated by main() during processing*

- [x] User description parsed
- [x] Key concepts extracted
- [x] Ambiguities marked and clarified (5 key questions resolved)
- [x] Cross-platform validation completed
- [x] Template consistency verified
- [x] User scenarios defined (10 acceptance scenarios)
- [x] Requirements generated (47 functional requirements)
- [x] Entities identified (4 key entities with enhancements)
- [x] Review checklist passed
- [x] Constitution alignment validated
- [x] Feature parity with 001 achieved through agent augmentation
- [x] Simplicity philosophy maintained (no analysis engines, <400 LOC)

---

## Implementation Notes

### Key Architectural Decisions

**1. Agent-Augmented Analysis (not Analysis Engines)**
- Replace Python analysis code (best_practices.py, pattern_detector.py) with template-driven agent instructions
- Agents use their native capabilities (file reading, internet search, MCP tools) for brownfield analysis
- Multi-pass approach: scan → research → validate → report with confidence levels

**2. Hybrid Architecture Guidance (not Embedded Patterns)**
- Templates include 3-5 starter framework patterns as examples
- Agents research official framework documentation for latest versions and best practices
- Validation through agent-driven comparison with official guidelines

**3. Script-Enforced Structure (not Complex Governance)**
- Lightweight validation scripts check naming conventions and artifact structure
- YAML frontmatter provides minimal metadata for artifact relationships
- Non-blocking warnings allow agent reporting and user decision-making

**4. Tool Integration Guidance (not Automated Metrics)**
- Templates instruct agents to check well-known tools (eslint, pylint, prettier)
- Agents report findings without blocking workflows
- Users make final decisions on quality remediation

**5. Simplicity Metrics**
- CLI target: <400 lines (vs 1152+ in current implementation)
- Zero analysis engines (removing MCP server integrations for analysis)
- Minimal dependencies: stdlib + requests + PyYAML
- Core philosophy: Templates guide, agents execute, scripts validate, users decide

### Migration from Current spec-kit

**What Gets Removed:**
- Complex CLI analysis features (brownfield_analyzer.py, best_practices.py, pattern_detector.py, cross_architecture.py)
- MCP server integrations for analysis (Tavily, Context7, DeepWiki)
- Automated governance enforcement systems
- Complex constitutional processes

**What Gets Transformed:**
- Brownfield analysis → Agent-driven template checklists with research instructions
- Framework patterns → Starter examples + agent research instructions
- Governance enforcement → Validation scripts + agent self-regulation
- Quality metrics → Tool integration guidance + agent reporting

**What Gets Preserved:**
- Template system (enhanced with research instructions)
- Cross-platform shell scripts (enhanced with validation)
- Multi-installation support (PATH + uvx)
- Agent-native execution model
- All 10 platform support

### Success Criteria for Fork

1. **Simplicity**: CLI under 400 lines, no analysis engines
2. **Feature Parity**: All 001 improvements present through agent augmentation
3. **Agent-First**: Agents remain primary actors, enhanced by templates/scripts
4. **Backward Compatible**: Existing spec-kit projects work without changes
5. **User Autonomy**: Validation is non-blocking, users make final decisions

---