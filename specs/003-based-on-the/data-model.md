# Data Model: Spec-Kit Realignment Fork - Back to Basics

**Feature**: 003-based-on-the | **Date**: 2025-09-30 | **Status**: Draft

## Overview

This document defines the core entities and data structures for the simplified spec-kit fork. The data model is intentionally minimal to support the simplicity principle while maintaining necessary functionality for template management, artifact tracking, and validation.

---

## Core Entities

### 1. Template

**Purpose**: Represents a markdown template file with embedded guidance for AI agents

**Attributes**:
- `name`: string - Template identifier (e.g., "spec-template", "plan-template")
- `version`: string - Semantic version (e.g., "2.0.0")
- `path`: string - Local file path (e.g., ".specify/templates/spec-template.md")
- `content`: string - Markdown content with embedded instructions
- `metadata`: TemplateMetadata - Template-specific configuration

**Validation Rules**:
- Name must match pattern: `[a-z-]+\\.md`
- Version must follow semantic versioning (MAJOR.MINOR.PATCH)
- Content must be valid UTF-8 markdown
- Must contain agent instruction sections

**State Transitions**:
- `download` → Template downloaded from GitHub Release
- `cache` → Template stored in local `.specify/templates/`
- `update` → Newer version replaces existing template
- `use` → Template copied/instantiated for feature

**Relationships**:
- Template → TemplateMetadata (1:1)
- Template → TemplateVersion (1:many historical versions)

---

### 2. TemplateMetadata

**Purpose**: Configuration and metadata for template files

**Attributes**:
- `category`: enum - Template type: "spec" | "plan" | "tasks" | "constitution" | "analysis" | "architecture"
- `required_fields`: list[string] - Placeholder fields that must be filled (e.g., "[FEATURE]", "[DATE]")
- `agent_instructions`: list[string] - Section markers for agent guidance
- `dependencies`: list[string] - Other templates required (e.g., plan depends on spec)
- `platforms`: list[string] - Supported AI platforms (default: all 10)

**Validation Rules**:
- Category must be from defined enum
- Required fields must exist in template content
- Dependencies must reference valid template names

**Example**:
```yaml
category: plan
required_fields: [FEATURE, DATE, ###-feature-name]
agent_instructions: ["Phase 0: Outline & Research", "Phase 1: Design & Contracts"]
dependencies: ["spec-template"]
platforms: ["all"]
```

---

### 3. Artifact

**Purpose**: Represents a generated specification artifact (spec, plan, tasks)

**Attributes**:
- `feature_id`: integer - Unique feature identifier (e.g., 3 from "003-based-on-the")
- `feature_slug`: string - URL-friendly feature name (e.g., "based-on-the")
- `artifact_type`: enum - "spec" | "plan" | "tasks" | "research" | "data-model" | "quickstart"
- `path`: string - File path (e.g., "specs/003-based-on-the/spec.md")
- `status`: enum - "draft" | "active" | "complete" | "archived"
- `created`: datetime - Creation timestamp
- `parent_spec`: string - Path to parent spec (for plan/tasks artifacts)
- `frontmatter`: ArtifactFrontmatter - YAML metadata

**Validation Rules**:
- Feature ID must be 3-digit zero-padded integer
- Feature slug must match pattern: `[a-z0-9-]+`
- Path must follow convention: `specs/{feature_id}-{feature_slug}/{artifact_type}.md`
- Parent spec must exist for plan/tasks artifacts
- Status transitions: draft → active → complete → archived

**State Transitions**:
```
create → draft
validate → (draft | active)  # After validation passes
complete → complete  # All tasks finished
archive → archived  # Feature superseded or cancelled
```

**Relationships**:
- Artifact → ArtifactFrontmatter (1:1)
- Artifact → Artifact (parent-child via parent_spec)

---

### 4. ArtifactFrontmatter

**Purpose**: YAML metadata embedded at start of artifact markdown files

