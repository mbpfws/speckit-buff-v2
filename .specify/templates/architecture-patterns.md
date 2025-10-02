# Framework Architecture Patterns & Validation

**Purpose**: Reference guide for validating common framework patterns and folder structures  
**Last Updated**: 2025-09-30

<!-- 
AGENT GUIDANCE:
Use this template when analyzing or designing projects with well-known frameworks.
For each framework:
1. Check if current project matches the standard pattern
2. Research latest version if pattern seems outdated
3. Document deviations and assess if intentional or problematic
4. Provide recommendations based on official documentation
-->

---

## How to Use This Template

### During Brownfield Analysis
1. Identify the framework (from package.json, dependencies, etc.)
2. Find the framework section below
3. Compare actual project structure with documented pattern
4. Note deviations in brownfield-analysis.md
5. Research if deviations are recommended or anti-patterns

### During Planning
1. Review the framework's standard pattern
2. Verify pattern matches project requirements
3. Check for latest version changes (research!)
4. Adapt pattern to project-specific needs
5. Document intentional deviations in plan.md

### Validation Checklist for Any Framework
- [ ] Folder structure follows documented conventions?
- [ ] Key configuration files present?
- [ ] Framework version is supported (not EOL)?
- [ ] Dependencies align with framework requirements?
- [ ] Entry points correctly structured?

---

## Tier 1: JavaScript/TypeScript Frameworks

### Next.js (React Framework)

**Framework**: Next.js  
**Official Docs**: https://nextjs.org/docs  
**Current Version**: 14.x (as of 2025-09-30)  
**Confidence**: Verify version at https://nextjs.org

#### Standard App Router Structure (v13+)
```
project-root/
├── app/                      # App Router (v13+)
│   ├── layout.tsx           # Root layout (required)
│   ├── page.tsx             # Home page
│   ├── globals.css          # Global styles
│   ├── [feature]/           # Feature folder
│   │   ├── page.tsx         # Feature page
│   │   └── layout.tsx       # Feature layout (optional)
│   ├── api/                 # API routes
│   │   └── [route]/
│   │       └── route.ts     # API handler
│   └── components/          # Shared components (alternative)
├── components/              # Shared React components
├── lib/                     # Utility functions
├── public/                  # Static assets
├── styles/                  # Additional styles (optional)
├── next.config.js           # Next.js configuration
├── package.json
└── tsconfig.json            # TypeScript config
```

#### Standard Pages Router Structure (Legacy but still supported)
```
project-root/
├── pages/                   # Pages Router (legacy)
│   ├── _app.tsx            # Custom App
│   ├── _document.tsx       # Custom Document
│   ├── index.tsx           # Home page
│   ├── [feature]/          # Dynamic routes
│   │   └── [id].tsx
│   └── api/                # API routes
│       └── [route].ts
├── components/             # React components
├── public/                 # Static files
├── styles/                 # CSS modules
├── lib/                    # Utilities
├── next.config.js
└── package.json
```

#### Key Configuration Files
- **next.config.js**: Framework configuration (required)
- **tsconfig.json**: TypeScript configuration (if using TS)
- **.env.local**: Environment variables (not committed)
- **middleware.ts**: Edge middleware (optional, in root or app/)

#### Validation Questions
- [ ] Using App Router (app/) or Pages Router (pages/)?
- [ ] Are Server Components used correctly? (default in App Router)
- [ ] Is data fetching done at component level or page level?
- [ ] Are API routes in correct location? (app/api/ or pages/api/)
- [ ] Is next.config.js present with proper configuration?

#### Research Checklist
- [ ] Check latest stable version: https://nextjs.org/blog
- [ ] Review App Router vs Pages Router decision
- [ ] Verify Server Components best practices
- [ ] Check for breaking changes since project version

---

### React (Library - Not Framework)

**Library**: React  
**Official Docs**: https://react.dev  
**Current Version**: 18.x (as of 2025-09-30)

#### Standard CRA/Vite Structure
```
project-root/
├── src/
│   ├── components/         # Reusable components
│   ├── pages/              # Page components
│   ├── hooks/              # Custom hooks
│   ├── utils/              # Utility functions
│   ├── services/           # API services
│   ├── contexts/           # React contexts
│   ├── assets/             # Images, fonts, etc.
│   ├── App.tsx             # Root component
│   ├── index.tsx           # Entry point
│   └── index.css           # Global styles
├── public/                 # Static assets
├── package.json
└── vite.config.ts or       # Build tool config
    craco.config.js
```

