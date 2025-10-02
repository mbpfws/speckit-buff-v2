# Dependency Analysis Report

**Project**: [name]  
**Date**: YYYY-MM-DD  
**Package Manager**: [npm|pip|bundler|cargo|go]  
**Analysis Tool**: [npm audit|pip-audit|bundler-audit|cargo audit]

---

## Executive Summary

**Total Dependencies**: [count]  
**Vulnerabilities Found**: [count] (Critical: X, High: Y, Medium: Z, Low: W)  
**Peer Conflicts**: [count]  
**Breaking Changes Detected**: [count]  
**Outdated Packages**: [count]

**Overall Risk**: [Low|Medium|High|Critical]

---

## Vulnerabilities Table

| Package | Current Version | Severity | Fix Available | CVE | Recommendation |
|---------|----------------|----------|---------------|-----|----------------|
| example-pkg | 1.2.3 | Critical | 1.2.4 | CVE-2024-XXXX | Update immediately |
| another-pkg | 2.0.0 | High | 2.1.0 | CVE-2024-YYYY | Update in next release |
| old-pkg | 0.9.0 | Medium | None | N/A | Consider alternative package |

**Script Output**:
```bash
# Run automated check
.specify/scripts/bash/check-dependencies.sh --json

# Output format:
{
  "vulnerabilities": [
    {
      "package": "example-pkg",
      "current_version": "1.2.3",
      "severity": "critical",
      "fix_available": "1.2.4",
      "cve": "CVE-2024-XXXX"
    }
  ],
  "outdated": [
    {
      "package": "react",
      "current": "18.2.0",
      "latest": "18.3.1"
    }
  ]
}
```

---

## Peer Dependency Conflicts

| Package | Required Version | Current Version | Conflict Type | Resolution |
|---------|-----------------|-----------------|---------------|------------|
| @types/react | ^18.0.0 | 17.0.50 | Version mismatch | Update to 18.x |
| vite | ^5.0.0 | 4.5.2 | Major version | Upgrade to 5.x (breaking changes) |

**Common Errors**:
```
ERESOLVE unable to resolve dependency tree
npm ERR! peer @types/react@"^18.0.0" from package-x@1.0.0
npm ERR! peer @types/react@"^17.0.0" from package-y@2.0.0
```

**Resolution Options**:
1. ✅ **Update conflicting package**: Upgrade package-y to version supporting React 18
2. ⚠️ **Use --legacy-peer-deps**: Bypass peer dependency checks (not recommended)
3. ⚠️ **Use --force**: Force install (dangerous, may break runtime)
4. ✅ **Find alternative package**: Replace package-y with compatible alternative

---

## Breaking Changes Section

### Detected from Changelogs

**Script Output**:
```bash
# Run breaking change detection
.specify/scripts/bash/detect-breaking-changes.sh --json

# Output format:
{
  "breaking_changes": [
    {
      "package": "react",
      "from_version": "18.2.0",
      "to_version": "19.0.0",
      "description": "Removed legacy lifecycle methods",
      "affected_files": [
        "src/components/LegacyComponent.tsx"
      ],
      "migration_guide": "https://react.dev/blog/2024/04/25/react-19-upgrade-guide"
    }
  ]
}
```

### Migration Requirements

#### React 18 → 19
**Breaking Changes**:
- Removed: `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate`
- Changed: Automatic batching now default
- New: Server Components architecture

**Affected Files**:
- `src/components/LegacyComponent.tsx` (uses componentWillMount)
- `src/utils/StateManager.ts` (relies on synchronous setState)

**Migration Steps**:
1. Replace lifecycle methods with hooks (`useEffect`, `useState`)
2. Update state management for automatic batching
3. Review Server Component compatibility
4. **Estimated Effort**: 4-8 hours
5. **Risk**: Medium (well-documented migration path)

**Migration Guide**: According to https://react.dev/blog/2024/04/25/react-19-upgrade-guide

---

## Outdated Packages

