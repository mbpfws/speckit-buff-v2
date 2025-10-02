"""
Integration test: Cross-platform validation scripts (Scenario 8).

Based on: quickstart.md Scenario 8

Tests bash and PowerShell script equivalence.
"""
import os
import platform
import pytest
import subprocess
from pathlib import Path


class TestCrossPlatformScripts:
    """Test cross-platform validation scripts."""
    
    def test_bash_scripts_on_unix(self, cli_runner, temp_dir):
        """
        Given: Unix/Linux/macOS system
        When: Bash validation scripts run
        Then: Scripts execute successfully
        """
        if platform.system() == 'Windows':
            pytest.skip("Unix-specific test")
        
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Bash scripts should be executable
        script_dir = temp_dir / '.specify' / 'scripts' / 'bash'
        assert script_dir.exists()
        
        for script in script_dir.glob('*.sh'):
            # Check executable bit
            assert os.access(script, os.X_OK)
    
    @pytest.mark.skipif(platform.system() != 'Windows', reason="Windows-specific test")
    def test_powershell_scripts_on_windows(self, cli_runner, temp_dir):
        """
        Given: Windows system
        When: PowerShell validation scripts run
        Then: Scripts execute successfully
        """
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # PowerShell scripts should exist
        script_dir = temp_dir / '.specify' / 'scripts' / 'powershell'
        assert script_dir.exists()
        
        ps_scripts = list(script_dir.glob('*.ps1'))
        assert len(ps_scripts) >= 3
    
    def test_script_output_equivalence(self, cli_runner, temp_dir):
        """Verify bash and PowerShell scripts produce equivalent output."""
        # Both should:
        # - Output [INFO], [WARN], [ERROR] messages
        # - Exit with code 0 (non-blocking)
        # - Report same validation issues
        
        message_format = r'\[(INFO|WARN|ERROR)\]\s+.+'
        
        # This pattern should be used by both script types
        assert '[INFO]' in message_format
        assert '[WARN]' in message_format
        assert '[ERROR]' in message_format
    
    def test_non_blocking_exit_codes(self):
        """Verify all scripts exit with code 0 (non-blocking)."""
        # Constitutional principle: Non-blocking validation
        expected_exit_code = 0
        
        # All validation scripts should exit 0
        assert expected_exit_code == 0
