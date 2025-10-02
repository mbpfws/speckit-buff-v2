# Enhancements to Original specify-cli.py

Based on your original script, here are the specific additions needed to implement our v2.2 features:

---

## 1. Update Repository Constants (Line 58)

**REPLACE**:
```python
# Constants
AI_CHOICES = {
```

**WITH**:
```python
# Constants
# UPDATED: Your GitHub repo
REPO_OWNER = "your-github-username"  # TODO: Replace with your GitHub username
REPO_NAME = "spec-kit"               # TODO: Replace with your repo name

AI_CHOICES = {
```

---

## 2. Add Platform Workflow Directory Mapping (After AI_CHOICES, around line 74)

**ADD**:
```python
# ENHANCED: Platform directory mapping for workflow installation
PLATFORM_WORKFLOW_DIRS = {
    "claude": ".claude/commands",
    "windsurf": ".windsurf/workflows",
    "cursor": ".cursor/commands",
    "copilot": ".github/copilot/commands",
    "roo": ".roo/commands",
    "gemini": ".gemini/commands",
    "qwen": ".qwen/commands",
    "opencode": ".opencode/commands",
    "codex": ".codex/prompts",
    "kilocode": ".kilocode/commands",
    "auggie": ".augment/commands",
}
```

---

## 3. Update Tagline (Line 93)

**REPLACE**:
```python
TAGLINE = "GitHub Spec Kit - Spec-Driven Development Toolkit"
```

**WITH**:
```python
TAGLINE = "Spec-Kit v2.2 - Conversational Spec-Driven Development"
```

---

## 4. Update download_template_from_github Function (Line 388)

**REPLACE**:
```python
def download_template_from_github(...):
    repo_owner = "github"
    repo_name = "spec-kit"
```

**WITH**:
```python
def download_template_from_github(...):
    # UPDATED: Use configured repo
    repo_owner = REPO_OWNER
    repo_name = REPO_NAME
```

---

## 5. Add New Helper Functions (Add before @app.command() for init)

**ADD THESE THREE FUNCTIONS**:

```python
def setup_platform_workflows(project_path: Path, ai_assistant: str, tracker: StepTracker | None = None) -> None:
    """Copy workflow commands to platform-specific directory."""
    if ai_assistant not in PLATFORM_WORKFLOW_DIRS:
        return
    
    workflow_dir = PLATFORM_WORKFLOW_DIRS[ai_assistant]
    platform_path = project_path / workflow_dir
    
    # Source workflows from .specify/templates/commands/
    source_workflows = project_path / ".specify" / "templates" / "commands"
    
    if not source_workflows.exists():
        if tracker:
            tracker.skip("platform-setup", f"no workflows in .specify/templates/commands")
        return
    
    try:
        if tracker:
            tracker.start("platform-setup", f"copying to {workflow_dir}")
        
        # Create platform directory
        platform_path.mkdir(parents=True, exist_ok=True)
        
        # Copy all .md workflow files
        workflow_count = 0
        for workflow_file in source_workflows.glob("*.md"):
            dest_file = platform_path / workflow_file.name
            shutil.copy2(workflow_file, dest_file)
            workflow_count += 1
        
        if tracker:
            tracker.complete("platform-setup", f"{workflow_count} workflows → {workflow_dir}")
    except Exception as e:
        if tracker:
            tracker.error("platform-setup", str(e))
        else:
            console.print(f"[yellow]Warning: Could not setup platform workflows: {e}[/yellow]")


def initialize_context_file(project_path: Path, tracker: StepTracker | None = None) -> None:
    """Create initial .specify/context.json for workflow state tracking."""
    context_file = project_path / ".specify" / "context.json"
    
    initial_context = {
        "version": "2.2.0",
        "initialized": True,
        "complexity_analyzed": False,
        "spec_created": False,
        "clarifications_recorded": False,
        "plan_generated": False,
        "tasks_generated": False,
        "research_complete": False
    }
    
    try:
        if tracker:
            tracker.start("context-init", "creating context.json")
        
        context_file.parent.mkdir(parents=True, exist_ok=True)
        with open(context_file, 'w') as f:
            json.dump(initial_context, f, indent=2)
        
        if tracker:
            tracker.complete("context-init", "workflow state initialized")
    except Exception as e:
        if tracker:
            tracker.error("context-init", str(e))


def create_readme_with_instructions(project_path: Path, ai_assistant: str, tracker: StepTracker | None = None) -> None:
    """Create README.md with platform-specific instructions."""
    readme_path = project_path / "README.md"
    
    # Check if README already exists (from template)
    if readme_path.exists():
        if tracker:
            tracker.skip("readme", "already exists from template")
        return
    
    workflow_dir = PLATFORM_WORKFLOW_DIRS.get(ai_assistant, ".specify/templates/commands")
    
    readme_content = f"""# Spec-Kit Project

**AI Platform**: {AI_CHOICES[ai_assistant]}  
**Workflows**: `{workflow_dir}/`

## Quick Start

### Option 1: Slash Commands (Automatic)

If your AI platform supports slash commands:

```bash
/{workflow_dir.split('/')[0].replace('.', '')} /specify "your feature description"
```

Example workflows:
- `/specify` - Create feature specification (conversational)
- `/clarify` - Ask clarifying questions
- `/plan` - Generate implementation plan with research
- `/tasks` - Break down into actionable tasks
- `/analyze` - Validate artifacts
- `/implement` - Execute implementation

### Option 2: Manual Chat (Works Everywhere)

In your AI chat:

```
"Follow .specify/templates/commands/specify.md to help me create a specification"
```

The agent will read the workflow and execute it conversationally.

## Conversational Workflows

All workflows are conversational (v2.2):
1. **Present understanding** - Agent shows what it understood
2. **Ask permission for research** - Complex features trigger research
3. **Show research findings** - Present sources before using
4. **Ask clarifying questions** - 3-5 targeted questions
5. **Preview spec** - Show what will be created
6. **Wait for approval** - User confirms before files are created

## Directory Structure

```
.specify/
├── templates/          # Markdown templates
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   └── commands/       # Workflow definitions
├── scripts/            # Helper + validation scripts
│   ├── bash/
│   └── powershell/
├── memory/
│   └── constitution.md # Governance principles
└── context.json        # Workflow state

