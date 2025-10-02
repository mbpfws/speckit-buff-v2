# Agent Prompt Engineering Patterns

**Purpose**: Reduce AI hallucinations and improve context management  
**Based on**: Research findings from specs/005-spec-kit-enhanced/research.md  
**Effectiveness**: 30% hallucination reduction with "According to..." prompting

---

## Pattern 1: "According to..." Prompting

**Goal**: Force citation of sources, reduce hallucinations by 30%

**Template**:
```
According to [SOURCE_URL], [FACT_OR_FINDING].

Example:
"According to https://nextjs.org/docs/app/building-your-application/routing/route-groups, 
route groups in Next.js 15 use parentheses (folder) to organize routes without affecting the URL structure."
```

**When to Use**:
- All research-driven responses
- Technical recommendations
- Framework best practices
- Dependency version suggestions

**Implementation**:
```markdown
<!-- Agent instruction in templates -->
CRITICAL: All research findings MUST use "According to [URL]" format.
Never state facts without citations.
```

---

## Pattern 2: Chain-of-Verification (CoVe)

**Goal**: Model generates response, then verifies its own output

**Process**:
1. **Generate**: Create initial response
2. **Question**: Generate verification questions about the response
3. **Answer**: Answer verification questions independently
4. **Verify**: Check for inconsistencies between original and verification
5. **Refine**: Correct any inconsistencies found

**Template**:
```
Step 1 - Initial Response:
[Your response here]

Step 2 - Verification Questions:
Q1: Is [claim from response] accurate?
Q2: Does [statement] contradict [other statement]?
Q3: Are there edge cases not covered?

Step 3 - Verification Answers:
A1: [Independent verification]
A2: [Check for contradictions]
A3: [Identify gaps]

Step 4 - Refined Response:
[Corrected response incorporating verification]
```

**When to Use**:
- Complex technical decisions
- Multi-step workflows
- Architecture recommendations
- Dependency conflict resolution

**Expected Outcome**: Reduces error rate from 53% to 23% (GPT-4o research data)

---

## Pattern 3: Step-Back Prompting

**Goal**: Ask high-level questions before specific ones

**Process**:
1. **Step Back**: Ask broader, conceptual question first
2. **Context**: Gather high-level understanding
3. **Step Forward**: Ask specific question with context
4. **Answer**: Provide detailed answer grounded in concepts

**Template**:
```
Step-Back Question: "What are the general principles of [domain]?"
→ Answer: [High-level concepts]

Specific Question: "How should I implement [specific feature]?"
→ Answer: [Detailed implementation using concepts from step-back]
```

**Example**:
```
Step-Back: "What are the general principles of Next.js App Router architecture?"
→ Server components by default, client components opt-in, route groups for organization

Specific: "How should I structure a Next.js dashboard with auth?"
→ Use route groups (auth) and (dashboard), server components for data fetching, 
  client components only for interactive elements
```

**When to Use**:
- Unfamiliar frameworks
- Complex architecture decisions
- When user lacks domain knowledge (novice tier)
- Before generating detailed implementation plans

---

## Pattern 4: Context Engineering

**Goal**: Structured context injection with real-time data grounding

**Template**:
```yaml
context:
  project_type: [greenfield|brownfield]
  complexity_tier: [novice|intermediate|expert]
  tech_stack:
    - framework: [name + version]
    - dependencies: [key deps with versions]
  constraints:
    - [constraint 1]
    - [constraint 2]
  real_time_data:
    - source: [URL or script output]
    - data: [JSON or structured data]
```

**Implementation in Spec-Kit**:
```markdown
<!-- Load context from .specify/context.json -->
<!-- Inject into agent instructions -->
<!-- Ground responses in project-specific data -->
```

**When to Use**:
- Beginning of every workflow (/specify, /plan, /tasks)
- After running helper scripts (analyze-codebase.sh, check-dependencies.sh)
- When switching between documents (spec.md → plan.md → tasks.md)

