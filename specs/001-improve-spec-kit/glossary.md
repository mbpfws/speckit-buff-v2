# Terminology Glossary

This glossary defines key terms used throughout the Spec-Kit Enhancement Initiative to ensure consistent communication across all artifacts.

## Core Concepts

### **Analysis vs Detection**
- **Analysis**: The comprehensive process of examining a project's structure, dependencies, history, and patterns to derive insights about its architecture, development practices, and context. Analysis is a holistic activity that may include multiple detection operations.
- **Detection**: The specific act of identifying or recognizing particular patterns, frameworks, or architectural elements within a codebase. Detection is a component of analysis.

### **Cross-Platform vs Multi-Platform**
- **Cross-Platform**: Refers to capabilities that work uniformly across all 10 supported AI coding platforms with identical functionality and behavior.
- **Multi-Platform**: Refers to support for multiple platforms, potentially with platform-specific adaptations or varying feature sets per platform.

### **Artifact**
- **Definition**: Any file, document, or metadata element generated or managed by Spec-Kit as part of the development workflow.
- **Examples**: specifications (spec.md), plans (plan.md), task lists (tasks.md), contracts, data models, quickstart guides, configuration files.
- **Note**: Artifacts are reference documents that agents use as baselines for values, parameters, naming, relationships, and schemas.

### **Template**
- **Definition**: A predefined file structure or content pattern that serves as a starting point for generating new artifacts or project components.
- **Purpose**: Ensures consistency across projects and reduces repetitive setup work.
- **Scope**: Includes document templates (like spec.md, plan.md), code templates, and project structure templates.

### **MCP Integration**
- **Definition**: The connection between Spec-Kit and Model Context Protocol (MCP) servers to enhance analysis capabilities with external knowledge and tools.
- **Purpose**: Provides access to up-to-date documentation, code examples, and specialized knowledge through servers like Tavily Expert, Context7, DeepWiki, and Fetch.

## Technical Terms

### **Multi-Cycle Analysis**
- **Definition**: An iterative analysis process where AI agents perform multiple passes over a project, with each cycle building on insights from previous cycles to improve accuracy and depth of understanding.
- **Cycle Count**: Typically 3-5 cycles, with convergence determined when new insights drop below 5% between cycles.
- **Evaluation**: Each cycle produces a confidence score that must reach ≥85% before analysis is considered complete.

### **Tiered Platform Support**
- **Tier 1 (Full Integration)**: Claude Code, Roo Code
  - Full integration with agents, hooks, MCP servers, automated workflows
  - Native command support with platform-specific optimizations
  - Complete feature parity with advanced capabilities

- **Tier 2 (Core Features)**: GitHub Copilot, Cursor, Gemini CLI
  - Core Spec-Kit commands with manual setup requirements
  - Basic MCP server integration with limited automation
  - Essential workflow support without advanced features

- **Tier 3 (Basic Support)**: Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI
  - Command-line interface access only
  - No MCP server integration
  - Manual configuration and execution required

### **Relational IDs**
- **Format**: `REL-{artifact_type}-{source_id}-{target_id}-{relationship_type}`
- **Purpose**: Unique identifiers that establish and track relationships between artifacts, components, and metadata.
- **Example**: `REL-SPEC-001-TASK-023-IMPLEMENTS` indicates that task T023 implements requirement FR-001.

### **Governance vs Compliance**
- **Governance**: The overall system of rules, processes, and controls that guide how Spec-Kit artifacts are created, managed, and evolved.
- **Compliance**: The act of adhering to specific governance rules or requirements. Compliance checking validates that artifacts follow established governance.

## Performance Metrics

### **Response Time Targets**
- **Analysis Operations**: <500ms for projects up to 10,000 files
- **API Calls**: <200ms for simple queries, <1s for complex analysis
- **CLI Commands**: <300ms perceived response time
- **Artifact Synchronization**: <100ms for propagation of changes

### **Accuracy Requirements**
- **Project Type Classification**: ≥90% accuracy
- **Architectural Pattern Detection**: ≥85% accuracy
- **Dependency Mapping**: ≥95% complete dependency tree
- **Cross-Platform Command Translation**: 100% functional equivalence

## Process Definitions

### **Agent-Native Execution**
- **Definition**: Commands and workflows that can be executed directly by AI coding agents using their native patterns and capabilities.
- **Requirements**: Must use shell/bash commands compatible with all target platforms, follow platform-specific command formats, and integrate with agent workflows.

### **Synchronization**
- **Definition**: The automatic propagation of changes across related artifacts to maintain consistency.
- **Scope**: Includes platform-specific files (.claude/, .roo/, etc.), template instances, and dependent documents.
- **Frequency**: Real-time for file system changes, batch-processed for metadata updates.

## Development Methodology

### **TDD (Test-Driven Development)**
- **Definition**: Development approach where tests are written before implementation code.
- **Requirements**:
  - Contract tests must fail before implementation
  - Test cases must cover all API endpoints and critical paths
  - Implementation is complete only when all tests pass
  - Refactoring preserves test coverage

### **Architecture-First Development**
- **Definition**: Comprehensive architectural planning must precede any implementation work.
- **Deliverables**: System architecture diagrams, technology stack analysis, interoperability validation, contingency plans.
- **Validation**: Architecture review must pass before implementation begins.

---

**Usage Guidelines**:
1. Use these definitions consistently across all artifacts
2. When introducing new terms, add them to this glossary
3. Refer to this glossary when terminology questions arise
4. Update this document as terminology evolves

**Version**: 1.0 | **Created**: 2025-09-29 | **Location**: `specs/001-improve-spec-kit/glossary.md`