# Conversational Mode Upgrade: /specify Workflow v2.2

**Date**: 2025-09-30  
**Based on**: Real Claude Code feedback  
**Status**: ✅ Implemented

---

## Problem Identified

When testing the orchestration system with Claude Code, the `/specify` workflow immediately created `spec.md` without:
1. ❌ Presenting understanding to user
2. ❌ Asking clarifying questions  
3. ❌ Showing research findings
4. ❌ Getting user approval
5. ❌ Iterating on requirements

**Result**: Spec was created but felt automated and non-interactive.

---

## Solution: Conversational Mode

Redesigned `/specify` workflow to be **conversation-first, spec-last**:

### New Workflow Phases

```
Phase 1: Analyze & Understand
├─ Detect complexity (auto, fallback to manual)
├─ Present initial understanding
└─ Wait for user feedback

Phase 2: Research & Discovery (if complex)
├─ Inform user about research needs
├─ Ask permission to proceed
├─ Conduct web searches (3 passes)
├─ Present findings with sources
└─ Wait for user feedback

Phase 3: Clarifying Questions
├─ Ask 3-5 targeted questions
├─ Based on complexity level
└─ Wait for user responses

Phase 4: Synthesis & Preview
├─ Summarize everything learned
├─ Show what will go in spec
├─ Ask for approval
└─ Wait for user confirmation

Phase 5: Create Spec (ONLY AFTER APPROVAL)
├─ Run create-new-feature.sh
├─ Load spec-template.md
├─ Fill template with gathered info
├─ Create research.md if applicable
└─ Save context.json

Phase 6: Report & Next Steps
├─ Show summary of what was created
├─ Highlight key decisions
└─ Recommend next workflow
```

---

## Key Changes

### 1. **Manual Complexity Fallback**

**Problem**: `detect-complexity.sh` fails silently

**Solution**: Workflow now includes manual complexity scoring:

```markdown
If script fails, analyze manually based on these indicators:
- Technology stack mentions (databases, APIs, frameworks) → ×2
- Integration requirements (third-party, payments, auth) → ×3
- Architecture needs (real-time, scalable, distributed) → ×4
- Complexity keywords (complex, enterprise, multi-tenant) → ×1

Score ≥10 = HIGH, ≥5 = MEDIUM, ≥2 = LOW-MEDIUM, <2 = LOW
```

### 2. **Present Understanding First**

**Before**: Jump to spec creation

**After**: Show analysis and wait for feedback:

```markdown
📊 **Feature Understanding**

I understand you want to build: [restate in own words]

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

### 3. **Ask Permission for Research**

**Before**: Auto-trigger research (confusing)

**After**: Explain why and ask:

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

### 4. **Show Research Progress**

**Before**: Research happens silently

**After**: Show what's being searched:

```markdown
🔬 **Researching...**

Pass 1: Technology Stack
- Searching: "WebRTC best practices 2025"
- Searching: "real-time voice communication frameworks"
→ Finding: WebRTC v1.0 spec with Safari support [URL]

Pass 2: Integration Patterns
- Searching: "AI tutoring system architecture"
- Searching: "educational AI agent management"
→ Finding: OpenAI Assistants API for agent spawning [URL]

Pass 3: Architecture
- Searching: "multimedia streaming platform patterns"
- Searching: "scalable voice infrastructure"
→ Finding: Agora.io case study for education [URL]
```

### 5. **Present Findings with Sources**

**Before**: Research results hidden

**After**: Show findings before using them:

```markdown
✅ **Research Complete**

**Technology Recommendations**:
- **WebRTC v1.0**: Modern browser support, low latency [MDN URL]
- **OpenAI Assistants API v2**: Agent spawning and management [OpenAI Docs]
- **Agora SDK v4.2**: Voice infrastructure with education focus [Agora Case Study]

**Architecture Pattern**: Event-driven microservices
- Based on: Coursera's real-time tutoring architecture [Coursera Tech Blog]
- Benefits: Scalable, agent isolation, independent scaling
- Trade-offs: Increased complexity, network latency

**Integration Approach**: WebSocket + REST hybrid
- Real-time: WebSocket for voice/cursor
- Management: REST for agent CRUD
- Reference: [Pusher architecture guide URL]

