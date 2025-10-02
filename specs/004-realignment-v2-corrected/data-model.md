# Data Model: Spec-Kit Realignment Fork v2.0

**Date**: 2025-09-30  
**Phase**: Phase 1 Design  
**Branch**: 004-realignment-v2-corrected

## Entity Overview

The system has 4 primary entities extracted from the feature specification:

1. **Template System** - Core template distribution and management
2. **Script Library** - Validation and workflow helper scripts
3. **Workflow Definition** - Markdown-based agent workflows
4. **Project Configuration** - User project settings and state

---

## Entity: Template System

### Description
Manages markdown templates that agents use to create feature specifications, plans, and tasks. Templates are embedded in the package and optionally updated from GitHub Releases.

### Attributes

| Attribute | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| source_location | Path | Yes | Package `templates/` directory | Must exist in package |
| user_location | Path | Yes | `.specify/templates/` after init | Created on init |
| version | String | Yes | Semantic version (e.g., "2.0.0") | Stored in `.specify/.version` |
| template_files | List[String] | Yes | 7 template filenames | Must include essential templates |
| update_source | URL | No | GitHub Releases URL | Optional for offline mode |
| cache_location | Path | No | `~/.specify/cache/{version}/` | Created if updates downloaded |

### Template Files
1. `spec-template.md` - Feature specification
2. `plan-template.md` - Implementation plan
3. `tasks-template.md` - Task generation
4. `constitution.md` - Constitutional principles
5. `brownfield-analysis.md` - 4-pass analysis
6. `architecture-patterns.md` - Framework patterns
7. `agent-file-template.md` - Agent context

### Relationships
- **Contains**: 7 template markdown files
- **Versioned by**: Semantic version string
- **Cached in**: User cache directory
- **Copied to**: User `.specify/templates/` directory

### State Transitions
```
[Embedded in Package] 
  → (specify init) → 
[Copied to .specify/templates/]
  → (specify init --force) → 
[Updated from GitHub + Cached]
```

### Business Rules
- Essential templates (spec, plan, tasks, constitution) MUST always be present
- Optional templates (brownfield-analysis, architecture-patterns) can be excluded with `--minimal` flag
- Template version MUST match semantic versioning (MAJOR.MINOR.PATCH)
- Offline mode MUST work with embedded templates (no network required)
- User-modified templates in `.specify/` MUST NOT be overwritten unless `--force` flag used

---

## Entity: Script Library

### Description
Collection of bash and PowerShell scripts that provide validation and workflow support. Scripts MUST be cross-platform identical in behavior.

### Attributes

| Attribute | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| source_location | Path | Yes | Package `scripts/` directory | bash/ and powershell/ subdirs |
| user_location | Path | Yes | `.specify/scripts/` after init | Created on init |
| script_type | Enum | Yes | "validation" or "helper" | Determines usage pattern |
| platform | Enum | Yes | "bash" or "powershell" | Platform selection |
| json_contract | Dict | Conditional | Output schema | Required for helpers with `--json` |
| exit_code | Integer | Yes | Always 0 | Non-blocking principle |

### Script Types

#### Validation Scripts (3 total)
- `validate-structure.sh/.ps1` - Directory structure validation
- `validate-naming.sh/.ps1` - File naming conventions
- `validate-frontmatter.sh/.ps1` - YAML frontmatter validation

Output format: `[INFO]`, `[WARN]`, `[ERROR]` messages

#### Workflow Helper Scripts (6+ total)
- `check-prerequisites.sh/.ps1` - Get feature paths (JSON output)
- `setup-plan.sh/.ps1` - Initialize planning artifacts (JSON output)
- `create-new-feature.sh/.ps1` - Create feature branch (JSON output)
- `update-agent-context.sh/.ps1` - Update agent files
- Additional helpers as workflows require

### JSON Output Contracts

**check-prerequisites.sh**:
```json
{
  "REPO_ROOT": "/absolute/path",
  "BRANCH": "branch-name",
  "FEATURE_DIR": "/absolute/path/specs/feature",
  "FEATURE_SPEC": "/absolute/path/specs/feature/spec.md",
  "IMPL_PLAN": "/absolute/path/specs/feature/plan.md",
  "TASKS": "/absolute/path/specs/feature/tasks.md",
  "AVAILABLE_DOCS": ["spec.md", "plan.md", ...]
}
```

