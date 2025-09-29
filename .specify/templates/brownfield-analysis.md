# Brownfield Project Analysis

**Project Path**: [path/to/project]  
**Analysis Date**: YYYY-MM-DD  
**Agent**: [Your name/identifier]

<!-- 
AGENT GUIDANCE:
This template guides you through a systematic 4-pass analysis of existing codebases.
Each pass builds on the previous, moving from quick scan to validated findings.

CRITICAL: Do NOT guess or assume. Mark uncertainties clearly and research them.
-->

---

## Multi-Pass Analysis Workflow

### Overview

Brownfield analysis requires **4 distinct passes**:

1. **Pass 1: Initial Scan** (5-10 minutes) - File system reconnaissance
2. **Pass 2: Online Research** (10-15 minutes) - Validate findings against official docs
3. **Pass 3: Deep Validation** (10-15 minutes) - Confirm with code inspection
4. **Pass 4: Report Generation** (5 minutes) - Structured findings with confidence

**Total Time**: 30-50 minutes for thorough analysis

---

## Pass 1: Initial Scan (File System Reconnaissance)

<!-- AGENT: Start here. Scan file system, look for technology indicators. -->

### Technology Detection Checklist

#### JavaScript/TypeScript
- [ ] `package.json` present?
  - If yes: Note dependencies (React, Vue, Angular, Express, Next.js, etc.)
  - Framework indicators: `next.config.js`, `vue.config.js`, `angular.json`
- [ ] `yarn.lock` or `package-lock.json`?
- [ ] `tsconfig.json` (TypeScript)?
- [ ] `node_modules/` directory?

**Initial Finding**: [e.g., "Next.js 14.x project with TypeScript"]

#### Python
- [ ] `requirements.txt`, `pyproject.toml`, `setup.py`, or `Pipfile`?
  - If yes: Note frameworks (Django, Flask, FastAPI, etc.)
- [ ] `manage.py` (Django indicator)?
- [ ] `app.py` or `main.py` (Flask/FastAPI indicator)?
- [ ] `.venv/` or `venv/` directory?

**Initial Finding**: [e.g., "FastAPI project with Poetry"]

#### Java/Kotlin
- [ ] `pom.xml` (Maven)?
- [ ] `build.gradle` or `build.gradle.kts` (Gradle)?
- [ ] `src/main/java/` or `src/main/kotlin/`?
- [ ] Spring Boot indicators: `application.properties`, `application.yml`

**Initial Finding**: [e.g., "Spring Boot 3.x with Gradle"]

#### Ruby
- [ ] `Gemfile` and `Gemfile.lock`?
- [ ] `config.ru` (Rack)?
- [ ] `config/routes.rb` (Rails indicator)?

**Initial Finding**: [e.g., "Ruby on Rails 7.x"]

#### Go
- [ ] `go.mod` and `go.sum`?
- [ ] `main.go`?
- [ ] Common frameworks: gin, echo, fiber in go.mod?

**Initial Finding**: [e.g., "Go 1.21 with Gin framework"]

#### .NET/C#
- [ ] `*.csproj` or `*.sln` files?
- [ ] `Program.cs` and `Startup.cs`?
- [ ] ASP.NET Core indicators?

**Initial Finding**: [e.g., "ASP.NET Core 8.0"]

#### Rust
- [ ] `Cargo.toml` and `Cargo.lock`?
- [ ] `src/main.rs` or `src/lib.rs`?
- [ ] Web frameworks: actix-web, rocket, axum in Cargo.toml?

**Initial Finding**: [e.g., "Rust with Axum web framework"]

#### PHP
- [ ] `composer.json` and `composer.lock`?
- [ ] Laravel indicators: `artisan`, `app/`, `routes/`?
- [ ] Symfony indicators: `symfony.lock`, `config/`?

**Initial Finding**: [e.g., "Laravel 10.x"]

### Architecture Pattern Detection

#### Folder Structure Analysis
```
[Paste actual folder structure here - first 2-3 levels]
```

#### Pattern Recognition
- [ ] **Monolith**: Single application, all code in one repo
- [ ] **Microservices**: Multiple service directories, separate deployments
- [ ] **MVC**: Models/, Views/, Controllers/ or similar structure
- [ ] **Layered**: Separate presentation, business logic, data layers
- [ ] **Frontend + Backend**: Separate `frontend/` and `backend/` or `client/` and `server/`
- [ ] **Mobile + API**: Separate mobile app and API service

