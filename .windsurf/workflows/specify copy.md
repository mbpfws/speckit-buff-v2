---
description: Create feature specification through iterative conversation with complexity analysis and research
auto_execution_mode: 3
---

**IMPORTANT**: This workflow is CONVERSATIONAL. Do NOT immediately create spec.md. Instead:
1. Analyze complexity
2. Present initial understanding
3. Ask clarifying questions
4. Do research if needed
5. Present findings and ask for feedback
6. THEN create spec with user approval

---

The user input to you can be provided directly by the agent or as a command argument - you **MUST** consider it before proceeding with the prompt (if not empty).

**User's Feature Request**:

$ARGUMENTS

---

## Workflow Execution (Conversational Mode)

### Phase 1: Analyze & Understand

**Objective**: Understand the feature without making assumptions

1. **Analyze complexity** (attempt automatic, fallback to manual):
   ```bash
   # Try automatic detection (may fail - that's OK)
   echo "$ARGUMENTS" | .specify/scripts/bash/detect-complexity.sh 2>/dev/null
   
   # If script fails, analyze manually based on these indicators:
   # - Technology stack mentions (databases, APIs, frameworks)
   # - Integration requirements (third-party, payments, auth)
   # - Architecture needs (real-time, scalable, distributed)
   # - Complexity keywords (complex, enterprise, multi-tenant)
   ```

2. **Manual complexity scoring** (if script fails):
   - Count technology indicators → multiply by 2
   - Count integration indicators → multiply by 3
   - Count architecture indicators → multiply by 4
   - Score ≥10 = HIGH, ≥5 = MEDIUM, ≥2 = LOW-MEDIUM, <2 = LOW

3. **Present your initial understanding** to the user:
   ```markdown
   📊 **Feature Understanding**
   
   I understand you want to build: [restate in your words]
   
   **Complexity Analysis**:
   - Level: [LOW/MEDIUM/HIGH]
   - Technology areas detected: [list]
   - Integration points: [list if any]
   - Architecture concerns: [list if any]
   
   **My initial thoughts**:
   - [Key challenge 1]
   - [Key challenge 2]
   - [Open question 1]
   - [Open question 2]
   ```

4. **DO NOT PROCEED** until you've shown this understanding

### Phase 2: Research & Discovery (Conditional)

**IF complexity is MEDIUM or HIGH**, initiate research conversation:

1. **Inform the user**:
   ```markdown
   🔍 **Research Needed**
   
   This is a complex feature spanning multiple domains. Before we finalize the spec,
   I'd like to research:
   
   1. [Research topic 1] - to find current best practices
   2. [Research topic 2] - to identify specific versions/SDKs
   3. [Research topic 3] - to understand architecture patterns
   
   This will take a few minutes but will result in a much more informed specification.
   
   **Proceed with research? [Y/n]**
   ```

2. **If user approves**, conduct research using web search:
   ```markdown
   🔬 **Researching...**
   
   Pass 1: Technology Stack
   - Searching: "[technology] best practices 2025"
   - Searching: "[framework] latest stable version"
   → Finding: [Key finding with URL]
   
   Pass 2: Integration Patterns
   - Searching: "[integration] SDK documentation"
   - Searching: "[service] API authentication"
   → Finding: [Key finding with URL]
   
   Pass 3: Architecture
   - Searching: "[domain] architecture patterns"
   - Searching: "[use case] scalability case study"
   → Finding: [Key finding with URL]
   ```

3. **Present research findings**:
   ```markdown
   ✅ **Research Complete**
   
   **Technology Recommendations**:
   - [Tech 1]: [Specific version] - [Why/URL]
   - [Tech 2]: [Specific SDK] - [Why/URL]
   
   **Architecture Pattern**: [Pattern name]
   - Based on: [Case study/URL]
   - Benefits: [List]
   - Trade-offs: [List]
   
   **Integration Approach**: [Approach]
   - [Detail 1]
   - [Detail 2]
   
   **Questions before we finalize**:
   1. [Technical choice question]
   2. [Scale/performance question]
   3. [Integration preference question]
   ```

4. **Wait for user feedback** on research findings

### Phase 3: Clarifying Questions (Interactive)

**Before creating spec**, ask 3-5 targeted questions based on complexity:

**For ALL features, ask about**:
- **Scope**: What's the MVP vs future phases?
- **Users**: Who are the primary users?
- **Success criteria**: How do we measure success?

**Additional questions based on complexity**:

**If HIGH complexity**:
- How many concurrent users do you expect?
- What are the performance requirements (latency, throughput)?
- Any compliance requirements (GDPR, HIPAA, etc.)?
- What's the scale/growth trajectory?

**If MEDIUM/HIGH with integrations**:
- Which third-party services are preferred?
- Any existing accounts/APIs we should use?
- Authentication method preferences?

**If MEDIUM/HIGH with real-time**:
- What's acceptable latency?
- Offline support needed?
- Conflict resolution strategy?

**Present questions conversationally**:
```markdown
🤔 **A few questions to help me create the best spec**:

1. [Question 1 based on above]
2. [Question 2 based on above]
3. [Question 3 based on above]
4. [Question 4 if needed]
5. [Question 5 if needed]

Feel free to answer what you know - we can refine during /clarify later!
```

**Wait for user responses**