**Attributes**:
- `feature_id`: integer - Links to parent feature
- `created`: date - ISO 8601 date (YYYY-MM-DD)
- `status`: enum - "draft" | "active" | "complete" | "archived"
- `parent_spec`: string - Relative path to parent (optional, plan/tasks only)
- `version`: string - Artifact version (optional)
- `branch`: string - Git branch name (optional)

**Validation Rules**:
- Required fields: `feature_id`, `created`, `status`
- Feature ID must match folder name pattern
- Created date must be valid ISO 8601 format
- Parent spec path must be relative (e.g., "../002-feature/spec.md")
- Status must be from defined enum

**Example**:
```yaml
---
feature_id: 3
created: 2025-09-30
status: draft
parent_spec: ./spec.md
branch: 003-based-on-the
---
```

**Format Specification**:
- YAML 1.2 compliant
- Enclosed in triple-dash delimiters (`---`)
- Must be at file start (before any markdown content)
- Parsed via PyYAML library

---

### 5. ValidationResult

**Purpose**: Output from validation script execution

**Attributes**:
- `script_name`: string - Name of validation script executed
- `target`: string - Path to validated artifact or directory
- `exit_code`: integer - Process exit code (always 0 for non-blocking)
- `messages`: list[ValidationMessage] - Structured output messages
- `timestamp`: datetime - When validation ran
- `platform`: enum - "unix" | "windows" - Script platform

**Validation Rules**:
- Exit code must be 0 (non-blocking philosophy)
- Messages must be parseable by agents
- Script name must match existing validation script

**Relationships**:
- ValidationResult → ValidationMessage (1:many)

---

### 6. ValidationMessage

**Purpose**: Individual message from validation script output

**Attributes**:
- `level`: enum - "INFO" | "WARN" | "ERROR"
- `message`: string - Human-readable description
- `file`: string - File path where issue found (optional)
- `line`: integer - Line number for issue (optional)
- `suggestion`: string - Recommended fix (optional)

**Validation Rules**:
- Level must be from defined enum
- Message must be non-empty
- Line number must be positive integer if provided

**Format Specification**:
```
[LEVEL] message
[LEVEL] file:line - message
[LEVEL] message (suggestion: fix description)
```

**Examples**:
```
[INFO] Artifact structure validated successfully
[WARN] specs/003-based-on-the/plan.md:45 - Missing optional frontmatter field: version
[ERROR] specs/003-based-on-the/ - Folder naming does not match pattern {id}-{slug}
[WARN] Task numbering gap detected: T001, T003 (suggestion: add T002 or renumber)
```

---

### 7. CLIConfig

**Purpose**: Configuration for CLI behavior and preferences

**Attributes**:
- `template_source`: string - GitHub releases URL (default: official repo)
- `template_version`: string - Preferred template version (default: "latest")
- `validation`: ValidationConfig - Validation script preferences
- `quality`: QualityConfig - Quality tool configuration
- `offline_mode`: boolean - Use cached templates only (default: false)

**Validation Rules**:
- Template source must be valid HTTPS URL
- Template version must be valid semver or "latest"

**File Location**: `.specify/config.yaml`

**Example**:
```yaml
template_source: https://github.com/specify-fork/templates/releases
template_version: latest
validation:
  skip_checks: []
  fail_on_error: false
quality:
  tools: [eslint, pylint]
  auto_fix: false
offline_mode: false
```

---

### 8. ValidationConfig

**Purpose**: Configuration for validation script behavior

**Attributes**:
- `skip_checks`: list[string] - Validation scripts to skip (e.g., ["naming", "frontmatter"])
- `fail_on_error`: boolean - Whether to exit non-zero on errors (default: false)
- `custom_scripts`: list[string] - User-provided validation scripts

**Validation Rules**:
- Skip checks must reference valid script names
- Custom scripts must be executable and follow output format

---

### 9. QualityConfig

**Purpose**: Configuration for quality tool integration

**Attributes**:
- `tools`: list[string] - Preferred quality tools (e.g., ["eslint", "pylint"])
- `auto_fix`: boolean - Whether to attempt automatic fixes (default: false)
- `thresholds`: dict[string, any] - Custom thresholds (e.g., {"max_complexity": 10})

