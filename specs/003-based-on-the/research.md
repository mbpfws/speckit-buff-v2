# Research: Spec-Kit Realignment Fork - Back to Basics

**Feature**: 003-based-on-the | **Date**: 2025-09-30 | **Status**: Complete

## Research Overview

This document consolidates research findings from the feature specification clarification process and additional technical investigation needed for implementation. All critical unknowns have been resolved through the clarification sessions documented in `spec.md`.

---

## 1. Brownfield Analysis Implementation

### Decision
**Agent-based analysis with template guidance and online validation**

### Rationale
- Modern AI agents (Claude Code, GPT-4, Gemini) have sufficient context windows (100K+ tokens) for file/folder expansion
- Agents already possess native capabilities for:
  - File system traversal and reading
  - Dependency file parsing (package.json, requirements.txt, pom.xml)
  - Internet search for framework documentation
  - Git history analysis through native commands
- Template-driven checklists provide structure without requiring complex Python analysis code
- Multi-pass approach (scan → research → validate → report) allows confidence-based reporting

### Alternatives Considered
- **Complex analysis engines** (current spec-kit approach): Rejected due to violation of simplicity principle (<400 LOC target)
- **Static embedded patterns**: Rejected due to framework version drift and maintenance burden
- **External API analysis services**: Rejected due to offline requirement and added dependencies

### Implementation Approach
1. Create `brownfield-analysis.md` template with structured checklists:
   - Technology stack identification (language, frameworks, build tools)
   - Architecture pattern detection (MVC, microservices, monolith, layered)
   - File organization analysis (module structure, naming conventions)
   - Dependency audit (versions, vulnerabilities, compatibility)
2. Agent instructions for multi-pass analysis:
   - **Pass 1**: Quick scan of project structure and key files
   - **Pass 2**: Internet research for framework versions and best practices
   - **Pass 3**: Validation of patterns against official documentation
   - **Pass 4**: Report generation with confidence levels (high/medium/low)
3. Template includes explicit agent prompts for file expansion and reading

### References
- Claude Code context window: 200K tokens (sufficient for medium projects)
- GitHub Copilot workspace context: Uses semantic indexing for large codebases
- Spec clarification Q1 decision (lines 111 in spec.md)

---

## 2. Architecture Guidance Strategy

### Decision
**Hybrid approach: Starter patterns in templates + agent research for latest versions**

### Rationale
- 3-5 common frameworks (React/Next.js, Django/FastAPI, Spring Boot) cover 80% of use cases
- Framework documentation changes rapidly; embedded patterns become stale
- Agents can research official guidelines to validate against latest versions
- Templates provide starting point; agent research ensures currency

### Alternatives Considered
- **Fully embedded patterns**: Rejected due to maintenance burden and version drift
- **No starter patterns**: Rejected due to lack of initial guidance for agents
- **External pattern libraries**: Rejected due to additional dependencies and complexity

### Implementation Approach
1. Create `architecture-patterns.md` template with:
   - **Starter Patterns Section**: 3-5 framework folder structures as examples
     - React/Next.js: `pages/`, `components/`, `lib/`, `public/`
     - Django/FastAPI: `apps/`, `models/`, `views/`, `serializers/`
     - Spring Boot: `controller/`, `service/`, `repository/`, `dto/`
   - **Research Instructions**: Agent prompts to validate patterns
     - Search official framework documentation for latest versions
     - Compare project structure with official recommendations
     - Identify deviations and suggest improvements
   - **Validation Checklist**: Questions for agent to answer
     - Is folder structure aligned with framework conventions?
     - Are dependencies using compatible versions?
     - Are there missing standard directories or configurations?
2. Template guides agents to use internet search tools (Tavily, web search MCP)
3. Agents report findings with references to official documentation

### Framework Coverage
- **Tier 1** (include starter patterns): React, Next.js, Django, FastAPI, Spring Boot
- **Tier 2** (research-only guidance): Vue.js, Angular, Flask, Express.js, Laravel
- **Tier 3** (generic guidance): Agent researches from scratch for less common frameworks

### References
- Next.js official docs: https://nextjs.org/docs/getting-started/project-structure
- Django project layout: https://docs.djangoproject.com/en/stable/intro/tutorial01/
- Spring Boot best practices: https://spring.io/guides/gs/spring-boot/
- Spec clarification Q2 decision (line 112 in spec.md)

---

## 3. Artifact Synchronization Mechanism

### Decision
**Combined approach: Validation scripts + YAML frontmatter with controlled IDs**

