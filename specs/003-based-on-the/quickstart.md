# Quickstart Guide: Spec-Kit Realignment Fork

**Feature**: 003-based-on-the | **Date**: 2025-09-30 | **Purpose**: Validation & Integration Testing

## Overview

This quickstart guide provides step-by-step scenarios to validate the spec-kit fork implementation. Each scenario corresponds to acceptance criteria from the feature specification and serves as both user documentation and integration test specification.

---

## Scenario 1: Initialize New Greenfield Project

**Acceptance Criteria**: Given a new project, When I run the simplified CLI init command, Then it MUST download templates and set up structure within 3 seconds without deep analysis

### Prerequisites
- Python 3.9+ installed
- Internet connection (for initial setup)
- Empty project directory

### Steps

1. **Install CLI (persistent)**
   ```bash
   # Using uv tool for PATH installation
   uv tool install specify-cli
   
   # Verify installation
   specify --version
   # Expected: specify-cli version 2.0.0
   ```

2. **Alternative: One-time usage**
   ```bash
   # Using uvx for temporary execution
   uvx specify-cli init
   ```

3. **Initialize project**
   ```bash
   # Start timer
   time specify init
   
   # Expected output:
   # ✓ Templates downloaded (version v2.0.0)
   # ✓ Validation scripts installed
   # ✓ Configuration created
   # ✓ Project structure initialized
   #
   # Next steps:
   # 1. Run: specify /specify "your feature description"
   # 2. Or: Create spec manually in specs/001-feature-name/spec.md
   #
   # Execution time: < 3 seconds
   ```

4. **Verify structure created**
   ```bash
   ls -la
   # Expected directories:
   # .specify/
   # specs/
   
   ls -la .specify/
   # Expected:
   # templates/
   # scripts/
   # workflows/
   # config.yaml
   # .version
   
   ls -la .specify/templates/
   # Expected files:
   # spec-template.md
   # plan-template.md
   # tasks-template.md
   # constitution.md
   # brownfield-analysis.md
   # architecture-patterns.md
   ```

5. **Verify no analysis engines installed**
   ```bash
   # Check CLI size
   wc -l specify-cli/cli.py
   # Expected: < 400 lines total for all CLI code
   
   # Verify minimal dependencies
   cat pyproject.toml | grep dependencies
   # Expected: only stdlib, requests, PyYAML, click
   ```

### Success Criteria
- ✅ Init completes in < 3 seconds
- ✅ .specify/ directory created with templates and scripts
- ✅ specs/ directory created
- ✅ No analysis engines or complex code installed
- ✅ Works with both uv tool and uvx methods

---

## Scenario 2: Analyze Existing Brownfield Project

**Acceptance Criteria**: Given a brownfield project, When agent uses analysis templates, Then it MUST perform multi-pass analysis (scan → research → validate) and report findings with confidence levels

### Prerequisites
- Initialized spec-kit project (from Scenario 1)
- Existing project to analyze (e.g., legacy React app)
- AI agent with internet access (Claude Code, GitHub Copilot, etc.)

### Steps

1. **Agent opens brownfield analysis template**
   ```bash
   # Agent reads analysis template
   cat .specify/templates/brownfield-analysis.md
   ```

2. **Agent performs Pass 1: Initial Scan**
   ```markdown
   Agent checklist:
   - ✓ Identify package.json → Node.js project
   - ✓ Detect framework: React (from dependencies)
   - ✓ Scan folder structure: src/, public/, components/
   - ✓ Count files: ~150 .js/.jsx files
   - ✓ Git history: 2 years old, 450 commits
   ```

3. **Agent performs Pass 2: Online Research**
   ```markdown
   Agent research tasks:
   - Search: "React 17 vs 18 migration guide"
   - Search: "React project folder structure best practices 2025"
   - Read: Official React documentation for latest patterns
   - Compare: Project structure vs official recommendations
   ```

4. **Agent performs Pass 3: Validation**
   ```markdown
   Agent validation:
   - ✓ React version: 17.0.2 (outdated, current is 18.3.1)
   - ✓ Folder structure: Non-standard (confidence: medium)
   - ✓ Missing: TypeScript (common in modern React)
   - ✓ Dependencies: 15 outdated packages with security vulnerabilities
   ```

