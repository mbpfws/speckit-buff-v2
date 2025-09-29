"""
Contract tests for `specify init` command.

Based on: contracts/cli-init.yaml

These tests define the expected behavior of the init command and MUST
fail initially (TDD). Implementation will make them pass.
"""
import os
from pathlib import Path

import pytest


class TestInitEmptyDirectory:
    """Test init command in empty directory."""
    
    def test_init_empty_directory(self, cli_runner, temp_dir):
        """Given empty directory, when specify init, then all structures created."""
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        
        # Should succeed
        assert result.exit_code == 0
        
        # Verify directory structure
        assert (temp_dir / ".specify" / "templates").exists()
        assert (temp_dir / ".specify" / "scripts").exists()
        assert (temp_dir / "specs").exists()
        assert (temp_dir / ".specify" / "config.yaml").exists()
        assert (temp_dir / ".specify" / ".version").exists()


class TestInitWithExistingSpecify:
    """Test init command when .specify/ already exists."""
    
    def test_init_with_existing_specify_no_force(self, cli_runner, temp_dir):
        """Given existing .specify/, when init without --force, then error."""
        os.chdir(temp_dir)
        
        # Create existing .specify/
        (temp_dir / ".specify").mkdir()
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        
        # Should fail
        assert result.exit_code == 1
        assert ".specify/ directory already exists" in result.stderr or \
               ".specify/ directory already exists" in result.output
    
    def test_init_with_force(self, cli_runner, temp_dir):
        """Given existing .specify/, when init --force, then backup and overwrite."""
        os.chdir(temp_dir)
        
        # Create existing .specify/ with content
        specify_dir = temp_dir / ".specify"
        specify_dir.mkdir()
        (specify_dir / "old_file.txt").write_text("old content")
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init', '--force'])
        
        # Should succeed
        assert result.exit_code == 0
        
        # Verify backup created
        assert (temp_dir / ".specify.backup").exists()
        assert (temp_dir / ".specify.backup" / "old_file.txt").exists()
        
        # Verify new structure
        assert (temp_dir / ".specify" / "templates").exists()


class TestInitTemplateVersion:
    """Test init with specific template version."""
    
    def test_init_specific_version(self, cli_runner, temp_dir):
        """Given empty dir, when init --template-version v2.0.0, then specific version downloaded."""
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init', '--template-version', 'v2.0.0'])
        
        # Should succeed
        assert result.exit_code == 0
        
        # Verify version file
        version_file = temp_dir / ".specify" / ".version"
        assert version_file.exists()
        assert "v2.0.0" in version_file.read_text()


class TestInitOfflineMode:
    """Test init in offline mode."""
    
    def test_init_offline_with_cache(self, cli_runner, temp_dir, monkeypatch):
        """Given cached templates, when init --offline, then uses cache."""
        os.chdir(temp_dir)
        
        # Mock cache existence
        cache_dir = Path.home() / ".specify" / "cache" / "latest"
        cache_dir.mkdir(parents=True, exist_ok=True)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init', '--offline'])
        
        # Should succeed without network
        assert result.exit_code == 0
        
        # Clean up mock cache
        import shutil
        shutil.rmtree(Path.home() / ".specify" / "cache", ignore_errors=True)
    
    def test_init_offline_no_cache(self, cli_runner, temp_dir):
        """Given no cached templates, when init --offline, then error."""
        os.chdir(temp_dir)
        
        # Ensure no cache
        import shutil
        shutil.rmtree(Path.home() / ".specify" / "cache", ignore_errors=True)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init', '--offline'])
        
        # Should fail
        assert result.exit_code == 1
        assert "no cached templates" in result.output.lower() or \
               "cache" in result.output.lower()


class TestInitMinimal:
    """Test init with minimal template set."""
    
    def test_init_minimal(self, cli_runner, temp_dir):
        """Given empty dir, when init --minimal, then only essential templates installed."""
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init', '--minimal'])
        
        # Should succeed
        assert result.exit_code == 0
        
        templates_dir = temp_dir / ".specify" / "templates"
        
        # Essential templates must exist
        assert (templates_dir / "spec-template.md").exists()
        assert (templates_dir / "plan-template.md").exists()
        assert (templates_dir / "tasks-template.md").exists()
        assert (templates_dir / "constitution.md").exists()
        
        # Optional templates should not exist
        assert not (templates_dir / "brownfield-analysis.md").exists()
        assert not (templates_dir / "architecture-patterns.md").exists()


class TestInitPerformance:
    """Test init performance requirements."""
    
    def test_init_performance_target(self, cli_runner, temp_dir):
        """Init must complete in <3 seconds."""
        import time
        
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        start = time.time()
        result = cli_runner.invoke(main, ['init'])
        elapsed = time.time() - start
        
        # Should succeed
        assert result.exit_code == 0
        
        # Performance target: <3 seconds
        assert elapsed < 3.0, f"Init took {elapsed:.2f}s, expected <3s"