### Rationale
- Scripts can enforce naming patterns (`{feature-id}-{feature-slug}/`) without complex governance engines
- YAML frontmatter provides minimal metadata for artifact relationships
- Non-blocking validation preserves agent autonomy and user decision-making
- Simplified REL format (controlled IDs only) reduces complexity while maintaining traceability

### Alternatives Considered
- **Complex governance system** (001-improve-spec-kit approach): Rejected due to simplicity violation
- **No validation**: Rejected due to risk of inconsistent artifact naming
- **Database-backed tracking**: Rejected due to added complexity and dependencies

### Implementation Approach
1. **Naming Convention Enforcement**:
   - Pattern: `specs/{feature-id}-{feature-slug}/`
   - Example: `specs/003-realignment-fork/`
   - Validation script checks folder names match pattern
2. **YAML Frontmatter Structure**:
   ```yaml
   ---
   feature_id: 003
   created: 2025-09-30
   status: draft
   parent_spec: ../002-another-feature/spec.md  # Optional, for plan/tasks only
   ---
   ```
3. **Validation Scripts**:
   - `validate-structure.sh` / `validate-structure.ps1`: Check folder/file existence
   - `validate-naming.sh` / `validate-naming.ps1`: Verify naming conventions
   - `validate-frontmatter.sh` / `validate-frontmatter.ps1`: Parse YAML, check required fields
4. **Agent Integration Points**:
   - Templates instruct agents to run validation after artifact creation
   - Scripts output warnings/errors in agent-readable format
   - Agents report findings to users for decision
5. **Non-Blocking Philosophy**:
   - All validation scripts use exit code 0 (success) even with warnings
   - Warnings formatted as `[WARN] message` for agent parsing
   - Agents encouraged but not forced to fix issues

### Script Outputs
```
# Success case
[INFO] Artifact structure validated successfully
[INFO] Naming conventions: PASS
[INFO] Frontmatter metadata: PASS

# Warning case
[WARN] Missing optional frontmatter field: parent_spec
[WARN] Task numbering gap detected: T001, T003 (T002 missing)
[INFO] Validation completed with 2 warnings
```

### References
- PyYAML library: https://pyyaml.org/wiki/PyYAMLDocumentation
- Bash YAML parsing: yq or basic grep/sed patterns
- Spec clarification Q3 decision (line 113 in spec.md)

---

## 4. Governance Enforcement Philosophy

### Decision
**Agent self-regulation with script checkpoints, users make final decisions**

### Rationale
- Preserves agent autonomy and user control over project decisions
- Scripts provide objective validation without blocking workflows
- Agents can interpret warnings and make recommendations to users
- Non-blocking approach prevents friction in development flow

### Alternatives Considered
- **Blocking enforcement** (traditional governance): Rejected due to loss of user autonomy
- **No governance**: Rejected due to risk of inconsistent quality and structure
- **AI-based governance evaluation**: Rejected due to added complexity and non-determinism

### Implementation Approach
1. **Constitutional Principles Document**:
   - Simple markdown with 5-7 guiding principles
   - No complex rule engines or automated enforcement
   - Examples: simplicity, cross-platform, template-driven, agent-native
2. **Script Integration Points**:
   - After artifact creation (spec, plan, tasks)
   - Before task completion (optional pre-commit hook)
   - On-demand validation (`specify check` command)
3. **Agent Instructions in Templates**:
   ```markdown
   ## Post-Task Validation
   After completing this artifact, run:
   bash .specify/scripts/bash/validate-structure.sh specs/003-realignment-fork/
   
   Review the output and report any warnings to the user. Suggest fixes but allow user decision.
   ```
4. **User Control Mechanisms**:
   - `--skip-validation` flag for check command
   - `.specify/config.yaml` to disable specific checks
   - Clear documentation on bypassing validation
5. **Agent Reporting Pattern**:
   - Agent summarizes validation results
   - Agent provides recommendations
   - Agent asks user for decision on warnings
   - Agent implements user's choice

### Governance Balance
- **Automation**: Scripts provide objective, deterministic checks
- **Autonomy**: Agents interpret and recommend, users decide
- **Quality**: Validation encourages best practices without enforcement

### References
- GitHub Copilot "suggestion" model (non-blocking guidance)
- Linting philosophy: warn but don't block (eslint, pylint)
- Spec clarification Q4 decision (line 114 in spec.md)

---

## 5. Quality Metrics Implementation

### Decision
**Well-known tool integration with agent instruction rules**

