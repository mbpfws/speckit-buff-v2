"""
Folder Structure Validator for Architecture Engine
Provides hierarchical folder structure analysis and naming convention validation
"""

import re
import os
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ValidationSeverity(Enum):
    """Severity levels for validation issues"""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class StructureCategory(Enum):
    """Categories for structure validation"""
    NAMING = "naming"
    ORGANIZATION = "organization"
    HIERARCHY = "hierarchy"
    CONSISTENCY = "consistency"
    CROSS_PLATFORM = "cross_platform"


@dataclass
class ValidationIssue:
    """Represents a validation issue"""
    category: StructureCategory
    severity: ValidationSeverity
    message: str
    location: str
    suggestion: str
    line_number: Optional[int] = None


@dataclass
class ValidationResult:
    """Result of structure validation"""
    is_valid: bool
    issues: List[ValidationIssue]
    recommendations: List[str]
    score: float  # 0-100 score
    categories: Dict[str, int]  # Issues per category
    structure_patterns: List[str]


class StructureValidator:
    """
    Hierarchical folder structure validator
    Provides naming convention validation and directory organization recommendations
    """
    
    def __init__(self):
        self.naming_conventions = self._initialize_naming_conventions()
        self.structure_patterns = self._initialize_structure_patterns()
        self.cross_platform_rules = self._initialize_cross_platform_rules()
        
    def _initialize_naming_conventions(self) -> Dict[str, Dict[str, Any]]:
        """Initialize naming convention rules"""
        return {
            'general': {
                'pattern': r'^[a-z][a-z0-9_-]*$',
                'description': 'Lowercase with hyphens or underscores',
                'examples': ['my-project', 'user_service', 'api-endpoint'],
                'forbidden': [' ', '.', '..', '__', '--'],
                'max_length': 50
            },
            'python': {
                'pattern': r'^[a-z_][a-z0-9_]*$',
                'description': 'Snake_case for Python',
                'examples': ['user_service', 'api_client', 'data_processor'],
                'forbidden': ['-', ' ', '.'],
                'max_length': 50
            },
            'javascript': {
                'pattern': r'^[a-z][a-z0-9-]*$',
                'description': 'Kebab-case for JavaScript/TypeScript',
                'examples': ['user-service', 'api-client', 'data-processor'],
                'forbidden': ['_', ' ', '.'],
                'max_length': 50
            },
            'java': {
                'pattern': r'^[a-z][a-z0-9]*$',
                'description': 'Lowercase for packages, CamelCase for classes',
                'examples': ['userservice', 'apiclient', 'dataprocessor'],
                'forbidden': ['-', '_', ' ', '.'],
                'max_length': 50
            },
            'csharp': {
                'pattern': r'^[A-Z][a-zA-Z0-9]*$',
                'description': 'PascalCase for C#',
                'examples': ['UserService', 'ApiClient', 'DataProcessor'],
                'forbidden': ['-', '_', ' ', '.'],
                'max_length': 50
            }
        }
        
    def _initialize_structure_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize recommended structure patterns"""
        return {
            'mvc': {
                'description': 'Model-View-Controller pattern',
                'required_dirs': ['models', 'views', 'controllers'],
                'optional_dirs': ['services', 'utils', 'tests'],
                'examples': ['django', 'spring', 'aspnet'],
                'naming_convention': 'framework_specific'
            },
            'microservices': {
                'description': 'Microservices architecture',
                'required_dirs': ['services', 'api-gateway', 'config'],
                'optional_dirs': ['shared', 'infrastructure', 'monitoring'],
                'examples': ['spring-boot', 'express', 'fastapi'],
                'naming_convention': 'service_based'
            },
            'component_based': {
                'description': 'Component-based architecture',
                'required_dirs': ['components', 'services', 'utils'],
                'optional_dirs': ['hooks', 'contexts', 'styles'],
                'examples': ['react', 'vue', 'angular'],
                'naming_convention': 'component_based'
            },
            'layered': {
                'description': 'Layered architecture',
                'required_dirs': ['presentation', 'business', 'data'],
                'optional_dirs': ['infrastructure', 'cross-cutting'],
                'examples': ['clean-architecture', 'onion-architecture'],
                'naming_convention': 'layer_based'
            },
            'feature_based': {
                'description': 'Feature-based organization',
                'required_dirs': ['features', 'shared', 'core'],
                'optional_dirs': ['assets', 'config', 'tests'],
                'examples': ['modern-frontend', 'modular-backend'],
                'naming_convention': 'feature_based'
            }
        }
        
    def _initialize_cross_platform_rules(self) -> List[Dict[str, Any]]:
        """Initialize cross-platform compatibility rules"""
        return [
            {
                'name': 'case_sensitivity',
                'description': 'Use case-sensitive naming',
                'check': lambda path: not any(c.isupper() for c in Path(path).name),
                'severity': ValidationSeverity.WARNING,
                'suggestion': 'Use lowercase names for cross-platform compatibility'
            },
            {
                'name': 'special_characters',
                'description': 'Avoid special characters in names',
                'check': lambda path: not re.search(r'[!@#$%^&*()+={}\[\]|\\:;"\'<>?,~`]', Path(path).name),
                'severity': ValidationSeverity.ERROR,
                'suggestion': 'Use only alphanumeric characters, hyphens, and underscores'
            },
            {
                'name': 'max_path_length',
                'description': 'Keep path lengths reasonable',
                'check': lambda path: len(str(Path(path))) < 260,  # Windows MAX_PATH
                'severity': ValidationSeverity.WARNING,
                'suggestion': 'Keep total path length under 260 characters for Windows compatibility'
            },
            {
                'name': 'reserved_names',
                'description': 'Avoid reserved file names',
                'check': lambda path: Path(path).name.lower() not in [
                    'con', 'prn', 'aux', 'nul', 'com1', 'com2', 'com3', 'com4',
                    'com5', 'com6', 'com7', 'com8', 'com9', 'lpt1', 'lpt2', 'lpt3',
                    'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8', 'lpt9'
                ],
                'severity': ValidationSeverity.ERROR,
                'suggestion': 'Avoid Windows reserved file names'
            }
        ]
        
    def validate_structure(self, project_path: str, 
                          detected_patterns: Dict[str, Any],
                          tech_stack: Dict[str, Any]) -> ValidationResult:
        """
        Validate folder structure and naming conventions
        
        Args:
            project_path: Path to project root
            detected_patterns: Detected architectural patterns
            tech_stack: Technology stack information
            
        Returns:
            Validation results
        """
        issues = []
        recommendations = []
        structure_patterns = []
        
        # Get framework and language information
        frameworks = tech_stack.get('frameworks', [])
        languages = tech_stack.get('languages', [])
        
        # Determine appropriate naming convention
        naming_convention = self._determine_naming_convention(frameworks, languages)
        
        # Validate naming conventions
        naming_issues = self._validate_naming_conventions(project_path, naming_convention)
        issues.extend(naming_issues)
        
        # Validate structure patterns
        structure_issues, detected_patterns = self._validate_structure_patterns(
            project_path, detected_patterns, frameworks
        )
        issues.extend(structure_issues)
        structure_patterns.extend(detected_patterns)
        
        # Validate cross-platform compatibility
        cross_platform_issues = self._validate_cross_platform_compatibility(project_path)
        issues.extend(cross_platform_issues)
        
        # Generate recommendations
        recommendations = self._generate_structure_recommendations(
            issues, frameworks, languages, detected_patterns
        )
        
        # Calculate score
        score = self._calculate_structure_score(issues)
        
        # Categorize issues
        categories = self._categorize_issues(issues)
        
        # Determine if structure is valid (score >= 70)
        is_valid = score >= 70 and not any(
            issue.severity == ValidationSeverity.ERROR for issue in issues
        )
        
        return ValidationResult(
            is_valid=is_valid,
            issues=issues,
            recommendations=recommendations,
            score=score,
            categories=categories,
            structure_patterns=structure_patterns
        )
    
    def _determine_naming_convention(self, frameworks: List[str], 
                                   languages: List[str]) -> str:
        """Determine appropriate naming convention based on tech stack"""
        # Framework-specific conventions
        framework_conventions = {
            'django': 'python',
            'flask': 'python',
            'fastapi': 'python',
            'react': 'javascript',
            'vue': 'javascript',
            'angular': 'javascript',
            'spring': 'java',
            'spring-boot': 'java',
            'aspnet': 'csharp'
        }
        
        # Check framework-specific conventions first
        for framework in frameworks:
            if framework.lower() in framework_conventions:
                return framework_conventions[framework.lower()]
        
        # Fall back to language-based conventions
        for language in languages:
            if language.lower() in ['python']:
                return 'python'
            elif language.lower() in ['javascript', 'typescript']:
                return 'javascript'
            elif language.lower() in ['java']:
                return 'java'
            elif language.lower() in ['csharp', 'c#']:
                return 'csharp'
        
        # Default to general convention
        return 'general'
    
    def _validate_naming_conventions(self, project_path: str, 
                                   convention: str) -> List[ValidationIssue]:
        """Validate naming conventions"""
        issues = []
        
        if convention not in self.naming_conventions:
            return issues
        
        convention_rules = self.naming_conventions[convention]
        
        # Walk through project directory
        for root, dirs, files in os.walk(project_path):
            # Skip hidden directories and common ignore patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', '.git']]
            
            # Check directory names
            for dir_name in dirs:
                if not self._is_valid_name(dir_name, convention_rules):
                    issues.append(ValidationIssue(
                        category=StructureCategory.NAMING,
                        severity=ValidationSeverity.WARNING,
                        message=f"Directory name '{dir_name}' doesn't follow {convention} naming convention",
                        location=os.path.join(root, dir_name),
                        suggestion=f"Use {convention_rules['description']}: {', '.join(convention_rules['examples'])}"
                    ))
            
            # Check file names
            for file_name in files:
                name_without_ext = os.path.splitext(file_name)[0]
                if not self._is_valid_name(name_without_ext, convention_rules):
                    issues.append(ValidationIssue(
                        category=StructureCategory.NAMING,
                        severity=ValidationSeverity.WARNING,
                        message=f"File name '{file_name}' doesn't follow {convention} naming convention",
                        location=os.path.join(root, file_name),
                        suggestion=f"Use {convention_rules['description']}: {', '.join(convention_rules['examples'])}"
                    ))
        
        return issues
    
    def _is_valid_name(self, name: str, convention_rules: Dict[str, Any]) -> bool:
        """Check if a name follows the convention rules"""
        # Check pattern
        if not re.match(convention_rules['pattern'], name):
            return False
        
        # Check forbidden characters/patterns
        for forbidden in convention_rules.get('forbidden', []):
            if forbidden in name:
                return False
        
        # Check length
        max_length = convention_rules.get('max_length', 50)
        if len(name) > max_length:
            return False
        
        return True
    
    def _validate_structure_patterns(self, project_path: str, 
                                   detected_patterns: Dict[str, Any],
                                   frameworks: List[str]) -> Tuple[List[ValidationIssue], List[str]]:
        """Validate structure patterns"""
        issues = []
        structure_patterns = []
        
        # Determine which patterns to check based on detected frameworks
        applicable_patterns = self._get_applicable_patterns(frameworks)
        
        for pattern_name, pattern_data in applicable_patterns.items():
            pattern_issues = self._check_pattern_compliance(
                project_path, pattern_name, pattern_data
            )
            issues.extend(pattern_issues)
            
            if not pattern_issues:
                structure_patterns.append(pattern_name)
        
        return issues, structure_patterns
    
    def _get_applicable_patterns(self, frameworks: List[str]) -> Dict[str, Dict[str, Any]]:
        """Get structure patterns applicable to the frameworks"""
        applicable = {}
        
        for pattern_name, pattern_data in self.structure_patterns.items():
            # Check if any of the project's frameworks match the pattern examples
            for example_framework in pattern_data.get('examples', []):
                if any(framework.lower() in example_framework.lower() for framework in frameworks):
                    applicable[pattern_name] = pattern_data
                    break
        
        # If no specific patterns match, use general patterns
        if not applicable:
            applicable = {
                'feature_based': self.structure_patterns['feature_based'],
                'layered': self.structure_patterns['layered']
            }
        
        return applicable
    
    def _check_pattern_compliance(self, project_path: str, 
                                pattern_name: str, 
                                pattern_data: Dict[str, Any]) -> List[ValidationIssue]:
        """Check compliance with a specific structure pattern"""
        issues = []
        
        required_dirs = pattern_data.get('required_dirs', [])
        optional_dirs = pattern_data.get('optional_dirs', [])
        
        # Check for required directories
        for required_dir in required_dirs:
            if not self._directory_exists(project_path, required_dir):
                issues.append(ValidationIssue(
                    category=StructureCategory.ORGANIZATION,
                    severity=ValidationSeverity.ERROR,
                    message=f"Missing required directory '{required_dir}' for {pattern_name} pattern",
                    location=project_path,
                    suggestion=f"Create the '{required_dir}' directory to follow {pattern_data['description']}"
                ))
        
        # Check for optional directories (warnings if missing)
        for optional_dir in optional_dirs:
            if not self._directory_exists(project_path, optional_dir):
                issues.append(ValidationIssue(
                    category=StructureCategory.ORGANIZATION,
                    severity=ValidationSeverity.INFO,
                    message=f"Consider adding optional directory '{optional_dir}' for {pattern_name} pattern",
                    location=project_path,
                    suggestion=f"Consider creating the '{optional_dir}' directory for better organization"
                ))
        
        return issues
    
    def _directory_exists(self, project_path: str, dir_name: str) -> bool:
        """Check if a directory exists in the project"""
        # Check at root level
        if os.path.isdir(os.path.join(project_path, dir_name)):
            return True
        
        # Check one level deep
        for item in os.listdir(project_path):
            item_path = os.path.join(project_path, item)
            if os.path.isdir(item_path):
                if os.path.isdir(os.path.join(item_path, dir_name)):
                    return True
        
        return False
    
    def _validate_cross_platform_compatibility(self, project_path: str) -> List[ValidationIssue]:
        """Validate cross-platform compatibility"""
        issues = []
        
        for rule in self.cross_platform_rules:
            if not rule['check'](project_path):
                issues.append(ValidationIssue(
                    category=StructureCategory.CROSS_PLATFORM,
                    severity=rule['severity'],
                    message=rule['description'],
                    location=project_path,
                    suggestion=rule['suggestion']
                ))
        
        return issues
    
    def _generate_structure_recommendations(self, issues: List[ValidationIssue],
                                          frameworks: List[str],
                                          languages: List[str],
                                          detected_patterns: List[str]) -> List[str]:
        """Generate structure recommendations"""
        recommendations = []
        
        # Framework-specific recommendations
        if 'django' in frameworks:
            recommendations.extend([
                'Use Django app structure: models.py, views.py, urls.py, templates/',
                'Implement proper Django project layout',
                'Use Django static files organization'
            ])
        
        if 'react' in frameworks:
            recommendations.extend([
                'Use component-based folder structure',
                'Separate containers and components',
                'Organize by features rather than file types'
            ])
        
        if 'spring' in frameworks:
            recommendations.extend([
                'Use Maven/Gradle standard directory layout',
                'Separate source code by layers: controller, service, repository',
                'Use proper package naming conventions'
            ])
        
        # Pattern-specific recommendations
        if 'mvc' in detected_patterns:
            recommendations.extend([
                'Ensure clear separation between models, views, and controllers',
                'Use appropriate naming for each layer',
                'Implement proper MVC routing'
            ])
        
        if 'microservices' in detected_patterns:
            recommendations.extend([
                'Use service-oriented directory structure',
                'Implement proper API versioning',
                'Use shared libraries for common functionality'
            ])
        
        # General recommendations
        recommendations.extend([
            'Use consistent naming conventions across the project',
            'Keep directory structures shallow (max 3-4 levels)',
            'Group related functionality together',
            'Use meaningful directory names',
            'Avoid mixing different architectural patterns',
            'Document the project structure in README'
        ])
        
        return list(set(recommendations))  # Remove duplicates
    
    def _calculate_structure_score(self, issues: List[ValidationIssue]) -> float:
        """Calculate structure validation score"""
        if not issues:
            return 100.0
        
        # Weight issues by severity
        severity_weights = {
            ValidationSeverity.ERROR: 10,
            ValidationSeverity.WARNING: 5,
            ValidationSeverity.INFO: 1
        }
        
        total_weight = sum(severity_weights[issue.severity] for issue in issues)
        
        # Calculate score (inverse of weighted issues)
        max_acceptable_weight = 50  # Arbitrary threshold
        score = max(0, 100 - (total_weight / max_acceptable_weight * 100))
        
        return score
    
    def _categorize_issues(self, issues: List[ValidationIssue]) -> Dict[str, int]:
        """Categorize issues by category"""
        categories = {}
        
        for issue in issues:
            category = issue.category.value
            categories[category] = categories.get(category, 0) + 1
        
        return categories
    
    def suggest_optimal_structure(self, frameworks: List[str], 
                                project_type: str) -> Dict[str, Any]:
        """
        Suggest optimal folder structure based on frameworks and project type
        
        Args:
            frameworks: List of frameworks used
            project_type: Type of project (greenfield, brownfield, etc.)
            
        Returns:
            Suggested structure configuration
        """
        suggestions = {
            'recommended_structure': {},
            'naming_convention': self._determine_naming_convention(frameworks, []),
            'explanation': '',
            'implementation_steps': []
        }
        
        # Determine optimal structure based on frameworks
        if 'django' in frameworks:
            suggestions['recommended_structure'] = {
                'project_name': {
                    'apps': {
                        'core': ['models.py', 'views.py', 'urls.py', 'admin.py'],
                        'users': ['models.py', 'views.py', 'urls.py', 'forms.py']
                    },
                    'config': ['settings.py', 'urls.py', 'wsgi.py'],
                    'templates': ['base.html', 'components/'],
                    'static': ['css/', 'js/', 'images/'],
                    'requirements': ['base.txt', 'dev.txt', 'prod.txt']
                }
            }
            suggestions['explanation'] = 'Django project structure with apps-based organization'
            
        elif 'react' in frameworks:
            suggestions['recommended_structure'] = {
                'src': {
                    'components': ['common/', 'features/'],
                    'hooks': ['useAuth.js', 'useApi.js'],
                    'services': ['api.js', 'auth.js'],
                    'utils': ['helpers.js', 'validators.js'],
                    'styles': ['global.css', 'variables.css'],
                    'tests': ['components/', 'hooks/', 'utils/']
                },
                'public': ['index.html', 'favicon.ico'],
                'config': ['webpack.config.js', 'jest.config.js']
            }
            suggestions['explanation'] = 'React component-based structure with feature organization'
            
        elif 'spring' in frameworks:
            suggestions['recommended_structure'] = {
                'src': {
                    'main': {
                        'java': {
                            'com': {
                                'company': {
                                    'project': {
                                        'controller': ['UserController.java'],
                                        'service': ['UserService.java', 'UserServiceImpl.java'],
                                        'repository': ['UserRepository.java'],
                                        'model': ['User.java'],
                                        'config': ['SecurityConfig.java']
                                    }
                                }
                            }
                        },
                        'resources': ['application.properties', 'templates/', 'static/']
                    },
                    'test': ['java/', 'resources/']
                }
            }
            suggestions['explanation'] = 'Spring Boot Maven structure with layered architecture'
        
        # Add implementation steps
        suggestions['implementation_steps'] = [
            'Create the recommended directory structure',
            'Move existing files to appropriate locations',
            'Update import paths and references',
            'Add configuration files for build tools',
            'Update documentation with new structure',
            'Test the restructured project'
        ]
        
        return suggestions


# Global instance for easy access
structure_validator = StructureValidator()