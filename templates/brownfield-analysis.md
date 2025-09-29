# Brownfield Project Analysis Template

**Project**: [path]  
**Date**: YYYY-MM-DD

<!-- 
AGENT GUIDANCE:
4-pass systematic analysis: Scan → Research → Validate → Report
Do NOT guess. Mark uncertainties clearly.
-->

## Multi-Pass Workflow

**Pass 1: Initial Scan** (5-10 min) - File system reconnaissance  
**Pass 2: Online Research** (10-15 min) - Validate with official docs  
**Pass 3: Deep Validation** (10-15 min) - Code inspection  
**Pass 4: Report Generation** (5 min) - Structured findings with confidence

---

## Pass 1: Initial Scan

### Technology Detection

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

### Recommendations
**Critical**: [High confidence + high impact]  
**High Priority**: [Med-high combinations]  
**Medium Priority**: [Lower combinations]

### Questions for Owner
1. [Architecture decision clarification]
2. [Technology choice rationale]

---

**Confidence Scoring**:
- **High** (90-100%): Evidence from all 3 passes
- **Medium** (60-89%): Evidence from 2 passes  
- **Low** (30-59%): Evidence from 1 pass only
- **Uncertain** (<30%): No clear evidence

*See `.specify/templates/brownfield-analysis.md` for full workflow.*
