# Windsurf Agent Instructions: Spec-Kit Realignment Fork

**Project**: spec-kit fork (v2.0.0) | **Feature**: 003-based-on-the | **Updated**: 2025-09-30

## Project Context

This is a fork of spec-kit that returns to its original vision: simple templates and scripts for AI agents. You are implementing a minimalist CLI (<400 LOC) that downloads high-quality markdown templates and provides non-blocking validation, while preserving brownfield analysis, architecture guidance, and quality validation through agent-augmented templates.

### Core Philosophy
- **Templates guide, agents execute, scripts validate, users decide**
- **Simplicity over complexity**: No analysis engines, minimal dependencies
- **Agent-first**: Leverage your native capabilities, don't replace them
- **Non-blocking**: Validation warns, never blocks workflows

---

## Available Commands

### /specify - Create Feature Specification
```markdown
1. Ask user for feature description
2. Load .specify/templates/spec-template.md
3. Fill template sections with user input
4. Create specs/{id}-{slug}/spec.md with YAML frontmatter
5. Run: bash .specify/scripts/bash/validate-frontmatter.sh
6. Report validation results to user
```

### /plan - Generate Implementation Plan
```markdown
1. Load feature spec from specs/{id}-{slug}/spec.md
2. Load .specify/templates/plan-template.md
3. Follow plan template execution flow (Phase 0-2)
4. Generate: research.md, data-model.md, contracts/, quickstart.md
5. Run validation scripts on all artifacts
6. Update this file with recent changes
```

### /tasks - Create Task Breakdown
```markdown
1. Load plan.md and design artifacts
2. Load .specify/templates/tasks-template.md
3. Generate ordered task list (TDD: tests before implementation)
4. Create tasks.md with task dependencies
5. Validate task numbering and structure
```

### /implement - Execute Task
```markdown
1. Read tasks.md for next pending task
2. Implement following TDD principles
3. Run tests to verify implementation
4. Update task status in tasks.md
5. Run validation and quality checks
6. Report completion to user
```

---

## Validation Instructions

### Running Validation Scripts

```bash
# After creating/modifying artifacts, run appropriate validation:

# Structure validation
bash .specify/scripts/bash/validate-structure.sh specs/003-based-on-the/

# Naming validation
bash .specify/scripts/bash/validate-naming.sh specs/003-based-on-the/

# Frontmatter validation
bash .specify/scripts/bash/validate-frontmatter.sh specs/003-based-on-the/spec.md

# Or use CLI wrapper (detects platform automatically)
specify check specs/003-based-on-the/
```

### Interpreting Validation Output

Parse output lines matching pattern: `\[(INFO|WARN|ERROR)\] (.+)`

- **[INFO]**: Validation passed, informational message
- **[WARN]**: Potential issue, non-critical, report to user
- **[ERROR]**: Critical issue, recommend fix to user

**Important**: All scripts exit with code 0 (non-blocking). Report findings to user and ask for decision.

### Example Agent Response
```markdown
Validation complete for specs/003-based-on-the/spec.md

Results:
- Structure: PASS (0 errors, 0 warnings)
- Naming: PASS (0 errors, 0 warnings)
- Frontmatter: PASS (0 errors, 1 warning)

Warning: Missing optional field 'version' in frontmatter

Recommendation: Add version field for better tracking, or proceed without it.
This warning is non-blocking.

Would you like me to add the version field?
```

---

## Quality Tool Integration

### Detecting and Running Quality Tools

```bash
# JavaScript/TypeScript projects
if [ -f "package.json" ]; then
  npm run lint 2>/dev/null || npx eslint . --format compact
  npx prettier --check . 2>/dev/null
fi

# Python projects
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
  pylint src/ --output-format=parseable 2>/dev/null
  flake8 src/ 2>/dev/null
fi

# Or use CLI wrapper
specify check --quality
```

### Reporting Quality Findings

