# Spec-Kit v2.2 - Complete Architecture Overview

**Date**: 2025-09-30  
**Status**: Production Ready

---

## System Architecture

### The Three-Tier System

```
┌─────────────────────────────────────────────────────────────┐
│                  1. CLI (Python Entry Point)                 │
│              specify_cli/__init__.py (1,248 LOC)             │
│  - Repository: MikeBirdTech/spec-kit                         │
│  - Commands: init, check                                      │
│  - Platform detection & workflow setup                        │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ copies on init
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              2. Templates (Markdown Guidance)                │
│         templates/ + templates/commands/ (15 files)          │
│  - Spec, plan, tasks templates                               │
│  - Workflow commands (8 workflows)                           │
│  - Architecture patterns & constitution                      │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ executed by agents
                           ↓
┌─────────────────────────────────────────────────────────────┐
│           3. Scripts (Validation & Helpers)                  │
│        scripts/bash/ + scripts/powershell/ (20 files)        │
│  - Validation: structure, naming, frontmatter                │
│  - Helpers: prerequisites, planning, feature creation        │
│  - Orchestration: workflow coordination, complexity          │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Breakdown

### 1. CLI Layer (`specify_cli/__init__.py`)

**Purpose**: Bootstrap and validate projects

**Key Features**:
- **Repository Configuration** (Lines 69-70):
  ```python
  REPO_OWNER = "MikeBirdTech"
  REPO_NAME = "spec-kit"
  ```

- **Platform Support** (Lines 89-101):
  ```python
  PLATFORM_WORKFLOW_DIRS = {
      "claude": ".claude/commands",
      "windsurf": ".windsurf/workflows",
      "cursor": ".cursor/commands",
      # ... 8 more platforms
  }
  ```

- **Commands**:
  - `specify init` - Initialize project with templates + scripts + workflows
  - `specify check` - Validate tool installation

**Initialization Flow**:
```
specify init <project> --ai windsurf
  ↓
1. Download templates from GitHub (MikeBirdTech/spec-kit)
2. Extract to .specify/templates/
3. Copy scripts to .specify/scripts/
4. Make bash scripts executable (Unix)
5. Copy workflows to .windsurf/workflows/  ← NEW in v2.2
6. Create .specify/context.json            ← NEW in v2.2
7. Initialize git repo (optional)
8. Display next steps with workflow info    ← NEW in v2.2
```

---

### 2. Template Layer (`templates/`)

#### 2.1 Core Templates (7 files)

| File | Purpose | Used By | Size |
|------|---------|---------|------|
| `spec-template.md` | Feature specification | `/specify` | ~200 LOC |
| `plan-template.md` | Implementation plan | `/plan` | ~150 LOC |
| `tasks-template.md` | Task breakdown | `/tasks` | ~100 LOC |
| `constitution.md` | Project principles | `/constitution` | ~80 LOC |
| `brownfield-analysis.md` | Legacy code analysis | `/specify` (brownfield) | ~120 LOC |
| `architecture-patterns.md` | Framework patterns | `/plan` (reference) | ~200 LOC |
| `agent-file-template.md` | Agent context file | `/plan` Phase 1 | ~80 LOC |

#### 2.2 Workflow Commands (`templates/commands/`)

| Workflow | Purpose | Calls Scripts | Output |
|----------|---------|---------------|--------|
| `specify.md` | Create feature spec | `create-new-feature.sh` | `specs/{id}-{slug}/spec.md` |
| `clarify.md` | Ask clarification questions | `check-prerequisites.sh` | Updates spec.md |
| `plan.md` | Generate implementation plan | `setup-plan.sh` | `plan.md`, `research.md`, `data-model.md` |
| `tasks.md` | Create task breakdown | `check-prerequisites.sh` | `tasks.md` |
| `analyze.md` | Cross-artifact analysis | `check-prerequisites.sh` | Consistency report |
| `implement.md` | Execute implementation | `check-prerequisites.sh` | Code changes |
| `constitution.md` | Establish principles | (none) | `.specify/memory/constitution.md` |
| `research-tech.md` | Technical research | (none) | `research.md` |

**How Workflows Work**:
```markdown
# Example: specify.md workflow

