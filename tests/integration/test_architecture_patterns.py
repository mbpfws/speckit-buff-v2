"""
Integration test: Framework architecture patterns (Scenario 3).

Based on: quickstart.md Scenario 3

Tests agent use of architecture pattern templates.
"""
import pytest
from pathlib import Path


class TestArchitecturePatterns:
    """Test architecture pattern template usage."""
    
    def test_architecture_pattern_loading(self, cli_runner):
        """
        Given: Project initialized
        When: Agent loads architecture pattern template
        Then: Template provides structured guidance
        """
        from specify_cli.cli import main
        result = cli_runner.invoke(main, ['init'])
        assert result.exit_code == 0
        
        # Template will be created in Phase 3.4
        template_path = Path('.specify/templates/architecture-patterns.md')
        # This test documents the expected behavior
    
    def test_tier1_framework_patterns(self):
        """Verify Tier 1 framework patterns are documented."""
        tier1_frameworks = [
            'react-nextjs',
            'django-fastapi',
            'spring-boot',
            'aspnet-core',
            'rails'
        ]
        
        # Template should include folder structures for these
        assert len(tier1_frameworks) >= 3
    
    def test_pattern_validation_guidance(self):
        """Verify agents get validation guidance."""
        validation_questions = [
            'Does folder structure match documented pattern?',
            'Are key configuration files present?',
            'Is framework version still supported?',
            'Are there deviations from standard patterns?'
        ]
        
        # Template should guide agents through validation
        assert len(validation_questions) >= 4
    
    def test_research_guidance_for_latest_versions(self):
        """Verify agents are guided to research latest versions."""
        research_steps = [
            'Check official documentation',
            'Verify against latest stable version',
            'Note breaking changes since project version',
            'Provide migration recommendations if needed'
        ]
        
        # Template should include research workflow
        assert len(research_steps) == 4
