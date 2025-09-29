"""
Architecture Engine Module for Spec-Kit Enhancement Initiative
Provides comprehensive architectural guidance and pattern detection
"""

from .framework_patterns import (
    FrameworkPatternLibrary,
    FrameworkPattern,
    PatternConfidence,
    framework_pattern_library
)

from .best_practices import (
    BestPracticesEngine,
    BestPracticeRule,
    best_practices_engine
)

from .structure_validator import (
    StructureValidator,
    ValidationResult,
    structure_validator
)

from .pattern_detector import (
    PatternDetector,
    IntegrationPattern,
    pattern_detector
)

from .cross_architecture import (
    CrossArchitectureGuidance,
    MigrationPath,
    MigrationRecommendation,
    cross_architecture_guidance
)

__all__ = [
    # Framework Patterns
    'FrameworkPatternLibrary',
    'FrameworkPattern', 
    'PatternConfidence',
    'framework_pattern_library',
    
    # Best Practices
    'BestPracticesEngine',
    'BestPracticeRule',
    'best_practices_engine',
    
    # Structure Validation
    'StructureValidator',
    'ValidationResult',
    'structure_validator',
    
    # Pattern Detection
    'PatternDetector',
    'IntegrationPattern',
    'pattern_detector',
    
    # Cross Architecture Guidance
    'CrossArchitectureGuidance',
    'MigrationPath',
    'MigrationRecommendation',
    'cross_architecture_guidance'
]