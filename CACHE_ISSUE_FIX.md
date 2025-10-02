# 🔥 UVX CACHE ISSUE - CRITICAL

## The Problem

You pushed all fixes to GitHub, but `uvx` is **caching the old version**!

### Evidence
```
├── ● Fetch latest release (release v0.0.55 (37,864 bytes))
├── ● Download template (spec-kit-template-roo-sh-v0.0.55.zip)
```

This is downloading from `github/spec-kit` v0.0.55 (the ORIGINAL), not your fork!

---

## Why This Happens

`uvx` caches packages by their Git commit hash. Even though you pushed new code, `uvx` may be using a cached version from before your fixes.

---

## Solution 1: Clear UV Cache (RECOMMENDED)

```bash
# Clear the entire UV cache
uv cache clean

# Then try again
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init --here --ai roo
```

---

## Solution 2: Force Specific Commit

```bash
# Get the latest commit hash
cd d:\speckit-buff
git rev-parse HEAD

# Use that specific commit (replace COMMIT_HASH)
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git@COMMIT_HASH specify init --here --ai roo
```

---

## Solution 3: Use Branch Name

```bash
# Force use of master branch HEAD
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git@master specify init --here --ai roo
```

---

## Solution 4: Install Globally First

```bash
# Clear cache
uv cache clean

# Install globally
uv tool install specify-cli --from git+https://github.com/mbpfws/speckit-buff-v2.git --force

# Then use
specify init --here --ai roo
```

---

## Verification

After clearing cache, you should see:
```
├── ● Fetch latest release (release v2.0.0 ...)
├── ● Download template (spec-kit-template-roo-sh-v2.0.0.zip)
```

**NOT v0.0.55!**

---

## The Real Issue

Your fork doesn't have releases yet! The CLI is falling back to the original repo because:

1. It tries: `https://api.github.com/repos/mbpfws/speckit-buff-v2/releases/latest`
2. Gets 404 (no releases)
3. Falls back to: `https://api.github.com/repos/github/spec-kit/releases/latest`
4. Downloads v0.0.55 from original!

---

## ACTUAL FIX NEEDED

You need to create a release on YOUR fork!

### Option A: Manual Release

1. Go to: https://github.com/mbpfws/speckit-buff-v2/releases
2. Click "Create a new release"
3. Tag: `v2.0.0`
4. Title: "Spec-Kit Enhanced Fork v2.0"
5. Click "Publish release"

This will trigger the GitHub Action to create the ZIP files!

### Option B: Trigger Workflow Manually

1. Go to: https://github.com/mbpfws/speckit-buff-v2/actions
2. Click "Create Release" workflow
3. Click "Run workflow"
4. Select "master" branch
5. Click "Run workflow"

---

## What's Actually Happening

```python
# src/specify_cli/__init__.py (CORRECT CODE)
REPO_OWNER = "mbpfws"
REPO_NAME = "speckit-buff-v2"

def download_template_from_github(...):
    repo_owner = REPO_OWNER  # ✅ Uses mbpfws
    repo_name = REPO_NAME    # ✅ Uses speckit-buff-v2
    
    # Tries to fetch from YOUR fork
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    # https://api.github.com/repos/mbpfws/speckit-buff-v2/releases/latest
    
    # But YOUR fork has NO releases yet!
    # So it gets 404 and falls back to original repo
```

---

## IMMEDIATE ACTION REQUIRED

### Step 1: Create Release on GitHub

Go to your fork and create a release. The GitHub Action will automatically:
1. Detect the release trigger
2. Run `create-release-packages.sh`
3. Generate 22 ZIP files
4. Upload them as release assets

### Step 2: Clear UV Cache

```bash
uv cache clean
```

### Step 3: Test Again

```bash
uvx --from git+https://github.com/mbpfws/speckit-buff-v2.git specify init test-project --ai roo
```

You should now see:
```
├── ● Fetch latest release (release v2.0.0 ...)
├── ● Download template (spec-kit-template-roo-sh-v2.0.0.zip)
```

---

## Summary

**Problem**: No releases on your fork → CLI falls back to original  
**Solution**: Create release v2.0.0 on GitHub  
**Then**: Clear UV cache and try again  

**The code is correct, you just need releases!**
