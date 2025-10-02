# Brownfield Project Analysis Template

**Project**: [path]  
**Date**: YYYY-MM-DD  
**Analyzer**: [agent/human]

<!-- 
AGENT GUIDANCE (Enhanced v2.0):
4-pass systematic analysis: Document → Analyze → Integrate → Risk
Based on BMAD Method research (see specs/005-spec-kit-enhanced/research.md)

CRITICAL: Report confidence levels for ALL findings
- High (90%+): Multiple confirming indicators, official docs validated
- Medium (60-90%): Some indicators, partial validation
- Low (<60%): Single indicator, no validation, educated guess

Use analyze-codebase.sh script for automated tech stack detection.
Conduct web research to validate framework versions against official docs.
-->

## 4-Pass Workflow

**Pass 1: Document System** (10-15 min) - Comprehensive file system scan + script execution  
**Pass 2: Analyze Architecture** (15-20 min) - Pattern recognition + web research validation  
**Pass 3: Design Integration** (10-15 min) - Identify integration points + migration strategy  
**Pass 4: Risk Assessment** (10 min) - Legacy dependencies + breaking changes + security

---

## Pass 1: Document System

### Automated Tech Stack Detection

**Run Script First**:
```bash
# Execute automated analysis
.specify/scripts/bash/analyze-codebase.sh --json > codebase-scan.json

# Review JSON output for:
# - framework: detected framework name
# - version: detected version
# - dependencies: key dependencies list
# - file_counts: breakdown by file type
# - confidence: high|medium|low
```

### Manual Technology Detection (if script unavailable)

#### JavaScript/TypeScript
- [ ] `package.json`? Dependencies: ___
- [ ] Framework: Next.js / React / Vue / Angular
- [ ] `tsconfig.json`?

#### Python
- [ ] `requirements.txt` / `pyproject.toml`?
- [ ] Framework: Django / FastAPI / Flask
- [ ] `manage.py`?

#### Java/Kotlin
- [ ] `pom.xml` / `build.gradle`?
- [ ] Spring Boot indicators?

#### Other
- [ ] Ruby: `Gemfile`
- [ ] Go: `go.mod`
- [ ] .NET: `*.csproj`
- [ ] Rust: `Cargo.toml`
- [ ] PHP: `composer.json`

**Initial Finding**: [Technology + version guess]

### Architecture Pattern
- [ ] Monolith
- [ ] Microservices
- [ ] MVC
- [ ] Frontend + Backend separation

**Initial Finding**: [Pattern]

### Confidence After Pass 1
- Technology Stack: [High/Med/Low] - Why?
- Framework Version: [High/Med/Low] - Why?
- Architecture: [High/Med/Low] - Why?

**Uncertainties for Pass 2**: [List]

---

## Pass 2: Online Research

### Framework Validation
**Technology**: ___  
**Official Docs**: [URL]  
**Detected Version**: ___  
**Current Version**: ___  
**Key Features**: ___  
**Breaking Changes**: ___

### Best Practices Research
- [ ] Official folder structure: ___
- [ ] Project follows conventions? [Yes/No/Partial]
- [ ] Deviations: ___

**Updated Confidence**: [High/Med/Low]

---

## Pass 3: Code Inspection

### Code-Level Verification
- [ ] Verify imports and component patterns
- [ ] Check database/ORM usage
- [ ] Inspect routing and config
- [ ] Note integration points

### Critical Dependencies
**Dependency**: ___  
**Version**: ___  
**Usage**: [Confirmed by code]  
**Status**: [Active/Deprecated]

---

## Pass 4: Report

### Executive Summary
**Project Type**: ___  
**Primary Stack**: ___  
**Architecture**: ___  
**Confidence**: [High/Med/Low]

### Technology Inventory
| Tech | Version | Status | Confidence | Notes |
|------|---------|--------|------------|-------|
| ___ | ___ | ___ | ___ | ___ |

### Key Findings

#### High Confidence ✅
1. [Finding with evidence from all 3 passes]

#### Medium Confidence ⚠️
1. [Finding from 2 passes]

#### Low Confidence / Needs Clarification ❓
1. [Hypothesis needing owner confirmation]

### Integration Strategy Template

**Approach**: [Incremental / Big Bang / Strangler Fig / Parallel Run]

**Migration Phases**:
1. **Phase 1**: [Initial integration point]
   - Confidence: [High/Med/Low]
   - Risk: [Low/Medium/High]
   - Estimated effort: [hours/days/weeks]

2. **Phase 2**: [Next integration point]
   - Confidence: [High/Med/Low]
   - Risk: [Low/Medium/High]
   - Estimated effort: [hours/days/weeks]

**Data Migration**:
- [ ] Schema compatibility: [Compatible / Needs transformation / Incompatible]
- [ ] Data volume: [Small <1GB / Medium 1-100GB / Large >100GB]
- [ ] Migration strategy: [One-time / Incremental / Dual-write]

**Testing Strategy**:
- [ ] Unit tests exist? Coverage: ___%
- [ ] Integration tests exist? Coverage: ___%
- [ ] E2E tests exist? Coverage: ___%
- [ ] Recommended: [Specific test additions based on risk areas]

### Recommendations
**Critical** (High confidence + high impact):  
1. [Finding with evidence from all 4 passes]

**High Priority** (Med-high combinations):  
1. [Finding from 2-3 passes]

**Medium Priority** (Lower combinations):  
1. [Finding from 1-2 passes]

### Questions for Owner
1. [Architecture decision clarification]
2. [Technology choice rationale]
3. [Historical context questions]

---

## Confidence Level Reference

**High (90%+)**:
- Multiple confirming indicators (package.json + lock file + node_modules)
- Official documentation validated via web research
- Code inspection confirms framework usage patterns
- Git history shows consistent technology use

**Medium (60-90%)**:
- Some indicators present (package.json but no lock file)
- Partial validation (docs found but version unclear)
- Code patterns suggest framework but not definitive

**Low (<60%)**:
- Single indicator only (package.json exists)
- No validation possible (offline, docs unavailable)
- Educated guess based on file naming conventions
- Requires owner confirmation

---

*Based on BMAD Method research - see specs/005-spec-kit-enhanced/research.md for methodology details*