{workflow_dir}/    # Platform-specific workflows
└── [workflows copied from .specify/templates/commands/]

specs/                  # Feature specifications
└── [created by workflows]
```

## Constitution

This project follows 11 governance principles defined in:
`.specify/memory/constitution.md`

Key principles:
- **Conversational**: Iterative, research-driven
- **Complexity-aware**: Auto-detects technical depth
- **Research-first**: Web search for current info
- **Template-driven**: Consistent structure
- **Non-blocking**: User decides, agent advises

## Next Steps

1. Review constitution: `cat .specify/memory/constitution.md`
2. Start specifying: Run `/specify` or chat with AI
3. Follow workflows: Each step is conversational

---

**Version**: 2.2.0  
**Repo**: {REPO_OWNER}/{REPO_NAME}
"""
    
    try:
        if tracker:
            tracker.start("readme", "creating README.md")
        
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        if tracker:
            tracker.complete("readme", "instructions added")
    except Exception as e:
        if tracker:
            tracker.error("readme", str(e))
```

---

## 6. Add Tracker Steps in init() Function

After line with `tracker.add("chmod", "Ensure scripts executable")`, **ADD**:

```python
tracker.add("platform-setup", "Setup platform workflows")
tracker.add("context-init", "Initialize workflow context")
tracker.add("readme", "Create README with instructions")
```

---

## 7. Call New Functions in init() (in the try block with Live)

After the `ensure_executable_scripts()` call, **ADD**:

```python
            # ENHANCED: Setup platform-specific workflows
            setup_platform_workflows(project_path, selected_ai, tracker=tracker)
            
            # ENHANCED: Initialize context file
            initialize_context_file(project_path, tracker=tracker)
            
            # ENHANCED: Create README with instructions
            create_readme_with_instructions(project_path, selected_ai, tracker=tracker)
```

---

## 8. Update Final Instructions Panel (around line 850)

**ADD after the enhancement commands panel**:

```python
    # ENHANCED: Platform-specific usage examples
    usage_examples = []
    if selected_ai == "claude":
        usage_examples.append("○ Run: [cyan]claude /specify \"your feature\"[/cyan]")
        usage_examples.append("○ Chat: [bright_black]\"Follow .claude/commands/specify.md...\"[/bright_black]")
    elif selected_ai == "windsurf":
        usage_examples.append("○ Run: [cyan]/specify \"your feature\"[/cyan]")
        usage_examples.append("○ Chat: [bright_black]\"Follow .windsurf/workflows/specify.md...\"[/bright_black]")
    else:
        workflow_dir = PLATFORM_WORKFLOW_DIRS.get(selected_ai, ".specify/templates/commands")
        usage_examples.append(f"○ Workflows: [cyan]{workflow_dir}/[/cyan]")
        usage_examples.append("○ Chat: [bright_black]\"Follow the workflow files...\"[/bright_black]")
    
    if usage_examples:
        examples_panel = Panel(
            "\n".join(["[bold]Usage Examples[/bold]", ""] + usage_examples),
            border_style="green",
            padding=(1, 2)
        )
        console.print()
        console.print(examples_panel)
```

---

## Summary of Changes

1. ✅ Repository configuration (your GitHub repo)
2. ✅ Platform workflow directory mapping
3. ✅ Updated tagline
4. ✅ Setup platform-specific workflows (`.claude/`, `.windsurf/`, etc.)
5. ✅ Initialize `context.json` for workflow state
6. ✅ Create README with platform-specific instructions
7. ✅ Enhanced final output with usage examples

---

## Testing

After making these changes:

```bash
# Test the enhanced CLI
python specify-cli.py init test-project --ai claude

# Check results
cd test-project
ls -la .claude/commands/    # Should have workflows
cat .specify/context.json   # Should exist
cat README.md              # Should have instructions
```

---

## TODO

1. Replace `REPO_OWNER` and `REPO_NAME` with your actual GitHub username and repo
2. Test with all platforms
3. Update your GitHub releases to include templates with:
   - All workflows in `.specify/templates/commands/`
   - All scripts in `.specify/scripts/bash/` and `.specify/scripts/powershell/`
   - Constitution in `.specify/memory/constitution.md`
4. Package and publish

---

**All enhancements maintain the original script's structure and UI!**
