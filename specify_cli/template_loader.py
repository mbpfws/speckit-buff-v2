"""
Template loader for downloading and caching templates from GitHub Releases.
Target: ~80 LOC
"""
import shutil
import tarfile
from pathlib import Path
from typing import Optional

import requests


def get_cache_dir() -> Path:
    """Get the cache directory path."""
    cache = Path.home() / ".specify" / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    return cache


def download_templates(version: str = "latest", offline: bool = False) -> Path:
    """
    Download templates from GitHub Releases.
    
    Args:
        version: Template version to download (default: "latest")
        offline: Use cached templates without network access
        
    Returns:
        Path to downloaded/cached templates directory
        
    Raises:
        RuntimeError: If download fails or offline mode without cache
    """
    cache_dir = get_cache_dir()
    version_dir = cache_dir / version
    
    if offline:
        if not version_dir.exists():
            raise RuntimeError(f"Offline mode enabled but no cached templates for version {version}")
        return version_dir
    
    # For now, use embedded templates (will be replaced with GitHub releases)
    # This is a simplified implementation for v2.0.0 MVP
    if not version_dir.exists():
        version_dir.mkdir(parents=True)
        
    return version_dir


def extract_templates(archive_path: Path, target_dir: Path, minimal: bool = False) -> None:
    """
    Extract templates from tar.gz archive.
    
    Args:
        archive_path: Path to template archive
        target_dir: Directory to extract to
        minimal: If True, extract only essential templates
    """
    essential = {"spec-template.md", "plan-template.md", "tasks-template.md", "constitution.md"}
    
    with tarfile.open(archive_path, "r:gz") as tar:
        for member in tar.getmembers():
            if minimal and Path(member.name).name not in essential:
                continue
            tar.extract(member, target_dir)


def cache_templates(version: str, templates_dir: Path) -> None:
    """
    Cache templates for offline use.
    
    Args:
        version: Template version
        templates_dir: Directory containing templates
    """
    cache_dir = get_cache_dir()
    version_cache = cache_dir / version
    
    if version_cache.exists():
        shutil.rmtree(version_cache)
    
    shutil.copytree(templates_dir, version_cache)


def get_cached_version() -> Optional[str]:
    """Get the currently cached template version."""
    cache_dir = get_cache_dir()
    version_file = cache_dir / ".version"
    
    if version_file.exists():
        return version_file.read_text().strip()
    
    return None


def check_for_updates() -> Optional[str]:
    """
    Check GitHub API for latest template version.
    
    Returns:
        Latest version string or None if check fails
    """
    try:
        url = "https://api.github.com/repos/github/spec-kit/releases/latest"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("tag_name")
    except Exception:
        pass
    
    return None
