# AI Platform Compatibility Research Brief

## Research Objective
Conduct comprehensive analysis of 10 supported AI platforms to understand integration requirements, command structures, and compatibility patterns for seamless spec-kit integration.

## Scope & Deliverables
- **Platforms**: Roo Code, Claude Code, GitHub Copilot, Cursor, Windsurf, Gemini CLI, Qwen Code, opencode, Kilo Code, Auggie CLI
- **Analysis Areas**: Command integration, file system integration, workflow orchestration, template execution, Git integration, error handling
- **Deliverables**: Platform-specific integration matrix, abstraction strategies, compatibility recommendations

## Confidence Threshold
- Critical claims: ≥0.9 confidence
- Integration patterns: ≥0.8 confidence
- Platform limitations: ≥0.7 confidence

## Time Budget
- Initial research: 3-4 platform analyses per research cycle
- Validation: Cross-reference multiple sources per platform
- Synthesis: Platform-by-platform comparison matrix

## Research Methodology
1. **Primary Sources**: Official documentation, GitHub repositories, API references
2. **Secondary Sources**: Integration guides, community discussions, technical articles
3. **Validation**: Cross-platform testing patterns, compatibility verification

## Key Research Questions

### Command Integration Patterns
- How does each platform handle slash commands?
- What are native command definitions and parameter passing mechanisms?
- How do custom commands get injected and executed?

### File System Integration
- What are the working directory assumptions?
- How are file modifications tracked and applied?
- What file access patterns are supported?

### Workflow Orchestration
- How do platforms handle multi-step workflows?
- What state management capabilities exist?
- How do commands chain together?

### Template & Script Execution
- What templating engines are supported?
- How are external scripts executed?
- How are environment variables handled?

### Git Integration
- What branching and commit patterns are used?
- How are merge conflicts handled?
- What Git workflow capabilities exist?

### Error Handling & Debugging
- How are command failures handled?
- What debugging capabilities are available?
- How are logs and outputs managed?

## Success Criteria
- Concrete evidence from each platform's documentation
- Identification of platform-specific quirks and limitations
- Actionable integration strategies for cross-platform compatibility
- Risk assessment for each platform
- Implementation priorities based on platform capabilities

## Research Phases
1. **Phase 1**: Roo Code, Claude Code, GitHub Copilot (high priority)
2. **Phase 2**: Cursor, Windsurf, Gemini CLI (medium priority)  
3. **Phase 3**: Qwen Code, opencode, Kilo Code, Auggie CLI (lower priority)
4. **Phase 4**: Cross-platform compatibility synthesis

## Source Validation Matrix
| Platform | Documentation | GitHub Repo | Integration Guides | Community Sources |
|----------|---------------|-------------|-------------------|-------------------|
| Roo Code | ✅ | ✅ | ✅ | ✅ |
| Claude Code | ✅ | ✅ | ✅ | ✅ |
| GitHub Copilot | ✅ | ✅ | ✅ | ✅ |
| Cursor | ✅ | ✅ | ✅ | ✅ |
| Windsurf | ✅ | ✅ | ✅ | ✅ |
| Gemini CLI | ✅ | ✅ | ✅ | ✅ |
| Qwen Code | ✅ | ✅ | ✅ | ✅ |
| opencode | ✅ | ✅ | ✅ | ✅ |
| Kilo Code | ✅ | ✅ | ✅ | ✅ |
| Auggie CLI | ✅ | ✅ | ✅ | ✅ |

## Risk Assessment
- **High Risk**: Platforms with limited documentation or closed-source nature
- **Medium Risk**: Platforms with evolving APIs or limited integration examples
- **Low Risk**: Platforms with comprehensive documentation and active communities

## Next Steps
1. Begin Phase 1 research with Roo Code analysis
2. Validate findings against current spec-kit implementation flaws
3. Create platform-specific integration recommendations
4. Develop abstraction patterns for cross-platform compatibility