| Package | Current | Latest | Type | Update Priority |
|---------|---------|--------|------|-----------------|
| react | 18.2.0 | 19.0.0 | Major | High (breaking changes) |
| typescript | 5.2.2 | 5.6.3 | Minor | Medium (new features) |
| eslint | 8.50.0 | 9.12.0 | Major | Low (config changes) |

**Update Strategy**:
1. **Critical Security**: Update immediately (vulnerabilities)
2. **Major Versions**: Schedule for next sprint (breaking changes)
3. **Minor/Patch**: Update during maintenance window
4. **Dev Dependencies**: Lower priority, update quarterly

---

## Dependency Tree Analysis

**Top-level Dependencies**: [count]  
**Transitive Dependencies**: [count]  
**Duplicate Packages**: [count]

**Duplicates to Dedupe**:
```bash
# Run deduplication
npm dedupe

# Expected savings:
# - Reduced node_modules size: X MB → Y MB
# - Fewer package versions: X → Y
```

**Dependency Graph** (critical paths only):
```
your-app
├── react@18.2.0
│   └── scheduler@0.23.0
├── next@14.0.0
│   ├── react@18.2.0 (deduped)
│   └── react-dom@18.2.0
└── @tanstack/react-query@5.0.0
    └── react@18.2.0 (deduped)
```

---

## Security Recommendations

### Critical Actions (Immediate)
1. **Update [package]** from [old] to [new] (CVE-XXXX)
2. **Remove [package]** (deprecated, security risk)
3. **Replace [package]** with [alternative] (unmaintained)

### High Priority (This Sprint)
1. **Upgrade [package]** to latest major version
2. **Audit [package]** for known vulnerabilities
3. **Review [package]** license compatibility

### Medium Priority (Next Sprint)
1. **Update minor versions** for [list of packages]
2. **Run `npm audit fix`** for automated patches
3. **Document accepted risks** for unfixable vulnerabilities

---

## Accepted Risks

**Vulnerabilities with No Fix Available**:

| Package | Severity | CVE | Reason | Mitigation |
|---------|----------|-----|--------|------------|
| old-lib | Medium | CVE-2023-XXXX | No patch, package unmaintained | Sandboxed usage, input validation |

**Sign-off Required**: [Name/Date]

---

## Resolution Options Reference

### For Peer Conflicts

**Option 1: Update Conflicting Package** ✅ Recommended
```bash
npm install package-y@latest
# Check if supports required peer dependency version
```

**Option 2: Use Overrides** (npm 8.3+)
```json
{
  "overrides": {
    "package-y": {
      "@types/react": "^18.0.0"
    }
  }
}
```

**Option 3: Legacy Peer Deps** ⚠️ Not Recommended
```bash
npm install --legacy-peer-deps
# Bypasses peer dependency checks, may cause runtime errors
```

**Option 4: Force Install** ❌ Dangerous
```bash
npm install --force
# Ignores all conflicts, high risk of breaking changes
```

### For Breaking Changes

**Option 1: Incremental Migration** ✅ Recommended
- Update one major version at a time
- Test thoroughly between updates
- Follow official migration guides

**Option 2: Fork Package** (Last Resort)
- Fork outdated package
- Apply security patches manually
- Maintain fork until alternative found

**Option 3: Find Alternative** ✅ Recommended for Unmaintained
- Research actively maintained alternatives
- Compare features and API compatibility
- Plan migration timeline

---

## Validation Checklist

- [ ] All vulnerabilities reviewed
- [ ] Critical vulnerabilities fixed or accepted with sign-off
- [ ] Peer conflicts resolved (no --force or --legacy-peer-deps)
- [ ] Breaking changes documented with migration plan
- [ ] Outdated packages prioritized for updates
- [ ] Dependency tree optimized (dedupe run)
- [ ] Lock file updated and committed

---

**Next Steps**:
1. Review this report with team
2. Prioritize updates based on severity
3. Schedule breaking change migrations
4. Run automated fixes: `npm audit fix`
5. Update lock file: `npm ci` (verify exact versions)
6. Commit changes with reference to this report

---

*Generated by check-dependencies.sh and detect-breaking-changes.sh*  
*Based on research findings - see specs/005-spec-kit-enhanced/research.md*