**Questions before we finalize**:
1. Expected concurrent students per session?
2. Voice quality requirements (bandwidth, latency)?
3. Content moderation needs for AI tutors?
```

### 6. **Ask Clarifying Questions**

**Before**: Create spec with unknowns

**After**: Ask targeted questions based on complexity:

```markdown
🤔 **A few questions to help me create the best spec**:

1. **Scale**: How many concurrent tutoring sessions do you expect?
2. **Voice Quality**: Acceptable latency for voice? (100ms, 250ms, 500ms?)
3. **AI Agents**: How many AI tutor types? (One general vs specialized per subject)
4. **Multimedia**: What types? (Video, images, PDFs, interactive simulations?)
5. **Platform**: Web-only or mobile apps needed?

Feel free to answer what you know - we can refine during /clarify later!
```

### 7. **Preview Before Creating**

**Before**: Create spec immediately

**After**: Show preview and ask approval:

```markdown
📝 **Specification Preview**

Based on our conversation, here's what I'll include in the spec:

**Feature**: Knowledge Synthesis Studio
**Complexity**: HIGH
**Technology Stack** (researched):
- WebRTC v1.0 for real-time voice
- OpenAI Assistants API v2 for AI tutors
- Agora SDK v4.2 for voice infrastructure
- Next.js v14 + tRPC for web framework

**Core Requirements**:
1. Spawn AI tutors on demand for any school subject
2. Real-time voice communication (<250ms latency)
3. Multimedia content integration (video, PDFs, interactive)
4. Multi-user sessions (student + up to 3 AI tutors)

**Architecture**:
- Pattern: Event-driven microservices
- Rationale: Allows independent scaling of AI agents and voice infrastructure

**Open Questions** (for /clarify phase):
1. Content moderation policy for AI tutor responses?
2. Session recording/replay requirements?
3. Integration with existing LMS systems?

**Does this look good? I'll create the formal spec if you approve. [Y/n]**
```

### 8. **Template Integration**

**Before**: Didn't use spec-template.md properly

**After**: Explicitly load and fill template:

```yaml
---
feature_id: 001
title: Knowledge Synthesis Studio
status: draft
created: 2025-09-30
version: 0.1.0
complexity_level: high
research_conducted: true
multi_domain: true
technology_recommendations:
  - WebRTC v1.0
  - OpenAI Assistants API v2
  - Agora SDK v4.2
  - Next.js v14.2.0
---

# Feature Description
[From conversation]

# User Stories
[Generated from discussion]

# Requirements
## Functional
[From feature description]

## Non-Functional
[From clarifying questions - performance, scale]

## Technical
[From research findings - with sources]

# Technical Constraints
## Technology Stack
- **WebRTC v1.0**: [Why + URL]
- **OpenAI Assistants API v2**: [Why + URL]

## Integration Approach
[From research with citations]

# Success Criteria
[From user responses]

# Clarifications Needed
### Session 1: Initial Specification (2025-09-30)

**Resolved**:
- Q: Expected concurrent sessions?
- A: Start with 100, scale to 10K

**Unresolved** (for /clarify):
- [ ] Content moderation policy?
- [ ] Session recording requirements?
```

---

## Expected Claude Code Behavior (New)

When user runs: `/specify "complex feature description"`

**Step 1**: Claude analyzes and presents understanding
```
📊 Feature Understanding

I understand you want to build: A knowledge synthesis studio...

Complexity Analysis:
- Level: HIGH
- Technology areas: real-time voice, AI agents, multimedia
- Integration points: OpenAI, voice infrastructure
- Architecture concerns: scalability, latency, agent management

My initial thoughts:
- Real-time voice is challenging - need <250ms latency
- AI agent spawning requires robust orchestration
- Multimedia delivery needs CDN strategy
- Open question: How many subjects? One generalist or many specialists?
```

**Step 2**: User provides feedback or asks questions

**Step 3**: If HIGH complexity, Claude asks permission for research
```
🔍 Research Needed

This feature requires:
1. Real-time voice technology research (WebRTC, Agora, Twilio)
2. AI agent orchestration patterns (OpenAI Assistants, LangChain)
3. Educational platform architecture (case studies)

