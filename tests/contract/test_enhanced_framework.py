"""
Contract tests for enhanced framework

Tests the enhanced framework components including cross-platform compatibility,
constitutional compliance monitoring, and brownfield project analysis tools.
"""
import pytest
from unittest.mock import Mock
from src.specify_cli.enhanced import (
    EnhancedFramework, PlatformTier, ConstitutionalComplianceMonitor,
    BrownfieldAnalysisTools, SecurityValidator, create_enhanced_framework
)


class TestEnhancedFramework:
    """Test suite for enhanced framework"""
    
    def test_platform_tier_definitions(self):
        """Test platform tier definitions"""
        assert PlatformTier.TIER_1.value == "tier_1"
        assert PlatformTier.TIER_2.value == "tier_2"
        assert PlatformTier.TIER_3.value == "tier_3"
    
    def test_enhanced_framework_initialization(self):
        """Test enhanced framework initialization"""
        framework = EnhancedFramework()
        result = framework.initialize_framework()
        
        assert result["success"] is True
        assert "compliance_monitor" in result["components"]
        assert "analysis_tools" in result["components"]
        assert "security_validator" in result["components"]
        assert result["components"]["compliance_monitor"] == "initialized"
        assert result["components"]["analysis_tools"] == "initialized"
        assert result["components"]["security_validator"] == "initialized"
    
    def test_platform_config_loading(self):
        """Test platform configuration loading"""
        framework = EnhancedFramework()
        framework.initialize_framework()
        
        # Test Claude Code (Tier 1)
        claude_config = framework.get_platform_config("claude_code")
        assert claude_config["tier"] == PlatformTier.TIER_1
        assert "full_integration" in claude_config["features"]
        assert "path" in claude_config["installation_methods"]
        assert "uvx" in claude_config["installation_methods"]
        
        # Test GitHub Copilot (Tier 2)
        copilot_config = framework.get_platform_config("github_copilot")
        assert copilot_config["tier"] == PlatformTier.TIER_2
        assert "core_features" in copilot_config["features"]
        
        # Test Qwen Code (Tier 3)
        qwen_config = framework.get_platform_config("qwen_code")
        assert qwen_config["tier"] == PlatformTier.TIER_3
        assert "basic_commands" in qwen_config["features"]
    
    def test_platform_compatibility_validation(self):
        """Test platform compatibility validation"""
        framework = EnhancedFramework()
        framework.initialize_framework()
        
        # Test valid platform
        result = framework.validate_platform_compatibility("claude_code")
        assert result["success"] is True
        assert result["supported"] is True
        assert result["tier"] == "tier_1"
        assert "full_integration" in result["features"]
        
        # Test invalid platform
        result = framework.validate_platform_compatibility("invalid_platform")
        assert result["success"] is False
        assert result["supported"] is False
    
    def test_all_platform_configs(self):
        """Test getting all platform configurations"""
        framework = EnhancedFramework()
        framework.initialize_framework()
        
        all_configs = framework.get_all_platform_configs()
        assert len(all_configs) == 10  # All 10 platforms
        
        # Check key platforms are present
        assert "claude_code" in all_configs
        assert "roo_code" in all_configs
        assert "github_copilot" in all_configs
        assert "cursor" in all_configs
        assert "gemini_cli" in all_configs
        assert "qwen_code" in all_configs
        assert "opencode" in all_configs
        assert "windsurf" in all_configs
        assert "kilo_code" in all_configs
        assert "auggie_cli" in all_configs


class TestConstitutionalComplianceMonitor:
    """Test suite for constitutional compliance monitor"""
    
    def test_compliance_validation(self):
        """Test compliance validation"""
        monitor = ConstitutionalComplianceMonitor()
        
        result = monitor.validate_compliance("test_operation", {"data": "test"})
        
        assert result["success"] is True
        assert result["compliant"] is True
        assert result["score"] >= 0.8
        assert isinstance(result["violations"], list)
    
    def test_compliance_scoring(self):
        """Test compliance scoring"""
        monitor = ConstitutionalComplianceMonitor()
        
        # Test high compliance operation
        result = monitor.validate_compliance("secure_operation", {"security": "high"})
        assert result["score"] >= 0.8
        
        # Test different operation
        result = monitor.validate_compliance("basic_operation", {"basic": "true"})
        assert result["score"] >= 0.0


class TestBrownfieldAnalysisTools:
    """Test suite for brownfield analysis tools"""
    
    def test_project_structure_analysis(self):
        """Test project structure analysis"""
        tools = BrownfieldAnalysisTools()
        
        result = tools.analyze_project_structure("/fake/path")
        
        assert result["success"] is True
        assert result["project_type"] == "brownfield"
        assert "structure" in result
        assert "dependencies" in result
        assert "recommendations" in result
    
    def test_framework_pattern_detection(self):
        """Test framework pattern detection"""
        tools = BrownfieldAnalysisTools()
        
        result = tools.detect_framework_patterns("/fake/path")
        
        assert result["success"] is True
        assert "patterns" in result
        assert "framework" in result
        assert "version" in result
        assert "migration_suggestions" in result


class TestSecurityValidator:
    """Test suite for security validator"""
    
    def test_security_validation(self):
        """Test security validation"""
        validator = SecurityValidator()
        
        config = {"security": "high", "authentication": True}
        result = validator.validate_security_requirements("claude_code", config)
        
        assert result["success"] is True
        assert result["secure"] is True
        assert result["score"] >= 0.7
        assert isinstance(result["recommendations"], list)
    
    def test_security_scoring(self):
        """Test security scoring"""
        validator = SecurityValidator()
        
        # Test high security config
        config = {"security": "high", "encryption": True}
        result = validator.validate_security_requirements("test_platform", config)
        assert result["score"] >= 0.7
        
        # Test low security config
        config = {"security": "low"}
        result = validator.validate_security_requirements("test_platform", config)
        assert result["score"] >= 0.0


class TestFactoryFunctions:
    """Test suite for factory functions"""
    
    def test_create_enhanced_framework(self):
        """Test enhanced framework factory function"""
        framework = create_enhanced_framework()
        
        assert framework is not None
        assert isinstance(framework, EnhancedFramework)
        assert framework.compliance_monitor is not None
        assert framework.analysis_tools is not None
        assert framework.security_validator is not None
        assert len(framework.platform_configs) == 10


if __name__ == "__main__":
    pytest.main([__file__])