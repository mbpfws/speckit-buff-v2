"""
Pytest configuration and common fixtures for spec-kit tests.
"""
import os
import shutil
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test isolation."""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def mock_project(temp_dir: Path) -> Path:
    """Create a mock project structure for testing."""
    # Create .specify structure
    specify_dir = temp_dir / ".specify"
    specify_dir.mkdir()
    
    (specify_dir / "templates").mkdir()
    (specify_dir / "scripts" / "bash").mkdir(parents=True)
    (specify_dir / "scripts" / "powershell").mkdir(parents=True)
    (specify_dir / "config.yaml").write_text("template_version: v2.0.0\n")
    (specify_dir / ".version").write_text("v2.0.0")
    
    # Create specs structure
    specs_dir = temp_dir / "specs"
    specs_dir.mkdir()
    
    return temp_dir


@pytest.fixture
def mock_feature(mock_project: Path) -> Path:
    """Create a mock feature directory with artifacts."""
    feature_dir = mock_project / "specs" / "001-test-feature"
    feature_dir.mkdir()
    
    # Create spec.md with frontmatter
    spec_content = """---
feature_id: 1
created: 2025-09-30
status: draft
---

# Feature Specification: Test Feature

This is a test feature specification.
"""
    (feature_dir / "spec.md").write_text(spec_content)
    
    return feature_dir


@pytest.fixture
def cli_runner():
    """Create a Click CLI test runner."""
    from click.testing import CliRunner
    return CliRunner()