### Phase 4: Synthesis & Preview

Before creating the final spec, synthesize everything:

```markdown
📝 **Specification Preview**

Based on our conversation, here's what I'll include in the spec:

**Feature**: [Title]
**Complexity**: [Level]
**Technology Stack** (researched):
- [Tech 1 with version]
- [Tech 2 with version]
- [Integration with details]

**Core Requirements**:
1. [Requirement from conversation]
2. [Requirement from research]
3. [Requirement from clarifications]

**Architecture**:
- Pattern: [Researched pattern]
- Rationale: [Why based on research]

**Open Questions** (for /clarify phase):
1. [Unresolved question 1]
2. [Unresolved question 2]

**Does this look good? I'll create the formal spec if you approve. [Y/n]**
```

**Wait for user approval**

### Phase 5: Create Feature Branch & Spec

**ONLY after user approval**, proceed:

1. Run the script `{SCRIPT}` from repo root and parse its JSON output for BRANCH_NAME and SPEC_FILE. All file paths must be absolute.
   **IMPORTANT** You must only ever run this script once. The JSON is provided in the terminal as output - always refer to it to get the actual content you're looking for.

2. Load `.specify/templates/spec-template.md` to understand required sections.

3. Write the specification to SPEC_FILE using the template structure:
   - Replace placeholders with concrete details from feature description
   - **If research was conducted**: Integrate research findings into:
     - Technical constraints section
     - Non-functional requirements
     - Technology recommendations (add new section if needed)
   - Preserve section order and headings
   - Mark ambiguities with `[NEEDS CLARIFICATION: question]`

4. Add complexity metadata to spec frontmatter:
   ```yaml
   complexity_level: <level>
   research_conducted: <boolean>
   multi_domain: <boolean>
   ```

5. **Create the spec file** at SPEC_FILE path

6. **If research was conducted**, create `research.md`:
   ```markdown
   # Research Findings: [Feature Title]
   
   **Date**: [Today]
   **Complexity Level**: [Level]
   **Research Passes**: [Number]
   
   ## Technology Stack Research
   
   ### [Technology 1]
   - **Version**: [Specific version]
   - **Why**: [Rationale]
   - **Source**: [URL]
   - **Notes**: [Key findings]
   
   ### [Technology 2]
   - **Version**: [Specific version]
   - **Why**: [Rationale]
   - **Source**: [URL]
   
   ## Integration Patterns
   
   ### [Integration 1]
   - **SDK**: [Specific SDK with version]
   - **Authentication**: [Method]
   - **Source**: [Official docs URL]
   - **Notes**: [Implementation notes]
   
   ## Architecture Patterns
   
   ### Recommended Pattern: [Pattern Name]
   - **Description**: [What it is]
   - **Why**: [Rationale from research]
   - **Case Study**: [URL to production example]
   - **Trade-offs**:
     - ✅ Benefits: [List]
     - ⚠️ Considerations: [List]
   
   ## Summary
   
   **Technology recommendations**:
   - [Summary list with versions]
   
   **Key architectural decisions**:
   1. [Decision with rationale]
   2. [Decision with rationale]
   ```

### Phase 6: Update Context & Report

1. **Save context** to `.specify/context.json`:
   ```json
   {
     "complexity_level": "<level>",
     "complexity_score": <number>,
     "multi_domain": <boolean>,
     "research_complete": <boolean>,
     "research_passes_completed": <number>,
     "technology_recommendations": {
       "stack": ["<tech with version>"],
       "integrations": ["<service with SDK>"]
     },
     "spec_created": true,
     "clarifications_from_specify": <number>,
     "feature_id": "<id>"
   }
   ```

2. **Report completion** with detailed summary:
   ```markdown
   ✅ **Specification Created Successfully**
   
   📄 **Location**: `specs/[feature-id]/spec.md`
   
   📊 **Details**:
   - **Complexity**: [Level] (score: [N])
   - **Research**: [Yes/No] ([N] passes, [M] sources)
   - **Technology stack**: [Tech1 vX.Y, Tech2 vA.B]
   - **Clarifications resolved**: [N]
   - **Open questions**: [N] (for /clarify)
   
   🔬 **Research Highlights** (if applicable):
   - [Key finding 1]
   - [Key finding 2]
   - [Key architectural decision]
   
   📋 **Next Steps**:
   1. **Review spec**: `cat specs/[feature-id]/spec.md`
   2. **Review research**: `cat specs/[feature-id]/research.md` (if exists)
   3. **Clarify ambiguities**: Run `/clarify` to address open questions
   4. **Create plan**: Run `/plan` for implementation approach
   
   📂 **Files Created**:
   - ✅ spec.md (main specification)
   - ✅ research.md (research findings) [if applicable]
   - ✅ .specify/context.json (workflow state)
   ```

## Agent Guidelines

1. **Be conversational**: This is a dialogue, not a form-filling exercise
2. **Show your work**: Present analysis before decisions
3. **Ask before acting**: Get user approval before creating files
4. **Research when needed**: Use web search for complex features
5. **Cite sources**: Always include URLs from research
6. **Iterate**: Refine understanding through questions
7. **Be specific**: Avoid vague recommendations ("use Express" → "Express v4.19.2")
8. **Track context**: Save state for downstream workflowsducted
- Recommended next workflow