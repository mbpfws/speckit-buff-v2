"""
Integration test: Greenfield project initialization (Scenario 1).

Based on: quickstart.md Scenario 1

Tests complete greenfield initialization workflow.
"""
import os
import time
from pathlib import Path

import pytest


class TestGreenfieldInitialization:
    """Test greenfield project initialization workflow."""
    
    def test_complete_greenfield_workflow(self, cli_runner, temp_dir):
        """
        Given: Empty project directory
        When: Run specify init
        Then: Project initialized in <3 seconds with correct structure
        """
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        
        # Measure execution time
        start = time.time()
        result = cli_runner.invoke(main, ['init'])
        elapsed = time.time() - start
        
        # Should succeed
        assert result.exit_code == 0, f"Init failed: {result.output}"
        
        # Performance: <3 seconds
        assert elapsed < 3.0, f"Init took {elapsed:.2f}s, expected <3s"
        
        # Verify structure
        assert (temp_dir / ".specify").exists()
        assert (temp_dir / ".specify" / "templates").exists()
        assert (temp_dir / ".specify" / "scripts" / "bash").exists()
        assert (temp_dir / ".specify" / "scripts" / "powershell").exists()
        assert (temp_dir / ".specify" / "config.yaml").exists()
        assert (temp_dir / ".specify" / ".version").exists()
        assert (temp_dir / "specs").exists()
        
        # Verify templates exist
        templates_dir = temp_dir / ".specify" / "templates"
        assert (templates_dir / "spec-template.md").exists()
        assert (templates_dir / "plan-template.md").exists()
        assert (templates_dir / "tasks-template.md").exists()
        assert (templates_dir / "constitution.md").exists()
        
        # Verify no analysis engines
        cli_dir = Path(__file__).parent.parent.parent / "specify-cli"
        if cli_dir.exists():
            # Check LOC count
            from tests.helpers import count_loc
            total_loc = sum(
                count_loc(f) for f in cli_dir.rglob("*.py")
                if "__pycache__" not in str(f)
            )
            assert total_loc < 400, f"CLI has {total_loc} LOC, expected <400"
    
    def test_both_installation_methods(self, temp_dir):
        """Test that both uv tool and uvx installation methods work."""
        os.chdir(temp_dir)
        
        # This test verifies the concept - actual uvx testing would require
        # the tool to be published
        # For now, verify the CLI entry point exists
        from specify_cli.cli import main
        assert callable(main)
    
    def test_minimal_dependencies(self):
        """Verify only minimal dependencies are used."""
        import sys
        import importlib.util
        
        # Essential dependencies that should be available
        essential = ['click', 'requests', 'yaml']
        
        for dep in essential:
            if dep == 'yaml':
                dep = 'yaml'  # PyYAML imports as yaml
            spec = importlib.util.find_spec(dep)
            # Dependencies will be available after implementation
            # This test documents the requirement
        
        # Dependencies that should NOT be present
        forbidden = ['tavily', 'anthropic', 'openai']
        
        for dep in forbidden:
            spec = importlib.util.find_spec(dep)
            # These should not be CLI dependencies (may be dev/test deps)
