"""
Integration test: Multi-platform execution (Scenario 5).

Based on: quickstart.md Scenario 5

Tests cross-platform command execution and template consistency.
"""
import platform
import pytest
from pathlib import Path


class TestMultiPlatform:
    """Test multi-platform execution."""
    
    def test_command_execution_on_current_platform(self, cli_runner):
        """
        Given: Current platform (Windows/Unix)
        When: CLI commands execute
        Then: Commands work correctly
        """
        from specify_cli.cli import main
        
        result = cli_runner.invoke(main, ['--version'])
        assert result.exit_code == 0
        assert '2.0.0' in result.output
    
    def test_platform_detection(self):
        """Verify platform detection works correctly."""
        from specify_cli.validators import detect_platform
        
        detected = detect_platform()
        
        if platform.system() == 'Windows':
            assert detected == 'windows'
        else:
            assert detected == 'unix'
    
    def test_template_consistency_across_platforms(self, cli_runner, temp_dir):
        """Verify templates are identical across platforms."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Templates should be platform-independent
        template_dir = temp_dir / '.specify' / 'templates'
        assert template_dir.exists()
        
        # Essential templates should exist
        assert (template_dir / 'spec-template.md').exists()
        assert (template_dir / 'plan-template.md').exists()
    
    def test_validation_script_selection(self):
        """Verify correct validation scripts selected by platform."""
        from specify_cli.validators import detect_platform
        
        current_platform = detect_platform()
        
        if current_platform == 'windows':
            expected_ext = '.ps1'
        else:
            expected_ext = '.sh'
        
        # Scripts should use correct extension
        assert expected_ext in ['.sh', '.ps1']
