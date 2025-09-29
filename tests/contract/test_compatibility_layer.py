"""
Contract tests for cross-platform compatibility layer

Tests the compatibility validator, platform adapter, and cross-platform
validation mechanisms for all 10 supported AI coding platforms.
"""
import pytest
from unittest.mock import Mock, patch
from src.specify_cli.compatibility import (
    CompatibilityValidator, PlatformAdapter, PlatformType, InstallationMethod,
    create_compatibility_validator, create_platform_adapter
)


class TestCompatibilityValidator:
    """Test suite for compatibility validator"""
    
    def test_platform_type_definitions(self):
        """Test platform type definitions"""
        assert PlatformType.CLAUDE_CODE.value == "claude_code"
        assert PlatformType.ROO_CODE.value == "roo_code"
        assert PlatformType.GITHUB_COPILOT.value == "github_copilot"
        assert PlatformType.CURSOR.value == "cursor"
        assert PlatformType.GEMINI_CLI.value == "gemini_cli"
        assert PlatformType.QWEN_CODE.value == "qwen_code"
        assert PlatformType.OPENCODE.value == "opencode"
        assert PlatformType.WINDSURF.value == "windsurf"
        assert PlatformType.KILO_CODE.value == "kilo_code"
        assert PlatformType.AUGGIE_CLI.value == "auggie_cli"
    
    def test_installation_method_definitions(self):
        """Test installation method definitions"""
        assert InstallationMethod.PATH.value == "path"
        assert InstallationMethod.UVX.value == "uvx"
    
    def test_detect_current_platform(self):
        """Test platform detection"""
        validator = CompatibilityValidator()
        
        with patch.dict('os.environ', {'CLAUDE_CODE': 'true'}):
            result = validator.detect_current_platform()
            assert result["success"] is True
            assert "claude_code" in result["platforms"]
            assert result["primary_platform"] == "claude_code"
    
    def test_validate_installation_method_valid(self):
        """Test valid installation method validation"""
        validator = CompatibilityValidator()
        
        result = validator.validate_installation_method("claude_code", "path")
        
        assert result["success"] is True
        assert result["supported"] is True
        assert result["platform"] == "claude_code"
        assert result["method"] == "path"
        assert "path" in result["supported_methods"]
        assert "uvx" in result["supported_methods"]
        assert len(result["recommendations"]) > 0
    
    def test_validate_installation_method_invalid_platform(self):
        """Test invalid platform validation"""
        validator = CompatibilityValidator()
        
        result = validator.validate_installation_method("invalid_platform", "path")
        
        assert result["success"] is False
        assert "error" in result
        assert result["platform"] == "invalid_platform"
    
    def test_get_compatibility_matrix(self):
        """Test compatibility matrix generation"""
        validator = CompatibilityValidator()
        
        result = validator.get_compatibility_matrix()
        
        assert result["success"] is True
        assert "matrix" in result
        assert result["version"] == "2.0.0"
        
        matrix = result["matrix"]
        assert len(matrix) == 10  # All 10 platforms
        
        # Check key platforms are present
        assert "claude_code" in matrix
        assert "roo_code" in matrix
        assert "github_copilot" in matrix
        assert "cursor" in matrix
        assert "gemini_cli" in matrix
        assert "qwen_code" in matrix
        assert "opencode" in matrix
        assert "windsurf" in matrix
        assert "kilo_code" in matrix
        assert "auggie_cli" in matrix
        
        # Check platform structure
        claude_config = matrix["claude_code"]
        assert "installation_methods" in claude_config
        assert "features" in claude_config
        assert "requirements" in claude_config
        assert "optimization_level" in claude_config
        assert "tier" in claude_config
    
    def test_validate_cross_platform_compatibility(self):
        """Test cross-platform compatibility validation"""
        validator = CompatibilityValidator()
        
        result = validator.validate_cross_platform_compatibility(
            "claude_code", 
            ["roo_code", "github_copilot", "cursor"]
        )
        
        assert result["success"] is True
        assert result["source_platform"] == "claude_code"
        assert result["target_platforms"] == ["roo_code", "github_copilot", "cursor"]
        assert "compatibility" in result
        assert "overall_compatibility" in result
        
        compatibility = result["compatibility"]
        assert "roo_code" in compatibility
        assert "github_copilot" in compatibility
        assert "cursor" in compatibility
        
        overall = result["overall_compatibility"]
        assert "score" in overall
        assert "compatible_platforms" in overall
        assert "total_platforms" in overall
        assert "status" in overall
    
    def test_validate_cross_platform_compatibility_invalid(self):
        """Test cross-platform compatibility with invalid platform"""
        validator = CompatibilityValidator()
        
        result = validator.validate_cross_platform_compatibility(
            "invalid_platform", 
            ["roo_code"]
        )
        
        assert result["success"] is False
        assert "error" in result


