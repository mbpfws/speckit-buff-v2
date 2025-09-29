"""
Brownfield Project Analysis Tools

This module provides comprehensive analysis capabilities for existing projects
(brownfield projects) with historical context, dependency mapping, and 
migration guidance.
"""

from enum import Enum
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass
from pathlib import Path
import json
import yaml
import ast
import os
import re
from datetime import datetime


class ProjectType(Enum):
    """Types of projects that can be analyzed."""
    BROWNFIELD = "brownfield"
    GREENFIELD = "greenfield"
    MIGRATION = "migration"
    REFACTORING = "refactoring"


class AnalysisScope(Enum):
    """Scope of analysis to perform."""
    FULL = "full"
    ARCHITECTURE = "architecture"
    DEPENDENCIES = "dependencies"
    CODE_QUALITY = "code_quality"
    SECURITY = "security"
    PERFORMANCE = "performance"


class TechStackCategory(Enum):
    """Categories for technology stack analysis."""
    FRONTEND = "frontend"
    BACKEND = "backend"
    DATABASE = "database"
    INFRASTRUCTURE = "infrastructure"
    TESTING = "testing"
    DEVOPS = "devops"
    MONITORING = "monitoring"


@dataclass
class Technology:
    """Information about a specific technology."""
    name: str
    version: Optional[str]
    category: TechStackCategory
    confidence: float  # 0.0 to 1.0
    evidence: List[str]


@dataclass
class Dependency:
    """Information about a project dependency."""
    name: str
    version: str
    type: str  # "direct", "dev", "peer"
    file_path: str
    is_vulnerable: bool = False
    vulnerabilities: List[str] = None


@dataclass
class ArchitecturePattern:
    """Information about detected architecture patterns."""
    name: str
    confidence: float
    evidence: List[str]
    recommendations: List[str]


@dataclass
class CodeQualityMetric:
    """Metrics for code quality analysis."""
    metric: str
    value: float
    threshold: float
    status: str  # "good", "warning", "critical"
    recommendations: List[str]


@dataclass
class AnalysisResult:
    """Comprehensive analysis result for a project."""
    project_type: ProjectType
    scope: AnalysisScope
    technologies: List[Technology]
    dependencies: List[Dependency]
    architecture_patterns: List[ArchitecturePattern]
    code_quality_metrics: List[CodeQualityMetric]
    security_issues: List[str]
    performance_bottlenecks: List[str]
    migration_guidance: List[str]
    timestamp: str
    summary: str