**setup-plan.sh**:
```json
{
  "REPO_ROOT": "/absolute/path",
  "BRANCH": "branch-name",
  "FEATURE_SPEC": "/absolute/path/specs/feature/spec.md",
  "IMPL_PLAN": "/absolute/path/specs/feature/plan.md",
  "SPECS_DIR": "/absolute/path/specs/feature"
}
```

**create-new-feature.sh**:
```json
{
  "REPO_ROOT": "/absolute/path",
  "BRANCH_NAME": "new-branch-name",
  "SPEC_FILE": "/absolute/path/specs/feature/spec.md",
  "FEATURE_DIR": "/absolute/path/specs/feature"
}
```

### Relationships
- **Executed by**: `specify check` command (validation scripts)
- **Referenced by**: Workflow definitions (helper scripts)
- **Outputs**: JSON for helpers, structured text for validation
- **Platform-paired**: Each bash script has PowerShell equivalent

### State Transitions
```
[Embedded in Package]
  → (specify init) →
[Copied to .specify/scripts/]
  → (specify check or workflow) →
[Executed with output parsed by agent]
```

### Business Rules
- Bash and PowerShell versions MUST produce identical output
- All scripts MUST exit with code 0 (non-blocking)
- JSON output MUST use forward slashes for paths (cross-platform)
- Helper scripts with `--json` flag MUST output valid JSON to stdout
- Validation scripts MUST use `[LEVEL]` prefix format
- Scripts MUST be executable after copying (chmod +x for bash)

---

## Entity: Workflow Definition

### Description
Markdown files with YAML frontmatter that define agent workflows. Agents read these files and execute the described steps.

### Attributes

| Attribute | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| file_location | Path | Yes | `templates/commands/{name}.md` | In package |
| description | String | Yes | Short workflow description | In YAML frontmatter |
| scripts | Dict | Yes | Platform-specific script paths | sh: bash path, ps: PS path |
| workflow_name | String | Yes | Command name (e.g., "plan") | Matches filename |
| execution_steps | List[String] | Yes | Numbered workflow steps | In markdown body |
| user_input | String | No | Arguments from user | Referenced as $ARGUMENTS |

### Workflow Files
1. `specify.md` - Create feature specification
2. `clarify.md` - Identify ambiguities  
3. `plan.md` - Generate implementation plan
4. `tasks.md` - Create task breakdown
5. `analyze.md` - Cross-artifact analysis
6. `implement.md` - Execute implementation
7. `constitution.md` - Constitution management

### YAML Frontmatter Schema
```yaml
description: "Workflow description"
scripts:
  sh: .specify/scripts/bash/script-name.sh --flags
  ps: .specify/scripts/powershell/script-name.ps1 -Flags
```

### Markdown Body Pattern
```markdown
User input: $ARGUMENTS

1. Run `{SCRIPT}` from repo root and parse JSON
2. Load required files
3. Execute workflow steps
4. Generate output artifacts
5. Report completion
```

### Relationships
- **References**: Helper scripts for execution
- **Reads**: Templates from `.specify/templates/`
- **Writes**: Artifacts to `specs/{feature}/`
- **Used by**: AI agents (not CLI commands)

### State Transitions
```
[Defined in templates/commands/]
  → (Agent reads workflow) →
[Agent parses YAML + markdown]
  → (Agent executes steps) →
[Artifacts created in specs/]
```

### Business Rules
- Workflow files are markdown, NOT Python CLI commands (preserves <400 LOC limit)
- Agents MUST substitute `{SCRIPT}` with platform-appropriate script path
- Workflows MUST reference `.specify/` paths (user space), not `templates/` (source)
- Workflows MUST output to `specs/{feature}/` directory
- User input accessed via `$ARGUMENTS` variable

---

## Entity: Project Configuration

### Description
User project settings and state stored in `.specify/` directory after initialization.

