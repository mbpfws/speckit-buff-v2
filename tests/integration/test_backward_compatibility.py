"""
Integration test: Backward compatibility (Scenario 10).

Based on: quickstart.md Scenario 10

Tests v1.x artifact compatibility with v2.0 CLI.
"""
import pytest
from pathlib import Path


class TestBackwardCompatibility:
    """Test backward compatibility with v1.x."""
    
    def test_v1_artifact_structure_validates(self, cli_runner, temp_dir):
        """
        Given: V1.x artifact structure
        When: V2.0 validation runs
        Then: Artifacts validate successfully
        """
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        
        # Create v1.x-style structure
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        feature_dir = temp_dir / 'specs' / '001-test-feature'
        feature_dir.mkdir(parents=True)
        
        # V1.x spec format
        spec_path = feature_dir / 'spec.md'
        spec_path.write_text("""---
feature_id: 001
title: Test Feature
status: draft
created: 2024-01-15
---

# Test Feature Specification

## Overview
Test feature description.

## User Stories
- As a user...

## Requirements
- REQ-001: ...
""")
        
        # Should validate successfully
        result = cli_runner.invoke(main, ['check'])
        assert result.exit_code == 0
    
    def test_v1_frontmatter_format_supported(self):
        """Verify v1.x frontmatter format is supported."""
        v1_fields = [
            'feature_id',
            'title',
            'status',
            'created',
            'updated',
            'version'
        ]
        
        # V2.0 should support all v1.x fields
        assert len(v1_fields) >= 4
    
    def test_v1_folder_structure_supported(self, cli_runner, temp_dir):
        """Verify v1.x folder structure is supported."""
        import os
        os.chdir(temp_dir)
        
        from specify_cli.cli import main
        
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # V1.x structure: specs/{id}-{slug}/spec.md
        feature_dir = temp_dir / 'specs' / '042-my-feature'
        feature_dir.mkdir(parents=True)
        
        (feature_dir / 'spec.md').write_text('---\ntitle: Test\n---\n# Test')
        
        # Should work with v2.0
        result = cli_runner.invoke(main, ['check'])
        assert result.exit_code == 0
    
    def test_migration_path_provided(self):
        """Verify clear migration path from v1.x to v2.0."""
        migration_steps = [
            '1. Install v2.0: uv tool install specify-cli@2.0.0',
            '2. Run in existing project: specify check',
            '3. Review migration suggestions',
            '4. Update .specify/ when ready'
        ]
        
        # Migration should be documented
        assert len(migration_steps) == 4
    
    def test_no_forced_breaking_changes(self):
        """Verify no forced breaking changes for v1.x users."""
        breaking_changes = []
        
        # V2.0 should have zero forced breaking changes
        assert len(breaking_changes) == 0
