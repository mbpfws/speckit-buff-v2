<!--
Sync Impact Report
==================

Version Change: None → 1.0.0 (initial constitution)

Modified Principles: None (all new)

Added Sections:
- Core Principles (I-VII)
- Cross-Platform Constraints
- Development Workflow
- Governance

Templates Updated:
✅ .specify/templates/plan-template.md - Added comprehensive Constitution Check section
✅ .specify/templates/spec-template.md - Added cross-platform validation and template consistency

## Core Principles

### I. Cross-Platform Compatibility
All features, templates, and workflows must function consistently across:
- **10 AI Coding platforms**: Claude Code, Roo Code, GitHub Copilot, Cursor, Gemini CLI, Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI
- **3 Operating Systems**: Windows, macOS, Linux
- **Platform-native patterns**: Each platform's workflow syntax and capabilities must be respected
- **Identical behavior**: Scripts must produce identical output regardless of platform

### II. Multi-Installation Support
The framework must work seamlessly with both installation methods:
- **Persistent installation**: `uv tool install specify-cli` (PATH-based)
- **One-time usage**: `uvx specify-cli init` (temporary execution)
- **No installation assumptions**: Workflows must not depend on specific installation method
- **Offline capability**: Essential operations must work without network access

### III. Template-Driven Consistency
Templates are the foundation of the system:
- **Templates guide**: High-quality markdown templates provide structure and guidance
- **Agents fill**: AI agents populate templates, not create from scratch
- **Standardized format**: YAML frontmatter + markdown body for all templates
- **Embedded guidance**: Templates include agent-specific instructions and examples
- **Version stability**: Template changes must be backward compatible

### IV. Agent-Native Execution
AI agents are the primary actors:
- **Workflows are markdown**: Commands defined as markdown files with YAML frontmatter, not CLI commands
- **Agents execute**: Agents read workflows and execute steps, system augments
- **Leverage capabilities**: Use agent native features (web search, code analysis, multi-file edits)
- **Multi-stage research**: Complex features trigger iterative research workflows
- **Intelligent orchestration**: Workflows can automatically trigger other workflows based on conditions
- Templates: All template files MUST maintain consistent structure
- Commands: Slash commands MUST follow established patterns
- Rules: Governance rules MUST be platform-agnostic
- Constitution: MUST remain the single source of truth

### V. Synchronicity Enforcement
Changes MUST propagate automatically across all related files and platforms:
- Single change MUST trigger updates to all dependent artifacts
- Platform-specific files (.claude/, .roo/, etc.) MUST stay synchronized
- Template modifications MUST reflect in all instantiated copies

### VI. Agent-Native Execution
All automation MUST be executable by the intended AI coding agents:
- Shell/bash commands MUST be runnable by all 10 platforms
- Git operations MUST use platform-native PR/branch/commit workflows
- MCP server tools MUST follow cross-platform compatibility patterns
- Features MUST inject as commands/rules that agents execute natively

### VII. Hierarchical Governance
- Constitution: Core principles and governance (this file)
- AGENTS.md: Platform-specific implementation guidelines
- CLAUDE.md: Claude Code specific instructions
- Templates: Reusable patterns for all artifacts
- Scripts: Automation executable by all platforms

## Cross-Platform Constraints

### Supported Platforms
All features MUST support these platforms without exception:
- Claude Code
- GitHub Copilot
- Gemini CLI
- Cursor
- Qwen Code
- opencode
- Windsurf
- Kilo Code
- Auggie CLI
- Roo Code

### Command Patterns
- MUST use each platform's native slash command format
- MUST NOT introduce platform-specific dependencies
- MUST provide consistent behavior across all platforms

### File Structure
- `.specify/`: Core template and script definitions
- `.claude/`: Claude Code specific configurations
- `.roo/`: Roo Code specific configurations
- `templates/`: Platform-agnostic template files
- All structures MUST follow hierarchical naming conventions

## Development Workflow

### 1. Architecture Planning Phase
- Comprehensive system analysis
- Technology stack validation
- Cross-platform compatibility verification
- Contingency planning

### 2. Knowledge Integration
- Utilize MCP servers for research
- Maintain hierarchical documentation
- Continuous knowledge ingestion cycles

### 3. Template Synchronization
- Single source of truth principle
- Automatic propagation across all platforms
- Validation of consistency before deployment

### 4. Agent Orchestration
- Role-based agent selection
- Context-aware switching
- Specialized task delegation

## Governance

### Amendment Process
1. Proposed changes MUST be validated against all 10 platforms
2. Impact analysis MUST include cross-platform compatibility
3. Changes MUST be tested on at least 3 platforms before approval
4. ALL dependent templates MUST be updated simultaneously

### Versioning Policy
- MAJOR: Backward incompatible changes or platform removals
- MINOR: New platform support or feature additions
- PATCH: Bug fixes or documentation updates

### Compliance Review
- Monthly cross-platform compatibility audits
- Quarterly template synchronization reviews
- Annual architecture validation

### Runtime Guidance
- Use AGENTS.md for platform-specific implementation patterns
- Consult CLAUDE.md for Claude Code specific instructions
- Reference individual platform documentation (.roo/, etc.)
- Follow constitution as supreme governance document

---

## Orchestration Principles (v2.0 Extension)

### VIII. Intelligent Workflow Chaining
Workflows can automatically trigger other workflows:
- **Auto-triggers**: Unconditional workflow execution (e.g., complexity detection before spec creation)
- **Conditional chains**: Trigger workflows based on context conditions (e.g., research-tech if complexity >= medium)
- **Pre-conditions**: Workflows can require specific context states before execution
- **Post-conditions**: Workflows update context on completion for downstream workflows
- **Maximum iterations**: Research workflows have iteration limits to prevent infinite loops

### IX. Complexity-Driven Research
Simple descriptions don't mean simple implementations:
- **Complexity detection**: Automatic analysis of feature descriptions for technical depth
- **Multi-stage research**: Iterative research passes for complex technology stacks
- **Web search mandatory**: Always use current information from web search, never assume
- **Research artifacts**: Document findings in research.md with citations and versions
- **Technology recommendations**: Research must produce specific versions and SDKs, not vague suggestions

### X. Context-Aware Execution
Workflows share state through persistent context:
- **Context file**: `.specify/context.json` stores workflow state and findings
- **Condition evaluation**: Workflows read context to determine execution path
- **State transitions**: Each workflow updates context with completion flags
- **Multi-domain detection**: Automatically identify when features span multiple domains
- **Research pass tracking**: Count research iterations to ensure thoroughness

### XI. Domain-Driven Architecture
Architecture decisions are research-driven:
- **Domain identification**: Automatically detect business domains from specifications
- **Pattern research**: Research proven patterns for detected domains
- **Multi-domain integration**: Trigger integration research when multiple domains detected
- **Case study priority**: Prefer production case studies over theoretical recommendations
- **Source citation**: All architectural decisions must cite research sources

**Version**: 2.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-01-30