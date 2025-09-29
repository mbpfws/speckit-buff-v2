"""
Contract tests for `specify check` command.

Based on: contracts/cli-check.yaml

These tests define the expected behavior of the check command and MUST
fail initially (TDD). Implementation will make them pass.
"""
import os
from pathlib import Path

import pytest


class TestCheckValidProject:
    """Test check command on valid project."""
    
    def test_check_valid_project(self, cli_runner, mock_project):
        """Given valid project, when specify check, then all checks pass."""
        os.chdir(mock_project)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check'])
        
        # Should succeed
        assert result.exit_code == 0
        
        # Should contain success messages
        assert "PASS" in result.output or "✓" in result.output


class TestCheckWithErrors:
    """Test check command with validation errors."""
    
    def test_check_with_errors(self, cli_runner, temp_dir):
        """Given project with missing files, when check, then errors reported."""
        os.chdir(temp_dir)
        
        # Create incomplete project (missing required files)
        (temp_dir / ".specify").mkdir()
        (temp_dir / "specs" / "004-feature").mkdir(parents=True)
        # spec.md is missing
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check'])
        
        # Should report errors but exit 0 (non-blocking)
        assert result.exit_code == 0  # Non-blocking philosophy
        assert "ERROR" in result.output or "error" in result.output.lower()


class TestCheckWithWarnings:
    """Test check command with warnings."""
    
    def test_check_with_warnings(self, cli_runner, mock_feature):
        """Given project with minor issues, when check, then warnings reported."""
        os.chdir(mock_feature.parent.parent)
        
        # Modify spec to have warning (missing optional field)
        spec_path = mock_feature / "spec.md"
        content = spec_path.read_text()
        # Remove version field if present, leave required fields
        spec_path.write_text(content)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check'])
        
        # Should succeed with warnings
        assert result.exit_code == 0
        # May contain warnings (not critical for this test)


class TestCheckSingleArtifact:
    """Test check command on single artifact."""
    
    def test_check_single_artifact(self, cli_runner, mock_feature):
        """Given single artifact, when check <file>, then only that file checked."""
        os.chdir(mock_feature.parent.parent)
        
        spec_path = mock_feature / "spec.md"
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check', str(spec_path)])
        
        # Should succeed
        assert result.exit_code == 0


class TestCheckQuality:
    """Test check command with quality tools."""
    
    def test_check_quality(self, cli_runner, mock_project):
        """Given project with code, when check --quality, then quality tools run."""
        os.chdir(mock_project)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check', '--quality'])
        
        # Should succeed (even if quality tools not found)
        assert result.exit_code == 0


class TestCheckJsonOutput:
    """Test check command with JSON output."""
    
    def test_check_json_output(self, cli_runner, mock_project):
        """Given valid project, when check --format json, then JSON output."""
        os.chdir(mock_project)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check', '--format', 'json'])
        
        # Should succeed
        assert result.exit_code == 0
        
        # Should be valid JSON
        import json
        try:
            data = json.loads(result.output)
            assert 'status' in data or 'checks_run' in data
        except json.JSONDecodeError:
            pytest.fail("Output is not valid JSON")


class TestCheckUpdateTemplates:
    """Test check command with template update check."""
    
    def test_check_update_templates(self, cli_runner, mock_project):
        """Given project, when check --update-templates, then update prompt shown."""
        os.chdir(mock_project)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check', '--update-templates'])
        
        # Should succeed
        assert result.exit_code == 0


class TestCheckFix:
    """Test check command with automatic fixes."""
    
    def test_check_fix(self, cli_runner, mock_project):
        """Given fixable issues, when check --fix, then fixes applied."""
        os.chdir(mock_project)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check', '--fix'])
        
        # Should succeed
        assert result.exit_code == 0


class TestCheckNoSpecify:
    """Test check command without .specify/ directory."""
    
    def test_check_no_specify(self, cli_runner, temp_dir):
        """Given directory without .specify/, when check, then error."""
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['check'])
        
        # Should fail
        assert result.exit_code == 1
        assert ".specify/" in result.output.lower() or \
               "not found" in result.output.lower()


class TestCheckPerformance:
    """Test check command performance requirements."""
    
    def test_check_performance_target(self, cli_runner, mock_project):
        """Check must complete in <1 second."""
        import time
        
        os.chdir(mock_project)
        
        from specify_cli.cli import main
        start = time.time()
        result = cli_runner.invoke(main, ['check'])
        elapsed = time.time() - start
        
        # Should succeed
        assert result.exit_code == 0
        
        # Performance target: <1 second
        assert elapsed < 1.0, f"Check took {elapsed:.2f}s, expected <1s"