```markdown
Quality validation complete:

Critical Issues (2):
1. specify-cli/cli.py:45 - Unused variable 'temp' (remove)
2. specify-cli/validators.py:78 - Line too long (92 > 80 chars)

Warnings (8):
- Mostly formatting and style issues

Recommendation:
- Fix critical issues before committing
- Address warnings in next refactoring session

Would you like me to fix these issues automatically?
```

**Note**: Quality checks are non-blocking. Exit code 0 even with issues found.

---

## Brownfield Analysis (Agent-Augmented)

### Multi-Pass Analysis Process

When analyzing existing projects, follow this template-guided approach:

#### Pass 1: Initial Scan
```markdown
Tasks:
1. Identify package manager files (package.json, requirements.txt, pom.xml)
2. Detect language and framework from dependencies
3. Scan folder structure (depth 2-3 levels)
4. Count files by type (.js, .py, .java, etc.)
5. Check git history (age, commit count, contributors)

Tools:
- Use file/folder expansion in context window
- Parse JSON/YAML dependency files
- Run: git log --oneline | wc -l (for commit count)
```

#### Pass 2: Online Research
```markdown
Tasks:
1. Search: "{framework} latest version 2025"
2. Search: "{framework} project structure best practices"
3. Read official documentation for recommended patterns
4. Research: "{framework} migration guide" if version outdated

Tools:
- Use internet search (Tavily MCP, web search tools)
- Read official docs, not blog posts when possible
- Focus on latest stable versions
```

#### Pass 3: Validation
```markdown
Compare findings:
1. Current version vs latest version
2. Project structure vs official recommendations
3. Dependencies: check for outdated/vulnerable packages
4. Identify missing standard directories or configs

Confidence Levels:
- High (95%+): Direct parsing of package files
- Medium (70-90%): Pattern matching in code structure
- Low (<70%): Assumptions requiring manual verification
```

#### Pass 4: Report
```markdown
# Brownfield Analysis Report

## Technology Stack (High Confidence)
- Language: [detected]
- Framework: [name] [version]
- Build Tool: [tool]

## Architecture Pattern (Medium/High Confidence)
- Pattern: [MVC, microservices, etc.]
- Structure: [standard, non-standard, custom]

## Recommendations (Prioritized)
1. Critical: [must address]
2. High: [should address soon]
3. Medium: [consider for improvement]
4. Low: [nice to have]

## Confidence Levels
- Technology Detection: [%]
- Architecture Pattern: [%]
- Recommendations: [%]

Would you like me to proceed with these recommendations?
```

**Template Location**: `.specify/templates/brownfield-analysis.md`

---

## Architecture Patterns (Framework-Specific)

### Using Starter Patterns

Load `.specify/templates/architecture-patterns.md` for framework examples:

**Tier 1 Frameworks** (starter patterns included):
- React/Next.js
- Django/FastAPI
- Spring Boot

**Tier 2+ Frameworks** (research-based):
- Vue.js, Angular, Flask, Express, Laravel
- Research official docs for latest patterns

### Research and Validation Process

```markdown
1. Check template for starter pattern
   - If exists: Use as baseline

2. Research official documentation
   - Query: "{framework} {version} project structure official"
   - Read: Official docs (not tutorials)

3. Validate pattern against docs
   - Compare folder structure
   - Check naming conventions
   - Verify latest best practices

4. Report findings
   - Template pattern: [correct/outdated/partial]
   - Recommended structure: [with reasoning]
   - Official references: [links]
```

**Example for Next.js 14**:
```markdown
Framework: Next.js 14.0.3
Template Pattern: Partially outdated (shows Pages Router)

Validation:
✓ App Router (app/ directory) - correct for v14
✗ Pages Router (pages/ directory) - legacy pattern
✓ API routes in app/api/ - correct

Recommendation: Use App Router exclusively (Next.js 13+)
Reference: https://nextjs.org/docs/app/building-your-application/routing
```

---

## Artifact Management

### Naming Conventions (Script-Enforced)

**Feature Folders**: `{id}-{slug}/`
- ID: 3-digit zero-padded (001, 002, ..., 042)
- Slug: lowercase-with-hyphens