### Rationale
- Tools like eslint, pylint, prettier are already widely adopted
- Agents can run commands and interpret output without custom metrics engines
- Template-based quality checklists provide guidance without enforcement
- Non-blocking approach preserves development velocity

### Alternatives Considered
- **Custom metrics engine**: Rejected due to complexity and maintenance burden
- **Automated quality gates**: Rejected due to blocking nature and loss of flexibility
- **No quality guidance**: Rejected due to risk of inconsistent code quality

### Implementation Approach
1. **Tool Detection and Support**:
   - **JavaScript/TypeScript**: eslint, prettier, tsc (type checking)
   - **Python**: pylint, flake8, mypy, black (formatting)
   - **Java**: checkstyle, spotbugs, pmd
   - **Go**: golint, gofmt, go vet
   - **Rust**: clippy, rustfmt
2. **Agent Instructions in Templates**:
   ```markdown
   ## Quality Validation
   Check for standard tools in project:
   1. If package.json exists → run `npm run lint` or `npx eslint .`
   2. If requirements.txt exists → run `pylint src/` or `flake8 src/`
   3. Report findings with counts: errors, warnings, info
   
   Suggest fixes for critical errors only. Report warnings to user for decision.
   ```
3. **Quality Checklists**:
   - **Code Complexity**: Max cyclomatic complexity 10, max function length 50 lines
   - **Test Coverage**: Encourage 80%+ coverage, don't enforce
   - **Documentation**: Public APIs require docstrings/JSDoc
   - **Naming**: Follow language conventions (PEP 8, Google Style, etc.)
4. **Integration with Check Command**:
   ```bash
   specify check --quality
   # Runs standard tools if configured in project
   # Reports results in agent-readable format
   # Exit code 0 even with warnings
   ```
5. **Agent Reporting Format**:
   ```markdown
   ## Quality Check Results
   - ESLint: 3 errors, 12 warnings
   - Critical Issues:
     1. Unused variable in src/cli.py line 45
     2. Missing type annotation in commands/init.py line 23
   - Recommendation: Fix critical errors, review warnings with user
   ```

### Tool Configuration
- Use existing tool configs (`.eslintrc.js`, `pylintrc`, etc.) if present
- Provide sensible defaults in `.specify/templates/` for new projects
- Allow full user customization of tool configurations

### References
- ESLint: https://eslint.org/docs/latest/use/getting-started
- Pylint: https://pylint.readthedocs.io/en/latest/
- Spec clarification Q5 decision (line 115 in spec.md)

---

## 6. Python CLI Best Practices

### Decision
**Use Click framework with minimal dependencies and uv tool installation**

### Rationale
- Click provides excellent CLI development experience with minimal boilerplate
- uv tool (UV package manager) supports both persistent and one-time installation patterns
- Click's command grouping and context management fit the simple init/check command structure
- Minimal dependencies: click, requests, pyyaml (all widely used, stable)

### Alternatives Considered
- **argparse** (stdlib): Rejected due to verbose boilerplate for simple CLI
- **typer**: Rejected due to additional dependency (though excellent library)
- **custom CLI**: Rejected due to maintenance burden

### Implementation Approach
1. **Package Structure**:
   ```python
   # specify-cli/cli.py
   import click
   
   @click.group()
   @click.version_option(version='2.0.0')
   def cli():
       """Specify CLI - Simple template system for AI agents"""
       pass
   
   @cli.command()
   @click.option('--template-version', default='latest')
   def init(template_version):
       """Initialize project with templates"""
       # Implementation <100 LOC
       pass
   
   @cli.command()
   @click.option('--quality/--no-quality', default=False)
   def check(quality):
       """Check project structure and run validations"""
       # Implementation <100 LOC
       pass
   ```
2. **Installation Methods**:
   - **Persistent**: `uv tool install specify-cli` (adds to PATH)
   - **One-time**: `uvx specify-cli init` (downloads, runs, discards)
3. **LOC Target Breakdown**:
   - `cli.py`: ~80 LOC (CLI setup, command definitions)
   - `commands/init.py`: ~100 LOC (template download, extraction)
   - `commands/check.py`: ~80 LOC (validation orchestration)
   - `template_loader.py`: ~80 LOC (GitHub API, download logic)
   - `validators.py`: ~60 LOC (script execution wrappers)
   - **Total**: ~400 LOC (meets constraint)
4. **Error Handling**:
   - Click's built-in exception handling
   - Custom ClickException for user-friendly errors
   - Proper exit codes (0 success, 1 error, 2 validation warnings)
