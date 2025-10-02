---
description: Multi-stage technology research workflow for complex specifications
orchestration:
  pre_conditions: ["complexity_analyzed"]
  post_conditions: ["research_complete"]
  max_iterations: 3
  next: "clarify"
---

# Multi-Stage Technology Research Workflow

This workflow conducts iterative, multi-pass research for complex technical requirements that involve:
- Multiple technology stacks
- Third-party integrations
- Architecture patterns
- Cross-domain dependencies

## Workflow Execution

### Phase 0: Load Context & Determine Scope

1. Load complexity analysis from `.specify/context.json`:
   ```bash
   # Read context
   cat .specify/context.json
   ```

2. Extract research scope:
   - `research_topics`: Array of research areas
   - `complexity_score`: Numeric score
   - `estimated_research_passes`: Number of iterations needed

3. Initialize research tracking:
   ```json
   {
     "research_passes_completed": 0,
     "research_findings": {},
     "research_complete": false
   }
   ```

### Phase 1: Technology Stack Research (Pass 1)

**Objective**: Identify and evaluate primary technology choices

1. **For each technology mentioned** in the feature description:
   - Use **web search** to find:
     - Latest stable version
     - Official documentation links
     - Best practices and patterns
     - Common integration approaches
     - Known limitations or gotchas
   
2. **Example searches**:
   ```
   "[Technology] latest version 2025 best practices"
   "[Technology] official documentation getting started"
   "[Framework] [Database] integration patterns"
   "[Technology] production deployment checklist"
   ```

3. **Document findings** in research.md:
   ```markdown
   ## Technology Stack Research
   
   ### [Technology Name]
   - **Version**: X.Y.Z (latest stable as of [date])
   - **Documentation**: [URL]
   - **Best Practices**:
     - [Practice 1]
     - [Practice 2]
   - **Integration Considerations**:
     - [Point 1]
   - **Limitations**:
     - [Limitation 1]
   ```

### Phase 2: Integration & Dependencies Research (Pass 2)

**Objective**: Understand how technologies work together

1. **For each integration point**:
   - Search for official SDKs/libraries
   - Find integration examples and tutorials
   - Identify authentication/authorization patterns
   - Document API rate limits and constraints

2. **Example searches**:
   ```
   "[Service A] [Service B] integration example"
   "[Framework] [Third-party API] SDK official"
   "[Payment Gateway] webhook implementation guide"
   "[Auth Provider] token validation best practices"
   ```

3. **Document in research.md**:
   ```markdown
   ## Integration Research
   
   ### [Service A] ↔ [Service B]
   - **SDK**: [Package name] v[version]
   - **Authentication**: [Method]
   - **Rate Limits**: [Limits]
   - **Example Implementation**: [URL]
   - **Error Handling**: [Approaches]
   ```

### Phase 3: Architecture Patterns Research (Pass 3)

**Objective**: Identify proven architecture patterns for the use case

1. **For complex requirements**:
   - Research architecture patterns (microservices, event-driven, etc.)
   - Find case studies of similar implementations
   - Identify scalability considerations
   - Document deployment patterns

2. **Example searches**:
   ```
   "[Use case] architecture patterns 2025"
   "[Technology] microservices best practices"
   "real-time [feature] scalable architecture"
   "[Industry] [use case] production architecture"
   ```

3. **Document in research.md**:
   ```markdown
   ## Architecture Patterns
   
   ### Recommended Pattern: [Pattern Name]
   - **Use Case Fit**: [Why this pattern]
   - **Pros**:
     - [Pro 1]
   - **Cons**:
     - [Con 1]
   - **Scalability**: [Considerations]
   - **Reference Architecture**: [URL]
   ```

### Phase 4: Synthesis & Recommendations

1. **Synthesize findings** into actionable recommendations:
   - Technology stack recommendation with versions
   - Integration approach with specific SDKs
   - Architecture pattern selection with rationale
   - Identified risks and mitigation strategies

2. **Create technology decision matrix**:
   ```markdown
   ## Technology Decisions
   
   | Decision Area | Recommendation | Rationale | Alternatives Considered |
   |---------------|----------------|-----------|------------------------|
   | Backend | [Choice] v[X] | [Why] | [Alt 1], [Alt 2] |
   | Database | [Choice] | [Why] | [Alt 1] |
   | Auth | [Choice] | [Why] | [Alt 1] |
   ```

3. **Document risks and unknowns**:
   ```markdown
   ## Risks & Unknowns
   
   ### Technical Risks
   1. **[Risk]**: [Description]
      - **Mitigation**: [Strategy]
      - **Severity**: High/Medium/Low
   
   ### Unknowns Requiring Clarification
   1. [Question requiring user input]
   2. [Question about requirements]
   ```

### Phase 5: Update Context & Completion

1. Update `.specify/context.json`:
   ```json
   {
     "complexity_level": "<level>",
     "multi_domain": <boolean>,
     "research_needed": false,
     "research_complete": true,
     "research_passes_completed": <number>,
     "technology_recommendations": {
       "stack": ["tech1", "tech2"],
       "integrations": ["sdk1", "sdk2"],
       "architecture_pattern": "<pattern>"
     }
   }
   ```

2. Save research findings to `specs/{feature}/research.md`

3. Report completion:
   ```
   ✅ Multi-stage research complete
   
   - Research passes: 3
   - Technologies evaluated: X
   - Integrations analyzed: Y
   - Architecture pattern: [Pattern]
   
   📝 Findings saved to: specs/{feature}/research.md
   
   ➡️ Next workflow: /clarify
   ```

## Iteration Logic

**IF** `research_passes_completed < estimated_research_passes`:
- Continue with next research pass
- Focus on gaps from previous passes

**ELSE**:
- Mark research complete
- Proceed to `/clarify` workflow

## Research Quality Guidelines

1. **Always use web search** - Don't rely on training data for current versions/practices
2. **Cite sources** - Include URLs in findings
3. **Date findings** - Research degrades quickly in tech
4. **Multiple sources** - Cross-reference critical decisions
5. **Official first** - Prioritize official documentation over tutorials
6. **Version specific** - Always specify version numbers
7. **Real-world focus** - Prefer production case studies over toy examples

## Agent Instructions

- Use **web search tools** for all research queries
- **Do not hallucinate** technology recommendations
- **Do not guess** at version numbers or API details
- If research is inconclusive, **document as an unknown**
- Research should take **5-15 minutes** depending on complexity
- Each pass should build on previous findings
- **Pause for user input** if critical decisions require business context

## Exit Conditions

Research is complete when:
1. All `research_topics` from complexity analysis are addressed
2. Minimum `estimated_research_passes` completed
3. Technology stack is clearly recommended with versions
4. Integration approaches are documented with SDKs
5. Architecture pattern is selected with rationale
6. Risks and unknowns are documented
