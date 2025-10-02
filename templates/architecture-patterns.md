# Framework Architecture Patterns Reference

**Purpose**: Validate common framework patterns  
**Updated**: 2025-09-30

<!-- 
AGENT GUIDANCE:
Use during brownfield analysis or planning. Compare actual vs expected structure.
Always verify against official documentation—frameworks evolve quickly!
-->

## Tier 1: JavaScript/TypeScript

### Next.js (App Router v13+)
```
app/
├── layout.tsx         # Root layout (required)
├── page.tsx          # Home page
├── [feature]/        # Feature folders
│   └── page.tsx
└── api/              # API routes
    └── [route]/route.ts

components/           # Shared components
lib/                 # Utilities
public/              # Static assets
next.config.js       # Config (required)
```

**Key Files**: next.config.js, tsconfig.json  
**Docs**: https://nextjs.org/docs

---

## Tier 1: Python

### Django
```
project_name/
├── settings.py      # Configuration
├── urls.py          # URL routing
├── wsgi.py          # WSGI entry
└── asgi.py          # ASGI entry

app_name/
├── models.py        # Data models
├── views.py         # Views
├── urls.py          # App URLs
└── migrations/      # DB migrations

manage.py            # Management (required)
```

**Key Files**: manage.py, settings.py  
**Docs**: https://docs.djangoproject.com

### FastAPI
```
app/
├── main.py          # FastAPI app entry
├── api/v1/          # API versioning
│   └── endpoints/
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas
├── crud/            # DB operations
└── core/config.py   # Settings

requirements.txt
```

**Key Files**: main.py, core/config.py  
**Docs**: https://fastapi.tiangolo.com

---

## Tier 1: Java

### Spring Boot
```
src/main/
├── java/com/company/project/
│   ├── ProjectApplication.java  # Main (required)
│   ├── controller/              # REST controllers
│   ├── service/                 # Business logic
│   ├── repository/              # Data access
│   ├── model/                   # Entities
│   └── config/                  # Configuration
└── resources/
    └── application.properties   # or .yml

pom.xml              # Maven
```

**Key Files**: pom.xml, Application.java, application.properties  
**Docs**: https://spring.io/projects/spring-boot

---

## Validation Workflow

1. **Identify Framework**: Check package files
2. **Locate Pattern**: Find in this document
3. **Compare**: Actual vs expected structure
4. **Research Deviations**: Intentional or anti-pattern?
5. **Verify Version**: Check for version-specific changes
6. **Document**: Record in brownfield-analysis.md

---

*Full patterns available in `.specify/templates/architecture-patterns.md`*
