# AI Agent Guidelines for Spec-Kit Enhancement Initiative

**Version**: 2.0.0 | **Date**: 2025-09-29 | **Constitution**: v2.1.1

## Overview

This document provides platform-specific guidelines for AI coding agents working with the enhanced Spec-Kit framework. These guidelines ensure cross-platform compatibility, governance compliance, and optimal performance across all 10 supported AI coding platforms.

## Supported Platforms

### Tier 1: Full Integration
- **Claude Code**: Full integration with agents, hooks, MCP servers, automated workflows
- **Roo Code**: Complete framework support with native command execution

### Tier 2: Core Features
- **GitHub Copilot**: Core features with manual setup requirements
- **Cursor**: Advanced IDE integration with context awareness
- **Gemini CLI**: Command-line interface with comprehensive support

### Tier 3: Basic Support
- **Qwen Code**: Basic command support with limited automation
- **opencode**: Core framework functionality
- **Windsurf**: Development environment integration
- **Kilo Code**: Lightweight framework support
- **Auggie CLI**: Basic command execution

## Core Framework Commands

### Project Analysis Commands
```bash
# Brownfield project analysis
specify analyze --brownfield --tech-stack --architecture

# Multi-cycle analysis with iterative refinement
specify analyze --depth deep --iterative --self-evaluate

# Cross-platform compatibility validation
specify validate --cross-platform --all-tiers
```

### Architecture Guidance Commands
```bash
# Framework-specific pattern detection
specify architecture --detect --framework-specific

# Best practices generation
specify architecture --best-practices --folder-structures

# Integration pattern analysis
specify architecture --integration-patterns --data-flow
```

### Governance and Synchronization Commands
```bash
# Constitutional compliance validation
specify governance --validate --constitution

# Cross-platform artifact synchronization
specify sync --all-platforms --auto --validate

# Governance rule enforcement
specify governance --enforce --rules --compliance
```

### Security and Compliance Commands
```bash
# Security requirements validation
specify security --validate --requirements --cross-platform

# Security audit and compliance testing
specify security --audit --compliance --platforms all

# Platform security gap analysis
specify security --analyze-gaps --platforms all --remediation

# Security incident response testing
specify security --test-incident-response --scenarios critical

# Data protection compliance validation
specify security --validate-data-protection --privacy --encryption

# API security testing and validation
specify security --test-api --endpoints all --authentication --rate-limiting

# Cross-platform security policy synchronization
specify security --sync-policies --platforms all --validate-consistency

# Security monitoring and alerting configuration
specify security --configure-monitoring --alerts --metrics --platform-specific

# Vulnerability assessment and management
specify security --assess-vulnerabilities --scan --remediation-plan

# Security compliance framework validation
specify security --validate-compliance --owasp --nist --iso-27001
```

## Platform-Specific Guidelines

### Claude Code
- **Context Management**: Use hierarchical context windows for large projects
- **MCP Integration**: Leverage MCP servers for enhanced capabilities
- **Workflow Automation**: Implement automated command insertion
- **Prompt Optimization**: Use auto-prompt enhancement features

### GitHub Copilot
- **IDE Integration**: Utilize VS Code extensions and workspace settings
- **Context Awareness**: Leverage file context and project structure
- **Code Completion**: Use intelligent code suggestions with framework patterns

### Roo Code
- **Native Commands**: Execute framework commands natively
- **Performance Optimization**: Use built-in performance monitoring
- **Integration Hooks**: Implement framework-specific integration points

### Cross-Platform Considerations

**All platforms must support:**
- Both installation methods (PATH and uvx)
- Template-driven consistency
- Hierarchical governance enforcement
- Agent-native execution patterns

## Implementation Patterns

### Brownfield Project Support
```bash
# Multi-cycle analysis pattern
specify analyze --project-type brownfield \
    --architecture-detection full \
    --historical-context \
    --dependency-mapping

# Architecture adaptation pattern  
specify architecture --adapt-existing \
    --framework-patterns \
    --best-practices \
    --migration-guidance
```

### Cross-Platform Development
```bash
# Platform-specific optimization
specify optimize --platform ${PLATFORM} \
    --native-patterns \
    --integration-points

# Multi-platform synchronization
specify sync --source ${PLATFORM} \
    --target-platforms all \
    --strategy incremental
```

### Governance Enforcement
```bash
# Constitutional compliance check
specify governance --audit \
    --principles all \
    --validation-rules \
    --compliance-report

# Artifact synchronization
specify governance --synchronize \
    --metadata-tracking \
    --relationship-ids \
    --hierarchical-organization
```

### Security Implementation Patterns
```bash
# Security requirements validation pattern
specify security --validate --requirements --cross-platform \
    --api-endpoints all \
    --data-protection \
    --access-control

# Security compliance testing pattern
specify security --audit --compliance --platforms all \
    --owasp-top-10 \
    --nist-framework \
    --iso-27001

# Cross-platform security synchronization
specify security --sync-policies --platforms all \
    --validate-consistency \
    --remediate-gaps

# Security incident response testing
specify security --test-incident-response --scenarios critical \
    --response-time 1-hour \
    --recovery-objective 4-hour
```