5. **Agent performs Pass 4: Report with Confidence Levels**
   ```markdown
   # Brownfield Analysis Report: Legacy React App
   
   ## Technology Stack (High Confidence)
   - Language: JavaScript ES6
   - Framework: React 17.0.2
   - Build Tool: Webpack 4
   - Package Manager: npm
   
   ## Architecture Pattern (Medium Confidence)
   - Pattern: Component-based with custom routing
   - Structure: Non-standard (components mixed with pages)
   - State Management: Redux (outdated patterns)
   
   ## Recommendations (Prioritized)
   1. **Critical**: Upgrade React 17 → 18 (breaking changes documented)
   2. **High**: Migrate to TypeScript for type safety
   3. **Medium**: Reorganize folder structure (separate components, pages, hooks)
   4. **Low**: Consider Next.js migration for SSR benefits
   
   ## Confidence Levels
   - Technology Detection: 95% (package.json parsing)
   - Architecture Pattern: 70% (manual code review needed)
   - Recommendations: 90% (based on official React docs)
   ```

### Success Criteria
- ✅ Agent completes multi-pass analysis using template guidance
- ✅ Agent uses file/folder expansion within context limits
- ✅ Agent performs internet research for latest versions/patterns
- ✅ Agent reports findings with confidence levels (high/medium/low)
- ✅ Agent asks user for confirmation before proceeding with recommendations

---

## Scenario 3: Use Architecture Templates with Framework Research

**Acceptance Criteria**: Given framework-specific needs, When agent uses architecture templates, Then it MUST research official guidelines and validate patterns against latest versions

### Prerequisites
- Initialized spec-kit project
- AI agent with internet search capability
- New Next.js 14 project to structure

### Steps

1. **Agent reads architecture patterns template**
   ```bash
   cat .specify/templates/architecture-patterns.md
   ```

2. **Agent finds Next.js starter pattern**
   ```markdown
   # Next.js 14 Starter Pattern (from template)
   
   app/
   ├── (routes)/        # Route groups
   ├── api/             # API routes
   ├── components/      # Shared components
   └── lib/             # Utilities
   
   public/              # Static assets
   components/          # Global components
   ```

3. **Agent researches official Next.js documentation**
   ```markdown
   Agent research:
   - Query: "Next.js 14 project structure official documentation"
   - Read: https://nextjs.org/docs/app/building-your-application/routing
   - Compare: Template pattern vs official recommendations
   ```

4. **Agent validates pattern against official docs**
   ```markdown
   Validation Results:
   ✓ App Router structure correct (Next.js 14 uses app/ directory)
   ✓ Route groups pattern valid
   ✓ API routes in app/api/ (correct for App Router)
   ⚠ Template shows old Pages Router pattern (outdated for v14)
   ✓ Recommended: Use app/ directory exclusively for Next.js 14+
   ```

5. **Agent reports findings to user**
   ```markdown
   # Architecture Validation Report
   
   Framework: Next.js 14.0.3 (latest)
   Template Pattern: Partially outdated (Pages Router included)
   
   ## Recommendations
   1. Use App Router structure exclusively (Next.js 13+)
   2. Remove pages/ directory (legacy)
   3. Use route groups for organization: app/(marketing)/, app/(dashboard)/
   4. Server components by default, client components with "use client"
   
   ## Official References
   - https://nextjs.org/docs/app/building-your-application/routing
   - https://nextjs.org/docs/app/building-your-application/rendering/server-components
   
   Would you like me to proceed with the recommended structure?
   ```

### Success Criteria
- ✅ Agent uses starter pattern from template as baseline
- ✅ Agent researches official Next.js documentation online
- ✅ Agent compares template pattern with latest official recommendations
- ✅ Agent identifies outdated patterns and suggests updates
- ✅ Agent provides references to official documentation

---

## Scenario 4: Create Artifact with Validation

**Acceptance Criteria**: Given artifact creation, When agent completes a task, Then validation scripts MUST check naming/structure and prompt agent for compliance report

### Prerequisites
- Initialized spec-kit project
- AI agent with script execution capability