$ARGUMENTS (user input: "Add user authentication")

1. Run: .specify/scripts/bash/create-new-feature.sh --json "$ARGUMENTS"
2. Parse JSON: BRANCH_NAME, SPEC_FILE, FEATURE_DIR
3. Load: .specify/templates/spec-template.md
4. Fill template with user description
5. Create: specs/005-add-user-authentication/spec.md
6. Report completion to user
```

---

### 3. Script Layer (`scripts/`)

#### 3.1 Validation Scripts (6 files - 3 bash + 3 PowerShell)

**Purpose**: Non-blocking quality checks

| Script | Validates | Exit Code | Output Format |
|--------|-----------|-----------|---------------|
| `validate-structure.sh/.ps1` | Directory structure, .specify/ exists | 0 (always) | `[INFO]`, `[WARN]`, `[ERROR]` |
| `validate-naming.sh/.ps1` | File naming (kebab-case, no spaces) | 0 (always) | `[INFO]`, `[WARN]`, `[ERROR]` |
| `validate-frontmatter.sh/.ps1` | YAML frontmatter presence & fields | 0 (always) | `[INFO]`, `[WARN]`, `[ERROR]` |

**Called By**: `specify check` command

**Example Output**:
```
[INFO] Validating project structure...
[INFO] ✓ .specify/ directory exists
[WARN] specs/003-old-feature/ missing plan.md
[ERROR] specs/004-current/spec.md has invalid frontmatter
[INFO] Validation complete (1 error, 1 warning)
```

#### 3.2 Helper Scripts (12 files - 6 bash + 6 PowerShell)

**Purpose**: Provide structured JSON data to workflows

| Script | Flags | Output (JSON) | Used By Workflow |
|--------|-------|---------------|------------------|
| `check-prerequisites.sh/.ps1` | `--json`, `--require-tasks`, `--include-tasks` | REPO_ROOT, BRANCH, FEATURE_DIR, FEATURE_SPEC, IMPL_PLAN, TASKS, AVAILABLE_DOCS | `/clarify`, `/tasks`, `/analyze`, `/implement` |
| `setup-plan.sh/.ps1` | `--json` | REPO_ROOT, BRANCH, FEATURE_SPEC, IMPL_PLAN, SPECS_DIR | `/plan` |
| `create-new-feature.sh/.ps1` | `--json` | REPO_ROOT, BRANCH_NAME, SPEC_FILE, FEATURE_DIR | `/specify` |
| `update-agent-context.sh/.ps1` | (agent type) | (no JSON, updates WINDSURF.md/CLAUDE.md) | `/plan` Phase 1 |
| `detect-complexity.sh/.ps1` | `--json` | COMPLEXITY_LEVEL, INDICATORS, RECOMMENDATIONS | (auto-detection) |
| `orchestrate-workflow.sh/.ps1` | `--json` | CURRENT_STEP, NEXT_STEPS, WORKFLOW_STATE | (workflow coordination) |

**Example: check-prerequisites.sh**
```bash
#!/bin/bash
# When called with --json flag

# Output:
{
  "REPO_ROOT": "/absolute/path/to/repo",
  "BRANCH": "004-realignment-v2-corrected",
  "FEATURE_DIR": "/absolute/path/to/repo/specs/004-realignment-v2-corrected",
  "FEATURE_SPEC": "/absolute/path/to/repo/specs/004-realignment-v2-corrected/spec.md",
  "IMPL_PLAN": "/absolute/path/to/repo/specs/004-realignment-v2-corrected/plan.md",
  "TASKS": "/absolute/path/to/repo/specs/004-realignment-v2-corrected/tasks.md",
  "AVAILABLE_DOCS": ["spec.md", "plan.md", "research.md", "data-model.md", "tasks.md"]
}
```

#### 3.3 Common Utilities (2 files)

| Script | Purpose | Exports |
|--------|---------|---------|
| `common.sh` | Shared bash functions | `find_repo_root()`, `get_current_branch()`, `normalize_path()` |
| `common.ps1` | Shared PowerShell functions | `Find-RepoRoot`, `Get-CurrentBranch`, `Normalize-Path` |

**Used By**: All other scripts for consistency

---

## Integration: How It All Works Together

### Scenario 1: Agent Uses `/specify` Workflow

**User Action**:
```
Agent: "Hey, I need to add user authentication"
User: "@/specify Add user authentication with JWT tokens"
```

**Behind the Scenes**:
```
1. Agent reads .windsurf/workflows/specify.md
   ↓
