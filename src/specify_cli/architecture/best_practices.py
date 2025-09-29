"""
Best Practices Engine for Architecture Engine
Provides rule-based recommendation system for architecture best practices
"""

import re
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum


class RuleSeverity(Enum):
    """Severity levels for best practice rules"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class RuleCategory(Enum):
    """Categories for best practice rules"""
    PERFORMANCE = "performance"
    SECURITY = "security"
    MAINTAINABILITY = "maintainability"
    SCALABILITY = "scalability"
    RELIABILITY = "reliability"
    CROSS_PLATFORM = "cross_platform"


@dataclass
class BestPracticeRule:
    """Represents a best practice rule"""
    id: str
    name: str
    description: str
    category: RuleCategory
    severity: RuleSeverity
    frameworks: List[str]
    patterns: List[str]
    recommendations: List[str]
    auto_fix_available: bool = False
    confidence_threshold: float = 0.7


@dataclass
class RuleViolation:
    """Represents a rule violation"""
    rule_id: str
    rule_name: str
    severity: RuleSeverity
    category: RuleCategory
    description: str
    location: str
    line_number: Optional[int]
    recommendation: str
    confidence: float
    auto_fixable: bool = False


@dataclass
class BestPracticesResult:
    """Result of best practices analysis"""
    violations: List[RuleViolation]
    compliant_rules: List[str]
    recommendations: List[str]
    score: float  # 0-100 score
    categories: Dict[str, int]  # Violations per category
    frameworks: Dict[str, int]  # Violations per framework


class BestPracticesEngine:
    """
    Rule-based best practices engine for architecture validation
    Provides performance, security, and cross-platform compatibility checks
    """
    
    def __init__(self):
        self.rules = self._initialize_rules()
        self.performance_targets = self._initialize_performance_targets()
        
    def _initialize_rules(self) -> Dict[str, BestPracticeRule]:
        """Initialize best practice rules"""
        return {
            # Performance Rules
            'PERF_001': BestPracticeRule(
                id='PERF_001',
                name='Database Query Optimization',
                description='Avoid N+1 query problems in ORM usage',
                category=RuleCategory.PERFORMANCE,
                severity=RuleSeverity.HIGH,
                frameworks=['django', 'spring', 'flask'],
                patterns=[
                    r'for.*in.*\.objects\.all\(\)',
                    r'for.*in.*\.filter\(',
                    r'\.objects\.get\(',
                    r'\.findById\(',
                    r'SELECT.*FROM.*WHERE.*='
                ],
                recommendations=[
                    'Use select_related() or prefetch_related() in Django',
                    'Use JOIN FETCH in Spring JPA',
                    'Use eager loading strategies',
                    'Implement proper query optimization'
                ],
                auto_fix_available=True,
                confidence_threshold=0.8
            ),
            
            'PERF_002': BestPracticeRule(
                id='PERF_002',
                name='Caching Implementation',
                description='Implement appropriate caching strategies',
                category=RuleCategory.PERFORMANCE,
                severity=RuleSeverity.MEDIUM,
                frameworks=['django', 'flask', 'spring', 'react', 'vue'],
                patterns=[
                    r'cache\.',
                    r'@cacheable',
                    r'useMemo\(',
                    r'computed\(',
                    r'RedisCache',
                    r'MemcachedCache'
                ],
                recommendations=[
                    'Implement Redis or Memcached caching',
                    'Use application-level caching',
                    'Implement proper cache invalidation',
                    'Use CDN for static assets'
                ],
                auto_fix_available=False,
                confidence_threshold=0.6
            ),
            
            # Security Rules
            'SEC_001': BestPracticeRule(
                id='SEC_001',
                name='SQL Injection Prevention',
                description='Use parameterized queries to prevent SQL injection',
                category=RuleCategory.SECURITY,
                severity=RuleSeverity.CRITICAL,
                frameworks=['django', 'flask', 'spring'],
                patterns=[
                    r'\.format\(',
                    r'%.*s.*%',
                    r'f".*{.*}.*"',
                    r'\.execute\(',
                    r'query.*=.*\+'
                ],
                recommendations=[
                    'Use ORM query methods',
                    'Use parameterized queries',
                    'Implement input validation',
                    'Use prepared statements'
                ],
                auto_fix_available=True,
                confidence_threshold=0.9
            ),
            
            'SEC_002': BestPracticeRule(
                id='SEC_002',
                name='Authentication Implementation',
                description='Implement proper authentication mechanisms',
                category=RuleCategory.SECURITY,
                severity=RuleSeverity.HIGH,
                frameworks=['django', 'flask', 'spring', 'express'],
                patterns=[
                    r'@login_required',
                    r'@authenticated',
                    r'JWT',
                    r'OAuth',
                    r'auth\.',
                    r'login\('
                ],
                recommendations=[
                    'Use JWT tokens for stateless authentication',
                    'Implement OAuth2 for third-party integration',
                    'Use secure password hashing',
                    'Implement proper session management'
                ],
                auto_fix_available=False,
                confidence_threshold=0.7
            ),
            
            # Maintainability Rules
            'MAINT_001': BestPracticeRule(
                id='MAINT_001',
                name='Code Documentation',
                description='Maintain proper code documentation',
                category=RuleCategory.MAINTAINABILITY,
                severity=RuleSeverity.MEDIUM,
                frameworks=['all'],
                patterns=[
                    r'def.*\(.*\).*:',
                    r'class.*:',
                    r'function.*\(.*\)',
                    r'method.*\(.*\)'
                ],
                recommendations=[
                    'Add docstrings to functions and classes',
                    'Use type hints where appropriate',
                    'Document complex algorithms',
                    'Maintain README files'
                ],
                auto_fix_available=False,
                confidence_threshold=0.5
            ),
            
            'MAINT_002': BestPracticeRule(
                id='MAINT_002',
                name='Error Handling',
                description='Implement comprehensive error handling',
                category=RuleCategory.MAINTAINABILITY,
                severity=RuleSeverity.HIGH,
                frameworks=['all'],
                patterns=[
                    r'try:',
                    r'except:',
                    r'catch.*\(',
                    r'\.catch\(',
                    r'Promise\.catch'
                ],
                recommendations=[
                    'Use specific exception types',
                    'Implement proper error logging',
                    'Provide meaningful error messages',
                    'Handle edge cases gracefully'
                ],
                auto_fix_available=False,
                confidence_threshold=0.8
            ),
            
            # Scalability Rules
            'SCALE_001': BestPracticeRule(
                id='SCALE_001',
                name='Microservices Architecture',
                description='Consider microservices for large applications',
                category=RuleCategory.SCALABILITY,
                severity=RuleSeverity.MEDIUM,
                frameworks=['spring', 'django', 'flask'],
                patterns=[
                    r'@RestController',
                    r'@app\.route',
                    r'urlpatterns',
                    r'class.*View',
                    r'def.*request'
                ],
                recommendations=[
                    'Implement service separation',
                    'Use API gateways',
                    'Implement service discovery',
                    'Use message queues for communication'
                ],
                auto_fix_available=False,
                confidence_threshold=0.6
            ),
            
            # Cross-Platform Rules
            'CROSS_001': BestPracticeRule(
                id='CROSS_001',
                name='Path Handling',
                description='Use cross-platform path handling',
                category=RuleCategory.CROSS_PLATFORM,
                severity=RuleSeverity.MEDIUM,
                frameworks=['all'],
                patterns=[
                    r'\\',
                    r'C:\\',
                    r'/home/',
                    r'/var/',
                    r'os\.path',
                    r'pathlib'
                ],
                recommendations=[
                    'Use os.path.join() or pathlib.Path',
                    'Avoid hardcoded paths',
                    'Use environment variables',
                    'Implement path abstraction'
                ],
                auto_fix_available=True,
                confidence_threshold=0.7
            ),
            
            'CROSS_002': BestPracticeRule(
                id='CROSS_002',
                name='Environment Configuration',
                description='Use environment-specific configuration',
                category=RuleCategory.CROSS_PLATFORM,
                severity=RuleSeverity.HIGH,
                frameworks=['all'],
                patterns=[
                    r'\.env',
                    r'config\.',
                    r'settings\.',
                    r'environment',
                    r'NODE_ENV',
                    r'DEBUG'
                ],
                recommendations=[
                    'Use environment variables for configuration',
                    'Implement configuration management',
                    'Separate development and production configs',
                    'Use secure configuration storage'
                ],
                auto_fix_available=False,
                confidence_threshold=0.8
            ),
            
            # Framework-Specific Rules
            'REACT_001': BestPracticeRule(
                id='REACT_001',
                name='React Component Structure',
                description='Follow React component best practices',
                category=RuleCategory.MAINTAINABILITY,
                severity=RuleSeverity.MEDIUM,
                frameworks=['react'],
                patterns=[
                    r'function.*\(.*\).*return',
                    r'class.*extends.*Component',
                    r'useState\(',
                    r'useEffect\('
                ],
                recommendations=[
                    'Use functional components with hooks',
                    'Keep components small and focused',
                    'Use proper prop validation',
                    'Implement proper component lifecycle'
                ],
                auto_fix_available=False,
                confidence_threshold=0.7
            ),
            
            'DJANGO_001': BestPracticeRule(
                id='DJANGO_001',
                name='Django Model Design',
                description='Follow Django model best practices',
                category=RuleCategory.MAINTAINABILITY,
                severity=RuleSeverity.MEDIUM,
                frameworks=['django'],
                patterns=[
                    r'class.*models\.Model',
                    r'Models\.',
                    r'CharField',
                    r'IntegerField',
                    r'ForeignKey'
                ],
                recommendations=[
                    'Use appropriate field types',
                    'Implement proper model relationships',
                    'Add database indexes for performance',
                    'Use model methods for business logic'
                ],
                auto_fix_available=False,
                confidence_threshold=0.8
            ),
            
            'SPRING_001': BestPracticeRule(
                id='SPRING_001',
                name='Spring Dependency Injection',
                description='Use Spring DI properly',
                category=RuleCategory.MAINTAINABILITY,
                severity=RuleSeverity.HIGH,
                frameworks=['spring'],
                patterns=[
                    r'@Autowired',
                    r'@Component',
                    r'@Service',
                    r'@Repository',
                    r'@Controller'
                ],
                recommendations=[
                    'Use constructor injection',
                    'Avoid field injection',
                    'Use appropriate stereotypes',
                    'Implement proper component scanning'
                ],
                auto_fix_available=False,
                confidence_threshold=0.9
            )
        }
        
    def _initialize_performance_targets(self) -> Dict[str, Any]:
        """Initialize performance targets"""
        return {
            'response_time_ms': 200,
            'memory_usage_mb': 512,
            'cpu_usage_percent': 80,
            'database_queries_per_request': 10,
            'cache_hit_ratio': 0.8,
            'error_rate_percent': 1.0
        }
        
    def analyze_best_practices(self, project_analysis: Dict[str, Any], 
                             include_auto_fix: bool = False) -> BestPracticesResult:
        """
        Analyze project for best practice violations
        
        Args:
            project_analysis: Project analysis data
            include_auto_fix: Whether to include auto-fix suggestions
            
        Returns:
            Best practices analysis results
        """
        violations = []
        compliant_rules = []
        recommendations = []
        category_counts = {}
        framework_counts = {}
        
        # Get project data
        tech_stack = project_analysis.get('tech_stack', {})
        frameworks = tech_stack.get('frameworks', [])
        languages = tech_stack.get('languages', [])
        files = project_analysis.get('files', [])
        architecture_patterns = project_analysis.get('architecture_patterns', [])
        
        # Analyze each rule
        for rule_id, rule in self.rules.items():
            # Check if rule applies to project frameworks
            if self._rule_applies_to_project(rule, frameworks, languages):
                violations_found = self._check_rule_violations(rule, files, project_analysis)
                
                if violations_found:
                    violations.extend(violations_found)
                    
                    # Update category counts
                    category = rule.category.value
                    category_counts[category] = category_counts.get(category, 0) + len(violations_found)
                    
                    # Update framework counts
                    for framework in rule.frameworks:
                        if framework in frameworks or framework == 'all':
                            framework_counts[framework] = framework_counts.get(framework, 0) + len(violations_found)
                else:
                    compliant_rules.append(rule_id)
        
        # Calculate score
        total_rules = len(self.rules)
        compliant_count = len(compliant_rules)
        violation_count = len(violations)
        
        # Calculate weighted score based on severity
        severity_weights = {
            RuleSeverity.CRITICAL: 4,
            RuleSeverity.HIGH: 3,
            RuleSeverity.MEDIUM: 2,
            RuleSeverity.LOW: 1,
            RuleSeverity.INFO: 0.5
        }
        
        total_weight = sum(severity_weights[rule.severity] for rule in self.rules.values())
        violation_weight = sum(severity_weights[violation.severity] for violation in violations)
        
        # Calculate score (0-100)
        if total_weight > 0:
            score = max(0, 100 - (violation_weight / total_weight * 100))
        else:
            score = 100
        
        # Generate recommendations
        recommendations = self._generate_recommendations(violations, frameworks)
        
        return BestPracticesResult(
            violations=violations,
            compliant_rules=compliant_rules,
            recommendations=recommendations,
            score=score,
            categories=category_counts,
            frameworks=framework_counts
        )
    
    def _rule_applies_to_project(self, rule: BestPracticeRule, 
                                frameworks: List[str], 
                                languages: List[str]) -> bool:
        """Check if a rule applies to the project"""
        # Check framework compatibility
        if 'all' in rule.frameworks:
            return True
            
        for framework in frameworks:
            if framework.lower() in [f.lower() for f in rule.frameworks]:
                return True
                
        # Check language compatibility for general rules
        if 'all' in rule.frameworks:
            return True
            
        return False
    
    def _check_rule_violations(self, rule: BestPracticeRule, 
                             files: List[Dict[str, Any]], 
                             project_analysis: Dict[str, Any]) -> List[RuleViolation]:
        """Check for violations of a specific rule"""
        violations = []
        
        for file_info in files:
            file_path = file_info.get('path', '')
            content = file_info.get('content', '')
            
            # Check if rule patterns are found
            pattern_matches = 0
            for pattern in rule.patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    pattern_matches += 1
            
            # Calculate confidence based on pattern matches
            confidence = pattern_matches / len(rule.patterns) if rule.patterns else 0
            
            if confidence >= rule.confidence_threshold:
                # Find specific violation locations
                violations.extend(
                    self._find_violation_locations(rule, file_info, confidence)
                )
        
        return violations
    
    def _find_violation_locations(self, rule: BestPracticeRule, 
                                file_info: Dict[str, Any], 
                                confidence: float) -> List[RuleViolation]:
        """Find specific locations of violations in a file"""
        violations = []
        file_path = file_info.get('path', '')
        content = file_info.get('content', '')
        
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            for pattern in rule.patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Get recommendation for this violation
                    recommendation = self._get_recommendation_for_violation(rule, line)
                    
                    violations.append(RuleViolation(
                        rule_id=rule.id,
                        rule_name=rule.name,
                        severity=rule.severity,
                        category=rule.category,
                        description=rule.description,
                        location=file_path,
                        line_number=i + 1,
                        recommendation=recommendation,
                        confidence=confidence,
                        auto_fixable=rule.auto_fix_available
                    ))
        
        return violations
    
    def _get_recommendation_for_violation(self, rule: BestPracticeRule, 
                                        violating_line: str) -> str:
        """Get specific recommendation for a violation"""
        # Try to match the violation to a specific recommendation
        for i, pattern in enumerate(rule.patterns):
            if re.search(pattern, violating_line, re.IGNORECASE):
                if i < len(rule.recommendations):
                    return rule.recommendations[i]
        
        # Return first recommendation as default
        return rule.recommendations[0] if rule.recommendations else "Follow best practices"
    
    def _generate_recommendations(self, violations: List[RuleViolation], 
                                frameworks: List[str]) -> List[str]:
        """Generate overall recommendations based on violations"""
        recommendations = []
        
        # Group violations by severity
        critical_violations = [v for v in violations if v.severity == RuleSeverity.CRITICAL]
        high_violations = [v for v in violations if v.severity == RuleSeverity.HIGH]
        
        if critical_violations:
            recommendations.append(
                f"Address {len(critical_violations)} critical security issues immediately"
            )
        
        if high_violations:
            recommendations.append(
                f"Review and fix {len(high_violations)} high-priority issues"
            )
        
        # Framework-specific recommendations
        if 'django' in frameworks:
            recommendations.extend([
                'Use Django ORM effectively to prevent SQL injection',
                'Implement proper Django security middleware',
                'Use Django\'s built-in authentication system'
            ])
        
        if 'react' in frameworks:
            recommendations.extend([
                'Use React hooks properly to avoid memory leaks',
                'Implement proper component composition',
                'Use React.memo for performance optimization'
            ])
        
        if 'spring' in frameworks:
            recommendations.extend([
                'Use Spring Security for authentication',
                'Implement proper dependency injection',
                'Use Spring Data JPA for database operations'
            ])
        
        # General recommendations
        recommendations.extend([
            'Implement comprehensive error handling',
            'Add proper logging and monitoring',
            'Use version control effectively',
            'Write unit tests for critical functionality',
            'Follow framework-specific best practices'
        ])
        
        return list(set(recommendations))  # Remove duplicates
    
    def get_rule_by_id(self, rule_id: str) -> Optional[BestPracticeRule]:
        """Get a specific rule by ID"""
        return self.rules.get(rule_id)
    
    def get_rules_by_category(self, category: RuleCategory) -> List[BestPracticeRule]:
        """Get all rules for a specific category"""
        return [rule for rule in self.rules.values() if rule.category == category]
    
    def get_rules_by_framework(self, framework: str) -> List[BestPracticeRule]:
        """Get all rules for a specific framework"""
        return [rule for rule in self.rules.values() 
                if framework.lower() in [f.lower() for f in rule.frameworks] or 'all' in rule.frameworks]
    
    def add_custom_rule(self, rule: BestPracticeRule) -> None:
        """Add a custom best practice rule"""
        self.rules[rule.id] = rule
    
    def validate_performance_targets(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate performance against targets
        
        Args:
            metrics: Performance metrics
            
        Returns:
            Validation results
        """
        results = {
            'met_targets': [],
            'missed_targets': [],
            'recommendations': []
        }
        
        for target, target_value in self.performance_targets.items():
            if target in metrics:
                actual_value = metrics[target]
                
                if target == 'response_time_ms':
                    if actual_value <= target_value:
                        results['met_targets'].append(f"Response time: {actual_value}ms")
                    else:
                        results['missed_targets'].append(
                            f"Response time: {actual_value}ms (target: {target_value}ms)"
                        )
                        results['recommendations'].append(
                            "Optimize database queries and implement caching"
                        )
                
                elif target == 'error_rate_percent':
                    if actual_value <= target_value:
                        results['met_targets'].append(f"Error rate: {actual_value}%")
                    else:
                        results['missed_targets'].append(
                            f"Error rate: {actual_value}% (target: {target_value}%)"
                        )
                        results['recommendations'].append(
                            "Improve error handling and add more robust validation"
                        )
        
        return results


# Global instance for easy access
best_practices_engine = BestPracticesEngine()