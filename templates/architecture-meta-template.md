# Architecture Meta-Template: Research-Driven Framework Patterns

**Purpose**: Guide agents to research latest framework architecture patterns  
**Philosophy**: No embedded patterns - always research official docs for current best practices  
**Based on**: Research findings from specs/005-spec-kit-enhanced/research.md

---

## Research Workflow: Detect → Research → Document → Report

### Step 1: Detect Framework

**Run Detection Script**:
```bash
.specify/scripts/bash/detect-framework.sh --json

# Output format:
{
  "framework": "Next.js",
  "version": "15.x",
  "detected_via": "next.config.js",
  "confidence": "high"
}
```

**Manual Detection** (if script unavailable):
- Next.js: `next.config.js`, `app/` or `pages/` directory
- Django: `manage.py`, `settings.py`
- Spring Boot: `pom.xml` with `spring-boot-starter`
- FastAPI: `main.py` with `from fastapi import`
- Rails: `Gemfile` with `gem 'rails'`
- Laravel: `composer.json` with `laravel/framework`

### Step 2: Research Official Documentation

**CRITICAL**: Always use "According to [URL]" format for citations

**Research Checklist**:
- [ ] Find official documentation URL
- [ ] Identify latest stable version
- [ ] Locate architecture/structure guide
- [ ] Find best practices page
- [ ] Identify common anti-patterns
- [ ] Check for breaking changes in recent versions

**Example Research Process**:
```markdown
1. Search: "[framework name] official documentation"
2. Navigate to: Architecture / Project Structure / Best Practices
3. Identify: Recommended folder structure for [version]
4. Note: Any version-specific patterns (e.g., Next.js App Router vs Pages Router)
5. Document: With "According to [URL]" citations
```

### Step 3: Document Framework-Specific Patterns

**Template for Each Framework**:

#### Framework: [Name + Version]

**Official Documentation**: [URL]

**Recommended Folder Structure**:
```
[Copy structure from official docs]
```

**Key Patterns** (with citations):
- According to [URL], [pattern 1]
- According to [URL], [pattern 2]
- According to [URL], [pattern 3]

**Common Anti-Patterns** (with citations):
- According to [URL], avoid [anti-pattern 1]
- According to [URL], avoid [anti-pattern 2]

**Version-Specific Notes**:
- [Version X]: [Specific pattern or breaking change]
- [Version Y]: [New feature or deprecation]

### Step 4: Report Deviations

**Compare Project vs Official Patterns**:
- [ ] Folder structure matches official recommendations?
- [ ] Naming conventions follow best practices?
- [ ] File organization aligns with framework patterns?
- [ ] No anti-patterns detected?

**Deviation Report Template**:
```markdown
## Architecture Deviations

### High Priority (Anti-patterns detected)
1. **Issue**: [Description]
   - Current: [What project does]
   - Recommended: According to [URL], [official pattern]
   - Impact: [Why this matters]
   - Fix: [Specific refactoring steps]

### Medium Priority (Suboptimal patterns)
1. **Issue**: [Description]
   - Current: [What project does]
   - Recommended: According to [URL], [better pattern]
   - Impact: [Performance/maintainability concern]
   - Fix: [Refactoring suggestion]

### Low Priority (Style preferences)
1. **Issue**: [Description]
   - Current: [What project does]
   - Alternative: According to [URL], [alternative pattern]
   - Impact: [Minor improvement]
```

---

## Framework-Specific Research Guides

### Next.js (App Router - 2025)

**Official Docs**: https://nextjs.org/docs

**Research Focus**:
1. **Route Groups**: `(folder)` syntax for organization without URL impact
2. **Private Folders**: `_components` for route-specific code
3. **Server/Client Boundaries**: `lib/server` vs `lib/client` separation
4. **Metadata Files**: `layout.tsx`, `page.tsx`, `loading.tsx`, `error.tsx`
5. **Colocation**: Keep route logic with route files

**Key Search Terms**:
- "Next.js App Router folder structure"
- "Next.js 15 best practices"
- "Next.js route groups"
- "Next.js server components architecture"

**Expected Findings** (validate with current docs):
```
src/
├── app/                    # App Router (routing only)
│   ├── (marketing)/        # Route group (no URL impact)
│   ├── (auth)/
│   │   ├── login/
│   │   └── register/
│   ├── dashboard/
│   │   ├── _components/    # Private folder (route-specific)
│   │   ├── layout.tsx
│   │   └── page.tsx
│   └── api/                # API routes
├── components/             # Shared components
│   ├── ui/                 # Reusable UI primitives
│   ├── features/           # Feature-specific components
│   └── common/             # Cross-feature components
├── lib/                    # Utilities and configs
│   ├── server/             # Server-only code (CRITICAL)
│   └── client/
├── hooks/                  # Custom React hooks
└── services/               # Business logic, API calls
```

**Anti-Patterns to Check**:
- "Everything in Pages" syndrome (old Next.js habit)
- 200+ files in single `/components` folder
- Mixed server/client code without clear boundaries

### Django

**Official Docs**: https://docs.djangoproject.com/

