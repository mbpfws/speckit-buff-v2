# Quickstart: Spec-Kit Enhanced Fork v2.0

**Feature**: 005-spec-kit-enhanced  
**Prerequisites**: Git, Python 3.9+, bash or PowerShell  
**Platforms**: Claude Code, Windsurf, Roo Code, Cursor  
**Time to Complete**: 5 minutes

---

## Installation & Setup

### Option 1: Clone Repository (Development)

```bash
# Clone the enhanced spec-kit fork
git clone https://github.com/mbpfws/speckit-buff-v2.git
cd speckit-buff-v2

# Install CLI
uv tool install -e .

# Initialize in your project
cd /path/to/your/project
specify init

# Verify installation
specify check
```

### Option 2: Direct Install (Production)

```bash
# One-line install from GitHub
uv tool install git+https://github.com/mbpfws/speckit-buff-v2.git

# Initialize in project
cd /path/to/your/project
specify init --platform windsurf  # Or: claude, roo, cursor

# Verify
specify check
```

### Option 3: One-Time Use (uvx)

```bash
# No installation required
cd /path/to/your/project
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init

# Each time you need it
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify check
```

---

## Quick Start Scenarios

### Scenario 1: New Greenfield Project

```bash
# 1. Initialize spec-kit
specify init --level intermediate

# 2. Create feature specification
/specify "Build user authentication system with JWT"

# 3. Clarify ambiguities
/clarify

# 4. Generate implementation plan
/plan

# 5. Create task breakdown
/tasks

# 6. Implement features
/implement
```

**Expected Output**:
- `.specify/` folder with templates and scripts
- `specs/001-user-authentication/spec.md`
- `specs/001-user-authentication/plan.md`
- `specs/001-user-authentication/tasks.md`
- Platform-specific file (`.windsurf/WINDSURF.md`, etc.)

---

### Scenario 2: Brownfield Project Analysis

```bash
# 1. Initialize spec-kit in existing project
cd /path/to/existing/nextjs-app
specify init

# 2. Analyze existing codebase
/analyze-brownfield

# Agent will:
# - Run analyze-codebase.sh (detect Next.js 15.x, dependencies)
# - Perform 4-pass analysis (Document → Analyze → Integrate → Risk)
# - Report findings with confidence levels (High/Med/Low)
# - Suggest architecture improvements

# 3. Validate architecture
/validate-governance

# 4. Generate migration plan
/specify "Migrate to App Router with server components"
/plan
```

**Expected Output**:
- Tech stack report with confidence levels
- Architecture deviations document
- Integration strategy
- Risk assessment with mitigation plans

---

### Scenario 3: Cross-Platform Migration

```bash
# Current platform: Windsurf
# Target platform: Cursor

# 1. Migrate workflows
/migrate-platform --from windsurf --to cursor

# Agent will:
# - Copy .specify/workflows/*.md → .cursor/
# - Copy .specify/templates/*.md → .cursor/
# - Copy .specify/scripts/ → .cursor/
# - Update platform-specific references
# - Preserve .specify/context.json state

# 2. Verify migration
specify check --platform cursor
```

**Expected Output**:
- `.cursor/` folder with all workflows
- Migration report JSON
- Updated CURSOR.md agent file

---

### Scenario 4: Task & File Tracking

```bash
# 1. Create feature with task tracking
/specify "Add payment processing with Stripe"
/plan
/tasks  # Generates tasks.md with YAML metadata

# 2. Implement task
# Edit: src/api/payments.ts
# Add comment: // TASK-T001: Stripe integration

# 3. Validate task sync
specify check --tasks

# Agent will:
# - Run sync-tasks.sh --validate
# - Cross-check: YAML task_id ↔ code tags ↔ git changes
# - Warn if misaligned

# 4. Track file rename
# Rename: src/api/payments.ts → src/api/stripe-payments.ts
# Run: track-file-rename.sh --old payments.ts --new stripe-payments.ts --task T001

# 5. Verify history
cat .specify/file-history.json
```

**Expected Output**:
- tasks.md with `files_affected: [src/api/payments.ts]`
- In-code tags validated
- File history tracking renames

---

### Scenario 5: Dependency Intelligence