**Initial Finding**: [e.g., "MVC monolith with separate React frontend"]

### Confidence Level After Pass 1

Rate your confidence (High/Medium/Low) for each finding:
- **Technology Stack**: [High/Medium/Low] - [Why?]
- **Framework Version**: [High/Medium/Low] - [Why?]
- **Architecture Pattern**: [High/Medium/Low] - [Why?]

**Uncertainties to Research in Pass 2**:
1. [e.g., "Exact Next.js version - saw config but need to verify"]
2. [e.g., "Whether using App Router or Pages Router"]
3. [e.g., "Database type - no clear indicators found"]

---

## Pass 2: Online Research (Validation & Discovery)

<!-- AGENT: Use web search and official documentation to validate Pass 1 findings -->

### Research Tasks

For each technology identified in Pass 1, research:

#### Framework Documentation
1. **Official Docs**: [URL to official documentation]
2. **Current Version**: [Latest stable version as of research date]
3. **Key Features**: [Notable features in detected version]
4. **Breaking Changes**: [Any major breaking changes since detected version]

#### Example Research Entry
**Technology**: Next.js  
**Official Docs**: https://nextjs.org/docs  
**Detected Version**: 14.0.3 (from package.json)  
**Current Version**: 14.2.0 (as of 2025-09-30)  
**Key Features**: App Router (stable), Server Components, Server Actions  
**Breaking Changes**: App Router became default in v13, Pages Router still supported  
**Confidence**: High - package.json explicitly lists version

### Best Practices Research

For the detected stack, research current best practices:

#### Folder Structure
- [ ] Official recommended structure: [URL or description]
- [ ] Does project follow conventions? [Yes/No/Partially]
- [ ] Notable deviations: [List any]

#### Configuration Files
- [ ] Required config files present? [List status]
- [ ] Recommended but missing? [List any]