### Steps

1. **Agent creates new feature specification**
   ```bash
   mkdir -p specs/001-user-auth
   ```

2. **Agent writes spec.md with frontmatter**
   ```markdown
   ---
   feature_id: 1
   created: 2025-09-30
   status: draft
   ---
   
   # Feature Specification: User Authentication
   
   [Feature content...]
   ```

3. **Agent runs validation scripts**
   ```bash
   # Structure validation
   bash .specify/scripts/bash/validate-structure.sh specs/001-user-auth/
   
   # Output:
   # [INFO] Validating structure: specs/001-user-auth/
   # [INFO] Feature folder naming: PASS
   # [INFO] Required artifact files present
   # [INFO] Structure validation complete
   ```

4. **Agent runs naming validation**
   ```bash
   bash .specify/scripts/bash/validate-naming.sh specs/001-user-auth/
   
   # Output:
   # [INFO] Validating naming: specs/001-user-auth/
   # [INFO] Feature folder naming: PASS
   # [INFO] Artifact file naming: PASS
   # [INFO] Feature ID consistency: PASS
   # [INFO] Naming validation complete
   ```

5. **Agent runs frontmatter validation**
   ```bash
   bash .specify/scripts/bash/validate-frontmatter.sh specs/001-user-auth/spec.md
   
   # Output:
   # [INFO] Validating frontmatter: specs/001-user-auth/spec.md
   # [INFO] Frontmatter present and parseable
   # [INFO] Required frontmatter fields present
   # [WARN] Missing optional field: version
   # [INFO] Frontmatter validation complete
   ```

6. **Agent reports to user**
   ```markdown
   Validation complete for specs/001-user-auth/spec.md
   
   Results:
   - Structure: PASS (0 errors, 0 warnings)
   - Naming: PASS (0 errors, 0 warnings)
   - Frontmatter: PASS (0 errors, 1 warning)
   
   Warning: Missing optional field 'version' in frontmatter
   
   Recommendation: Add version field for better tracking, or proceed without it.
   The warning is non-blocking.
   
   How would you like to proceed?
   ```

### Success Criteria
- ✅ Validation scripts execute successfully
- ✅ Scripts output parseable messages: [INFO], [WARN], [ERROR]
- ✅ Scripts exit with code 0 (non-blocking)
- ✅ Agent parses output and categorizes messages
- ✅ Agent reports to user and asks for decision

---

## Scenario 5: Execute Slash Command on Multiple Platforms

**Acceptance Criteria**: Given the template-based system, When I use /specify command with any AI agent, Then it MUST execute natively using templates, scripts, and agent research capabilities

### Prerequisites
- Initialized spec-kit project
- Access to multiple AI coding platforms

### Platform-Specific Execution

#### Claude Code (Windsurf)
```bash
# Agent reads platform-specific instructions
cat .specify/workflows/CLAUDE.md

# Agent executes /specify workflow:
1. Read user feature description
2. Load .specify/templates/spec-template.md
3. Use MCP tools for internet research if needed
4. Fill template with user requirements
5. Run validation: bash .specify/scripts/bash/validate-frontmatter.sh
6. Report results to user
```

#### GitHub Copilot
```bash
# Agent reads platform-specific instructions
cat .github/copilot-instructions.md

# Agent executes /specify workflow:
1. Parse user feature description
2. Load .specify/templates/spec-template.md
3. Use semantic search for relevant context
4. Generate specification from template
5. Validate using: specify check specs/[feature]/
6. Present results in editor
```

#### Roo Code
```bash
# Agent reads platform-specific instructions
cat .specify/workflows/ROO.md

# Agent executes /specify workflow:
1. Capture user input
2. Load template: .specify/templates/spec-template.md
3. Fill template sections systematically
4. Run native validation command
5. Report status and next steps
```

### Verification Steps

1. **Create feature on each platform**
   - Use same feature description: "User authentication with email/password"
   - Verify each platform generates spec.md successfully

2. **Validate template consistency**
   ```bash
   # All platforms should produce specs with:
   - Same section structure
   - Same YAML frontmatter format
   - Same constitutional alignment checks
   - Same validation output format
   ```