#### Key Configuration Files
- **package.json**: Must include react and react-dom
- **vite.config.ts** or **webpack.config.js**: Build configuration
- **tsconfig.json**: TypeScript config (if applicable)

---

### Vue.js

**Framework**: Vue.js  
**Official Docs**: https://vuejs.org  
**Current Version**: 3.x (as of 2025-09-30)

#### Standard Vue 3 Structure
```
project-root/
├── src/
│   ├── components/         # Vue components
│   ├── views/              # Page-level components
│   ├── router/             # Vue Router config
│   │   └── index.ts
│   ├── stores/             # Pinia stores (Vue 3)
│   ├── composables/        # Composition API functions
│   ├── assets/             # Static assets
│   ├── App.vue             # Root component
│   └── main.ts             # Entry point
├── public/                 # Public assets
├── vite.config.ts          # Vite config (common)
└── package.json
```

#### Key Configuration Files
- **vite.config.ts** or **vue.config.js**: Build config
- **tsconfig.json**: TypeScript config
- **router/index.ts**: Vue Router configuration

---

## Tier 1: Python Frameworks

### Django (Full-Stack Framework)

**Framework**: Django  
**Official Docs**: https://docs.djangoproject.com  
**Current Version**: 5.x (as of 2025-09-30)

#### Standard Django Project Structure
```
project-root/
├── project_name/           # Project settings
│   ├── __init__.py
│   ├── settings.py         # Configuration
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI entry
│   └── asgi.py             # ASGI entry (async)
├── app_name/               # Django app
│   ├── migrations/         # Database migrations
│   ├── __init__.py
│   ├── admin.py            # Admin interface
│   ├── apps.py             # App configuration
│   ├── models.py           # Data models
│   ├── views.py            # View functions/classes
│   ├── urls.py             # App URLs
│   ├── serializers.py      # DRF serializers (if using)
│   └── tests.py            # Tests
├── static/                 # Static files
├── templates/              # HTML templates
├── media/                  # User-uploaded files
├── manage.py               # Management script
└── requirements.txt        # Dependencies
```

#### Key Configuration Files
- **settings.py**: INSTALLED_APPS, MIDDLEWARE, DATABASES, etc.
- **manage.py**: Django management interface (required)
- **requirements.txt** or **pyproject.toml**: Dependencies
- **.env**: Environment variables (not committed)

#### Validation Questions
- [ ] Is manage.py executable and functional?
- [ ] Are all apps listed in INSTALLED_APPS?
- [ ] Is database configured properly in settings.py?
- [ ] Are migrations up to date?
- [ ] Is Django REST Framework used? (Check for serializers.py)

---

### FastAPI (API Framework)

**Framework**: FastAPI  
**Official Docs**: https://fastapi.tiangolo.com  
**Current Version**: 0.110+ (as of 2025-09-30)

#### Standard FastAPI Project Structure
```
project-root/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI application entry
│   ├── api/                # API routes
│   │   ├── __init__.py
│   │   ├── v1/             # API version
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/  # Route handlers
│   │   │   └── api.py      # API router
│   ├── models/             # Pydantic models / SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── crud/               # Database operations
│   ├── db/                 # Database configuration
│   │   ├── base.py
│   │   └── session.py
│   ├── core/               # Configuration
│   │   ├── config.py
│   │   └── security.py
│   └── tests/              # Tests
├── alembic/                # Database migrations (if using Alembic)
├── requirements.txt
└── pyproject.toml          # If using Poetry
```

#### Key Configuration Files
- **main.py**: FastAPI() app initialization
- **core/config.py**: Settings (often using pydantic BaseSettings)
- **requirements.txt** or **pyproject.toml**: Dependencies
- **alembic.ini**: Alembic migrations (if applicable)

---

### Flask (Micro Framework)

**Framework**: Flask  
**Official Docs**: https://flask.palletsprojects.com  
**Current Version**: 3.x (as of 2025-09-30)

#### Standard Flask Application Structure
```
project-root/
├── app/
│   ├── __init__.py         # App factory
│   ├── routes/             # Route blueprints
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── api.py
│   ├── models/             # Database models
│   ├── templates/          # Jinja2 templates
│   ├── static/             # Static files
│   └── utils/              # Utilities
├── migrations/             # Flask-Migrate (Alembic)
├── tests/
├── config.py               # Configuration
├── requirements.txt
└── run.py or wsgi.py       # Entry point
```

---

## Tier 1: Java/JVM Frameworks

### Spring Boot

**Framework**: Spring Boot  
**Official Docs**: https://spring.io/projects/spring-boot  
**Current Version**: 3.x (as of 2025-09-30)