2. Workflow instructs agent to run:
   .specify/scripts/bash/create-new-feature.sh --json "Add user authentication with JWT tokens"
   ↓
3. Script creates:
   - Git branch: 005-add-user-authentication
   - Directory: specs/005-add-user-authentication/
   - File: specs/005-add-user-authentication/spec.md (from template)
   ↓
4. Script returns JSON:
   {
     "BRANCH_NAME": "005-add-user-authentication",
     "SPEC_FILE": "/path/to/specs/005-add-user-authentication/spec.md",
     "FEATURE_DIR": "/path/to/specs/005-add-user-authentication"
   }
   ↓
5. Agent parses JSON, loads spec-template.md
   ↓
6. Agent fills template with user description
   ↓
7. Agent writes completed spec to SPEC_FILE
   ↓
8. Agent reports to user: "✅ Created spec at specs/005-add-user-authentication/spec.md"
```

### Scenario 2: Agent Uses `/plan` Workflow

**User Action**:
```
User: "@/plan Generate implementation plan for feature 005"
```

**Behind the Scenes**:
```
1. Agent reads .windsurf/workflows/plan.md
   ↓
2. Workflow instructs: Run setup-plan.sh --json
   ↓
3. Script verifies spec.md exists, returns paths
   ↓
4. Workflow instructs: Load .specify/memory/constitution.md
   ↓
5. Agent evaluates 7 constitutional principles
   ↓
6. Workflow instructs: Phase 0 - Create research.md (use web search)
   ↓
7. Agent researches 5 technical areas, writes research.md
   ↓
8. Workflow instructs: Phase 1 - Create data-model.md, contracts/
   ↓
9. Agent generates design artifacts
   ↓
10. Workflow instructs: Phase 2 - Describe task generation approach
   ↓