**Validation Rules**:
- Tools must be from supported tool list
- Thresholds must be valid for specified tools

---

### 10. FrameworkPattern

**Purpose**: Starter architecture pattern for common frameworks

**Attributes**:
- `framework`: string - Framework name (e.g., "Next.js", "Django", "Spring Boot")
- `version_range`: string - Compatible versions (e.g., "14.x", "4.x-5.x")
- `folder_structure`: dict - Directory hierarchy with descriptions
- `key_files`: list[string] - Important configuration files
- `validation_checklist`: list[string] - Questions for agent validation

**Validation Rules**:
- Framework must be from Tier 1 or Tier 2 supported list
- Version range must be valid semver range
- Folder structure must be valid nested dictionary

**Example**:
```yaml
framework: Next.js
version_range: 14.x
folder_structure:
  app/: "App Router pages and layouts"
  components/: "Reusable React components"
  lib/: "Utility functions and helpers"
  public/: "Static assets"
key_files: [next.config.js, package.json, tsconfig.json]
validation_checklist:
  - "Does project use App Router or Pages Router?"
  - "Are server components properly distinguished from client?"
  - "Is TypeScript configuration aligned with Next.js recommendations?"
```

**Storage**: Embedded in `.specify/templates/architecture-patterns.md`

---

## Entity Relationships Diagram

```
Template (1) ──has──> (1) TemplateMetadata

Artifact (1) ──has──> (1) ArtifactFrontmatter
Artifact (parent) ──has──> (*) Artifact (children)

ValidationResult (1) ──has──> (*) ValidationMessage
ValidationResult (*) ──validates──> (1) Artifact

CLIConfig (1) ──has──> (1) ValidationConfig
CLIConfig (1) ──has──> (1) QualityConfig

FrameworkPattern (*) ──stored_in──> (1) Template[architecture-patterns]
```

---

## Data Storage Locations

### Local Filesystem
- **Templates**: `.specify/templates/*.md`
- **Artifacts**: `specs/{feature-id}-{feature-slug}/*.md`
- **Config**: `.specify/config.yaml`
- **Scripts**: `.specify/scripts/{bash,powershell}/*.{sh,ps1}`
- **Workflows**: `.specify/workflows/*.md`

### Remote (GitHub)
- **Template Distribution**: GitHub Releases (tar.gz archives)
- **Version Metadata**: Release tags (v2.0.0, v2.1.0, etc.)

### No Database
The system is intentionally file-based with no external database requirements, supporting the simplicity and offline-capable principles.

---

## Data Validation Summary

### Template Validation
- ✅ Valid markdown syntax
- ✅ Contains required placeholder fields
- ✅ Has agent instruction sections
- ✅ Matches metadata configuration

### Artifact Validation
- ✅ Folder naming: `{3-digit-id}-{slug}/`
- ✅ Frontmatter present and valid YAML
- ✅ Required frontmatter fields populated
- ✅ Parent references resolve correctly

### Script Output Validation
- ✅ Parseable message format: `[LEVEL] message`
- ✅ Non-blocking exit codes (0)
- ✅ Actionable suggestions provided

---

## Constitutional Alignment

### Cross-Platform ✅
- All data structures are platform-agnostic (UTF-8 text, YAML)
- File paths use forward slashes (Python normalizes automatically)
- No platform-specific data dependencies

### Template-Driven ✅
- Templates are first-class entities with full metadata
- All workflows driven by template content
- Minimal runtime data processing

### Agent-Native ✅
- Data structures support agent interpretation (markdown, YAML)
- Validation messages designed for agent parsing
- No complex data transformations required

### Simplicity ✅
- Minimal entity count (10 core entities)
- File-based storage (no database)
- Simple relationships (mostly 1:1, 1:many)

---

**Data Model Status**: Complete  
**Next Artifact**: contracts/ (API contracts for CLI commands)
