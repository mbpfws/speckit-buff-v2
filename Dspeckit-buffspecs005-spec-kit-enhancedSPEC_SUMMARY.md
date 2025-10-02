# Spec-Kit Enhanced Fork v2.0 - Executive Summary

## Core Changes (32 Files Modified/Created)

### Sector 1: Commands (6 new/modified)
- `/specify`: Add --level flag for complexity tiers
- `/plan`: Use architecture-meta-template (research-driven)
- `/tasks`: Add YAML metadata (files_affected, task_id, test_required)
- `/analyze-brownfield`: NEW - 4-pass analysis workflow
- `/validate-governance`: NEW - Check tags/metadata
- `/migrate-platform`: NEW - Cross-platform file copying

### Sector 2: Templates (8 new)
- brownfield-analysis.md (4-pass checklist)
- agent-prompt-patterns.md (CoVe, Step-Back, Citations)
- dependency-report.md (npm audit template)
- testing-strategy.md (realistic E2E guidelines)
- architecture-meta-template.md (research workflow)
- Enhanced: spec/plan/tasks templates with conditional sections

### Sector 3: Scripts (20+ new bash/PowerShell pairs)
- analyze-codebase.sh (tech stack detection → JSON)
- sync-tasks.sh (validate YAML ↔ code tags ↔ git)
- validate-tags.sh (scan TODO/FIXME/HACK/TASK-XXX)
- inject-tags.sh (auto-add with confirmation)
- check-dependencies.sh (npm audit/pip check)
- detect-breaking-changes.sh (changelog parsing)
- detect-framework.sh (Next.js/Django/etc)
- scaffold-feature.sh (boilerplate by tier)
- extract-section.sh (parse large docs)
- migrate-platform.sh (copy .windsurf → .cursor)
- track-file-rename.sh, mark-file-deprecated.sh, build-task-graph.sh

### Sector 4: Governance (AGENTS.md + constitution.md)
- AGENTS.md: Add 4 platform sections (Claude/Windsurf/Roo/Cursor)
- AGENTS.md: Brownfield guidance, self-regulation patterns, tag rules
- constitution.md: 3 new principles (Self-Regulation, Brownfield Support, Context Management)

### Sector 5: CLI (specify_cli/__init__.py)
- `specify init`: Download from GitHub, detect platform, copy to .specify/ + platform folder
- `specify check`: Add --tags, --dependencies, --tasks flags

## Key Research Findings Applied

1. **Brownfield**: 4-pass analysis (Document → Analyze → Integrate → Risk) with confidence levels
2. **Context Management**: "According to..." prompting reduces hallucinations 30%
3. **Dependencies**: npm audit + changelog parsing for breaking changes
4. **Next.js 2025**: Route groups, private folders, server/client boundary
5. **TDD**: Realistic E2E for extended stories, skip trivial code

## User Decisions (10 Questions)

1. Brownfield: Both template + scripts
2. Task Tracking: YAML + in-code tags + validation script
3. Architecture: Meta-template with research (no embedded patterns)
4. Tags: All three (validation + injection + templates)
5. Self-Regulation: User confirmation loops
6. Migration: Copy workflow files to platform folders
7. Testing: Realistic E2E covering extended stories
8. Governance: Enforce but allow flexibility
9. Context: Frontmatter indexes + section tags
10. Scaffolding: Complexity tiers with helper scripts

## Implementation Constraints

- ✅ Preserve <400 LOC CLI (only modify init/check)
- ✅ NO new Python analysis engines
- ✅ Only templates, scripts, workflows
- ✅ Support 4 platforms: Claude, Windsurf, Roo Code, Cursor
- ✅ Download from: https://github.com/mbpfws/speckit-buff-v2/
- ✅ No duplicate files (modify existing or remove-before-create)
