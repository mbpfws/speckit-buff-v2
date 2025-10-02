---
description: Migrate workflows/templates/scripts between AI coding platforms
scripts:
  sh: scripts/bash/migrate-platform.sh --from {SOURCE} --to {TARGET}
  ps: scripts/powershell/migrate-platform.ps1 -From {SOURCE} -To {TARGET}
orchestration:
  pre_conditions: ["source_platform_exists"]
  post_conditions: ["target_platform_configured", "state_preserved"]
  next: "validate"
supported_platforms: ["claude", "windsurf", "cursor", "roo"]  # MVP platforms
---

# Platform Migration Workflow

**Purpose**: Copy workflows/templates/scripts between AI coding platforms  
**Supported**: Claude Code, Windsurf, Roo Code, Cursor (MVP)

## Workflow Execution

### 1. Detect Current Platform

```bash
# Auto-detect or use --from flag
if [[ -d ".windsurf" ]]; then
    SOURCE="windsurf"
elif [[ -d ".claude" ]]; then
    SOURCE="claude"
elif [[ -d ".cursor" ]]; then
    SOURCE="cursor"
elif [[ -d ".roo" ]]; then
    SOURCE="roo"
fi
```

### 2. Execute Migration Script

```bash
.specify/scripts/bash/migrate-platform.sh \
    --from $SOURCE \
    --to $TARGET \
    --json

# Output: {status, files_copied, references_updated, state_preserved}
```

### 3. Copy Files

**Source → Target mapping**:
```
.specify/workflows/*.md  → .{target}/commands/*.md
.specify/templates/*.md  → .{target}/templates/*.md (if platform-specific)
.specify/scripts/        → .{target}/scripts/ (symlink or copy)
```

**Platform-specific files**:
- Claude Code: `.claude/CLAUDE.md`
- Windsurf: `.windsurf/rules/specify-rules.md`
- Cursor: `.cursor/CURSOR.md`
- Roo Code: `.roo/ROO.md`

### 4. Update Platform References

**Find and replace**:
- Workflow trigger syntax (e.g., `/specify` vs `@specify`)
- Script execution patterns (terminal vs embedded)
- Platform-specific tool references (MCP servers, etc.)

### 5. Preserve Workflow State

**Copy `.specify/context.json`** (unchanged):
- Current feature_id
- Workflow progress
- Complexity level
- Research findings

**DO NOT modify**:
- Feature directories (specs/*)
- Source code
- Git history

## Platform-Specific Adjustments

### Claude Code
- Workflow trigger: `/specify`, `/plan`, `/tasks`
- MCP tools: Available
- Script execution: Via terminal or embedded

### Windsurf
- Workflow trigger: `/specify`, `/plan`, `/tasks`
- Script execution: Native terminal integration
- Rules file: `.windsurf/rules/specify-rules.md`

### Cursor
- Workflow trigger: `@specify`, `@plan`, `@tasks`
- IDE integration: Full context awareness
- Agent file: `.cursor/CURSOR.md`

### Roo Code
- Workflow trigger: `/specify`, `/plan`, `/tasks`
- Command execution: Native support
- Agent file: `.roo/ROO.md`

## Validation

After migration, verify:
```bash
# Check target platform folder exists
ls -la .{target}/

# Verify workflow files copied
ls .{target}/commands/

# Test workflow execution
/{target-workflow-trigger} --help
```

## Output

Migration report:
```json
{
  "status": "success",
  "source_platform": "windsurf",
  "target_platform": "cursor",
  "files_copied": 15,
  "references_updated": 8,
  "state_preserved": true,
  "validation": {
    "workflows": "ok",
    "templates": "ok",
    "scripts": "ok",
    "context": "preserved"
  }
}
```

## Agent Instructions

**Preserve User Work**:
- Never delete source platform files
- Keep `.specify/` folder intact
- Maintain git history
- Preserve context.json state

**User Confirmation**:
- Show migration plan before executing
- Ask confirmation for file operations
- Provide rollback instructions if needed

**Example**:
```
📋 Migration Plan: Windsurf → Cursor

Will copy:
- 6 workflow files (.windsurf/commands → .cursor/commands)
- 8 template files (shared, no copy needed)
- Scripts (symlink to .specify/scripts)

Will update:
- Workflow triggers (/ → @)
- 8 platform references

Will preserve:
- .specify/context.json (unchanged)
- All feature directories
- Git history

Proceed? [Y/n]
```
