# ✅ FINAL CORRECT USAGE

## The Issue

**You typed**:
```bash
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify-cli init --here --ai roo
                                                                      ^^^^^^^^^^^
                                                                      WRONG - this is the package name
```

**Error**:
```
An executable named `specify-cli` is not provided by package `specify-cli`.
The following executables are available:
- specify.exe
```

---

## The Solution

### ✅ CORRECT Command

```bash
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai roo
                                                                      ^^^^^^^
                                                                      CORRECT - this is the executable name
```

---

## Why This Happens

In `pyproject.toml`:
```toml
[project]
name = "specify-cli"          # Package name (for pip/uv install)

[project.scripts]
specify = "specify_cli:main"  # Executable name (what you run)
```

- **Package name** (`specify-cli`): Used for installation
- **Executable name** (`specify`): Used for running commands

---

## All Correct Commands

### One-Time Usage (uvx)

```bash
# Initialize in new directory
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init my-project --ai roo

# Initialize in current directory
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai roo

# With different platforms
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai claude
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai windsurf
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai cursor
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai copilot
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai gemini
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai qwen
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai opencode
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai codex
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai kilocode
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai auggie
```

### Global Installation (uv tool)

```bash
# Install once (note: package name is specify-cli)
uv tool install specify-cli --from git+https://github.com/mbpfws/speckit-buff-v2.git

# Then use 'specify' command (note: executable name is specify)
specify init my-project --ai roo
specify init --here --ai claude
specify check
```

---

## What Gets Installed

When you run the command, the fork will:

1. **Create `.specify/` directory** with:
   - 13 templates (8 enhanced + 5 new)
   - 26 scripts (bash + PowerShell pairs)
   - config.yaml

2. **Create platform directory** (e.g., `.roo/commands/`) with:
   - specify.md - `/specify` workflow
   - plan.md - `/plan` workflow
   - tasks.md - `/tasks` workflow
   - analyze-brownfield.md - `/analyze-brownfield` workflow (NEW)
   - validate-governance.md - `/validate-governance` workflow (NEW)
   - migrate-platform.md - `/migrate-platform` workflow (NEW)

3. **Create memory/** with:
   - constitution.md (v2.1.1 with 14 principles)

4. **Create specs/** directory for your specifications

5. **Initialize git** (unless --no-git)

---

## Available Commands After Init

### Original Commands
```bash
/specify "Feature description"  # Create specification
/plan                           # Generate implementation plan
/tasks                          # Create task breakdown
/implement                      # Execute implementation
```

### Enhanced Commands (NEW in Fork)
```bash
/analyze-brownfield    # 4-pass brownfield analysis
/validate-governance   # Check tags and metadata
/migrate-platform      # Migrate between AI platforms
```

### CLI Commands
```bash
specify check --all           # Run all checks
specify check --tags          # Validate code tags
specify check --dependencies  # Check for vulnerabilities
specify check --tasks         # Sync task tracking
```

---

## Summary

**Package name**: `specify-cli` (for installation)  
**Executable name**: `specify` (for running)  

**ALWAYS use `specify` in uvx commands, NOT `specify-cli`**

✅ **CORRECT**: `uvx --from ... specify init --here --ai roo`  
❌ **WRONG**: `uvx --from ... specify-cli init --here --ai roo`

---

**Status**: ✅ All files are correct  
**README**: ✅ Updated with correct usage  
**Ready to use**: ✅ YES