## Quality and Validation

### Testing Requirements
- **Cross-Platform Testing**: Validate functionality across all 10 platforms
- **Performance Testing**: Ensure framework performance targets are met
- **Integration Testing**: Verify cross-component communication
- **Compliance Testing**: Validate constitutional principles adherence

### Validation Commands
```bash
# Comprehensive validation suite
specify validate --suite comprehensive \
    --platforms all \
    --performance \
    --compliance

# Quick validation for development
specify validate --quick \
    --essential \
    --cross-platform
```

## Performance Optimization

### Context Management
- Use hierarchical section management for large codebases
- Implement token-efficient prompt structures
- Optimize context window usage across platforms

### Execution Patterns
- Prefer incremental synchronization over full syncs
- Use caching strategies for repeated operations
- Implement parallel execution where possible

## Troubleshooting

### Common Issues and Solutions

**Platform Integration Issues**
```bash
# Reset platform configuration
specify platform --reset --reconfigure

# Validate platform support
specify platform --validate --compatibility
```

**Governance Compliance Issues**
```bash
# Audit current compliance status
specify governance --audit --detailed

# Generate compliance report
specify governance --report --recommendations
```

**Performance Issues**
```bash
# Analyze performance bottlenecks
specify analyze --performance --bottlenecks

# Optimize framework performance
specify optimize --performance --caching
```

## Best Practices

### Development Workflow
1. **Analyze**: Start with comprehensive project analysis
2. **Design**: Generate architecture and governance plans
3. **Implement**: Follow platform-specific implementation patterns
4. **Validate**: Test across all platforms and scenarios
5. **Synchronize**: Ensure cross-platform consistency

### Code Quality
- Follow framework-specific coding standards
- Maintain backward compatibility
- Ensure cross-platform compatibility
- Adhere to constitutional principles

### Documentation
- Update platform-specific documentation
- Maintain cross-platform compatibility notes
- Document governance compliance status
- Track performance optimization results

## Version Compatibility

### Framework Versions
- **v2.0.0**: Enhanced brownfield support and cross-platform compatibility
- **v1.x.x**: Maintain backward compatibility with existing projects

### Platform Support Matrix
| Platform | Minimum Version | Enhanced Features |
|----------|----------------|-------------------|
| Claude Code | 3.5+ | Full integration |
| Roo Code | 1.0+ | Native support |
| GitHub Copilot | Latest | Core features |
| Cursor | 2.0+ | Advanced integration |
| Gemini CLI | 1.2+ | Comprehensive support |

## Platform-Specific Implementation Details

### Tier 1: Full Integration Platforms

#### Claude Code
**Installation Methods**: Both PATH and uvx fully supported
**Native Integration Features**:
- MCP server integration for enhanced tool capabilities
- Hierarchical context window management for large codebases
- Automated command insertion and workflow transitions
- Prompt optimization with auto-enhancement
- Full governance rule enforcement

**Security Features**:
- MCP server security validation and sandboxing
- Context window security boundaries and isolation
- Automated workflow security controls and validation
- Platform-native authentication and authorization

**Command Examples**:
```bash
# PATH installation
specify analyze --brownfield --platform claude --context-optimized

# uvx installation
uvx run specify-cli analyze --brownfield --platform claude

# Security validation
specify security --validate --platform claude --mcp-integration
```

#### Roo Code
**Installation Methods**: Both PATH and uvx fully supported
**Native Integration Features**:
- Native command execution with performance monitoring
- Built-in context management and optimization
- Framework-specific integration hooks
- Real-time validation and feedback
- Cross-platform synchronization automation

**Security Features**:
- Native command execution security with process isolation
- Performance monitoring with security metrics
- Integration hook security validation
- Real-time security feedback and alerts

**Command Examples**:
```bash
# PATH installation
specify architecture --detect --platform roo --performance-optimized

# uvx installation
uvx run specify-cli architecture --detect --platform roo

# Security monitoring
specify security --configure-monitoring --platform roo --real-time
```

### Tier 2: Core Features Platforms

#### GitHub Copilot
**Installation Methods**: PATH preferred, uvx supported with manual setup
**Integration Requirements**:
- VS Code workspace configuration for context awareness
- Manual template synchronization setup
- Project structure analysis for intelligent suggestions
- Code completion patterns with framework awareness

**Command Examples**:
```bash
# PATH installation (recommended)
specify governance --validate --platform copilot --workspace-aware

# uvx installation (requires manual context setup)
uvx run specify-cli governance --validate --platform copilot
```

#### Cursor
**Installation Methods**: Both PATH and uvx supported
**Integration Features**:
- Advanced IDE integration with real-time context
- Project structure awareness for pattern detection
- Intelligent code suggestions with framework patterns
- Cross-file dependency analysis

