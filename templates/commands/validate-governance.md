---
description: Validate code tags, metadata completeness, and document relationships
scripts:
  sh: scripts/bash/validate-tags.sh --json
  ps: scripts/powershell/validate-tags.ps1 -Json
  validate_context: scripts/bash/validate-context.sh --json
  sync_tasks: scripts/bash/sync-tasks.sh --validate --json
orchestration:
  pre_conditions: ["tasks_exist"]
  auto_trigger: ["validate-all"]
  post_conditions: ["validation_complete"]
  severity_levels: ["CRITICAL", "MAJOR", "MINOR"]  # Non-blocking warnings
---

# Governance Validation Workflow

**Purpose**: Validate tags, metadata, and document relationships (non-blocking)  
**Philosophy**: Warn, don't block - user has final say

## Workflow Execution

### 1. Validate Code Tags

```bash
# Scan for missing/orphaned tags
.specify/scripts/bash/validate-tags.sh --json

# Output: {missing_task_tags, orphaned_todos, metadata_issues}
```

**Check for**:
- TODO/FIXME/HACK without TASK-XXX tags
- TASK-XXX tags referencing non-existent tasks
- Missing `// TASK-XXX:` comments in files_affected

### 2. Validate Metadata Completeness

```bash
# Check YAML frontmatter
.specify/scripts/bash/validate-context.sh --json

# Output: {valid, errors, warnings}
```

**Required fields**:
- spec.md: feature_id, status, created, version
- plan.md: feature_id, parent_spec
- tasks.md: feature_id, parent_spec, tasks array

### 3. Validate Document Relationships

**Check cross-references**:
- tasks.md `parent_spec` → spec.md exists
- plan.md `parent_spec` → spec.md exists
- Artifact files have `artifact_id: {feature_id}-{slug}`

### 4. Validate Task Synchronization

```bash
# Cross-check YAML ↔ code tags ↔ git
.specify/scripts/bash/sync-tasks.sh --validate --json

# Output: {misalignments, warnings}
```

**Checks**:
- YAML `files_affected` matches in-code `// TASK-XXX` tags
- Git changes have corresponding TASK tags
- No orphaned task references

## Severity Levels

**CRITICAL** (Block workflow):
- Circular task dependencies
- Missing required frontmatter fields
- Invalid parent references

**MAJOR** (Ask user confirmation):
- Files modified without TASK tags
- Orphaned TODO/FIXME comments
- Metadata inconsistencies

**MINOR** (Warn and continue):
- Style guide violations
- Optional field missing
- Suggested improvements

## Output Format

```json
{
  "status": "pass_with_warnings",
  "critical": [],
  "major": [
    "src/api/users.ts: modified but has no TASK tag"
  ],
  "minor": [
    "plan.md: missing optional 'complexity_level' field"
  ],
  "recommendations": [
    "Run: .specify/scripts/bash/inject-tags.sh --file src/api/users.ts --task T001"
  ]
}
```

## Agent Instructions

**Non-Blocking Philosophy**:
- CRITICAL issues: Pause and ask user how to proceed
- MAJOR issues: Present findings, ask for confirmation to continue
- MINOR issues: Show warnings, continue automatically

**User Autonomy**:
- Never auto-fix without permission
- Provide clear remediation commands
- Allow user to accept risks

**Example User Confirmation Loop**:
```
⚠️ MAJOR Issue Detected:
src/api/users.ts was modified but has no TASK tag.

Recommendation: Add TASK-T001 tag to track this change.

Options:
1. Add tag now (run inject-tags.sh)
2. Continue without tag (accept risk)
3. Cancel workflow

Your choice: [1/2/3]
```
