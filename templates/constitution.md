# Project Constitutional Principles

**Version**: 2.1.1  
**Last Updated**: 2025-09-30  
**Purpose**: Define governing principles for this project's development

<!-- 
AGENT GUIDANCE:
Evaluate these principles for every feature. Document deviations in plan.md Complexity Tracking.
Constitution violations require justification or simplification.
-->

---

## The Seven Constitutional Principles

### 1. Cross-Platform Compatibility ✅
**Principle**: Support all 10 major AI coding platforms with consistent behavior.

**Platforms**: Claude Code, Roo Code, GitHub Copilot, Cursor, Gemini CLI, Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI

**Evaluation**:
- ✅ Templates work identically on all platforms
- ✅ Scripts available in bash (Unix) and PowerShell (Windows)
- ✅ CLI produces consistent output across OSes
- ✅ No platform-specific features for core functionality

### 2. Multi-Installation Support ✅
**Principle**: Work with both PATH (`uv tool`) and one-time (`uvx`) installation.

**Evaluation**:
- ✅ CLI works identically with both methods
- ✅ Templates accessible in both scenarios
- ✅ No persistent state required between invocations

### 3. Template-Driven Consistency ✅
**Principle**: High-quality markdown templates as core—agents fill, not create.

**Evaluation**:
- ✅ New features have corresponding templates
- ✅ Agent guidance embedded in HTML comments
- ✅ Examples and patterns provided

### 4. Agent-Native Execution ✅
**Principle**: AI agents are primary actors—system augments, never replaces.

**Evaluation**:
- ✅ System provides tools, agents use intelligence
- ✅ No automated analysis engines
- ✅ Agents explicitly run validation
- ✅ Human-readable output

### 5. Simplicity Principle ✅
**Principle**: Minimal tooling, zero complex engines.

**Targets**:
- CLI: <400 LOC
- Dependencies: Only 4 (stdlib, requests, PyYAML, click)
- Commands: Only 2 (init, check)
- Analysis Engines: Zero

### 6. Governance Balance ✅
**Principle**: Non-blocking validation preserving user autonomy.

**Evaluation**:
- ✅ Scripts exit 0 (non-blocking)
- ✅ Clear severity levels ([INFO], [WARN], [ERROR])
- ✅ Users make final decisions

### 7. Backward Compatibility ✅
**Principle**: V1.x projects work without modification.

**Evaluation**:
- ✅ V1.x frontmatter supported
- ✅ V1.x folder structure works
- ✅ No forced breaking changes

---

*See `.specify/templates/constitution.md` in your project for full documentation.*