---

## Pattern 5: Metamorphic Prompt Mutations

**Goal**: Detect inconsistencies across rephrasings

**Process**:
1. **Original Prompt**: Ask question in original form
2. **Rephrase**: Ask same question 2-3 different ways
3. **Compare**: Check if answers are consistent
4. **Flag**: If inconsistent, mark as low confidence

**Template**:
```
Original: "What's the latest stable version of React?"
Rephrase 1: "Which React version should I use for production?"
Rephrase 2: "What React version is currently recommended?"

If answers differ → Low confidence, require web research
If answers match → Higher confidence, but still verify with "According to..."
```

**When to Use**:
- Critical version decisions
- Breaking change detection
- Security vulnerability assessment
- When user input is ambiguous

---

## Pattern 6: Reward Models (Encourage "I don't know")

**Goal**: Prefer "I don't know" over guessing

**Template**:
```
If uncertain:
✅ "I don't know the latest version. Let me research: [web search]"
❌ "The latest version is probably X.Y.Z" (hallucination risk)

If partially certain:
✅ "Based on [SOURCE], version X.Y is latest, but let me verify: [search]"
❌ "Version X.Y is latest" (no citation)
```

**Implementation**:
```markdown
<!-- Agent instruction -->
CRITICAL: If you don't have definitive information, say "I don't know" 
and conduct web research. Never guess version numbers, API endpoints, 
or configuration details.
```

**When to Use**:
- All technical recommendations
- Version-specific questions
- API/configuration details
- Framework-specific patterns

---

## Pattern 7: Temperature Control

**Goal**: Lower temperature = less hallucination (but less creativity)

**Guidance**:
- **Temperature 0.0-0.3**: Factual responses, version numbers, API docs
- **Temperature 0.4-0.7**: Balanced (default for most spec-kit workflows)
- **Temperature 0.8-1.0**: Creative tasks (naming, brainstorming)

**Spec-Kit Defaults**:
```yaml
workflows:
  /specify: 0.7  # Balanced creativity + accuracy
  /clarify: 0.5  # More factual, less creative
  /plan: 0.6     # Slightly creative for architecture
  /tasks: 0.4    # More structured, less creative
  /implement: 0.3  # Highly factual, minimal hallucination
```

---

## Integration with Spec-Kit Workflows

### In `/specify` Workflow:
```markdown
1. Use "According to..." for all research
2. Apply Step-Back for complex features
3. Load context from .specify/context.json
4. Encourage "I don't know" + web research
```

### In `/plan` Workflow:
```markdown
1. Use CoVe for architecture decisions
2. Apply Context Engineering with plan.md data
3. Use "According to..." for framework patterns
4. Metamorphic mutations for critical tech choices
```

### In `/analyze-brownfield` Workflow:
```markdown
1. Use "According to..." for framework validation
2. Apply CoVe for confidence level assessment
3. Context Engineering with analyze-codebase.sh output
4. Step-Back for unfamiliar tech stacks
```

---

## Validation Checklist

Before finalizing any response:
- [ ] All facts cited with "According to [URL]"
- [ ] No version numbers without source
- [ ] No API details without documentation link
- [ ] Uncertainties marked with "I don't know" + research plan
- [ ] Complex decisions verified with CoVe
- [ ] High-level context established with Step-Back (for novice tier)

---

## Expected Outcomes

**With Patterns Applied**:
- ✅ 30% reduction in hallucinations ("According to..." prompting)
- ✅ 53% → 23% error rate (Reward models encouraging "I don't know")
- ✅ Improved consistency across rephrasings (Metamorphic mutations)
- ✅ Better grounding in real-time data (Context Engineering)

**Without Patterns**:
- ❌ Higher hallucination rate
- ❌ Inconsistent responses
- ❌ Version number guesses
- ❌ Ungrounded recommendations

---

*Based on 2025 AI research - see specs/005-spec-kit-enhanced/research.md for sources*
