# Project Constitutional Principles

**Version**: 2.1.1  
**Last Updated**: 2025-09-30  
**Purpose**: Define the governing principles for this project's development approach

<!-- 
AGENT GUIDANCE:
These principles guide ALL development decisions. When creating plans or implementing features:
1. Evaluate each principle for the current work
2. Document any deviations in plan.md Complexity Tracking
3. Provide clear justification for any principle violations
4. Seek simpler alternatives before accepting complexity
-->

---

## The Seven Constitutional Principles

### 1. Cross-Platform Compatibility ✅

**Principle**: Support all 10 major AI coding platforms with consistent behavior across Windows, macOS, and Linux.

**Supported Platforms**:
- **Tier 1** (Full Integration): Claude Code, Roo Code
- **Tier 2** (Core Features): GitHub Copilot, Cursor, Gemini CLI
- **Tier 3** (Basic Support): Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI

**Evaluation Criteria**:
- ✅ Templates work identically on all platforms
- ✅ Validation scripts available in bash (Unix) and PowerShell (Windows)
- ✅ CLI commands produce consistent output across OSes
- ✅ No platform-specific features required for core functionality

**Violation Example**: Feature requires Windows-only API or macOS-only framework
**Justification Required**: Demonstrate no cross-platform alternative exists

---

### 2. Multi-Installation Support ✅

**Principle**: Work seamlessly with both persistent (`uv tool`) and one-time (`uvx`) installation methods.

**Installation Methods**:
1. **PATH Installation**: `uv tool install specify-cli` (persistent)
2. **One-time Execution**: `uvx specify-cli init` (no installation)

**Evaluation Criteria**:
- ✅ CLI works identically with both methods
- ✅ Templates accessible in both scenarios
- ✅ No installation-specific configuration required
- ✅ Cache location consistent across methods

**Violation Example**: Feature requires persistent state between invocations
**Justification Required**: Explain why state cannot be stored in `.specify/`

---

### 3. Template-Driven Consistency ✅

**Principle**: High-quality markdown templates as the core system—agents fill templates, not write from scratch.

**Template Philosophy**:
- Templates are self-contained with embedded agent guidance
- Agents augment templates with research and domain knowledge
- Templates provide structure, agents provide intelligence
- No template should assume agent memorizes formats

**Evaluation Criteria**:
- ✅ New features have corresponding templates
- ✅ Agent guidance embedded in HTML comments
- ✅ Examples and patterns provided within templates
- ✅ Templates updated based on agent feedback

**Violation Example**: Feature requires agents to remember complex formats
**Justification Required**: Show why format cannot be templated

---

### 4. Agent-Native Execution ✅

**Principle**: AI agents remain the primary actors. The system augments capabilities, never replaces agent intelligence.

**Agent-First Design**:
- Agents read templates and create artifacts
- Agents perform research using online resources
- Agents validate using provided scripts
- Agents make final decisions based on findings

**Evaluation Criteria**:
- ✅ System provides tools, agents use intelligence
- ✅ No automated analysis engines
- ✅ Agents explicitly run validation, not automated
- ✅ Human-readable output for user decision-making

**Violation Example**: Automated code analysis without agent involvement
**Justification Required**: Demonstrate agents cannot perform the analysis

---

### 5. Simplicity Principle ✅

**Principle**: Minimal tooling overhead with zero complex analysis engines.

**Simplicity Targets**:
- **CLI**: <400 lines of code total
- **Dependencies**: Only 4 (stdlib, requests, PyYAML, click)
- **Commands**: Only 2 (init, check)
- **Analysis Engines**: Zero

**Evaluation Criteria**:
- ✅ Total CLI LOC stays under 400
- ✅ No new heavy dependencies (no ML, no AST parsers, no compilers)
- ✅ New features use templates + scripts, not engines
- ✅ Low cyclomatic complexity (<10 per function)

**Violation Example**: Adding dependency with >1000 LOC or AST analysis engine
**Justification Required**: Prove no simpler alternative exists

---

### 6. Governance Balance ✅

**Principle**: Non-blocking validation that preserves user autonomy.

**Governance Philosophy**:
- Scripts provide warnings, not errors (exit code 0)
- Agents report findings to users
- Users make final decisions
- Validation guides, never blocks

**Evaluation Criteria**:
- ✅ Validation scripts exit 0 (non-blocking)
- ✅ Clear severity levels ([INFO], [WARN], [ERROR])
- ✅ Agents explain findings before user acts
- ✅ Users can override recommendations

**Violation Example**: Validation that prevents users from proceeding
**Justification Required**: Explain why blocking is absolutely necessary

---

### 7. Backward Compatibility ✅

**Principle**: Existing v1.x projects work without modification. Clear migration path provided.

**Compatibility Requirements**:
- V1.x frontmatter format supported
- V1.x folder structure works
- V1.x artifacts validate successfully
- Optional migration to v2.x enhancements

**Evaluation Criteria**:
- ✅ V1.x specs validate without changes
- ✅ V1.x folder patterns recognized
- ✅ No forced breaking changes
- ✅ Migration guide available

**Violation Example**: Required v2.x-only frontmatter fields
**Justification Required**: Show why backward compatibility impossible

---

## Using This Constitution

### During Feature Planning (/plan)

1. **Load this constitution**: Read all 7 principles
2. **Evaluate each principle**: Check if feature aligns
3. **Document violations**: Use Complexity Tracking table in plan.md
4. **Justify or simplify**: Either justify violation or simplify approach
5. **Re-check after design**: Ensure Phase 1 design still complies

### During Implementation (/implement)

1. **Reference during development**: Keep principles in mind
2. **Validate before committing**: Run `specify check`
3. **Document deviations**: Explain any principle compromises
4. **Seek simplification**: Always look for simpler alternatives

### During Code Review

1. **Check LOC count**: Ensure CLI stays under 400 LOC
2. **Verify dependencies**: Ensure only essential deps added
3. **Test cross-platform**: Verify on Windows + Unix
4. **Validate templates**: Ensure agent guidance clear

---

## Amendment Process

This constitution can be amended when:

1. **Evidence accumulates**: Multiple features blocked by same principle
2. **User feedback**: Clear user need contradicts principle
3. **Technical evolution**: Platform changes require adaptation
4. **Team consensus**: All stakeholders agree on amendment

**Amendment Procedure**:
1. Document proposed change
2. Explain why current principle insufficient
3. Show alternatives considered
4. Update version number
5. Communicate to all developers

---

## References

- **Spec-Kit v2.0 Specification**: `specs/003-based-on-the/spec.md`
- **Research Documentation**: `specs/003-based-on-the/research.md`
- **Implementation Plan**: `specs/003-based-on-the/plan.md`

---

*This constitution guides all development. When in doubt, choose simplicity.*