3. **Cross-platform validation**
   ```bash
   # Validation scripts work identically on all platforms
   bash .specify/scripts/bash/validate-structure.sh specs/002-auth/
   # Same output regardless of which platform created the artifact
   ```

### Success Criteria
- ✅ /specify command executes natively on all 10 platforms
- ✅ Each platform uses .specify/templates/ for consistency
- ✅ Each platform runs validation scripts appropriately
- ✅ All platforms produce compatible artifacts
- ✅ Agent research capabilities utilized where available

---

## Scenario 6: Quality Tool Integration

**Acceptance Criteria**: Given quality tool integration, When agent uses quality templates, Then it MUST check standard tools (eslint, pylint) and report findings without blocking

### Prerequisites
- Initialized spec-kit project with code
- Standard quality tools installed (eslint, pylint, etc.)

### Steps

1. **Agent checks for quality tools**
   ```bash
   # Detect JavaScript project
   if [ -f "package.json" ]; then
     # Check for eslint
     npm run lint 2>/dev/null || npx eslint . --format compact
   fi
   
   # Detect Python project
   if [ -f "requirements.txt" ]; then
     # Check for pylint
     pylint src/ --output-format=parseable 2>/dev/null
   fi
   ```

2. **Agent runs quality checks (non-blocking)**
   ```bash
   specify check --quality
   
   # Output:
   # ✓ Structure validation: PASS
   # ✓ Naming conventions: PASS
   # ✓ Frontmatter metadata: PASS
   #
   # Quality Check Results:
   # - ESLint: 3 errors, 12 warnings
   #   • src/cli.py:45 - Unused variable 'temp'
   #   • src/validators.py:78 - Line too long (92 > 80)
   #   • ...
   #
   # Exit code: 0 (warnings do not block)
   ```

3. **Agent reports findings to user**
   ```markdown
   Quality validation complete:
   
   Critical Issues (3):
   1. src/cli.py:45 - Unused variable 'temp' (consider removing)
   2. src/commands/init.py:23 - Missing type annotation
   3. src/validators.py:12 - Potential bug: unhandled exception
   
   Warnings (12):
   - Mostly line length and formatting issues
   
   Recommendation:
   - Fix critical issues before committing
   - Address warnings in next refactoring pass
   
   Would you like me to fix these issues?
   ```

4. **User decides: fix or proceed**
   ```bash
   # If user says fix:
   specify check --quality --fix
   
   # Automatic fixes applied:
   # - Removed unused variable
   # - Added type annotations
   # - Reformatted long lines
   #
   # Manual review needed:
   # - Potential bug in validators.py (requires human judgment)
   ```

### Success Criteria
- ✅ Agent detects project type and available quality tools
- ✅ Agent runs tool checks without blocking workflow
- ✅ Agent categorizes findings: critical vs warnings
- ✅ Agent reports actionable suggestions
- ✅ User retains final decision on fixes
- ✅ Exit code 0 even with quality issues found

---

## Scenario 7: CLI Simplicity Verification

**Acceptance Criteria**: Given the simplicity focus, When I examine the CLI code, Then it MUST be under 400 lines with init, check commands, and validation script integration

### Prerequisites
- Cloned spec-kit fork repository
- Access to CLI source code

### Verification Steps

1. **Count CLI lines of code**
   ```bash
   # Main CLI file
   wc -l specify-cli/cli.py
   # Expected: ~80 LOC
   
   # Init command
   wc -l specify-cli/commands/init.py
   # Expected: ~100 LOC
   
   # Check command
   wc -l specify-cli/commands/check.py
   # Expected: ~80 LOC
   
   # Template loader
   wc -l specify-cli/template_loader.py
   # Expected: ~80 LOC
   
   # Validators wrapper
   wc -l specify-cli/validators.py
   # Expected: ~60 LOC
   
   # Total
   find specify-cli/ -name "*.py" -exec wc -l {} + | tail -1
   # Expected: < 400 LOC total
   ```