**Research Focus**:
1. **App Structure**: One app per feature/domain
2. **Settings Organization**: Split settings for dev/prod
3. **URL Configuration**: App-level URLconfs
4. **Model Organization**: Fat models, thin views
5. **Template Structure**: App-level templates

**Key Search Terms**:
- "Django project structure best practices"
- "Django app organization"
- "Django settings.py structure"

**Expected Findings** (validate with current docs):
```
project/
├── manage.py
├── project/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/users/
│   └── blog/
│       ├── models.py
│       ├── views.py
│       └── urls.py
└── static/
```

### Spring Boot

**Official Docs**: https://spring.io/guides

**Research Focus**:
1. **Package Structure**: Domain-driven organization
2. **Layer Separation**: Controller → Service → Repository
3. **Configuration**: `application.yml` vs `application.properties`
4. **Component Scanning**: Package naming conventions

**Key Search Terms**:
- "Spring Boot project structure"
- "Spring Boot package organization"
- "Spring Boot best practices"

### FastAPI

**Official Docs**: https://fastapi.tiangolo.com/

**Research Focus**:
1. **Router Organization**: Feature-based routers
2. **Dependency Injection**: Depends() pattern
3. **Model Structure**: Pydantic models
4. **Async Patterns**: async/await best practices

**Key Search Terms**:
- "FastAPI project structure"
- "FastAPI folder organization"
- "FastAPI best practices"

---

## Research Validation Checklist

Before documenting architecture patterns:
- [ ] Official documentation URL verified (not third-party blog)
- [ ] Version-specific patterns confirmed (check for latest version)
- [ ] All patterns cited with "According to [URL]"
- [ ] Anti-patterns documented with sources
- [ ] Breaking changes noted for version migrations
- [ ] Alternative patterns researched (if multiple valid approaches)

---

## Integration with /plan Workflow

**In plan.md, replace embedded patterns with**:

```markdown
## Architecture Patterns

**Framework Detected**: [Name + Version]  
**Detection Method**: [Script output or manual detection]  
**Confidence**: [High/Medium/Low]

**Research Conducted**:
- Official Docs: [URL]
- Best Practices: [URL]
- Latest Version: [URL]

**Recommended Structure**:
According to [URL], the recommended folder structure for [Framework Version] is:
[Copy structure from official docs]

**Key Patterns**:
1. According to [URL], [pattern with explanation]
2. According to [URL], [pattern with explanation]

**Anti-Patterns to Avoid**:
1. According to [URL], avoid [anti-pattern with reason]
2. According to [URL], avoid [anti-pattern with reason]

**Project Deviations**:
[Use deviation report template from Step 4]

**Refactoring Recommendations**:
[Prioritized list of changes to align with official patterns]
```

---

## Example: Next.js 15 App Router Research

**Step 1: Detect**
```bash
$ .specify/scripts/bash/detect-framework.sh --json
{
  "framework": "Next.js",
  "version": "15.0.0",
  "detected_via": "next.config.js + app/ directory",
  "confidence": "high"
}
```

**Step 2: Research**
- Official Docs: https://nextjs.org/docs/app/building-your-application/routing
- Search: "Next.js 15 App Router folder structure best practices"
- Found: Route groups, private folders, server/client boundaries

**Step 3: Document**
```markdown
## Next.js 15 App Router Architecture

According to https://nextjs.org/docs/app/building-your-application/routing/route-groups, 
route groups in Next.js 15 use parentheses (folder) to organize routes without affecting the URL structure.

According to https://nextjs.org/docs/app/building-your-application/routing/colocation#private-folders,
private folders prefixed with underscore (_components) are excluded from routing and used for route-specific code.

According to https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns#keeping-server-only-code-out-of-the-client-environment,
server-only code MUST be separated into lib/server to prevent accidental client-side imports.
```

**Step 4: Report Deviations**
```markdown
## Architecture Deviations

### High Priority
1. **Mixed Server/Client Code**
   - Current: Server utilities in lib/utils.ts imported by client components
   - Recommended: According to [URL], separate into lib/server and lib/client
   - Impact: Risk of exposing server secrets to client bundle
   - Fix: Move server utilities to lib/server, add 'server-only' package

### Medium Priority
1. **Flat Component Structure**
   - Current: All components in single components/ folder (200+ files)
   - Recommended: According to [URL], organize by feature or UI/common/features
   - Impact: Difficult to navigate, unclear component ownership
   - Fix: Reorganize into components/ui, components/features, components/common
```

---

## Continuous Updates

**Framework versions change** - This meta-template ensures:
- ✅ Always research latest official docs
- ✅ No outdated embedded patterns
- ✅ Version-specific guidance
- ✅ Citations for all recommendations
- ✅ Easy to update (just research again)

**When to Re-Research**:
- Major version upgrade detected
- New framework features announced
- Official docs updated (check quarterly)
- Anti-patterns discovered in code review

---

*This meta-template replaces embedded framework patterns in plan-template.md*  
*Always research official docs - never rely on outdated embedded structures*  
*Based on Next.js 2025 research - see specs/005-spec-kit-enhanced/research.md*
