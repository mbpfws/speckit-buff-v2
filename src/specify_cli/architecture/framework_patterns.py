"""
Framework Pattern Library for Architecture Engine
Provides comprehensive framework pattern detection and validation
"""

import re
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum


class PatternConfidence(Enum):
    """Confidence levels for pattern detection"""
    HIGH = 0.9
    MEDIUM = 0.7
    LOW = 0.5
    UNCERTAIN = 0.3


@dataclass
class FrameworkPattern:
    """Represents a detected framework pattern"""
    name: str
    framework: str
    pattern_type: str
    confidence: float
    evidence: List[str]
    recommendations: List[str]
    anti_patterns: List[str]


@dataclass
class PatternEvidence:
    """Evidence for pattern detection"""
    type: str
    location: str
    content: str
    confidence: float


class FrameworkPatternLibrary:
    """
    Comprehensive framework pattern detection library
    Supports React, Vue, Angular, Django, Flask, Spring patterns
    """
    
    def __init__(self):
        self.framework_patterns = self._initialize_patterns()
        self.anti_patterns = self._initialize_anti_patterns()
        
    def _initialize_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize framework-specific patterns"""
        return {
            'react': {
                'component_based': {
                    'indicators': [
                        r'import.*React.*from',
                        r'function.*\(.*\).*{.*return',
                        r'class.*extends.*Component',
                        r'useState\(',
                        r'useEffect\(',
                        r'jsx|\.jsx$'
                    ],
                    'file_patterns': ['*.jsx', '*.tsx', 'components/', 'src/components/'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use functional components with hooks',
                        'Implement proper component composition',
                        'Follow React best practices for state management'
                    ]
                },
                'hooks_pattern': {
                    'indicators': [
                        r'useState\(',
                        r'useEffect\(',
                        r'useContext\(',
                        r'useReducer\(',
                        r'useCallback\(',
                        r'useMemo\('
                    ],
                    'file_patterns': ['*.jsx', '*.tsx'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use custom hooks for reusable logic',
                        'Follow hooks rules and conventions',
                        'Implement proper dependency arrays'
                    ]
                },
                'redux_pattern': {
                    'indicators': [
                        r'import.*redux',
                        r'createStore\(',
                        r'combineReducers\(',
                        r'connect\(',
                        r'useSelector\(',
                        r'useDispatch\('
                    ],
                    'file_patterns': ['*redux*', '*store*', '*actions*', '*reducers*'],
                    'confidence': PatternConfidence.MEDIUM.value,
                    'recommendations': [
                        'Use Redux Toolkit for modern Redux',
                        'Implement proper action creators',
                        'Follow Redux best practices'
                    ]
                }
            },
            'vue': {
                'component_based': {
                    'indicators': [
                        r'export.*default.*{',
                        r'template.*:',
                        r'script.*:',
                        r'style.*:',
                        r'\.vue$'
                    ],
                    'file_patterns': ['*.vue', 'components/', 'src/components/'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Vue 3 Composition API',
                        'Implement proper component props',
                        'Follow Vue style guide'
                    ]
                },
                'vuex_pattern': {
                    'indicators': [
                        r'import.*vuex',
                        r'createStore\(',
                        r'state:',
                        r'mutations:',
                        r'actions:',
                        r'getters:'
                    ],
                    'file_patterns': ['*store*', '*vuex*'],
                    'confidence': PatternConfidence.MEDIUM.value,
                    'recommendations': [
                        'Use Vuex 4 for Vue 3',
                        'Implement proper module structure',
                        'Follow Vuex best practices'
                    ]
                }
            },
            'angular': {
                'component_based': {
                    'indicators': [
                        r'@Component\(',
                        r'@Component\({',
                        r'selector:',
                        r'templateUrl:',
                        r'styleUrls:'
                    ],
                    'file_patterns': ['*.component.ts', '*.component.html', '*.component.css'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Angular CLI for scaffolding',
                        'Implement proper component lifecycle',
                        'Follow Angular style guide'
                    ]
                },
                'dependency_injection': {
                    'indicators': [
                        r'@Injectable\(',
                        r'constructor\(.*private.*\)',
                        r'@Inject\(',
                        r'providers:',
                        r'imports:'
                    ],
                    'file_patterns': ['*.service.ts', '*.module.ts'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use dependency injection properly',
                        'Implement proper service architecture',
                        'Follow Angular DI best practices'
                    ]
                },
                'rxjs_pattern': {
                    'indicators': [
                        r'import.*rxjs',
                        r'Observable',
                        r'Subject',
                        r'pipe\(',
                        r'subscribe\(',
                        r'map\(',
                        r'filter\('
                    ],
                    'file_patterns': ['*.service.ts', '*.component.ts'],
                    'confidence': PatternConfidence.MEDIUM.value,
                    'recommendations': [
                        'Use RxJS operators effectively',
                        'Implement proper subscription management',
                        'Follow reactive programming patterns'
                    ]
                }
            },
            'django': {
                'mvc_pattern': {
                    'indicators': [
                        r'from.*django.*import',
                        r'class.*View\(',
                        r'def.*request.*:',
                        r'models\.',
                        r'forms\.',
                        r'templates/'
                    ],
                    'file_patterns': ['views.py', 'models.py', 'forms.py', 'templates/'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Django ORM effectively',
                        'Implement proper view classes',
                        'Follow Django best practices'
                    ]
                },
                'orm_pattern': {
                    'indicators': [
                        r'class.*models\.Model',
                        r'Models\.',
                        r'objects\.',
                        r'filter\(',
                        r'get\(',
                        r'save\('
                    ],
                    'file_patterns': ['models.py'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Django ORM methods properly',
                        'Implement proper model relationships',
                        'Follow Django ORM best practices'
                    ]
                },
                'middleware_pattern': {
                    'indicators': [
                        r'class.*Middleware',
                        r'def.*__call__\(',
                        r'request\.',
                        r'response\.',
                        r'MIDDLEWARE.*='
                    ],
                    'file_patterns': ['middleware.py', 'settings.py'],
                    'confidence': PatternConfidence.MEDIUM.value,
                    'recommendations': [
                        'Use middleware for cross-cutting concerns',
                        'Implement proper middleware ordering',
                        'Follow Django middleware patterns'
                    ]
                }
            },
            'flask': {
                'microframework_pattern': {
                    'indicators': [
                        r'from.*flask.*import',
                        r'@app\.route\(',
                        r'Flask\(',
                        r'request\.',
                        r'response\.',
                        r'jsonify\('
                    ],
                    'file_patterns': ['app.py', 'routes.py', 'api.py'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Flask blueprints for organization',
                        'Implement proper error handling',
                        'Follow Flask best practices'
                    ]
                },
                'restful_pattern': {
                    'indicators': [
                        r'flask_restful',
                        r'Resource',
                        r'api\.add_resource',
                        r'get\(',
                        r'post\(',
                        r'put\(',
                        r'delete\('
                    ],
                    'file_patterns': ['*resource*', '*api*'],
                    'confidence': PatternConfidence.MEDIUM.value,
                    'recommendations': [
                        'Use Flask-RESTful for APIs',
                        'Implement proper HTTP methods',
                        'Follow RESTful conventions'
                    ]
                }
            },
            'spring': {
                'dependency_injection': {
                    'indicators': [
                        r'@Autowired',
                        r'@Component',
                        r'@Service',
                        r'@Repository',
                        r'@Controller',
                        r'@RestController'
                    ],
                    'file_patterns': ['*.java'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Spring DI annotations properly',
                        'Implement proper component scanning',
                        'Follow Spring best practices'
                    ]
                },
                'mvc_pattern': {
                    'indicators': [
                        r'@Controller',
                        r'@RestController',
                        r'@RequestMapping',
                        r'@GetMapping',
                        r'@PostMapping',
                        r'Model.*model'
                    ],
                    'file_patterns': ['*Controller.java'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Spring MVC annotations',
                        'Implement proper request mapping',
                        'Follow Spring MVC patterns'
                    ]
                },
                'jpa_pattern': {
                    'indicators': [
                        r'@Entity',
                        r'@Repository',
                        r'JpaRepository',
                        r'@Transactional',
                        r'@Query',
                        r'EntityManager'
                    ],
                    'file_patterns': ['*Entity.java', '*Repository.java'],
                    'confidence': PatternConfidence.HIGH.value,
                    'recommendations': [
                        'Use Spring Data JPA',
                        'Implement proper repository patterns',
                        'Follow JPA best practices'
                    ]
                }
            }
        }
        
    def _initialize_anti_patterns(self) -> Dict[str, List[str]]:
        """Initialize anti-patterns to detect"""
        return {
            'react': [
                'Large component files (>500 lines)',
                'Direct DOM manipulation',
                'Missing key props in lists',
                'Uncontrolled components',
                'Memory leaks in useEffect',
                'Prop drilling without context'
            ],
            'vue': [
                'Large component files',
                'Direct DOM manipulation',
                'Missing key attributes',
                'Overuse of watchers',
                'Tight coupling between components'
            ],
            'angular': [
                'Large component classes',
                'Direct DOM manipulation',
                'Memory leaks in subscriptions',
                'Overuse of any type',
                'Tight coupling between services'
            ],
            'django': [
                'Fat models with business logic',
                'Fat views with too much logic',
                'Direct SQL queries',
                'Missing database indexes',
                'N+1 query problems'
            ],
            'flask': [
                'Large route functions',
                'Business logic in routes',
                'Missing error handling',
                'No input validation',
                'Tight coupling between modules'
            ],
            'spring': [
                'Large controller methods',
                'Business logic in controllers',
                'Missing service layer',
                'Tight coupling between components',
                'Improper exception handling'
            ]
        }
        
    def detect_patterns(self, project_analysis: Dict[str, Any], 
                       target_frameworks: List[str]) -> Dict[str, Any]:
        """
        Detect framework patterns in project analysis
        
        Args:
            project_analysis: Project analysis data
            target_frameworks: List of frameworks to analyze
            
        Returns:
            Dictionary containing detected patterns, confidence scores, and recommendations
        """
        detected_patterns = {
            'framework_patterns': [],
            'architectural_patterns': [],
            'integration_patterns': [],
            'confidence_scores': {},
            'evidence': {},
            'recommendations': []
        }
        
        # Get tech stack from project analysis
        tech_stack = project_analysis.get('tech_stack', {})
        languages = tech_stack.get('languages', [])
        frameworks = tech_stack.get('frameworks', [])
        files = project_analysis.get('files', [])
        
        # Combine target frameworks with detected frameworks
        all_frameworks = list(set(target_frameworks + frameworks))
        
        for framework in all_frameworks:
            if framework.lower() in self.framework_patterns:
                framework_patterns = self.framework_patterns[framework.lower()]
                
                for pattern_name, pattern_data in framework_patterns.items():
                    confidence, evidence = self._calculate_pattern_confidence(
                        pattern_data, files, languages
                    )
                    
                    if confidence >= PatternConfidence.LOW.value:
                        pattern_key = f"{framework.lower()}_{pattern_name}"
                        detected_patterns['framework_patterns'].append(pattern_key)
                        detected_patterns['confidence_scores'][pattern_key] = confidence
                        detected_patterns['evidence'][pattern_key] = evidence
                        
                        # Add architectural pattern classification
                        if 'mvc' in pattern_name or 'component' in pattern_name:
                            detected_patterns['architectural_patterns'].append(pattern_key)
                        elif 'integration' in pattern_name or 'api' in pattern_name:
                            detected_patterns['integration_patterns'].append(pattern_key)
        
        return detected_patterns
    
    def _calculate_pattern_confidence(self, pattern_data: Dict[str, Any], 
                                    files: List[Dict[str, Any]], 
                                    languages: List[str]) -> Tuple[float, List[str]]:
        """
        Calculate confidence score for a specific pattern
        
        Args:
            pattern_data: Pattern detection data
            files: List of file information
            languages: List of programming languages
            
        Returns:
            Tuple of (confidence_score, evidence_list)
        """
        evidence = []
        total_indicators = len(pattern_data['indicators'])
        matched_indicators = 0
        
        # Check file patterns
        file_pattern_matches = 0
        for file_info in files:
            file_path = file_info.get('path', '')
            for pattern in pattern_data['file_patterns']:
                if self._match_file_pattern(file_path, pattern):
                    file_pattern_matches += 1
                    evidence.append(f"File pattern '{pattern}' found in {file_path}")
                    break
        
        # Check content indicators
        for indicator in pattern_data['indicators']:
            for file_info in files:
                content = file_info.get('content', '')
                if re.search(indicator, content, re.IGNORECASE):
                    matched_indicators += 1
                    evidence.append(f"Indicator '{indicator}' found in {file_info.get('path', '')}")
                    break
        
        # Calculate confidence
        indicator_confidence = (matched_indicators / total_indicators) if total_indicators > 0 else 0
        file_confidence = min(file_pattern_matches / 2, 1.0)  # Normalize file pattern confidence
        
        # Weighted average
        confidence = (indicator_confidence * 0.7 + file_confidence * 0.3) * pattern_data['confidence']
        
        return confidence, evidence
    
    def _match_file_pattern(self, file_path: str, pattern: str) -> bool:
        """
        Check if file path matches the given pattern
        
        Args:
            file_path: File path to check
            pattern: Pattern to match against
            
        Returns:
            True if pattern matches, False otherwise
        """
        # Handle glob patterns
        if '*' in pattern:
            import fnmatch
            return fnmatch.fnmatch(file_path.lower(), pattern.lower())
        else:
            return pattern.lower() in file_path.lower()
    
    def get_recommendations(self, detected_patterns: Dict[str, Any]) -> List[str]:
        """
        Get recommendations based on detected patterns
        
        Args:
            detected_patterns: Detected patterns data
            
        Returns:
            List of recommendations
        """
        recommendations = []
        
        for pattern in detected_patterns.get('framework_patterns', []):
            framework = pattern.split('_')[0]
            pattern_name = '_'.join(pattern.split('_')[1:])
            
            if framework in self.framework_patterns and pattern_name in self.framework_patterns[framework]:
                pattern_data = self.framework_patterns[framework][pattern_name]
                recommendations.extend(pattern_data.get('recommendations', []))
        
        # Add general recommendations
        recommendations.extend([
            'Follow framework-specific best practices',
            'Implement proper error handling',
            'Use appropriate design patterns',
            'Maintain code consistency and readability'
        ])
        
        return list(set(recommendations))  # Remove duplicates
    
    def detect_anti_patterns(self, detected_patterns: Dict[str, Any]) -> List[str]:
        """
        Detect anti-patterns based on detected patterns
        
        Args:
            detected_patterns: Detected patterns data
            
        Returns:
            List of detected anti-patterns
        """
        anti_patterns = []
        
        for pattern in detected_patterns.get('framework_patterns', []):
            framework = pattern.split('_')[0]
            
            if framework in self.anti_patterns:
                anti_patterns.extend(self.anti_patterns[framework])
        
        return list(set(anti_patterns))
    
    def validate_pattern_compliance(self, detected_patterns: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate pattern compliance with best practices
        
        Args:
            detected_patterns: Detected patterns data
            
        Returns:
            Compliance validation results
        """
        compliance_results = {
            'compliant': [],
            'non_compliant': [],
            'warnings': [],
            'suggestions': []
        }
        
        # Check for common compliance issues
        for pattern in detected_patterns.get('framework_patterns', []):
            framework = pattern.split('_')[0]
            
            # Framework-specific compliance checks
            if framework == 'react':
                if 'hooks' in pattern:
                    compliance_results['suggestions'].append(
                        'Ensure hooks are used according to React rules'
                    )
                if 'redux' in pattern:
                    compliance_results['suggestions'].append(
                        'Consider using Redux Toolkit for modern Redux patterns'
                    )
            
            elif framework == 'django':
                if 'mvc' in pattern:
                    compliance_results['suggestions'].append(
                        'Ensure proper separation of concerns in MVC pattern'
                    )
                if 'orm' in pattern:
                    compliance_results['suggestions'].append(
                        'Check for N+1 query issues and optimize database queries'
                    )
            
            elif framework == 'spring':
                if 'dependency_injection' in pattern:
                    compliance_results['suggestions'].append(
                        'Ensure proper dependency injection configuration'
                    )
                if 'jpa' in pattern:
                    compliance_results['suggestions'].append(
                        'Check for proper JPA entity relationships and transactions'
                    )
        
        return compliance_results


# Global instance for easy access
framework_pattern_library = FrameworkPatternLibrary()