5. **Configuration File**:
   ```yaml
   # .specify/config.yaml (optional)
   template_source: https://github.com/user/templates/releases
   validation:
     skip_checks: [naming]  # Optional disable
   quality:
     tools: [eslint, pylint]  # Tool preferences
   ```

### Dependencies Rationale
- **click** (8.1+): CLI framework, ~50KB, zero dependencies
- **requests** (2.31+): HTTP client for template downloads, widely used, stable
- **pyyaml** (6.0+): YAML parsing for frontmatter, minimal footprint

### References
- Click documentation: https://click.palletsprojects.com/
- UV tool: https://github.com/astral-sh/uv
- Python packaging guide: https://packaging.python.org/

---

## 7. Template Distribution Strategy

### Decision
**GitHub Releases with semantic versioning**

### Rationale
- GitHub Releases provide built-in version tagging and artifact hosting
- Users can download specific template versions for reproducibility
- No additional infrastructure or hosting costs
- Simple HTTP download via requests library

### Alternatives Considered
- **PyPI package data**: Rejected due to coupling CLI and templates
- **Git submodules**: Rejected due to complexity for end users
- **External CDN**: Rejected due to added infrastructure dependency

### Implementation Approach
1. **Release Structure**:
   ```
   Repository: specify-fork/templates
   Release Tag: v2.0.0
   Assets:
   - templates.tar.gz (all templates)
   - spec-template.md (individual files)
   - plan-template.md
   - ...
   ```
2. **Download Logic**:
   ```python
   def download_templates(version='latest'):
       url = f'https://github.com/user/repo/releases/download/{version}/templates.tar.gz'
       response = requests.get(url)
       extract_to('.specify/templates/')
   ```
3. **Version Management**:
   - Default: `latest` tag (most recent release)
   - Explicit: `--template-version v2.0.0`
   - Local cache: Check `.specify/templates/.version` file
4. **Update Workflow**:
   ```bash
   specify check --update-templates
   # Compares local .version with latest GitHub release
   # Prompts user to download if newer version available
   ```
5. **Offline Support**:
   - Templates cached in `.specify/templates/` after first init
   - Offline mode: Use cached templates if network unavailable
   - Agent workflows fully functional offline after initial setup

### Versioning Convention
- **MAJOR**: Breaking changes to template structure
- **MINOR**: New templates or backward-compatible enhancements
- **PATCH**: Bug fixes, typos, clarifications

### References
- GitHub Releases API: https://docs.github.com/en/rest/releases
- Semantic Versioning: https://semver.org/

---

## 8. Cross-Platform Script Implementation

### Decision
**Dual implementation: bash (Unix/Linux/macOS) + PowerShell (Windows)**

### Rationale
- Covers all major platforms with native scripting
- No additional runtime dependencies (bash/PowerShell are pre-installed)
- Identical functionality and output formats across platforms
- Agents can detect platform and run appropriate scripts

### Alternatives Considered
- **Python scripts**: Rejected due to added complexity and Python version variations
- **Shell agnostic (sh)**: Rejected due to limited Windows support
- **Single cross-platform tool**: Rejected due to added dependency

### Implementation Approach
1. **Script Pairing**:
   - Every bash script has PowerShell equivalent
   - Identical command-line arguments
   - Identical output format
   - Identical exit codes
2. **Validation Scripts**:
   ```bash
   # .specify/scripts/bash/validate-structure.sh
   #!/bin/bash
   SPECS_DIR=$1
   # Check folder structure
   # Output: [INFO], [WARN], [ERROR] messages
   exit 0  # Non-blocking
   ```
   ```powershell
   # .specify/scripts/powershell/validate-structure.ps1
   param([string]$SpecsDir)
   # Check folder structure
   # Output: [INFO], [WARN], [ERROR] messages
   exit 0  # Non-blocking
   ```
3. **Platform Detection in CLI**:
   ```python
   import platform
   import subprocess
   
   def run_validation(script_name, args):
       if platform.system() == 'Windows':
           script = f'.specify/scripts/powershell/{script_name}.ps1'
           subprocess.run(['powershell', '-File', script] + args)
       else:
           script = f'.specify/scripts/bash/{script_name}.sh'
           subprocess.run(['bash', script] + args)
   ```
4. **Agent Instructions**:
   ```markdown
   ## Running Validation Scripts
   - On Unix/Linux/macOS: bash .specify/scripts/bash/validate-*.sh
   - On Windows: powershell .specify/scripts/powershell/validate-*.ps1
   
   Platform detection is automatic when using `specify check` command.
   ```