#### Standard Spring Boot Maven Structure
```
project-root/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/company/project/
│   │   │       ├── ProjectApplication.java  # Main class
│   │   │       ├── controller/              # REST controllers
│   │   │       ├── service/                 # Business logic
│   │   │       ├── repository/              # Data access
│   │   │       ├── model/                   # Domain entities
│   │   │       ├── dto/                     # Data transfer objects
│   │   │       └── config/                  # Configuration
│   │   └── resources/
│   │       ├── application.properties       # or application.yml
│   │       ├── static/                      # Static resources
│   │       └── templates/                   # Thymeleaf templates
│   └── test/
│       └── java/
│           └── com/company/project/
├── pom.xml                 # Maven dependencies
└── mvnw, mvnw.cmd          # Maven wrapper
```

#### Key Configuration Files
- **pom.xml** or **build.gradle**: Dependencies and build
- **application.properties** or **application.yml**: Configuration
- **ProjectApplication.java**: @SpringBootApplication entry point

---

## Tier 1: Other Major Frameworks

### Ruby on Rails

**Framework**: Ruby on Rails  
**Official Docs**: https://guides.rubyonrails.org  
**Current Version**: 7.x (as of 2025-09-30)

#### Standard Rails Structure
```
project-root/
├── app/
│   ├── controllers/        # Controllers
│   ├── models/             # ActiveRecord models
│   ├── views/              # ERB templates
│   ├── helpers/            # View helpers
│   ├── mailers/            # Action Mailer
│   ├── jobs/               # Active Job
│   └── assets/             # Assets pipeline
├── config/
│   ├── routes.rb           # Routes configuration
│   ├── database.yml        # Database config
│   └── application.rb      # App config
├── db/
│   ├── migrate/            # Migrations
│   └── schema.rb           # Current schema
├── Gemfile                 # Dependencies
└── config.ru               # Rack config
```

---

### ASP.NET Core

**Framework**: ASP.NET Core  
**Official Docs**: https://docs.microsoft.com/aspnet/core  
**Current Version**: 8.0 (as of 2025-09-30)

#### Standard ASP.NET Core Structure
```
project-root/
├── Controllers/            # MVC controllers
├── Models/                 # Data models
├── Views/                  # Razor views
├── wwwroot/                # Static files
│   ├── css/
│   ├── js/
│   └── lib/
├── Data/                   # EF Core DbContext
├── Services/               # Business logic
├── Program.cs              # Entry point (.NET 6+)
├── appsettings.json        # Configuration
└── ProjectName.csproj      # Project file
```

---

## Pattern Validation Workflow

### Step-by-Step Validation

1. **Identify Framework**
   - Check package.json, requirements.txt, pom.xml, etc.
   - Note exact version

2. **Locate Pattern in This Document**
   - Find framework section
   - Review standard structure

3. **Compare Actual vs Expected**
   - List matching elements ✅
   - List missing elements ❌
   - List extra/unexpected elements ⚠️

4. **Research Deviations**
   - Are deviations intentional optimizations?
   - Are they recommended by community?
   - Are they anti-patterns?

5. **Verify Framework Version**
   - Check official docs for version-specific changes
   - Note if project uses outdated patterns
   - Document migration path if needed

6. **Document Findings**
   - In brownfield-analysis.md: Record deviations with confidence
   - In plan.md: Reference this document for pattern adherence

---

## Research Checklist Template

For any framework analysis, research:

- [ ] **Official Documentation**: [URL]
- [ ] **Latest Stable Version**: [Version number and date]
- [ ] **Version in Project**: [Version number]
- [ ] **Breaking Changes**: [Any major changes between versions]
- [ ] **Folder Structure**: [Official recommendation matches this doc?]
- [ ] **Best Practices**: [Any recent best practice changes]
- [ ] **Community Consensus**: [Check GitHub, Stack Overflow, Reddit]
- [ ] **Deprecations**: [Any deprecated patterns in project]

---

## Adding New Frameworks

If analyzing a framework not listed here:

1. **Create Section**: Use same structure as above
2. **Document Structure**: From official docs
3. **List Key Files**: Configuration and entry points
4. **Add Validation Questions**: Framework-specific checks
5. **Provide URLs**: Official docs, GitHub, community resources
6. **Note Version**: Framework version as of documentation date

**Submit PR**: Help others by adding well-documented patterns!

---

## Version History

- **2025-09-30**: Initial template with Tier 1 frameworks
- **Future**: Add Rust (Actix/Axum), Go (Gin/Echo), PHP (Laravel/Symfony)

---

*Always verify against official documentation. Frameworks evolve quickly!*
