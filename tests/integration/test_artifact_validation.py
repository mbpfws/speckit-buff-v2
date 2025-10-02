"""
Integration test: Artifact validation workflow (Scenario 4).

Based on: quickstart.md Scenario 4

Tests artifact creation and validation script execution.
"""
import pytest
from pathlib import Path


class TestArtifactValidation:
    """Test artifact validation workflow."""
    
    def test_artifact_with_frontmatter_validation(self, cli_runner, temp_dir):
        """
        Given: Artifact with YAML frontmatter
        When: Validation scripts run
        Then: Frontmatter parsed and validated successfully
        """
        import os
        os.chdir(temp_dir)
        
        # Initialize project
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Create artifact with frontmatter
        feature_dir = temp_dir / 'specs' / '001-test-feature'
        feature_dir.mkdir(parents=True)
        
        spec_path = feature_dir / 'spec.md'
        spec_path.write_text("""---
feature_id: 001
title: Test Feature
status: draft
created: 2025-09-30
---

# Test Feature

Description here.
""")
        
        # Run validation
        result = cli_runner.invoke(main, ['check'])
        
        # Should succeed (non-blocking)
        assert result.exit_code == 0
    
    def test_validation_message_parsing(self, cli_runner, temp_dir):
        """Verify validation messages are parsed correctly."""
        from specify_cli.validators import parse_validation_output
        
        sample_output = """[INFO] Starting validation
[WARN] Missing optional field: version
[ERROR] Missing required field: feature_id
[INFO] Validation complete"""
        
        messages = parse_validation_output(sample_output)
        
        assert len(messages) == 4
        assert messages[0].level == "INFO"
        assert messages[1].level == "WARN"
        assert messages[2].level == "ERROR"
        assert messages[3].level == "INFO"
    
    def test_non_blocking_validation(self, cli_runner, temp_dir):
        """Verify validation is non-blocking (exit 0 even with errors)."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Check even with no specs directory
        result = cli_runner.invoke(main, ['check'])
        
        # Non-blocking: exit 0 even with issues
        assert result.exit_code == 0