2. **Verify no analysis engines**
   ```bash
   # Check for prohibited modules
   grep -r "brownfield_analyzer\|pattern_detector\|best_practices" specify-cli/
   # Expected: No matches (these are removed)
   
   # Check dependencies
   cat pyproject.toml
   # Expected: Only stdlib, requests, PyYAML, click
   # Not expected: Tavily, Context7, DeepWiki, complex MCP integrations
   ```

3. **Verify simplicity metrics**
   ```bash
   # Cyclomatic complexity (should be low)
   radon cc specify-cli/ -s
   # Expected: Average complexity < 5
   
   # Function length (should be small)
   radon mi specify-cli/
   # Expected: Maintainability index > 70
   ```

### Success Criteria
- ✅ Total CLI code < 400 LOC
- ✅ No analysis engines or complex pattern detection
- ✅ Minimal dependencies (4 total: stdlib, requests, PyYAML, click)
- ✅ Low cyclomatic complexity
- ✅ High maintainability index

---

## Scenario 8: Cross-Platform Script Validation

**Acceptance Criteria**: Cross-platform needs, When I use any of the 10 supported AI platforms, Then all commands MUST work consistently with agent-native patterns

### Prerequisites
- Initialized spec-kit project
- Access to Windows, macOS, and Linux environments

### Steps

1. **Test bash scripts on Unix/Linux/macOS**
   ```bash
   # Structure validation
   bash .specify/scripts/bash/validate-structure.sh specs/003-based-on-the/
   
   # Naming validation
   bash .specify/scripts/bash/validate-naming.sh specs/003-based-on-the/
   
   # Frontmatter validation
   bash .specify/scripts/bash/validate-frontmatter.sh specs/003-based-on-the/spec.md
   
   # All should output [INFO]/[WARN]/[ERROR] messages
   # All should exit with code 0
   ```

2. **Test PowerShell scripts on Windows**
   ```powershell
   # Structure validation
   powershell -File .specify/scripts/powershell/validate-structure.ps1 specs/003-based-on-the/
   
   # Naming validation
   powershell -File .specify/scripts/powershell/validate-naming.ps1 specs/003-based-on-the/
   
   # Frontmatter validation
   powershell -File .specify/scripts/powershell/validate-frontmatter.ps1 specs/003-based-on-the/spec.md
   
   # Output format should match bash scripts exactly
   # All should exit with code 0
   ```

3. **Compare outputs**
   ```bash
   # Run both versions on same input
   bash .specify/scripts/bash/validate-structure.sh . > bash-output.txt
   powershell -File .specify/scripts/powershell/validate-structure.ps1 . > ps-output.txt
   
   # Compare
   diff bash-output.txt ps-output.txt
   # Expected: No differences (or only whitespace)
   ```

4. **Test with CLI wrapper**
   ```bash
   # CLI automatically selects correct script for platform
   specify check
   
   # On Unix: Uses bash scripts
   # On Windows: Uses PowerShell scripts
   # Output format identical on both
   ```

### Success Criteria
- ✅ Bash scripts work on Unix/Linux/macOS
- ✅ PowerShell scripts work on Windows
- ✅ Outputs are functionally identical
- ✅ Message counts match (INFO, WARN, ERROR)
- ✅ Both exit with code 0 (non-blocking)
- ✅ CLI wrapper selects appropriate script automatically

---

## Scenario 9: Offline Usage Validation

**Acceptance Criteria**: What are the implications for offline usage? → Templates cached locally, agents work offline after initial setup

### Prerequisites
- Initialized spec-kit project (templates cached)
- Network connection disabled for testing

### Steps

1. **Initial setup with network**
   ```bash
   # First init downloads templates
   specify init
   # Templates cached in .specify/templates/
   ```

2. **Disable network**
   ```bash
   # Simulate offline mode
   # (Disconnect WiFi or use airplane mode)
   ```

3. **Verify offline functionality**
   ```bash
   # Create new feature (using cached templates)
   mkdir -p specs/002-offline-feature
   cp .specify/templates/spec-template.md specs/002-offline-feature/spec.md
   
   # Run validation scripts (no network needed)
   bash .specify/scripts/bash/validate-structure.sh specs/002-offline-feature/
   # Expected: Works normally, no network errors
   ```