Proceed with research? [Y/n]
```

**Step 4**: User approves, Claude researches (with visible progress)

**Step 5**: Claude presents findings with sources

**Step 6**: Claude asks clarifying questions

**Step 7**: User answers questions

**Step 8**: Claude shows preview

**Step 9**: User approves

**Step 10**: Claude creates spec.md + research.md

**Step 11**: Claude reports completion with next steps

---

## Files Modified

### Primary Changes

1. **`templates/commands/specify.md`** ⚡ (357 lines, was 265)
   - Added conversational mode phases
   - Manual complexity fallback
   - Research approval flow
   - Clarifying questions framework
   - Preview + approval gate
   - Detailed template filling instructions
   - Agent guidelines section

### Supporting Files

2. **`test-orchestration-demo/.claude/commands/specify.md`** (updated)
3. **`test-orchestration-demo/.specify/templates/commands/specify.md`** (updated)

---

## Testing the New Workflow

### Test Case 1: Simple Feature (No Research)

**Command**: `/specify "add user profile settings page"`

**Expected Flow**:
1. Analyze: LOW complexity
2. Present understanding
3. Ask 3 basic questions (scope, users, success)
4. Show preview
5. Create spec (no research)

**Duration**: ~2 minutes

### Test Case 2: Medium Complexity (Optional Research)

**Command**: `/specify "REST API with JWT authentication and PostgreSQL"`

**Expected Flow**:
1. Analyze: MEDIUM complexity
2. Present understanding
3. Offer research (user can decline)
4. If researched: Show JWT + PostgreSQL versions
5. Ask 4-5 questions
6. Show preview with tech recommendations
7. Create spec + research.md

**Duration**: ~5 minutes (with research)

### Test Case 3: High Complexity (Required Research) **Command**: `/specify "knowledge synthesis studio with AI tutors and real-time voice"`

**Expected Flow**:
1. Analyze: HIGH complexity
2. Present understanding with concerns
3. Ask permission for research
4. Research 3 passes:
   - WebRTC/voice technologies
   - AI agent orchestration
   - Educational platform architecture
5. Present findings with URLs
6. Ask 5 targeted questions
7. Show comprehensive preview
8. Create spec + research.md

**Duration**: ~10-15 minutes

---

## Comparison: Before vs After

| Aspect | Before (v2.1) | After (v2.2) |
|--------|--------------|--------------|
| **User Interaction** | None until spec created | Conversation throughout |
| **Complexity Detection** | Auto-only (failed silently) | Auto + manual fallback |
| **Research** | Auto-triggered (confusing) | Permission-based |
| **Questions** | None | 3-5 targeted questions |
| **Preview** | None | Full preview before creating |
| **Approval** | None | Explicit user approval |
| **Template Usage** | Partial | Full integration |
| **Source Citations** | Missing | URLs for all research |
| **Context Tracking** | Basic | Detailed with counts |
| **Iteration** | One-shot | Multi-turn conversation |

---

## Constitutional Compliance

✅ **Principle IV: Agent-Native Execution**
- Conversational mode leverages agent's dialogue capabilities
- Web search integration for research
- Multi-turn interaction supported

✅ **Principle IX: Complexity-Driven Research**
- Manual fallback ensures complexity always detected
- Research is permission-based and visible
- Findings presented before use

✅ **Principle VI: Governance Balance**
- Non-blocking: User can decline research
- User approves spec before creation
- Iterative refinement supported

---

## Next Steps

1. ✅ Test new workflow with Claude Code
2. ⏳ Gather user feedback on conversation flow
3. ⏳ Tune question templates based on usage
4. ⏳ Add more domain-specific question sets
5. ⏳ Create conversation examples library

---

## Status: ✅ Ready for Testing

The `/specify` workflow is now conversational, iterative, and respects user agency. 

**Test it**: Navigate to `test-orchestration-demo/` and run:
```bash
claude /specify "your complex feature description"
```

**Watch for**:
- Initial understanding presentation
- Research permission request
- Visible research progress
- Targeted clarifying questions
- Preview before spec creation
- User approval gates

**The workflow is now truly conversational!** 🎉
