"""
Cross-platform compatibility layer for Spec-Kit

Provides platform detection, adaptation mechanisms, and validation utilities
to ensure compatibility across all 10 supported AI coding platforms.
"""
from typing import Dict, Any, List, Optional
from enum import Enum
import platform
import os
import sys
import logging


class PlatformType(Enum):
    """Supported platform types"""
    CLAUDE_CODE = "claude_code"
    ROO_CODE = "roo_code"
    GITHUB_COPILOT = "github_copilot"
    CURSOR = "cursor"
    GEMINI_CLI = "gemini_cli"
    QWEN_CODE = "qwen_code"
    OPENCODE = "opencode"
    WINDSURF = "windsurf"
    KILO_CODE = "kilo_code"
    AUGGIE_CLI = "auggie_cli"


class InstallationMethod(Enum):
    """Supported installation methods"""
    PATH = "path"
    UVX = "uvx"


class CompatibilityValidator:
    """
    Validates and ensures cross-platform compatibility across all 10 AI platforms
    """
    
    def __init__(self):
        self.platform_detectors = {
            PlatformType.CLAUDE_CODE: self._detect_claude_code,
            PlatformType.ROO_CODE: self._detect_roo_code,
            PlatformType.GITHUB_COPILOT: self._detect_github_copilot,
            PlatformType.CURSOR: self._detect_cursor,
            PlatformType.GEMINI_CLI: self._detect_gemini_cli,
            PlatformType.QWEN_CODE: self._detect_qwen_code,
            PlatformType.OPENCODE: self._detect_opencode,
            PlatformType.WINDSURF: self._detect_windsurf,
            PlatformType.KILO_CODE: self._detect_kilo_code,
            PlatformType.AUGGIE_CLI: self._detect_auggie_cli,
        }
        self.logger = logging.getLogger(__name__)
    
    def detect_current_platform(self) -> Dict[str, Any]:
        """Detect the current AI coding platform"""
        detected_platforms = []
        
        for platform_type, detector in self.platform_detectors.items():
            if detector():
                detected_platforms.append(platform_type.value)
        
        if detected_platforms:
            return {
                "success": True,
                "platforms": detected_platforms,
                "primary_platform": detected_platforms[0],
                "detection_method": "environment_analysis"
            }
        else:
            return {
                "success": False,
                "platforms": [],
                "primary_platform": None,
                "detection_method": "environment_analysis",
                "error": "No supported AI platform detected"
            }
    
    def validate_installation_method(self, platform_type: str, method: str) -> Dict[str, Any]:
        """Validate installation method compatibility for a platform"""
        try:
            platform_enum = PlatformType(platform_type)
            method_enum = InstallationMethod(method)
            
            # Check if installation method is supported
            supported_methods = self._get_supported_installation_methods(platform_enum)
            
            return {
                "success": True,
                "supported": method_enum.value in supported_methods,
                "platform": platform_type,
                "method": method,
                "supported_methods": supported_methods,
                "recommendations": self._get_installation_recommendations(platform_enum)
            }
            
        except ValueError as e:
            return {
                "success": False,
                "error": f"Invalid platform or method: {e}",
                "platform": platform_type,
                "method": method
            }
    
    def get_compatibility_matrix(self) -> Dict[str, Any]:
        """Get comprehensive compatibility matrix for all platforms"""
        matrix = {}
        
        for platform_type in PlatformType:
            platform_name = platform_type.value
            matrix[platform_name] = {
                "installation_methods": self._get_supported_installation_methods(platform_type),
                "features": self._get_platform_features(platform_type),
                "requirements": self._get_platform_requirements(platform_type),
                "optimization_level": self._get_optimization_level(platform_type),
                "tier": self._get_platform_tier(platform_type)
            }
        
        return {
            "success": True,
            "matrix": matrix,
            "last_updated": "2025-09-29",
            "version": "2.0.0"
        }
    
    def validate_cross_platform_compatibility(self, source_platform: str, target_platforms: List[str]) -> Dict[str, Any]:
        """Validate compatibility between platforms"""
        try:
            source = PlatformType(source_platform)
            targets = [PlatformType(tp) for tp in target_platforms]
            
            compatibility_results = {}
            
            for target in targets:
                compatibility_results[target.value] = self._validate_platform_pair_compatibility(source, target)
            
            return {
                "success": True,
                "source_platform": source_platform,
                "target_platforms": target_platforms,
                "compatibility": compatibility_results,
                "overall_compatibility": self._calculate_overall_compatibility(compatibility_results)
            }
            
        except ValueError as e:
            return {
                "success": False,
                "error": f"Invalid platform: {e}",
                "source_platform": source_platform,
                "target_platforms": target_platforms
            }
    
    def _get_supported_installation_methods(self, platform_type: PlatformType) -> List[str]:
        """Get supported installation methods for a platform"""
        # All platforms support both methods, but with different optimization levels
        return [method.value for method in InstallationMethod]
    
    def _get_platform_features(self, platform_type: PlatformType) -> List[str]:
        """Get platform-specific features"""
        features_map = {
            PlatformType.CLAUDE_CODE: ["full_integration", "mcp_servers", "automated_workflows", "hierarchical_context"],
            PlatformType.ROO_CODE: ["native_commands", "performance_monitoring", "integration_hooks", "real_time_validation"],
            PlatformType.GITHUB_COPILOT: ["core_features", "ide_integration", "context_awareness", "intelligent_suggestions"],
            PlatformType.CURSOR: ["advanced_ide", "real_time_context", "pattern_detection", "cross_file_analysis"],
            PlatformType.GEMINI_CLI: ["cli_interface", "batch_processing", "script_automation", "terminal_optimization"],
            PlatformType.QWEN_CODE: ["basic_commands", "limited_automation", "core_framework"],
            PlatformType.OPENCODE: ["core_functionality", "standard_execution", "manual_synchronization"],
            PlatformType.WINDSURF: ["ide_integration", "project_awareness", "development_workflow"],
            PlatformType.KILO_CODE: ["lightweight", "minimal_footprint", "basic_analysis"],
            PlatformType.AUGGIE_CLI: ["fundamental_support", "basic_validation", "manual_setup"]
        }
        return features_map.get(platform_type, [])
    
    def _get_platform_requirements(self, platform_type: PlatformType) -> Dict[str, Any]:
        """Get platform-specific requirements"""
        requirements_map = {
            PlatformType.CLAUDE_CODE: {
                "min_version": "3.5",
                "dependencies": ["mcp_servers", "hierarchical_context"],
                "environment": ["vscode", "claude_desktop"],
                "capabilities": ["full_automation", "advanced_integration"]
            },
            PlatformType.ROO_CODE: {
                "min_version": "1.0",
                "dependencies": ["native_execution", "performance_tools"],
                "environment": ["roo_environment"],
                "capabilities": ["native_integration", "real_time_monitoring"]
            },
            # Add requirements for other platforms...
        }
        return requirements_map.get(platform_type, {})
    
    def _get_optimization_level(self, platform_type: PlatformType) -> str:
        """Get optimization level for platform"""
        optimization_map = {
            PlatformType.CLAUDE_CODE: "high",
            PlatformType.ROO_CODE: "high",
            PlatformType.GITHUB_COPILOT: "medium",
            PlatformType.CURSOR: "medium",
            PlatformType.GEMINI_CLI: "medium",
            PlatformType.QWEN_CODE: "basic",
            PlatformType.OPENCODE: "basic",
            PlatformType.WINDSURF: "basic",
            PlatformType.KILO_CODE: "basic",
            PlatformType.AUGGIE_CLI: "basic"
        }
        return optimization_map.get(platform_type, "basic")
    
    def _get_platform_tier(self, platform_type: PlatformType) -> str:
        """Get platform tier"""
        tier_map = {
            PlatformType.CLAUDE_CODE: "tier_1",
            PlatformType.ROO_CODE: "tier_1",
            PlatformType.GITHUB_COPILOT: "tier_2",
            PlatformType.CURSOR: "tier_2",
            PlatformType.GEMINI_CLI: "tier_2",
            PlatformType.QWEN_CODE: "tier_3",
            PlatformType.OPENCODE: "tier_3",
            PlatformType.WINDSURF: "tier_3",
            PlatformType.KILO_CODE: "tier_3",
            PlatformType.AUGGIE_CLI: "tier_3"
        }
        return tier_map.get(platform_type, "tier_3")
    
    def _validate_platform_pair_compatibility(self, source: PlatformType, target: PlatformType) -> Dict[str, Any]:
        """Validate compatibility between two platforms"""
        # Tier 1 platforms have full compatibility
        if self._get_platform_tier(source) == "tier_1" and self._get_platform_tier(target) == "tier_1":
            return {"compatible": True, "level": "full", "notes": "Full integration compatibility"}
        
        # Cross-tier compatibility with appropriate adaptations
        source_tier = self._get_platform_tier(source)
        target_tier = self._get_platform_tier(target)
        
        if source_tier == target_tier:
            return {"compatible": True, "level": "high", "notes": "Same tier compatibility"}
        elif abs(int(source_tier[-1]) - int(target_tier[-1])) == 1:
            return {"compatible": True, "level": "medium", "notes": "Adjacent tier compatibility"}
        else:
            return {"compatible": True, "level": "basic", "notes": "Cross-tier compatibility with limitations"}
    
    def _calculate_overall_compatibility(self, compatibility_results: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate overall compatibility score"""
        compatible_count = sum(1 for result in compatibility_results.values() if result["compatible"])
        total_count = len(compatibility_results)
        
        return {
            "score": compatible_count / total_count if total_count > 0 else 0,
            "compatible_platforms": compatible_count,
            "total_platforms": total_count,
            "status": "excellent" if compatible_count == total_count else "good" if compatible_count >= total_count * 0.8 else "fair"
        }
    
    def _get_installation_recommendations(self, platform_type: PlatformType) -> List[str]:
        """Get installation recommendations for platform"""
        recommendations = {
            PlatformType.CLAUDE_CODE: ["Use PATH installation for full integration", "uvx for quick setup"],
            PlatformType.ROO_CODE: ["PATH installation recommended for native performance"],
            PlatformType.GITHUB_COPILOT: ["PATH installation with VS Code workspace configuration"],
            PlatformType.CURSOR: ["Either method works, PATH for better IDE integration"],
            PlatformType.GEMINI_CLI: ["uvx for simplicity, PATH for advanced usage"],
            PlatformType.QWEN_CODE: ["Both methods supported, manual sync required"],
            PlatformType.OPENCODE: ["Standard installation methods"],
            PlatformType.WINDSURF: ["IDE integration works with both methods"],
            PlatformType.KILO_CODE: ["Lightweight installation either method"],
            PlatformType.AUGGIE_CLI: ["Basic installation support"]
        }
        return recommendations.get(platform_type, ["Standard installation recommended"])
    
    # Platform detection methods
    def _detect_claude_code(self) -> bool:
        """Detect Claude Code environment"""
        return any([
            "CLAUDE_CODE" in os.environ,
            "ANTHROPIC" in os.environ,
            any("claude" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_roo_code(self) -> bool:
        """Detect Roo Code environment"""
        return any([
            "ROO_CODE" in os.environ,
            any("roo" in arg.lower() for arg in sys.argv),
            "roocode" in sys.executable.lower()
        ])
    
    def _detect_github_copilot(self) -> bool:
        """Detect GitHub Copilot environment"""
        return any([
            "GITHUB_COPILOT" in os.environ,
            "VSCODE" in os.environ,
            any("copilot" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_cursor(self) -> bool:
        """Detect Cursor environment"""
        return any([
            "CURSOR" in os.environ,
            any("cursor" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_gemini_cli(self) -> bool:
        """Detect Gemini CLI environment"""
        return any([
            "GEMINI_CLI" in os.environ,
            any("gemini" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_qwen_code(self) -> bool:
        """Detect Qwen Code environment"""
        return any([
            "QWEN_CODE" in os.environ,
            any("qwen" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_opencode(self) -> bool:
        """Detect opencode environment"""
        return any([
            "OPENCODE" in os.environ,
            any("opencode" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_windsurf(self) -> bool:
        """Detect Windsurf environment"""
        return any([
            "WINDSURF" in os.environ,
            any("windsurf" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_kilo_code(self) -> bool:
        """Detect Kilo Code environment"""
        return any([
            "KILO_CODE" in os.environ,
            any("kilo" in arg.lower() for arg in sys.argv)
        ])
    
    def _detect_auggie_cli(self) -> bool:
        """Detect Auggie CLI environment"""
        return any([
            "AUGGIE_CLI" in os.environ,
            any("auggie" in arg.lower() for arg in sys.argv)
        ])


class PlatformAdapter:
    """
    Adapts framework behavior for different platforms
    """
    
    def __init__(self, platform_type: PlatformType):
        self.platform_type = platform_type
        self.adaptation_rules = self._load_adaptation_rules()
        self.logger = logging.getLogger(__name__)
    
    def adapt_command(self, command: str, context: Dict[str, Any]) -> str:
        """Adapt command for specific platform"""
        adaptation_rules = self.adaptation_rules.get("commands", {})
        
        for pattern, replacement in adaptation_rules.items():
            if pattern in command:
                command = command.replace(pattern, replacement)
        
        return command
    
    def adapt_configuration(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Adapt configuration for specific platform"""
        platform_config = self.adaptation_rules.get("configuration", {})
        
        # Merge platform-specific configuration
        adapted_config = {**config, **platform_config}
        
        return adapted_config
    
    def get_platform_optimizations(self) -> Dict[str, Any]:
        """Get platform-specific optimizations"""
        return self.adaptation_rules.get("optimizations", {})
    
    def _load_adaptation_rules(self) -> Dict[str, Any]:
        """Load adaptation rules for platform"""
        rules_map = {
            PlatformType.CLAUDE_CODE: {
                "commands": {
                    "specify": "specify --platform claude --context-optimized",
                    "analyze": "specify analyze --platform claude --hierarchical-context"
                },
                "configuration": {
                    "context_window": "large",
                    "mcp_integration": True,
                    "automated_workflows": True
                },
                "optimizations": {
                    "context_management": "hierarchical",
                    "prompt_optimization": "auto_enhancement",
                    "workflow_transitions": "automated"
                }
            },
            PlatformType.ROO_CODE: {
                "commands": {
                    "specify": "specify --platform roo --performance-optimized",
                    "analyze": "specify analyze --platform roo --native-execution"
                },
                "configuration": {
                    "performance_monitoring": True,
                    "integration_hooks": True,
                    "real_time_validation": True
                },
                "optimizations": {
                    "execution_speed": "native",
                    "memory_usage": "optimized",
                    "integration_points": "framework_specific"
                }
            },
            # Add adaptation rules for other platforms...
        }
        return rules_map.get(self.platform_type, {})


def create_compatibility_validator() -> CompatibilityValidator:
    """Factory function to create compatibility validator"""
    return CompatibilityValidator()


def create_platform_adapter(platform_type: str) -> PlatformAdapter:
    """Factory function to create platform adapter"""
    try:
        platform_enum = PlatformType(platform_type)
        return PlatformAdapter(platform_enum)
    except ValueError:
        # Default to basic platform adapter
        return PlatformAdapter(PlatformType.AUGGIE_CLI)