```bash
# 1. Check for dependency issues
specify check --dependencies

# Agent will:
# - Run check-dependencies.sh (npm audit or pip check)
# - Run detect-breaking-changes.sh (parse CHANGELOGs)
# - Output JSON with vulnerabilities + peer conflicts + breaking changes

# 2. Review dependency report
cat specs/current-feature/dependency-report.md

# 3. Resolve conflicts
# Follow agent recommendations with source URLs
```

**Expected Output**:
- Vulnerability table (package, severity, fix available)
- Peer conflict table (current vs required versions)
- Breaking changes report (affected files, migration guides)

---

### Scenario 6: Complexity Tiers for Novices

```bash
# 1. Initialize for novice developer
specify init --level novice

# 2. Create feature
/specify "Create blog with comments"

# Agent will:
# - Use spec-template.md with novice conditional sections
# - Provide step-by-step explanations
# - Include learning resources for unfamiliar tech
# - Scaffold detailed boilerplate

# 3. Generate novice-friendly tasks
/tasks

# Tasks include:
# - Detailed substeps
# - Links to tutorials
# - Example code snippets
```

**Expected Output**:
- Spec with `<!-- IF tier=novice -->` sections expanded
- Tasks with educational context
- Scaffolded boilerplate code

---

## Validation Tests

### Test 1: Cross-Platform Script Parity

```bash
# Run on Windows PowerShell
.specify/scripts/powershell/analyze-codebase.ps1 --json > output-ps.json

# Run on Linux/macOS bash
.specify/scripts/bash/analyze-codebase.sh --json > output-sh.json

# Validate identical output
diff output-ps.json output-sh.json
# Expected: No differences
```

### Test 2: Template Tier Conditional Rendering

```bash
# Novice tier
specify init --level novice
grep "<!-- IF tier=novice -->" .specify/templates/spec-template.md
# Expected: Sections expanded with explanations

# Expert tier
specify init --level expert
grep "<!-- IF tier=expert -->" .specify/templates/spec-template.md
# Expected: Minimal guidance
```

### Test 3: Governance Validation

```bash
# Create spec without required metadata
echo "# Bad Spec" > specs/999-test/spec.md

# Run validation
/validate-governance

# Expected warnings:
# - [ERROR] Missing feature_id in frontmatter
# - [ERROR] Missing artifact_id for spec.md
# - [WARN] No parent_spec reference
```

---

## Troubleshooting

### Issue: "Script not found"

**Cause**: Scripts not copied during init  
**Solution**:
```bash
specify init --force  # Re-copy templates and scripts
```

### Issue: "Platform detection failed"

**Cause**: Multiple platform folders exist (.windsurf/ + .cursor/)  
**Solution**:
```bash
specify init --platform cursor  # Explicit platform
```

### Issue: "Task sync validation failed"

**Cause**: File renamed without tracking  
**Solution**:
```bash
# Manually update file history
.specify/scripts/bash/track-file-rename.sh \
  --old src/old-file.ts \
  --new src/new-file.ts \
  --task T001
```

### Issue: "Dependency conflict resolution"

**Cause**: Peer dependency mismatch  
**Solution**:
```bash
# Review agent recommendations
specify check --dependencies

# Check dependency report
cat specs/current-feature/dependency-report.md

# Follow resolution options (use stable versions, avoid --force)
```

---

## Performance Benchmarks

**Target Performance** (from spec.md):
- `specify init`: <3s
- `specify check`: <1s
- Script execution: <500ms
- Template copy: <200ms

**Validation Commands**:
```bash
# Benchmark init
time specify init

# Benchmark check
time specify check

# Benchmark script
time .specify/scripts/bash/analyze-codebase.sh --json
```

---

## Next Steps

1. ✅ **Installation Complete** → Run `specify check` to verify
2. ✅ **Greenfield Project** → Use `/specify` to create first feature
3. ✅ **Brownfield Project** → Use `/analyze-brownfield` for existing codebase
4. ✅ **Platform Migration** → Use `/migrate-platform` if switching AI tools
5. ✅ **Task Tracking** → Use `specify check --tasks` to validate sync
6. ✅ **Dependency Intelligence** → Use `specify check --dependencies` for audits

**Documentation**: See [spec.md](./spec.md), [plan.md](./plan.md), [research.md](./research.md)

---

**Quickstart Complete** ✅  
You're ready to use the enhanced spec-kit fork!