**Examples**:
- ✅ `specs/003-based-on-the/`
- ✅ `specs/001-improve-spec-kit/`
- ❌ `specs/3-feature/` (ID not padded)
- ❌ `specs/Feature-Name/` (uppercase)

**Artifact Files**: `spec.md`, `plan.md`, `tasks.md`, `research.md`, `data-model.md`, `quickstart.md`

### YAML Frontmatter (Required)

```yaml
---
feature_id: 3
created: 2025-09-30
status: draft
parent_spec: ./spec.md  # For plan.md and tasks.md
---
```

**Required Fields**: `feature_id`, `created`, `status`  
**Optional Fields**: `parent_spec`, `version`, `branch`

### Validation at Integration Points

```markdown
After creating artifact:
1. Run appropriate validation script
2. Parse output for [INFO], [WARN], [ERROR]
3. Report findings to user
4. Ask: "Would you like me to fix issues or proceed?"
5. Implement user's decision
```

---

## Recent Changes

### 2025-09-30: Feature 003 Planning Complete
- ✅ Phase 0: research.md with 9 key technical decisions
- ✅ Phase 1: data-model.md (10 core entities), contracts (3 contracts), quickstart.md (10 scenarios)
- ✅ Constitutional alignment validated (7 principles)
- Ready for Phase 2: /tasks command to generate task breakdown

### Technology Stack
- Language: Python 3.9+
- CLI Framework: Click
- Dependencies: stdlib, requests, PyYAML, click (minimal)
- Templates: Markdown with YAML frontmatter
- Scripts: Bash (Unix) + PowerShell (Windows)

### Key Constraints
- CLI: <400 LOC total
- No analysis engines (removed from original spec-kit)
- Performance: <3s init, <1s validation
- Non-blocking: All validation exit code 0

---

## Development Workflow

### Creating a New Feature
```markdown
1. User provides feature description
2. Run /specify to generate spec.md
3. Clarify ambiguities with user (use [NEEDS CLARIFICATION] markers)
4. Run /plan to generate plan.md and design artifacts
5. Run /tasks to generate tasks.md
6. Run /implement for each task (TDD: test → implement → refactor)
```

### Before Committing
```markdown
1. Run: specify check --quality
2. Review validation output
3. Fix critical issues (errors)
4. User decides on warnings
5. Commit with clean validation report
```

### Updating This File
```markdown
After completing plan.md:
1. Add entry to Recent Changes section (keep last 3)
2. Update Technology Stack if dependencies changed
3. Update Key Constraints if requirements evolved
4. Keep file under 150 lines for token efficiency
```

---

## Platform-Specific Optimizations (Windsurf)

### IDE Integration
- Use Windsurf's terminal for script execution
- Leverage code editor for artifact creation
- Utilize file navigation for template loading

### Context Management
- Keep templates in view when filling them
- Reference data-model.md for entity structures
- Use contracts/ for test-driven development

### Workflow Automation
- Windsurf workflows can chain commands:
  ```
  /specify → /plan → /tasks → /implement
  ```

---

## Quick Reference

### File Locations
- Templates: `.specify/templates/`
- Scripts: `.specify/scripts/{bash,powershell}/`
- Specs: `specs/{id}-{slug}/`
- Config: `.specify/config.yaml`

### Command Summary
- `specify init` - Initialize project
- `specify check` - Run validations
- `specify check --quality` - Include quality tools
- `specify check --update-templates` - Check for template updates

### Validation Scripts
- `validate-structure.sh` - Check folder/file structure
- `validate-naming.sh` - Check naming conventions
- `validate-frontmatter.sh` - Parse and validate YAML

### Exit Codes (Always 0)
All validation scripts use non-blocking exit code 0. Issues reported via [WARN] and [ERROR] messages, not exit codes.

---

**Last Updated**: 2025-09-30 (Feature 003 planning phase complete)  
**Next Action**: Run /tasks command to generate task breakdown from plan artifacts