11. Agent writes plan.md with approach (DON'T create tasks.md yet)
   ↓
12. Agent reports: "✅ Implementation plan complete. Run /tasks next."
```

### Scenario 3: Agent Uses `/implement` Workflow

**User Action**:
```
User: "@/implement Execute the implementation plan"
```

**Behind the Scenes**:
```
1. Agent reads .windsurf/workflows/implement.md
   ↓
2. Workflow instructs: Run check-prerequisites.sh --json --require-tasks --include-tasks
   ↓
3. Script returns:
   {
     "FEATURE_DIR": "/path/to/specs/005-...",
     "AVAILABLE_DOCS": ["spec.md", "plan.md", "tasks.md", ...],
     "TASKS": [
       {"id": "T001", "description": "Setup", "status": "pending"},
       {"id": "T002", "description": "Tests", "status": "pending"},
       ...
     ]
   }
   ↓
4. Agent loads tasks.md, parses task list
   ↓
5. For each task:
   a. Execute task (write code, create files, run tests)
   b. Mark task complete: [x] in tasks.md
   c. Report progress to user
   ↓
6. Agent reports: "✅ Implementation complete (T001-T050 done)"
```

---

## File Distribution: `specify init` Creates

### In Project Root
```
your-project/
├── .windsurf/workflows/        ← Platform workflows (v2.2)
│   ├── specify.md
│   ├── clarify.md
│   ├── plan.md
│   ├── tasks.md
│   ├── implement.md
│   ├── analyze.md
│   ├── constitution.md
│   └── research-tech.md
├── .specify/
│   ├── templates/              ← 7 core templates
│   │   ├── spec-template.md
│   │   ├── plan-template.md
│   │   ├── tasks-template.md
│   │   ├── constitution.md
│   │   ├── brownfield-analysis.md
│   │   ├── architecture-patterns.md
│   │   ├── agent-file-template.md
│   │   └── commands/           ← 8 workflow commands (source)
│   │       ├── (same 8 files as .windsurf/workflows/)
│   ├── scripts/                ← 20 scripts
│   │   ├── bash/               ← 10 bash scripts
│   │   │   ├── check-prerequisites.sh (executable)
│   │   │   ├── common.sh
│   │   │   ├── create-new-feature.sh
│   │   │   ├── detect-complexity.sh
│   │   │   ├── orchestrate-workflow.sh
│   │   │   ├── setup-plan.sh
│   │   │   ├── update-agent-context.sh
│   │   │   ├── validate-frontmatter.sh
│   │   │   ├── validate-naming.sh
│   │   │   └── validate-structure.sh
│   │   └── powershell/         ← 10 PowerShell scripts
│   │       ├── (same 10 files as bash, .ps1 extension)
│   ├── memory/                 ← Constitution copy (v2.2)
│   │   └── constitution.md
│   ├── context.json            ← Workflow state tracking (v2.2)
│   └── config.yaml             ← User configuration
├── specs/                      ← Feature specifications (created by workflows)
│   └── (empty initially)
└── .gitignore                  ← Standard ignores
```

---

## Context Tracking (v2.2 Feature)

### `.specify/context.json`
```json
{
  "version": "2.2.0",
  "initialized": true,
  "complexity_analyzed": false,    // After /detect-complexity
  "spec_created": false,           // After /specify
  "clarifications_recorded": false, // After /clarify
  "plan_generated": false,         // After /plan
  "tasks_generated": false,        // After /tasks
  "research_complete": false       // After /research-tech
}
```

**Purpose**: 
- Track workflow progression across sessions
- Enable agents to understand project state
- Allow workflows to check prerequisites
- Support conversational development flow

**Updated By**: 
- Agents during workflow execution
- Workflows can read to determine next steps

---

## Platform Support

### 11 Supported AI Platforms

| Platform | Workflow Dir | Format | Notes |
|----------|--------------|--------|-------|
| **Windsurf** | `.windsurf/workflows/` | Markdown | ✅ Default recommended |
| **Claude Code** | `.claude/commands/` | Markdown | Official Anthropic |
| **Cursor** | `.cursor/commands/` | Markdown | Popular editor |
| **GitHub Copilot** | `.github/copilot/commands/` | Markdown | GitHub native |
| **Roo Code** | `.roo/commands/` | Markdown | Emerging platform |
| **Gemini CLI** | `.gemini/commands/` | Markdown | Google |
| **Qwen Code** | `.qwen/commands/` | Markdown | Alibaba |
| **opencode** | `.opencode/commands/` | Markdown | Open source |
| **Codex CLI** | `.codex/prompts/` | Markdown | OpenAI |
| **Kilo Code** | `.kilocode/commands/` | Markdown | Emerging |
| **Auggie CLI** | `.augment/commands/` | Markdown | Augment Code |

**How It Works**:
1. User runs: `specify init project --ai windsurf`
2. CLI copies workflows from `.specify/templates/commands/` to `.windsurf/workflows/`
3. Agent can now use: `/specify`, `/plan`, `/tasks`, etc.
4. Workflows are markdown files that agent reads and executes

---

## Cross-Platform Script Parity

### Bash vs PowerShell

**Requirement**: Both must produce **identical JSON output**

**Example: check-prerequisites.sh vs check-prerequisites.ps1**

**Bash**:
```bash
#!/bin/bash
REPO_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
BRANCH=$(git rev-parse --abbrev-ref HEAD)
printf '{"REPO_ROOT":"%s","BRANCH":"%s"}\n' "$REPO_ROOT" "$BRANCH"
```

**PowerShell**:
```powershell
$RepoRoot = (Get-Location).Path -replace '\\', '/'
$Branch = git rev-parse --abbrev-ref HEAD
@{REPO_ROOT=$RepoRoot; BRANCH=$Branch} | ConvertTo-Json -Compress
```

**Both Output**:
```json
{"REPO_ROOT":"/absolute/path","BRANCH":"main"}
```

**Key Practices**:
- Forward slashes for paths (Windows accepts them)
- UPPER_SNAKE_CASE for JSON keys
- Absolute paths only
- Exit code 0 (non-blocking)

---

## The 10 Scripts Integrated with v2.2 CLI

### How Scripts Are Used

1. **During Init** (`specify init`):
   ```python
   # CLI copies scripts to .specify/scripts/
   # Makes bash scripts executable (chmod +x on Unix)
   # Creates context.json for state tracking
   # Copies workflows to platform directory
   ```

2. **During Workflows** (Agent execution):
   ```
   Agent reads: .windsurf/workflows/specify.md
   Workflow says: "Run .specify/scripts/bash/create-new-feature.sh --json"
   Agent executes script, gets JSON back
   Agent uses JSON to fill templates and create files
   Agent updates context.json with progress
   ```

3. **During Validation** (`specify check`):
   ```python
   # CLI runs validate-*.sh scripts
   # Displays warnings/errors to user
   # User decides what to fix (non-blocking)
   ```

### Scripts Added to v2.2 CLI Integration

**In `specify_cli/__init__.py` (lines 1112-1116)**:
```python
# Ensure scripts are executable (POSIX)
ensure_executable_scripts(project_path, tracker=tracker)

# Setup platform-specific workflows ← Uses PLATFORM_WORKFLOW_DIRS
setup_platform_workflows(project_path, selected_ai, tracker=tracker)

# Initialize context.json for workflow state tracking ← Creates context.json
initialize_context_file(project_path, tracker=tracker)
```

**Result**: 
- Scripts copied to `.specify/scripts/`
- Workflows copied to `.windsurf/workflows/` (or platform equivalent)
- Context tracking enabled for conversational flow
- Agent can now execute workflows that call scripts

---

## Summary: The Orchestration

```
User: "I want to add a feature"
  ↓
Agent: Reads .windsurf/workflows/specify.md
  ↓
Workflow: Instructs agent to run create-new-feature.sh
  ↓
Script: Creates spec directory, returns JSON paths
  ↓
Agent: Loads spec-template.md, fills it, saves to disk
  ↓
Agent: Updates .specify/context.json (spec_created: true)
  ↓
Agent: "✅ Feature spec created. Next: /clarify or /plan"
```

**The Magic**:
- **CLI** = Setup & distribution
- **Templates** = Structure & guidance
- **Scripts** = Data & automation
- **Workflows** = Orchestration & instructions
- **Context** = State & continuity

**Result**: Conversational, spec-driven development that agents understand and users control.

---

## Testing the Integration

```bash
# 1. Initialize with Windsurf
uvx specify_cli/__init__.py init my-project --ai windsurf

# 2. Verify files created
cd my-project
ls .windsurf/workflows/        # Should have 8 workflow .md files
ls .specify/scripts/bash/      # Should have 10 .sh files (executable)
ls .specify/scripts/powershell/ # Should have 10 .ps1 files
cat .specify/context.json      # Should have v2.2.0 structure

# 3. Test a workflow
# In Windsurf agent: "@/specify Add user authentication"
# Agent will:
#   - Read .windsurf/workflows/specify.md
#   - Run .specify/scripts/bash/create-new-feature.sh
#   - Create specs/001-add-user-authentication/spec.md
#   - Update .specify/context.json
```

---

**Architecture Status**: ✅ Complete & Production Ready  
**Integration Status**: ✅ All components working together  
**Platform Support**: ✅ 11 AI coding assistants  
**Script Parity**: ✅ Bash & PowerShell identical output  
**State Tracking**: ✅ context.json conversational flow
