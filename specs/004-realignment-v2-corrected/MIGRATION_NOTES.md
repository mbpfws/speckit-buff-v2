# Migration Notes: 003 → 004

**Date**: 2025-09-30  
**Branch**: 004-realignment-v2-corrected  
**Status**: Foundation Fixed, Ready for Workflows

## What Was Fixed

### 1. Template Architecture ✅
**Problem**: Created templates directly in `.specify/` (user space) instead of `templates/` (source)

**Solution**:
- Created proper SOURCE templates in `templates/`:
  - ✅ `templates/spec-template.md` (updated with v2.0 frontmatter)
  - ✅ `templates/plan-template.md` (updated with v2.0 guidance)
  - ✅ `templates/tasks-template.md` (updated with v2.0 guidance)
  - ✅ `templates/constitution.md` (NEW - 7 principles)
  - ✅ `templates/brownfield-analysis.md` (NEW - 4-pass workflow)
  - ✅ `templates/architecture-patterns.md` (NEW - 10+ frameworks)
  - ✅ `templates/agent-file-template.md` (existing)

- Updated `specify_cli/commands/init.py`:
  - ✅ Copy templates from `templates/` → `.specify/templates/`
  - ✅ Create `.specify/memory/` for constitution
  - ✅ Copy constitution from source to `.specify/memory/constitution.md`

### 2. Workflow Commands ✅
**Problem**: Workflows referenced wrong paths (`/templates/` vs `.specify/templates/`)

**Solution**: Updated `templates/commands/`:
- ✅ `/plan` now references `.specify/templates/plan-template.md`
- ✅ `/plan` now loads `.specify/memory/constitution.md`
- ✅ `/tasks` now references `.specify/templates/tasks-template.md`
- ✅ `/analyze` now references `.specify/memory/constitution.md`

### 3. Spec Migration ✅
**Problem**: `specs/003-based-on-the/` created with wrong understanding

**Solution**:
- ✅ Created `specs/004-realignment-v2-corrected/`
- ✅ Migrated valid content (requirements, scenarios, acceptance criteria)
- ✅ Added proper v2.0 YAML frontmatter
- ✅ Updated for corrected template/workflow architecture
- ✅ Documented migration path and changes

## What's Valid from 003

### ✅ Can Migrate
- **spec.md**: Requirements and scenarios are valid
- **Contracts** (cli-init.yaml, cli-check.yaml, validation-api.yaml): API definitions valid
- **Tests**: Contract and integration tests valid (51/66 passing)
- **Core CLI**: Implementation valid (224 LOC < 400 target)

### ⚠️ Needs Regeneration
- **plan.md**: Must regenerate with corrected workflow
- **tasks.md**: Must regenerate with corrected template
- **research.md**: May need updates for v2.0 additions
- **data-model.md**: May need validation
- **quickstart.md**: May need scenario updates
- **WINDSURF.md**: Needs path corrections

## The Corrected Architecture

```
Package (source):
├── templates/                    # SOURCE templates
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   ├── constitution.md          # NEW v2.0
│   ├── brownfield-analysis.md   # NEW v2.0
│   ├── architecture-patterns.md # NEW v2.0
│   └── agent-file-template.md
├── templates/commands/           # Workflow definitions
│   ├── specify.md
│   ├── clarify.md
│   ├── plan.md                  # FIXED paths
│   ├── tasks.md                 # FIXED paths
│   ├── analyze.md               # FIXED paths
│   └── implement.md
└── specify_cli/                  # CLI implementation
    ├── __init__.py
    ├── cli.py
    ├── commands/
    │   ├── init.py              # FIXED: copies templates
    │   └── check.py
    ├── template_loader.py
    └── validators.py

User Project (after init):
└── .specify/                     # USER space
    ├── templates/                # Copied from source
    │   ├── spec-template.md
    │   ├── plan-template.md
    │   ├── tasks-template.md
    │   ├── constitution.md       # v2.0
    │   ├── brownfield-analysis.md
    │   ├── architecture-patterns.md
    │   └── agent-file-template.md
    ├── memory/                   # NEW v2.0
    │   └── constitution.md
    ├── scripts/
    │   ├── bash/
    │   └── powershell/
    └── config.yaml
```

## Next Steps

### Ready Now ✅
1. **`specify init`** - Works correctly, copies templates
2. **Template System** - Properly structured
3. **Workflows** - Reference correct paths
4. **CLI Implementation** - 224 LOC, under budget

### To Complete 🎯
1. **`/clarify`** - Run on `specs/004-realignment-v2-corrected/spec.md`
2. **`/plan`** - Generate plan.md with corrected workflow
3. **`/tasks`** - Generate tasks.md with corrected template
4. **Phase 3.5** - Create validation scripts (bash + PowerShell)
5. **Phase 3.6** - Integration & documentation
6. **Phase 3.7** - QA & validation

## Testing Status

**Current**: 51/66 tests passing (77%)

**Passing**:
- ✅ Init command (8/8)
- ✅ Check command (9/10)
- ✅ Greenfield workflow (3/3)
- ✅ Multi-platform (4/4)
- ✅ Offline usage (5/5)
- ✅ Backward compatibility (6/6)

**Failing** (Need Phase 3.5 - Validation Scripts):
- ⚠️ Validation script execution (need actual scripts)
- ⚠️ Template-driven tests (need Phase 3.4 complete)

## Key Improvements in 004

1. **Proper Template Architecture**: Source vs user space separation
2. **Constitution Integration**: 7 principles in `.specify/memory/`
3. **Enhanced Templates**: Brownfield analysis, architecture patterns
4. **Fixed Workflow Paths**: All commands reference correct locations
5. **Agent Guidance**: HTML comments in all templates
6. **Version Tracking**: YAML frontmatter with version info

## Commands to Run

```bash
# Verify init works
specify init
ls .specify/templates/    # Should show 7 templates
ls .specify/memory/       # Should show constitution.md

# Run workflows on new spec
cd specs/004-realignment-v2-corrected/
# User runs: /clarify
# User runs: /plan  
# User runs: /tasks
```

## Success Criteria

- [x] Templates in `templates/` (source)
- [x] Init copies to `.specify/templates/` (user)
- [x] Constitution in `.specify/memory/`
- [x] Workflows reference `.specify/` paths
- [x] Spec migrated with v2.0 format
- [ ] /clarify identifies ambiguities
- [ ] /plan generates with constitution check
- [ ] /tasks uses corrected template
- [ ] All tests pass (target: 66/66)

---

**Ready for user to run `/clarify`, `/plan`, `/tasks` with the corrected v2.0 system!**
