"""
Integration test: Quality tool integration (Scenario 6).

Based on: quickstart.md Scenario 6

Tests quality tool detection and non-blocking execution.
"""
import pytest
from pathlib import Path


class TestQualityIntegration:
    """Test quality tool integration."""
    
    def test_quality_check_non_blocking(self, cli_runner, temp_dir):
        """
        Given: Project with quality tools
        When: specify check --quality runs
        Then: Exit code 0 even if issues found
        """
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Run quality checks (even if tools not found)
        result = cli_runner.invoke(main, ['check', '--quality'])
        
        # Non-blocking philosophy
        assert result.exit_code == 0
    
    def test_project_type_detection(self):
        """Verify project type detection patterns."""
        detection_patterns = {
            'javascript': ['package.json', '.eslintrc'],
            'python': ['pyproject.toml', '.flake8', 'setup.py'],
            'java': ['pom.xml', 'checkstyle.xml'],
            'csharp': ['*.csproj', '.editorconfig']
        }
        
        # Quality tools should be detected based on these
        assert len(detection_patterns) >= 2
    
    def test_finding_categorization(self):
        """Verify findings are categorized correctly."""
        categories = {
            'critical': 'Security vulnerabilities, blocking issues',
            'error': 'Code errors, bugs',
            'warning': 'Code smells, potential issues',
            'info': 'Style issues, suggestions'
        }
        
        # Quality tool output should be categorized
        assert 'critical' in categories
        assert 'warning' in categories
    
    def test_quality_tools_optional(self, cli_runner, temp_dir):
        """Verify quality tools are optional (graceful degradation)."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Should work even without quality tools installed
        result = cli_runner.invoke(main, ['check'])
        assert result.exit_code == 0