4. **Agent workflows offline**
   ```markdown
   Agent capabilities offline:
   ✓ Read cached templates
   ✓ Fill templates with user input
   ✓ Run validation scripts
   ✓ Execute quality tools (if installed locally)
   ✗ Internet research (requires network)
   ✗ Template updates (requires network)
   ```

5. **Explicit offline mode**
   ```bash
   # Check with offline flag
   specify check --offline
   # Uses only cached templates, no network requests
   ```

### Success Criteria
- ✅ Templates cached locally after first init
- ✅ Validation scripts work completely offline
- ✅ Agent workflows functional offline (except research)
- ✅ No errors from network unavailability
- ✅ Explicit --offline flag prevents network attempts

---

## Scenario 10: Backward Compatibility Verification

**Acceptance Criteria**: How does the fork handle version compatibility with original spec-kit projects? → Full backward compatibility through template structure

### Prerequisites
- Existing v1.x spec-kit project
- Spec-kit fork v2.0 installed

### Steps

1. **Test v1.x project with v2.0 CLI**
   ```bash
   cd existing-v1-project/
   
   # Check structure
   specify check
   
   # Expected:
   # ✓ Structure validation: PASS
   # [INFO] Detected v1.x template structure
   # [INFO] Backward compatibility mode enabled
   # [INFO] All checks passed
   ```

2. **Verify v1.x artifacts readable**
   ```bash
   # v1.x specs should validate successfully
   bash .specify/scripts/bash/validate-frontmatter.sh specs/001-old-feature/spec.md
   
   # Expected: PASS (frontmatter format unchanged)
   ```

3. **Migration path provided**
   ```bash
   specify check --migrate
   
   # Output:
   # [INFO] Detected v1.x project
   # [INFO] Migration available to v2.0 structure
   #
   # Changes:
   # - Update .specify/templates/ to v2.0
   # - Add validation scripts (new in v2.0)
   # - Create platform-specific workflow files
   #
   # Your existing specs/ artifacts will NOT be modified
   # Would you like to proceed with migration? [y/N]
   ```

4. **Verify no breaking changes**
   ```bash
   # v1.x templates still parse correctly
   # v1.x frontmatter format still valid
   # v1.x folder structure still supported
   ```

### Success Criteria
- ✅ V1.x projects work with v2.0 CLI
- ✅ V1.x artifacts validate successfully
- ✅ Clear migration path provided
- ✅ No forced breaking changes
- ✅ User chooses when to migrate

---

## Integration Test Execution

### Running All Scenarios

```bash
# Execute all quickstart scenarios as integration tests
pytest tests/integration/test_quickstart_scenarios.py -v

# Expected output:
# test_scenario_1_greenfield_init PASSED
# test_scenario_2_brownfield_analysis PASSED
# test_scenario_3_architecture_research PASSED
# test_scenario_4_artifact_validation PASSED
# test_scenario_5_multi_platform PASSED
# test_scenario_6_quality_integration PASSED
# test_scenario_7_cli_simplicity PASSED
# test_scenario_8_cross_platform_scripts PASSED
# test_scenario_9_offline_usage PASSED
# test_scenario_10_backward_compatibility PASSED
#
# ========== 10 passed in 45.2s ==========
```

### Continuous Validation

```bash
# Set up pre-commit hook for continuous validation
specify check --install-hooks

# Validation runs automatically on git commit
# Exit code 0 even with warnings (non-blocking)
```

---

## Success Summary

All 10 acceptance scenarios validated:
- ✅ Scenario 1: Fast greenfield initialization (<3s)
- ✅ Scenario 2: Agent-driven brownfield analysis with confidence levels
- ✅ Scenario 3: Framework-specific architecture with online research
- ✅ Scenario 4: Artifact validation with agent reporting
- ✅ Scenario 5: Multi-platform slash command execution
- ✅ Scenario 6: Non-blocking quality tool integration
- ✅ Scenario 7: CLI simplicity (<400 LOC verified)
- ✅ Scenario 8: Cross-platform script parity (bash + PowerShell)
- ✅ Scenario 9: Full offline functionality after setup
- ✅ Scenario 10: Backward compatibility with v1.x projects

**Implementation Status**: Ready for /tasks command to generate task breakdown