5. **Testing Strategy**:
   - CI/CD matrix: Ubuntu, macOS, Windows Server
   - Identical test cases for both script families
   - Output comparison tests to ensure parity

### Script Organization
```
.specify/scripts/
├── bash/
│   ├── validate-structure.sh     # 50-100 LOC
│   ├── validate-naming.sh        # 50-100 LOC
│   └── validate-frontmatter.sh   # 50-100 LOC
└── powershell/
    ├── validate-structure.ps1    # 50-100 LOC
    ├── validate-naming.ps1       # 50-100 LOC
    └── validate-frontmatter.ps1  # 50-100 LOC
```

### References
- Bash scripting guide: https://www.gnu.org/software/bash/manual/
- PowerShell documentation: https://docs.microsoft.com/en-us/powershell/
- Cross-platform best practices: Avoid platform-specific commands

---

## 9. Agent Platform Integration

### Decision
**Platform-specific workflow files with shared core instructions**

### Rationale
- Each AI platform has different instruction file conventions
- Shared core ensures consistency across platforms
- Platform-specific optimizations where needed
- Agents can read relevant file for their platform

### Implementation Approach
1. **Platform-Specific Files**:
   - Claude Code: `.specify/workflows/CLAUDE.md`
   - Roo Code: `.specify/workflows/ROO.md`
   - Windsurf: `.specify/workflows/WINDSURF.md`
   - GitHub Copilot: `.github/copilot-instructions.md`
   - Generic: `.specify/workflows/AGENTS.md` (fallback)
2. **File Structure**:
   ```markdown
   # Specify Workflow for [Platform]
   
   ## Project Context
   [Auto-generated from recent changes]
   
   ## Available Commands
   - /specify: Create feature specification
   - /plan: Generate implementation plan
   - /tasks: Create task breakdown
   - /implement: Execute tasks
   
   ## Validation Instructions
   [Platform-specific script execution guidance]
   
   ## Quality Tools
   [Tool detection and execution]
   
   ## Recent Changes
   [Last 3 feature additions - auto-updated]
   ```
3. **Auto-Generation via Script**:
   ```bash
   # .specify/scripts/bash/update-agent-context.sh
   PLATFORM=$1  # windsurf, claude, etc.
   # Read recent git commits
   # Update Recent Changes section
   # Preserve manual additions between markers
   # Keep under 150 lines for token efficiency
   ```
4. **Platform Optimizations**:
   - **Claude Code**: MCP tool instructions for enhanced capabilities
   - **GitHub Copilot**: Semantic search guidance for large codebases
   - **Windsurf**: IDE integration hooks
   - **Generic**: Basic file operation instructions

### Update Frequency
- Auto-update after each phase completion (plan, tasks)
- Manual update if significant project changes
- Keep last 3 feature changes only (token efficiency)

### References
- Claude Code workflows: https://docs.anthropic.com/claude/docs
- GitHub Copilot instructions: https://docs.github.com/copilot
- Agent instruction best practices: concise, actionable, versioned

---

## Research Completion Status

### All Critical Unknowns Resolved ✅
1. ✅ Brownfield analysis: Agent-driven with template checklists
2. ✅ Architecture guidance: Hybrid starter patterns + agent research
3. ✅ Artifact synchronization: Validation scripts + YAML frontmatter
4. ✅ Governance philosophy: Agent self-regulation + user decisions
5. ✅ Quality metrics: Well-known tool integration + agent reporting
6. ✅ CLI framework: Click with minimal dependencies
7. ✅ Template distribution: GitHub Releases with semantic versioning
8. ✅ Cross-platform scripts: Bash + PowerShell dual implementation
9. ✅ Agent integration: Platform-specific workflow files

### No NEEDS CLARIFICATION Remaining
All technical context decisions are complete and documented. Ready to proceed to Phase 1 (Design & Contracts).

### Constitutional Alignment Validated
- ✅ Cross-Platform: Bash + PowerShell scripts cover all OS
- ✅ Multi-Installation: uv tool + uvx support confirmed
- ✅ Template-Driven: Research confirms template-first approach viable
- ✅ Agent-Native: All decisions leverage agent capabilities, not replace
- ✅ Simplicity: CLI target <400 LOC achievable with Click framework
- ✅ Governance Balance: Non-blocking validation preserves autonomy

---

**Research Complete**: 2025-09-30  
**Next Phase**: Phase 1 - Design & Contracts (data-model.md, contracts/, quickstart.md, agent files)
