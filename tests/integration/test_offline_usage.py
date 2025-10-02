"""
Integration test: Offline usage (Scenario 9).

Based on: quickstart.md Scenario 9

Tests offline functionality and template caching.
"""
import pytest
from pathlib import Path
import shutil


class TestOfflineUsage:
    """Test offline usage capabilities."""
    
    def test_template_caching_after_first_init(self, cli_runner, temp_dir):
        """
        Given: First-time init downloads templates
        When: Templates cached locally
        Then: Subsequent inits can use cache
        """
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        from specify_cli.template_loader import get_cache_dir
        
        # First init (may download)
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Cache directory should exist
        cache_dir = get_cache_dir()
        assert cache_dir.exists()
    
    def test_offline_flag_uses_cache(self, cli_runner, temp_dir):
        """Verify --offline flag uses cached templates."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        from specify_cli.template_loader import get_cache_dir
        
        # Create cache
        cache_dir = get_cache_dir()
        version_dir = cache_dir / 'latest'
        version_dir.mkdir(parents=True, exist_ok=True)
        
        # Offline init should use cache
        result = cli_runner.invoke(main, ['init', '--offline'])
        assert result.exit_code == 0
    
    def test_offline_error_without_cache(self, cli_runner, temp_dir):
        """Verify error when offline without cache."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        from specify_cli.template_loader import get_cache_dir
        
        # Ensure no cache
        cache_dir = get_cache_dir()
        if cache_dir.exists():
            shutil.rmtree(cache_dir)
        
        # Offline without cache should fail
        result = cli_runner.invoke(main, ['init', '--offline'])
        assert result.exit_code == 1
        assert 'cache' in result.output.lower() or 'offline' in result.output.lower()
    
    def test_validation_works_offline(self, cli_runner, temp_dir):
        """Verify validation scripts work without network."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        
        # Init project
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Validation should work offline (local scripts)
        result = cli_runner.invoke(main, ['check'])
        assert result.exit_code == 0
    
    def test_no_network_errors_during_validation(self, cli_runner, temp_dir):
        """Verify no network errors during validation."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Check should not require network
        result = cli_runner.invoke(main, ['check'])
        assert result.exit_code == 0
        assert 'network' not in result.output.lower()
        assert 'timeout' not in result.output.lower()