**Command Examples**:
```bash
# PATH installation
specify analyze --architecture --platform cursor --context-rich

# uvx installation
uvx run specify-cli analyze --architecture --platform cursor
```

#### Gemini CLI
**Installation Methods**: Both PATH and uvx fully supported
**Integration Features**:
- Command-line interface with comprehensive support
- Terminal-based workflow optimization
- Batch processing capabilities
- Script automation integration

**Command Examples**:
```bash
# PATH installation
specify sync --all-platforms --platform gemini --batch-mode

# uvx installation
uvx run specify-cli sync --all-platforms --platform gemini
```

### Tier 3: Basic Support Platforms

#### Qwen Code
**Installation Methods**: Both PATH and uvx supported
**Support Level**: Basic command execution with limited automation
**Features**:
- Core framework command execution
- Basic project analysis capabilities
- Manual synchronization required

**Command Examples**:
```bash
# PATH installation
specify analyze --quick --platform qwen

# uvx installation
uvx run specify-cli analyze --quick --platform qwen
```

#### opencode
**Installation Methods**: Both PATH and uvx supported
**Support Level**: Core framework functionality
**Features**:
- Basic project analysis and validation
- Standard command execution
- Manual platform-specific optimizations

**Command Examples**:
```bash
# PATH installation
specify validate --cross-platform --platform opencode

# uvx installation
uvx run specify-cli validate --cross-platform --platform opencode
```

#### Windsurf
**Installation Methods**: Both PATH and uvx supported
**Support Level**: Development environment integration
**Features**:
- IDE environment integration
- Project context awareness
- Development workflow optimization

**Command Examples**:
```bash
# PATH installation
specify implement --platform windsurf --ide-integrated

# uvx installation
uvx run specify-cli implement --platform windsurf
```

#### Kilo Code
**Installation Methods**: Both PATH and uvx supported
**Support Level**: Lightweight framework support
**Features**:
- Lightweight command execution
- Basic analysis capabilities
- Minimal resource footprint

**Command Examples**:
```bash
# PATH installation
specify analyze --lightweight --platform kilo

# uvx installation
uvx run specify-cli analyze --lightweight --platform kilo
```

#### Auggie CLI
**Installation Methods**: Both PATH and uvx supported
**Support Level**: Basic command execution
**Features**:
- Fundamental command support
- Basic validation capabilities
- Manual synchronization setup

**Command Examples**:
```bash
# PATH installation
specify governance --basic --platform auggie

# uvx installation
uvx run specify-cli governance --basic --platform auggie
```

## Installation Method Compatibility Matrix

| Platform | PATH Installation | uvx Installation | Notes |
|----------|------------------|------------------|--------|
| Claude Code | ✅ Full support | ✅ Full support | Native integration both methods |
| Roo Code | ✅ Full support | ✅ Full support | Optimized for both installation types |
| GitHub Copilot | ✅ Recommended | ⚠️ Manual setup | Workspace configuration required for uvx |
| Cursor | ✅ Full support | ✅ Full support | IDE integration works with both |
| Gemini CLI | ✅ Full support | ✅ Full support | Command-line optimized for both |
| Qwen Code | ✅ Supported | ✅ Supported | Basic functionality both methods |
| opencode | ✅ Supported | ✅ Supported | Core features available both methods |
| Windsurf | ✅ Supported | ✅ Supported | IDE integration both methods |
| Kilo Code | ✅ Supported | ✅ Supported | Lightweight support both methods |
| Auggie CLI | ✅ Supported | ✅ Supported | Basic commands both methods |

## Cross-Platform Validation Commands

### Installation Method Testing
```bash
# Test PATH installation compatibility
specify validate --installation path --platforms all

# Test uvx installation compatibility
specify validate --installation uvx --platforms all

# Comprehensive installation validation
specify validate --installation both --platforms all --detailed
```

### Platform-Specific Feature Validation
```bash
# Validate Tier 1 platform features
specify validate --tier 1 --features all --installation both

# Validate Tier 2 platform features
specify validate --tier 2 --features core --installation both

# Validate Tier 3 platform features
specify validate --tier 3 --features basic --installation both
```

## Support and Resources

### Documentation
- [Constitution](memory/constitution.md) - Supreme governance document
- [Security Requirements](specs/001-improve-spec-kit/security-requirements.md) - Comprehensive security specifications
- [Quickstart Guide](.specify/specs/001-improve-spec-kit/quickstart.md) - Getting started guide
- [API Contracts](.specify/specs/001-improve-spec-kit/contracts/) - Integration specifications
- [Research Findings](.specify/specs/001-improve-spec-kit/research.md) - Technical background

### Community Resources
- GitHub repository: [github.com/github/spec-kit](https://github.com/github/spec-kit)
- Issue tracking and feature requests
- Community discussions and support

---

**Constitutional Compliance**: This document adheres to all constitutional principles and provides comprehensive platform-specific implementation guidelines following the hierarchical governance structure. All installation methods (PATH and uvx) are fully supported across all 10 AI coding platforms with appropriate optimization levels for each tier.