### Attributes

| Attribute | Type | Required | Description | Validation |
|-----------|------|----------|-------------|------------|
| config_file | Path | Yes | `.specify/config.yaml` | Created on init |
| version_file | Path | Yes | `.specify/.version` | Template version |
| template_source | URL | Yes | GitHub Releases URL | For updates |
| template_version | String | Yes | Current template version | Semantic version |
| validation_config | Dict | Yes | Validation settings | skip_checks, fail_on_error |
| quality_config | Dict | Yes | Quality tool settings | tools list, auto_fix |
| offline_mode | Boolean | Yes | Offline operation flag | Default: false |
| memory_location | Path | Yes | `.specify/memory/` directory | For constitution |

### Configuration Schema (config.yaml)
```yaml
template_source: "https://github.com/github/spec-kit/releases"
template_version: "2.0.0"
validation:
  skip_checks: []
  fail_on_error: false
quality:
  tools: []
  auto_fix: false
offline_mode: false
```

### Directory Structure
```
.specify/
├── config.yaml          # Configuration
├── .version             # Template version
├── templates/           # Copied templates (7 files)
├── scripts/             # Copied scripts (~18 files)
│   ├── bash/            # Unix scripts
│   └── powershell/      # Windows scripts
└── memory/              # NEW v2.0
    └── constitution.md  # Constitution copy
```

### Relationships
- **Contains**: Templates, scripts, configuration
- **Created by**: `specify init` command
- **Read by**: `specify check` command and workflows
- **Modified by**: User (config.yaml customization)

### State Transitions
```
[No .specify/ directory]
  → (specify init) →
[.specify/ created with defaults]
  → (user customization) →
[.specify/ with user settings]
  → (specify init --force) →
[.specify/ updated with new templates]
```

### Business Rules
- `.specify/` directory MUST NOT be committed to version control (user-local)
- `config.yaml` can be customized by users after init
- Templates in `.specify/templates/` can be modified by users
- Scripts in `.specify/scripts/` should generally not be modified (cross-platform parity)
- `.specify/memory/constitution.md` is reference copy, source is in templates
- Version file `.specify/.version` tracks template version for update detection

---

## Entity Relationships Diagram

```
┌─────────────────────┐
│ Template System     │
│ (source)            │──────┐
└─────────────────────┘      │
                             │ copied on init
┌─────────────────────┐      │
│ Script Library      │      │
│ (source)            │──────┤
└─────────────────────┘      │
                             ↓
                    ┌─────────────────────┐
                    │ Project Config      │
                    │ (.specify/)         │
                    └─────────────────────┘
                             ↑
                             │ references
┌─────────────────────┐      │
│ Workflow Definition │──────┘
│ (commands/*.md)     │
└─────────────────────┘
         │
         │ reads/writes
         ↓
    specs/{feature}/
    (artifacts)
```

---

## Data Validation Rules

### Cross-Entity Validation
1. Template version in `config.yaml` MUST match `.specify/.version`
2. All workflow-referenced scripts MUST exist in `.specify/scripts/`
3. All workflow-referenced templates MUST exist in `.specify/templates/`
4. JSON output from helper scripts MUST match documented contracts

### Integrity Constraints
1. Cannot have `.specify/templates/` without `config.yaml`
2. Cannot execute workflows without `.specify/scripts/`
3. Cannot run validation without all 3 validation scripts present
4. bash and PowerShell script pairs MUST have matching filenames

---

## Migration Notes (003 → 004)

### Data Model Changes
1. **NEW Entity**: Script Library (scripts weren't modeled in 003)
2. **NEW Entity**: Workflow Definition (workflows weren't clarified in 003)
3. **Enhanced Entity**: Template System (added cache_location, update_source)
4. **Enhanced Entity**: Project Configuration (added memory/ directory)

### Key Clarifications
- Scripts are now first-class entities (not just "some validation scripts")
- Workflows are markdown files, not CLI commands (architectural clarity)
- JSON contracts standardized for all helper scripts
- Constitution gets its own storage location (`.specify/memory/`)

---

**Data model complete**. All entities, relationships, and business rules documented.