class BrownfieldAnalyzer:
    """
    Analyzes brownfield projects with comprehensive capabilities.
    
    Provides deep analysis of existing projects including technology stack,
    architecture patterns, dependencies, code quality, and migration guidance.
    """
    
    def __init__(self):
        self.known_technologies = self._load_known_technologies()
        self.architecture_patterns = self._load_architecture_patterns()
        self.code_quality_rules = self._load_code_quality_rules()
    
    def analyze_project(self, project_path: str, scope: AnalysisScope = AnalysisScope.FULL) -> AnalysisResult:
        """Perform comprehensive analysis of a brownfield project."""
        project_path = Path(project_path)
        
        if not project_path.exists():
            raise ValueError(f"Project path does not exist: {project_path}")
        
        # Perform analysis based on scope
        technologies = self._analyze_technology_stack(project_path)
        dependencies = self._analyze_dependencies(project_path)
        
        architecture_patterns = []
        code_quality_metrics = []
        security_issues = []
        performance_bottlenecks = []
        migration_guidance = []
        
        if scope in [AnalysisScope.FULL, AnalysisScope.ARCHITECTURE]:
            architecture_patterns = self._analyze_architecture(project_path, technologies)
        
        if scope in [AnalysisScope.FULL, AnalysisScope.CODE_QUALITY]:
            code_quality_metrics = self._analyze_code_quality(project_path)
        
        if scope in [AnalysisScope.FULL, AnalysisScope.SECURITY]:
            security_issues = self._analyze_security(project_path, dependencies)
        
        if scope in [AnalysisScope.FULL, AnalysisScope.PERFORMANCE]:
            performance_bottlenecks = self._analyze_performance(project_path)
        
        # Generate migration guidance
        migration_guidance = self._generate_migration_guidance(
            technologies, architecture_patterns, code_quality_metrics
        )
        
        # Determine project type
        project_type = self._determine_project_type(project_path, technologies)
        
        # Generate summary
        summary = self._generate_analysis_summary(
            project_type, technologies, dependencies, architecture_patterns,
            code_quality_metrics, security_issues, performance_bottlenecks
        )
        
        return AnalysisResult(
            project_type=project_type,
            scope=scope,
            technologies=technologies,
            dependencies=dependencies,
            architecture_patterns=architecture_patterns,
            code_quality_metrics=code_quality_metrics,
            security_issues=security_issues,
            performance_bottlenecks=performance_bottlenecks,
            migration_guidance=migration_guidance,
            timestamp=self._get_timestamp(),
            summary=summary
        )
    
    def _analyze_technology_stack(self, project_path: Path) -> List[Technology]:
        """Analyze the technology stack used in the project."""
        technologies = []
        
        # Check for package managers and configuration files (only implemented ones)
        config_files = [
            ("package.json", TechStackCategory.FRONTEND, self._analyze_package_json),
            ("requirements.txt", TechStackCategory.BACKEND, self._analyze_requirements_txt),
            ("pyproject.toml", TechStackCategory.BACKEND, self._analyze_pyproject_toml),
            # Skip unimplemented methods: composer.json, Gemfile, go.mod, Cargo.toml, docker-compose.yml, Dockerfile
        ]
        
        for file_name, category, analyzer_func in config_files:
            file_path = project_path / file_name
            if file_path.exists():
                try:
                    techs = analyzer_func(file_path)
                    for tech in techs:
                        tech.category = category
                        technologies.append(tech)
                except Exception as e:
                    # Continue with other files if one fails
                    continue
        
        # Analyze file extensions for additional technology detection
        technologies.extend(self._analyze_file_extensions(project_path))
        
        return technologies
    
    def _analyze_package_json(self, file_path: Path) -> List[Technology]:
        """Analyze package.json for JavaScript/TypeScript technologies."""
        technologies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Analyze dependencies
            for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
                if dep_type in data:
                    for dep, version in data[dep_type].items():
                        tech = Technology(
                            name=dep,
                            version=version,
                            category=TechStackCategory.FRONTEND,  # Will be overridden
                            confidence=0.9,
                            evidence=[f"Found in {dep_type} of package.json"]
                        )
                        technologies.append(tech)
            
            # Detect framework from scripts and dependencies
            scripts = data.get('scripts', {})
            dependencies = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
            
            # React detection
            if 'react' in dependencies or any('react-scripts' in script for script in scripts.values()):
                technologies.append(Technology(
                    name="React",
                    version=dependencies.get('react', 'unknown'),
                    category=TechStackCategory.FRONTEND,
                    confidence=0.95,
                    evidence=["React dependencies found in package.json"]
                ))
            
            # Vue detection
            if 'vue' in dependencies:
                technologies.append(Technology(
                    name="Vue",
                    version=dependencies.get('vue', 'unknown'),
                    category=TechStackCategory.FRONTEND,
                    confidence=0.95,
                    evidence=["Vue dependencies found in package.json"]
                ))
            
            # Angular detection
            if '@angular/core' in dependencies:
                technologies.append(Technology(
                    name="Angular",
                    version=dependencies.get('@angular/core', 'unknown'),
                    category=TechStackCategory.FRONTEND,
                    confidence=0.95,
                    evidence=["Angular dependencies found in package.json"]
                ))
            
        except Exception as e:
            # Return empty list on error
            pass
        
        return technologies
    
    def _analyze_requirements_txt(self, file_path: Path) -> List[Technology]:
        """Analyze requirements.txt for Python technologies."""
        technologies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add Python as a technology when requirements.txt exists
            technologies.append(Technology(
                name="Python",
                version="3.8+",
                category=TechStackCategory.BACKEND,
                confidence=0.9,
                evidence=["Found requirements.txt file indicating Python project"]
            ))
            
            # Parse requirements
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Basic parsing of package name and version
                    parts = re.split(r'[=<>!]', line, 1)
                    package = parts[0].strip()
                    version = parts[1].strip() if len(parts) > 1 else 'unknown'
                    
                    tech = Technology(
                        name=package,
                        version=version,
                        category=TechStackCategory.BACKEND,
                        confidence=0.9,
                        evidence=[f"Found in requirements.txt: {line}"]
                    )
                    technologies.append(tech)
        
        except Exception as e:
            # Still add Python even if parsing fails
            technologies.append(Technology(
                name="Python",
                version="Unknown",
                category=TechStackCategory.BACKEND,
                confidence=0.5,
                evidence=["Requirements.txt file exists but parsing failed"]
            ))
        
        return technologies
    
    def _analyze_pyproject_toml(self, file_path: Path) -> List[Technology]:
        """Analyze pyproject.toml for Python technologies."""
        technologies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple TOML parsing for dependencies
            if '[tool.poetry.dependencies]' in content:
                # Poetry project
                tech = Technology(
                    name="Poetry",
                    version="unknown",
                    category=TechStackCategory.BACKEND,
                    confidence=0.9,
                    evidence=["Poetry configuration found in pyproject.toml"]
                )
                technologies.append(tech)
            
            if '[tool.pdm]' in content:
                # PDM project
                tech = Technology(
                    name="PDM",
                    version="unknown",
                    category=TechStackCategory.BACKEND,
                    confidence=0.9,
                    evidence=["PDM configuration found in pyproject.toml"]
                )
                technologies.append(tech)
        
        except Exception as e:
            pass
        
        return technologies
    
    def _analyze_file_extensions(self, project_path: Path) -> List[Technology]:
        """Analyze file extensions to detect technologies."""
        technologies = []
        extensions_count = {}
        
        # Count file extensions
        for root, dirs, files in os.walk(project_path):
            for file in files:
                ext = Path(file).suffix.lower()
                if ext:
                    extensions_count[ext] = extensions_count.get(ext, 0) + 1
        
        # Map extensions to technologies
        extension_tech_map = {
            '.py': ('Python', TechStackCategory.BACKEND, 0.8),
            '.js': ('JavaScript', TechStackCategory.FRONTEND, 0.8),
            '.ts': ('TypeScript', TechStackCategory.FRONTEND, 0.9),
            '.jsx': ('React', TechStackCategory.FRONTEND, 0.9),
            '.tsx': ('React with TypeScript', TechStackCategory.FRONTEND, 0.9),
            '.vue': ('Vue', TechStackCategory.FRONTEND, 0.9),
            '.java': ('Java', TechStackCategory.BACKEND, 0.9),
            '.cs': ('C#', TechStackCategory.BACKEND, 0.9),
            '.php': ('PHP', TechStackCategory.BACKEND, 0.9),
            '.rb': ('Ruby', TechStackCategory.BACKEND, 0.9),
            '.go': ('Go', TechStackCategory.BACKEND, 0.9),
            '.rs': ('Rust', TechStackCategory.BACKEND, 0.9),
            '.sql': ('SQL', TechStackCategory.DATABASE, 0.7),
            '.html': ('HTML', TechStackCategory.FRONTEND, 0.8),
            '.css': ('CSS', TechStackCategory.FRONTEND, 0.8),
            '.scss': ('Sass', TechStackCategory.FRONTEND, 0.8),
        }
        
        for ext, (tech_name, category, confidence) in extension_tech_map.items():
            if ext in extensions_count and extensions_count[ext] > 0:
                technologies.append(Technology(
                    name=tech_name,
                    version="unknown",
                    category=category,
                    confidence=confidence,
                    evidence=[f"Found {extensions_count[ext]} files with extension {ext}"]
                ))
        
        return technologies
    
    def _analyze_dependencies(self, project_path: Path) -> List[Dependency]:
        """Analyze project dependencies."""
        dependencies = []
        
        # Check various dependency files (only implemented ones)
        dep_files = [
            ("package.json", self._analyze_npm_dependencies),
            ("requirements.txt", self._analyze_pip_dependencies),
            # Skip unimplemented methods: composer.json, Gemfile, go.mod, Cargo.toml
        ]
        
        for file_name, analyzer_func in dep_files:
            file_path = project_path / file_name
            if file_path.exists():
                try:
                    deps = analyzer_func(file_path)
                    dependencies.extend(deps)
                except Exception as e:
                    continue
        
        return dependencies
    
    def _analyze_npm_dependencies(self, file_path: Path) -> List[Dependency]:
        """Analyze npm dependencies from package.json."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
                if dep_type in data:
                    for name, version in data[dep_type].items():
                        dependency = Dependency(
                            name=name,
                            version=version,
                            type=dep_type.replace('ependencies', ''),
                            file_path=str(file_path),
                            is_vulnerable=False,
                            vulnerabilities=[]
                        )
                        dependencies.append(dependency)
        
        except Exception as e:
            pass
        
        return dependencies
    
    def _analyze_pip_dependencies(self, file_path: Path) -> List[Dependency]:
        """Analyze pip dependencies from requirements.txt."""
        dependencies = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = re.split(r'[=<>!]', line, 1)
                    name = parts[0].strip()
                    version = parts[1].strip() if len(parts) > 1 else 'unknown'
                    
                    dependency = Dependency(
                        name=name,
                        version=version,
                        type="direct",
                        file_path=str(file_path),
                        is_vulnerable=False,
                        vulnerabilities=[]
                    )
                    dependencies.append(dependency)
        
        except Exception as e:
            pass
        
        return dependencies
    
    def _analyze_architecture(self, project_path: Path, technologies: List[Technology]) -> List[ArchitecturePattern]:
        """Analyze architecture patterns in the project."""
        patterns = []
        
        # Simple pattern detection based on directory structure and technologies
        dir_structure = self._analyze_directory_structure(project_path)
        
        # MVC pattern detection
        if self._detect_mvc_pattern(dir_structure):
            patterns.append(ArchitecturePattern(
                name="MVC (Model-View-Controller)",
                confidence=0.8,
                evidence=["Directory structure suggests MVC pattern"],
                recommendations=["Consider using established MVC frameworks"]
            ))
        
        # Microservices pattern detection
        if self._detect_microservices_pattern(dir_structure):
            patterns.append(ArchitecturePattern(
                name="Microservices",
                confidence=0.7,
                evidence=["Multiple service-like directories detected"],
                recommendations=["Ensure proper service boundaries and communication"]
            ))
        
        # Monolith pattern detection
        if self._detect_monolith_pattern(dir_structure):
            patterns.append(ArchitecturePattern(
                name="Monolithic Architecture",
                confidence=0.9,
                evidence=["Centralized codebase structure detected"],
                recommendations=["Consider modularization for scalability"]
            ))
        
        return patterns
    
    def _analyze_directory_structure(self, project_path: Path) -> Dict[str, List[str]]:
        """Analyze the directory structure of the project."""
        structure = {}
        
        for root, dirs, files in os.walk(project_path):
            # Skip common directories that don't indicate architecture
            skip_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'vendor'}
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            rel_path = os.path.relpath(root, project_path)
            if rel_path == '.':
                rel_path = '/'
            
            structure[rel_path] = files
        
        return structure
    
    def _detect_mvc_pattern(self, structure: Dict[str, List[str]]) -> bool:
        """Detect MVC architecture pattern."""
        mvc_indicators = [
            any('model' in key.lower() for key in structure.keys()),
            any('view' in key.lower() for key in structure.keys()),
            any('controller' in key.lower() for key in structure.keys()),
            any('templates' in key.lower() for key in structure.keys()),
        ]
        
        return sum(mvc_indicators) >= 2
    
    def _detect_microservices_pattern(self, structure: Dict[str, List[str]]) -> bool:
        """Detect microservices architecture pattern."""
        service_indicators = [
            any('service' in key.lower() for key in structure.keys()),
            any('api' in key.lower() for key in structure.keys() if key != '/'),
            len([key for key in structure.keys() if 'service' in key.lower()]) > 1,
        ]
        
        return sum(service_indicators) >= 2
    
    def _detect_monolith_pattern(self, structure: Dict[str, List[str]]) -> bool:
        """Detect monolithic architecture pattern."""
        # Monolith typically has fewer top-level service directories
        # and more centralized structure
        top_level_dirs = [key for key in structure.keys() if key != '/' and '/' not in key]
        service_dirs = [d for d in top_level_dirs if 'service' in d.lower()]
        
        return len(service_dirs) <= 1 and len(top_level_dirs) > 5
    
    def _analyze_code_quality(self, project_path: Path) -> List[CodeQualityMetric]:
        """Analyze code quality metrics."""
        metrics = []
        
        # Basic metrics based on file analysis
        total_lines = 0
        total_files = 0
        has_tests = False
        has_docs = False
        
        for root, dirs, files in os.walk(project_path):
            # Skip common directories
            skip_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'vendor'}
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix in ['.py', '.js', '.ts', '.java', '.cs']:
                    total_files += 1
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            total_lines += len(lines)
                    except:
                        pass
                
                # Check for test files
                if 'test' in file.lower() or 'spec' in file.lower():
                    has_tests = True
                
                # Check for documentation
                if file.lower() in ['readme.md', 'readme', 'docs.md']:
                    has_docs = True
        
        # Add metrics
        if total_files > 0:
            avg_lines_per_file = total_lines / total_files
            metrics.append(CodeQualityMetric(
                metric="Average Lines per File",
                value=avg_lines_per_file,
                threshold=200.0,
                status="good" if avg_lines_per_file < 200 else "warning",
                recommendations=["Keep files under 200 lines for maintainability"]
            ))
        
        metrics.append(CodeQualityMetric(
            metric="Test Coverage",
            value=1.0 if has_tests else 0.0,
            threshold=0.8,
            status="good" if has_tests else "critical",
            recommendations=["Implement comprehensive test suite"]
        ))
        
        metrics.append(CodeQualityMetric(
            metric="Documentation",
            value=1.0 if has_docs else 0.0,
            threshold=0.5,
            status="good" if has_docs else "warning",
            recommendations=["Add comprehensive documentation"]
        ))
        
        return metrics
    
    def _analyze_security(self, project_path: Path, dependencies: List[Dependency]) -> List[str]:
        """Analyze security issues."""
        issues = []
        
        # Check for common security configuration files
        security_files = ['.env', 'config.yml', 'settings.py']
        for file in security_files:
            file_path = project_path / file
            if file_path.exists():
                # Basic check for hardcoded secrets
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if any(keyword in content.lower() for keyword in ['password', 'secret', 'key', 'token']):
                            issues.append(f"Potential hardcoded secrets in {file}")
                except:
                    pass
        
        # Check dependency vulnerabilities (simplified)
        vulnerable_deps = [dep for dep in dependencies if self._is_vulnerable_dependency(dep)]
        if vulnerable_deps:
            issues.append(f"Found {len(vulnerable_deps)} potentially vulnerable dependencies")
        
        return issues
    
    def _analyze_performance(self, project_path: Path) -> List[str]:
        """Analyze performance bottlenecks."""
        bottlenecks = []
        
        # Simple checks based on project structure and technologies
        # In a real implementation, this would use more sophisticated analysis
        
        # Check for large dependency trees
        package_json = project_path / 'package.json'
        if package_json.exists():
            try:
                with open(package_json, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    deps_count = len(data.get('dependencies', {})) + len(data.get('devDependencies', {}))
                    if deps_count > 50:
                        bottlenecks.append(f"Large dependency tree ({deps_count} packages) may impact performance")
            except:
                pass
        
        return bottlenecks
    
    def _generate_migration_guidance(self, technologies: List[Technology], 
                                   architecture_patterns: List[ArchitecturePattern],
                                   code_quality_metrics: List[CodeQualityMetric]) -> List[str]:
        """Generate migration guidance based on analysis results."""
        guidance = []
        
        # Technology migration guidance
        for tech in technologies:
            if tech.confidence < 0.5:
                guidance.append(f"Consider verifying technology: {tech.name}")
            
            # Outdated technology detection (simplified)
            if any(old_tech in tech.name.lower() for old_tech in ['angularjs', 'backbone', 'ember']):
                guidance.append(f"Consider migrating from {tech.name} to modern framework")
        
        # Architecture guidance
        for pattern in architecture_patterns:
            if pattern.name == "Monolithic Architecture":
                guidance.append("Consider microservices for better scalability")
            elif pattern.name == "MVC (Model-View-Controller)":
                guidance.append("Ensure proper separation of concerns in MVC pattern")
        
        # Code quality guidance
        for metric in code_quality_metrics:
            if metric.status == "critical":
                guidance.append(f"Address critical issue: {metric.metric}")
            elif metric.status == "warning":
                guidance.append(f"Improve: {metric.metric}")
        
        return guidance
    
    def _determine_project_type(self, project_path: Path, technologies: List[Technology]) -> ProjectType:
        """Determine the type of project based on analysis."""
        # Simple heuristic based on technologies and structure
        tech_names = [tech.name.lower() for tech in technologies]
        
        if any(framework in tech_names for framework in ['react', 'vue', 'angular']):
            return ProjectType.BROWNFIELD
        
        # Check for migration indicators
        migration_files = ['migration', 'upgrade', 'legacy']
        for file in migration_files:
            if (project_path / file).exists():
                return ProjectType.MIGRATION
        
        return ProjectType.BROWNFIELD
    
    def _generate_analysis_summary(self, project_type: ProjectType, technologies: List[Technology],
                                 dependencies: List[Dependency], architecture_patterns: List[ArchitecturePattern],
                                 code_quality_metrics: List[CodeQualityMetric], security_issues: List[str],
                                 performance_bottlenecks: List[str]) -> str:
        """Generate a comprehensive analysis summary."""
        summary = f"Project Analysis Summary\n"
        summary += f"======================\n"
        summary += f"Type: {project_type.value}\n"
        summary += f"Technologies: {len(technologies)} detected\n"
        summary += f"Dependencies: {len(dependencies)} found\n"
        summary += f"Architecture Patterns: {len(architecture_patterns)} identified\n"
        summary += f"Code Quality Metrics: {len(code_quality_metrics)} analyzed\n"
        summary += f"Security Issues: {len(security_issues)} detected\n"
        summary += f"Performance Bottlenecks: {len(performance_bottlenecks)} identified\n"
        
        return summary
    
    def _is_vulnerable_dependency(self, dependency: Dependency) -> bool:
        """Check if a dependency is potentially vulnerable (simplified)."""
        # In a real implementation, this would query vulnerability databases
        # For now, use simple heuristics based on version patterns
        vulnerable_patterns = [
            r'0\.[0-8]\.',  # Early versions
            r'[0-9]+\.[0-9]+\.0',  # Major.minor.0 (often first release)
        ]
        
        for pattern in vulnerable_patterns:
            if re.search(pattern, dependency.version):
                return True
        
        return False
    
    def _load_known_technologies(self) -> Dict[str, Any]:
        """Load known technologies database (simplified)."""
        # In a real implementation, this would load from a comprehensive database
        return {}
    
    def _load_architecture_patterns(self) -> Dict[str, Any]:
        """Load architecture patterns database (simplified)."""
        return {}
    
    def _load_code_quality_rules(self) -> Dict[str, Any]:
        """Load code quality rules (simplified)."""
        return {}
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        return datetime.now().isoformat()


# Factory functions for easy creation
def create_brownfield_analyzer() -> BrownfieldAnalyzer:
    """Create a brownfield analyzer instance."""
    return BrownfieldAnalyzer()


def analyze_project(project_path: str, scope: AnalysisScope = AnalysisScope.FULL) -> AnalysisResult:
    """Convenience function to analyze a project."""
    analyzer = create_brownfield_analyzer()
    return analyzer.analyze_project(project_path, scope)