#### Dependency Management
- [ ] Dependencies up to date? [Check with https://npmjs.com or equivalent]
- [ ] Known security vulnerabilities? [Check npm audit, safety, etc.]
- [ ] Deprecated packages? [List any]

### Updated Findings After Pass 2

**Technology Stack** (Confidence: [High/Medium/Low]):
- [Technology 1]: [Version] - [Status: Current/Outdated/Legacy]
- [Technology 2]: [Version] - [Status: Current/Outdated/Legacy]

**Architecture Pattern** (Confidence: [High/Medium/Low]):
- Pattern: [Name]
- Conventions: [Following/Partial/Custom]
- Assessment: [Brief description]

**Remaining Uncertainties for Pass 3**:
1. [e.g., "Database schema - need to inspect models"]
2. [e.g., "Authentication method - need to check middleware"]

---

## Pass 3: Deep Validation (Code Inspection)

<!-- AGENT: Inspect actual code to confirm hypotheses from Pass 1 and 2 -->

### Code-Level Verification

#### Technology Stack Confirmation
For each technology, verify by inspecting actual code:

**Example: React Components**
- [ ] Check import statements: `import React from 'react'`
- [ ] Verify component patterns: Functional vs Class components
- [ ] Check hooks usage: useState, useEffect, custom hooks
- [ ] Note any deprecated patterns

**Example: Database Layer**
- [ ] Inspect model files or schema definitions
- [ ] Check ORM usage: Prisma, TypeORM, SQLAlchemy, etc.
- [ ] Verify database connections in config
- [ ] Note migration patterns

#### Architecture Validation
- [ ] Verify folder structure matches detected pattern
- [ ] Check if separation of concerns followed
- [ ] Inspect key files (main entry points, routers, config)
- [ ] Validate data flow patterns

#### Integration Points
- [ ] External APIs called? [List with confidence]
- [ ] Third-party services? [List: auth, payment, analytics, etc.]
- [ ] Message queues or event systems? [List if found]
- [ ] Caching layers? [Redis, Memcached, etc.]

### Dependency Analysis

For critical dependencies, verify usage:

**Dependency**: [package name]  
**Version**: [x.y.z]  
**Usage**: [How it's used - confirmed by code inspection]  
**Criticality**: [Core/Important/Optional]  
**Status**: [Active/Maintenance/Deprecated]

### Code Quality Observations

*Note: This is observational, not judgmental*

- **Test Coverage**: [Present/Minimal/None] - [Where: unit/integration/e2e]
- **Documentation**: [Present/Minimal/None] - [Type: README/inline/external]
- **Code Style**: [Consistent/Mixed] - [Linter present?]
- **Error Handling**: [Comprehensive/Basic/Minimal]

---

## Pass 4: Report Generation (Structured Findings)

<!-- AGENT: Synthesize all passes into actionable report -->

### Executive Summary

**Project Type**: [e.g., "Full-stack web application"]  
**Primary Stack**: [e.g., "Next.js 14 + TypeScript + PostgreSQL"]  
**Architecture**: [e.g., "MVC monolith with React frontend"]  
**Overall Confidence**: [High/Medium/Low] - [Why?]

### Technology Inventory

| Technology | Version | Status | Confidence | Notes |
|------------|---------|--------|------------|-------|
| [Framework] | [x.y.z] | [Current/Outdated] | [High/Med/Low] | [Brief note] |
| [Database] | [x.y.z] | [Current/Outdated] | [High/Med/Low] | [Brief note] |
| [Language] | [x.y.z] | [Current/Outdated] | [High/Med/Low] | [Brief note] |

### Architecture Assessment

**Pattern**: [Name of pattern]  
**Adherence**: [Strict/Loose/Custom]  
**Strengths**: [List 2-3]  
**Potential Issues**: [List any concerns with LOW confidence]

### Key Findings

#### High Confidence Findings ✅
1. [Finding with evidence from all 3 passes]
2. [Finding with evidence from all 3 passes]
3. [Finding with evidence from all 3 passes]

#### Medium Confidence Findings ⚠️
1. [Finding with evidence from 2 passes]
2. [Finding with evidence from 2 passes]

#### Low Confidence / Needs Clarification ❓
1. [Hypothesis that needs owner confirmation]
2. [Area that requires deeper investigation]

### Recommendations

Priority levels based on confidence and impact:

#### Critical (High Confidence + High Impact)
1. [Recommendation]  
   **Rationale**: [Based on findings]  
   **Evidence**: [Pass 1, 2, and 3 sources]

#### High Priority (High Confidence + Medium Impact OR Medium Confidence + High Impact)
1. [Recommendation]  
   **Rationale**: [Based on findings]

#### Medium Priority (Lower confidence/impact combinations)
1. [Recommendation]  
   **Rationale**: [Based on findings]

### Next Steps for Owner

1. **Validate Low Confidence Items**: [What to check]
2. **Address Critical Recommendations**: [Action items]
3. **Consider High Priority Items**: [Discussion points]

### Questions for Project Owner

*These emerged during analysis and need owner input*:

1. [Question about architecture decision]
2. [Question about technology choice]
3. [Question about business requirements]

---

## Confidence Scoring Methodology

**High Confidence** (90-100%):
- Evidence from all 3 passes (file system + docs + code)
- Official version numbers confirmed
- Standard patterns observed

**Medium Confidence** (60-89%):
- Evidence from 2 passes
- Inferred from conventions
- Common patterns assumed

**Low Confidence** (30-59%):
- Evidence from 1 pass only
- Contradictory indicators
- Unusual or custom patterns

**Uncertain** (<30%):
- No clear evidence
- Multiple conflicting indicators
- Requires owner clarification

---

## Analysis Metadata

**Pass 1 Duration**: [X minutes]  
**Pass 2 Duration**: [X minutes]  
**Pass 3 Duration**: [X minutes]  
**Pass 4 Duration**: [X minutes]  
**Total Duration**: [X minutes]

**Tools Used**:
- [ ] File system inspection
- [ ] Web search (specify: Google, official docs, GitHub)
- [ ] Code editor/grep
- [ ] Package managers (npm info, pip show, etc.)
- [ ] Other: [specify]

**Limitations**:
- [e.g., "Could not access production environment"]
- [e.g., "Database schema not fully explored"]
- [e.g., "Third-party API keys not available for testing"]

---

*Analysis complete. Review findings with project owner before making decisions.*
