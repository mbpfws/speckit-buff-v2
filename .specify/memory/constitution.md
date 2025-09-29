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
✅ .specify/templates/tasks-template.md - Added constitution-related tasks and validation
✅ .specify/scripts/bash/ (5 files) - Added constitution compliance headers and documentation

Follow-up TODOs:
- Create AGENTS.md for platform-specific implementation guidelines
- Establish cross-platform testing framework
- Set up template synchronization automation
-->

# Spec-Kit Buff Constitution

## Core Principles

### I. Cross-Platform Compatibility
Any new feature or modification MUST work seamlessly across all 10 supported AI coding platforms (Claude Code, GitHub Copilot, Gemini CLI, Cursor, Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI, Roo Code). Features MUST use each platform's native command definitions and execution patterns.

### II. Multi-Installation Support
All features MUST support both installation options:
- Persistent installation: Tool stays installed and available in PATH
- One-time usage: Run directly without installation using uvx
Features MUST NOT assume or depend on a specific installation method.

### III. Architecture-First Development
- MUST conduct comprehensive system architecture planning before implementation
- MUST include technology stack interoperability analysis
- MUST validate library/SDK compatibility across all platforms
- MUST create contingency plans for real-world scenarios

### IV. Template-Driven Consistency
All modifications MUST preserve and extend the existing template system:
- Scripts: Bash/PowerShell automation MUST work across platforms
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

**Version**: 1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-01-18