# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the Spec Kit repository - a toolkit for Spec-Driven Development (SDD) that enables building high-quality software faster by making specifications executable rather than just guiding implementation. The project provides a CLI tool (`specify`) that bootstraps projects for structured development across multiple AI coding platforms.

## Common Commands

### CLI Development
```bash
# Install the CLI locally for development
uv tool install -e .

# Run the CLI
specify init <project-name>
specify check

# Test the CLI directly with uvx
uvx --from git+https://github.com/github/spec-kit.git specify init <project-name>
```

### Project Setup Commands
After running `specify init`, the following slash commands are available in AI agents:
- `/constitution` - Create project governing principles
- `/specify` - Define feature requirements and user stories
- `/clarify` - Resolve underspecified areas (required before planning)
- `/plan` - Create technical implementation plans
- `/tasks` - Generate actionable task lists
- `/analyze` - Validate cross-artifact consistency
- `/implement` - Execute implementation tasks

## Architecture

### Core Components

1. **CLI Tool (`src/specify_cli/`)**
   - Python-based CLI using Typer for command handling
   - Downloads and configures templates from GitHub
   - Supports 10 AI coding platforms with platform-specific configurations
   - Handles both persistent installation (PATH) and one-time usage (uvx)

2. **Template System (`.specify/templates/`)**
   - Defines project structure and governance artifacts
   - Includes templates for specifications, plans, and tasks
   - Supports both bash and PowerShell scripts

3. **Governance Framework**
   - **Constitution** (`memory/constitution.md`): Supreme governance document
   - **AGENTS.md**: Platform-specific implementation guidelines
   - Hierarchical structure: Constitution → AGENTS.md → Platform-specific files

4. **Specification System**
   - Features are organized in numbered directories (`specs/001-feature-name/`)
   - Each feature contains: spec.md, plan.md, tasks.md, research.md, data-model.md
   - Supports both greenfield and brownfield development

### Key Design Principles

1. **Cross-Platform Compatibility**: All features work across 10 supported AI coding platforms
2. **Agent-Native Execution**: Commands are executable by all intended AI agents
3. **Template-Driven Consistency**: Preserves existing template system while extending it
4. **Synchronicity Enforcement**: Changes automatically propagate across related files
5. **Architecture-First Development**: Comprehensive planning before implementation

### Development Workflow

1. **Initialize**: `specify init <project>` - Sets up project structure
2. **Constitution**: `/constitution` - Establishes governing principles
3. **Specify**: `/specify` - Defines what to build (focus on what/why, not how)
4. **Clarify**: `/clarify` - Resolves ambiguities (required step)
5. **Plan**: `/plan` - Creates technical implementation with chosen stack
6. **Tasks**: `/tasks` - Breaks down into actionable items
7. **Analyze**: `/analyze` - Validates consistency across artifacts
8. **Implement**: `/implement` - Executes the implementation plan

## File Structure

```
├── src/specify_cli/          # CLI source code
├── .specify/                 # Specify configuration
│   ├── scripts/bash/         # Automation scripts
│   ├── specs/               # Feature specifications
│   └── templates/           # Project templates
├── memory/                  # Governance documents
│   └── constitution.md      # Supreme governance document
├── specs/                   # Feature development work
├── templates/               # Template definitions
├── scripts/                 # Development scripts
└── media/                   # Images and assets
```

## Platform Support

The project supports 10 AI coding platforms:
- **Tier 1 (Full Integration)**: Claude Code, Roo Code
- **Tier 2 (Core Features)**: GitHub Copilot, Cursor, Gemini CLI
- **Tier 3 (Basic Support)**: Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI

Each platform has specific configuration files in the project root (`.claude/`, `.roo/`, etc.) that are kept synchronized.

## Important Notes

- Always follow the hierarchical governance structure
- Maintain cross-platform compatibility for all features
- Use the template system for consistency
- Execute commands through native agent patterns
- Test across multiple platforms before submitting changes
- Follow TDD methodology with comprehensive integration testing