class TestPlatformAdapter:
    """Test suite for platform adapter"""
    
    def test_platform_adapter_creation(self):
        """Test platform adapter creation"""
        adapter = PlatformAdapter(PlatformType.CLAUDE_CODE)
        
        assert adapter.platform_type == PlatformType.CLAUDE_CODE
        assert adapter.adaptation_rules is not None
    
    def test_adapt_command(self):
        """Test command adaptation"""
        adapter = PlatformAdapter(PlatformType.CLAUDE_CODE)
        
        original_command = "specify analyze --brownfield"
        adapted_command = adapter.adapt_command(original_command, {})
        
        # Command should be adapted for Claude Code
        assert "specify" in adapted_command
        assert "--platform claude" in adapted_command
        assert "--context-optimized" in adapted_command
    
    def test_adapt_configuration(self):
        """Test configuration adaptation"""
        adapter = PlatformAdapter(PlatformType.CLAUDE_CODE)
        
        original_config = {"setting1": "value1", "setting2": "value2"}
        adapted_config = adapter.adapt_configuration(original_config)
        
        # Configuration should be merged with platform-specific settings
        assert "setting1" in adapted_config
        assert "setting2" in adapted_config
        assert "context_window" in adapted_config
        assert "mcp_integration" in adapted_config
        assert adapted_config["mcp_integration"] is True
    
    def test_get_platform_optimizations(self):
        """Test platform optimization retrieval"""
        adapter = PlatformAdapter(PlatformType.CLAUDE_CODE)
        
        optimizations = adapter.get_platform_optimizations()
        
        assert optimizations is not None
        assert "context_management" in optimizations
        assert "prompt_optimization" in optimizations
        assert "workflow_transitions" in optimizations


class TestFactoryFunctions:
    """Test suite for factory functions"""
    
    def test_create_compatibility_validator(self):
        """Test compatibility validator factory function"""
        validator = create_compatibility_validator()
        
        assert validator is not None
        assert isinstance(validator, CompatibilityValidator)
    
    def test_create_platform_adapter_valid(self):
        """Test platform adapter factory function with valid platform"""
        adapter = create_platform_adapter("claude_code")
        
        assert adapter is not None
        assert isinstance(adapter, PlatformAdapter)
        assert adapter.platform_type == PlatformType.CLAUDE_CODE
    
    def test_create_platform_adapter_invalid(self):
        """Test platform adapter factory function with invalid platform"""
        # Should default to basic platform adapter
        adapter = create_platform_adapter("invalid_platform")
        
        assert adapter is not None
        assert isinstance(adapter, PlatformAdapter)
        assert adapter.platform_type == PlatformType.AUGGIE_CLI


class TestPlatformDetection:
    """Test platform detection methods"""
    
    @patch.dict('os.environ', {'CLAUDE_CODE': 'true'})
    def test_detect_claude_code(self):
        """Test Claude Code detection"""
        validator = CompatibilityValidator()
        assert validator._detect_claude_code() is True
    
    @patch.dict('os.environ', {'ROO_CODE': 'true'})
    def test_detect_roo_code(self):
        """Test Roo Code detection"""
        validator = CompatibilityValidator()
        assert validator._detect_roo_code() is True
    
    @patch.dict('os.environ', {'GITHUB_COPILOT': 'true'})
    def test_detect_github_copilot(self):
        """Test GitHub Copilot detection"""
        validator = CompatibilityValidator()
        assert validator._detect_github_copilot() is True
    
    @patch.dict('os.environ', {'CURSOR': 'true'})
    def test_detect_cursor(self):
        """Test Cursor detection"""
        validator = CompatibilityValidator()
        assert validator._detect_cursor() is True
    
    @patch.dict('os.environ', {'GEMINI_CLI': 'true'})
    def test_detect_gemini_cli(self):
        """Test Gemini CLI detection"""
        validator = CompatibilityValidator()
        assert validator._detect_gemini_cli() is True
    
    def test_detect_no_platform(self):
        """Test detection when no platform is present"""
        validator = CompatibilityValidator()
        
        # Clear environment variables
        with patch.dict('os.environ', {}, clear=True):
            result = validator.detect_current_platform()
            assert result["success"] is False
            assert result["platforms"] == []
            assert result["primary_platform"] is None


class TestPlatformFeatures:
    """Test platform feature definitions"""
    
    def test_platform_features_claude_code(self):
        """Test Claude Code features"""
        validator = CompatibilityValidator()
        features = validator._get_platform_features(PlatformType.CLAUDE_CODE)
        
        assert "full_integration" in features
        assert "mcp_servers" in features
        assert "automated_workflows" in features
        assert "hierarchical_context" in features
    
    def test_platform_features_roo_code(self):
        """Test Roo Code features"""
        validator = CompatibilityValidator()
        features = validator._get_platform_features(PlatformType.ROO_CODE)
        
        assert "native_commands" in features
        assert "performance_monitoring" in features
        assert "integration_hooks" in features
        assert "real_time_validation" in features
    
    def test_platform_optimization_levels(self):
        """Test platform optimization levels"""
        validator = CompatibilityValidator()
        
        assert validator._get_optimization_level(PlatformType.CLAUDE_CODE) == "high"
        assert validator._get_optimization_level(PlatformType.ROO_CODE) == "high"
        assert validator._get_optimization_level(PlatformType.GITHUB_COPILOT) == "medium"
        assert validator._get_optimization_level(PlatformType.AUGGIE_CLI) == "basic"
    
    def test_platform_tiers(self):
        """Test platform tiers"""
        validator = CompatibilityValidator()
        
        assert validator._get_platform_tier(PlatformType.CLAUDE_CODE) == "tier_1"
        assert validator._get_platform_tier(PlatformType.ROO_CODE) == "tier_1"
        assert validator._get_platform_tier(PlatformType.GITHUB_COPILOT) == "tier_2"
        assert validator._get_platform_tier(PlatformType.AUGGIE_CLI) == "tier_3"


if __name__ == "__main__":
    pytest.main([__file__])