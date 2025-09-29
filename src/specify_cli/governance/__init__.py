"""
Constitutional Compliance Monitoring System

This module provides comprehensive monitoring and validation of constitutional compliance
for the Spec-Kit Enhancement Initiative. It validates all 7 core principles from the
constitution and provides reporting mechanisms.
"""

from enum import Enum
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import json
import yaml
from pathlib import Path


class PrincipleType(Enum):
    """Enumeration of constitutional principles to monitor."""
    CROSS_PLATFORM_COMPATIBILITY = "I. Cross-Platform Compatibility"
    MULTI_INSTALLATION_SUPPORT = "II. Multi-Installation Support"
    ARCHITECTURE_FIRST_DEVELOPMENT = "III. Architecture-First Development"
    TEMPLATE_DRIVEN_CONSISTENCY = "IV. Template-Driven Consistency"
    SYNCHRONICITY_ENFORCEMENT = "V. Synchronicity Enforcement"
    AGENT_NATIVE_EXECUTION = "VI. Agent-Native Execution"
    HIERARCHICAL_GOVERNANCE = "VII. Hierarchical Governance"


class ComplianceStatus(Enum):
    """Status of constitutional compliance validation."""
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PENDING_VALIDATION = "pending_validation"
    PARTIALLY_COMPLIANT = "partially_compliant"


@dataclass
class PrincipleValidation:
    """Validation result for a single constitutional principle."""
    principle: PrincipleType
    status: ComplianceStatus
    violations: List[str]
    evidence: List[str]
    recommendations: List[str]
    timestamp: str


@dataclass
class ComplianceReport:
    """Comprehensive compliance report for all constitutional principles."""
    validations: Dict[PrincipleType, PrincipleValidation]
    overall_status: ComplianceStatus
    summary: str
    timestamp: str
    version: str = "1.0.0"


class ConstitutionalValidator:
    """
    Validates compliance with the Spec-Kit constitution.
    
    This validator checks all 7 core principles and provides detailed reporting
    on compliance status, violations, and recommendations.
    """
    
    def __init__(self):
        self.supported_platforms = [
            "Claude Code", "GitHub Copilot", "Gemini CLI", "Cursor", 
            "Qwen Code", "opencode", "Windsurf", "Kilo Code", "Auggie CLI", "Roo Code"
        ]
        self.installation_methods = ["PATH", "uvx"]
        
    def validate_all_principles(self) -> ComplianceReport:
        """Validate all 7 constitutional principles."""
        validations = {}
        
        validations[PrincipleType.CROSS_PLATFORM_COMPATIBILITY] = self.validate_cross_platform_compatibility()
        validations[PrincipleType.MULTI_INSTALLATION_SUPPORT] = self.validate_multi_installation_support()
        validations[PrincipleType.ARCHITECTURE_FIRST_DEVELOPMENT] = self.validate_architecture_first_development()
        validations[PrincipleType.TEMPLATE_DRIVEN_CONSISTENCY] = self.validate_template_driven_consistency()
        validations[PrincipleType.SYNCHRONICITY_ENFORCEMENT] = self.validate_synchronicity_enforcement()
        validations[PrincipleType.AGENT_NATIVE_EXECUTION] = self.validate_agent_native_execution()
        validations[PrincipleType.HIERARCHICAL_GOVERNANCE] = self.validate_hierarchical_governance()
        
        overall_status = self._determine_overall_status(validations)
        summary = self._generate_summary(validations, overall_status)
        
        return ComplianceReport(
            validations=validations,
            overall_status=overall_status,
            summary=summary,
            timestamp=self._get_timestamp()
        )
    
    def validate_cross_platform_compatibility(self) -> PrincipleValidation:
        """Validate Principle I: Cross-Platform Compatibility."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check platform detection capabilities
        from ..compatibility import create_compatibility_validator
        try:
            validator = create_compatibility_validator()
            platform_detection = validator.detect_current_platform()
            if platform_detection:
                evidence.append(f"Platform detection working: {platform_detection}")
            else:
                violations.append("Platform detection not functioning properly")
        except Exception as e:
            violations.append(f"Platform detection failed: {str(e)}")
        
        # Check cross-platform validation
        try:
            compatibility_result = validator.validate_cross_platform_compatibility()
            if compatibility_result["status"] == "valid":
                evidence.append("Cross-platform compatibility validation working")
            else:
                violations.append("Cross-platform compatibility validation failed")
        except Exception as e:
            violations.append(f"Cross-platform validation failed: {str(e)}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.CROSS_PLATFORM_COMPATIBILITY,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def validate_multi_installation_support(self) -> PrincipleValidation:
        """Validate Principle II: Multi-Installation Support."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check installation method detection
        from ..compatibility import create_compatibility_validator
        try:
            validator = create_compatibility_validator()
            for method in self.installation_methods:
                result = validator.validate_installation_method("Claude Code", method)
                if result["status"] == "valid":
                    evidence.append(f"Installation method '{method}' validated for Claude Code")
                else:
                    violations.append(f"Installation method '{method}' validation failed")
        except Exception as e:
            violations.append(f"Installation method validation failed: {str(e)}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.MULTI_INSTALLATION_SUPPORT,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def validate_architecture_first_development(self) -> PrincipleValidation:
        """Validate Principle III: Architecture-First Development."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check if architecture planning files exist
        architecture_files = [
            "specs/001-improve-spec-kit/plan.md",
            "specs/001-improve-spec-kit/architecture.md",
            "specs/001-improve-spec-kit/contracts/"
        ]
        
        for file_path in architecture_files:
            if Path(file_path).exists():
                evidence.append(f"Architecture file exists: {file_path}")
            else:
                violations.append(f"Missing architecture file: {file_path}")
        
        # Check if MCP integration architecture exists
        mcp_files = [
            "src/specify_cli/mcp/__init__.py",
            "src/specify_cli/mcp/orchestrator.py"
        ]
        
        for file_path in mcp_files:
            if Path(file_path).exists():
                evidence.append(f"MCP architecture file exists: {file_path}")
            else:
                violations.append(f"Missing MCP architecture file: {file_path}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.ARCHITECTURE_FIRST_DEVELOPMENT,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def validate_template_driven_consistency(self) -> PrincipleValidation:
        """Validate Principle IV: Template-Driven Consistency."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check template directory structure
        template_dirs = ["templates", "templates/commands"]
        for dir_path in template_dirs:
            if Path(dir_path).exists():
                evidence.append(f"Template directory exists: {dir_path}")
            else:
                violations.append(f"Missing template directory: {dir_path}")
        
        # Check key template files
        template_files = [
            "templates/plan-template.md",
            "templates/spec-template.md",
            "templates/tasks-template.md",
            "templates/commands/analyze.md"
        ]
        
        for file_path in template_files:
            if Path(file_path).exists():
                evidence.append(f"Template file exists: {file_path}")
            else:
                violations.append(f"Missing template file: {file_path}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.TEMPLATE_DRIVEN_CONSISTENCY,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def validate_synchronicity_enforcement(self) -> PrincipleValidation:
        """Validate Principle V: Synchronicity Enforcement."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check if governance documents are synchronized
        governance_files = [
            "memory/constitution.md",
            "AGENTS.md",
            "CLAUDE.md"
        ]
        
        for file_path in governance_files:
            if Path(file_path).exists():
                evidence.append(f"Governance file exists: {file_path}")
            else:
                violations.append(f"Missing governance file: {file_path}")
        
        # Check if platform-specific directories exist
        platform_dirs = [".claude", ".roo"]
        for dir_path in platform_dirs:
            if Path(dir_path).exists():
                evidence.append(f"Platform directory exists: {dir_path}")
            else:
                recommendations.append(f"Consider creating platform directory: {dir_path}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.SYNCHRONICITY_ENFORCEMENT,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def validate_agent_native_execution(self) -> PrincipleValidation:
        """Validate Principle VI: Agent-Native Execution."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check script directories
        script_dirs = ["scripts/bash", "scripts/powershell"]
        for dir_path in script_dirs:
            if Path(dir_path).exists():
                evidence.append(f"Script directory exists: {dir_path}")
                # Check if scripts are executable
                script_files = list(Path(dir_path).glob("*.sh")) if dir_path.endswith("bash") else list(Path(dir_path).glob("*.ps1"))
                if script_files:
                    evidence.append(f"Script files found in {dir_path}: {len(script_files)}")
                else:
                    violations.append(f"No script files found in {dir_path}")
            else:
                violations.append(f"Missing script directory: {dir_path}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.AGENT_NATIVE_EXECUTION,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def validate_hierarchical_governance(self) -> PrincipleValidation:
        """Validate Principle VII: Hierarchical Governance."""
        violations = []
        evidence = []
        recommendations = []
        
        # Check hierarchical governance structure
        governance_structure = {
            "Constitution": "memory/constitution.md",
            "Agent Guidelines": "AGENTS.md",
            "Claude Specific": "CLAUDE.md",
            "Templates": "templates/",
            "Scripts": "scripts/"
        }
        
        for level, path in governance_structure.items():
            if Path(path).exists():
                evidence.append(f"Governance level '{level}' exists: {path}")
            else:
                violations.append(f"Missing governance level '{level}': {path}")
        
        status = ComplianceStatus.COMPLIANT if not violations else ComplianceStatus.NON_COMPLIANT
        
        return PrincipleValidation(
            principle=PrincipleType.HIERARCHICAL_GOVERNANCE,
            status=status,
            violations=violations,
            evidence=evidence,
            recommendations=recommendations,
            timestamp=self._get_timestamp()
        )
    
    def _determine_overall_status(self, validations: Dict[PrincipleType, PrincipleValidation]) -> ComplianceStatus:
        """Determine overall compliance status based on individual validations."""
        statuses = [validation.status for validation in validations.values()]
        
        if all(status == ComplianceStatus.COMPLIANT for status in statuses):
            return ComplianceStatus.COMPLIANT
        elif any(status == ComplianceStatus.NON_COMPLIANT for status in statuses):
            return ComplianceStatus.NON_COMPLIANT
        elif any(status == ComplianceStatus.PARTIALLY_COMPLIANT for status in statuses):
            return ComplianceStatus.PARTIALLY_COMPLIANT
        else:
            return ComplianceStatus.PENDING_VALIDATION
    
    def _generate_summary(self, validations: Dict[PrincipleType, PrincipleValidation], overall_status: ComplianceStatus) -> str:
        """Generate a summary of the compliance report."""
        compliant_count = sum(1 for v in validations.values() if v.status == ComplianceStatus.COMPLIANT)
        total_count = len(validations)
        
        summary = f"Constitutional Compliance Summary: {compliant_count}/{total_count} principles compliant\n"
        summary += f"Overall Status: {overall_status.value}\n\n"
        
        for principle, validation in validations.items():
            summary += f"{principle.value}: {validation.status.value}\n"
            if validation.violations:
                summary += f"  Violations: {len(validation.violations)}\n"
            if validation.evidence:
                summary += f"  Evidence: {len(validation.evidence)} items\n"
        
        return summary
    
    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format."""
        from datetime import datetime
        return datetime.now().isoformat()


class ComplianceMonitor:
    """
    Continuous compliance monitoring with reporting capabilities.
    
    Provides real-time monitoring of constitutional compliance and generates
    comprehensive reports for governance review.
    """
    
    def __init__(self):
        self.validator = ConstitutionalValidator()
        self.history: List[ComplianceReport] = []
    
    def run_compliance_check(self) -> ComplianceReport:
        """Run a comprehensive compliance check and store in history."""
        report = self.validator.validate_all_principles()
        self.history.append(report)
        return report
    
    def generate_report(self, format: str = "text") -> str:
        """Generate compliance report in specified format."""
        report = self.run_compliance_check()
        
        if format == "json":
            return self._generate_json_report(report)
        elif format == "yaml":
            return self._generate_yaml_report(report)
        else:
            return self._generate_text_report(report)
    
    def _generate_text_report(self, report: ComplianceReport) -> str:
        """Generate human-readable text report."""
        report_text = f"=== CONSTITUTIONAL COMPLIANCE REPORT ===\n"
        report_text += f"Generated: {report.timestamp}\n"
        report_text += f"Overall Status: {report.overall_status.value.upper()}\n\n"
        
        report_text += report.summary + "\n"
        
        for principle, validation in report.validations.items():
            report_text += f"\n--- {principle.value} ---\n"
            report_text += f"Status: {validation.status.value}\n"
            
            if validation.violations:
                report_text += "Violations:\n"
                for violation in validation.violations:
                    report_text += f"  - {violation}\n"
            
            if validation.evidence:
                report_text += "Evidence:\n"
                for evidence in validation.evidence:
                    report_text += f"  + {evidence}\n"
            
            if validation.recommendations:
                report_text += "Recommendations:\n"
                for rec in validation.recommendations:
                    report_text += f"  * {rec}\n"
        
        return report_text
    
    def _generate_json_report(self, report: ComplianceReport) -> str:
        """Generate JSON format report."""
        report_dict = {
            "timestamp": report.timestamp,
            "overall_status": report.overall_status.value,
            "version": report.version,
            "validations": {}
        }
        
        for principle, validation in report.validations.items():
            report_dict["validations"][principle.value] = {
                "status": validation.status.value,
                "violations": validation.violations,
                "evidence": validation.evidence,
                "recommendations": validation.recommendations,
                "timestamp": validation.timestamp
            }
        
        return json.dumps(report_dict, indent=2)
    
    def _generate_yaml_report(self, report: ComplianceReport) -> str:
        """Generate YAML format report."""
        report_dict = {
            "timestamp": report.timestamp,
            "overall_status": report.overall_status.value,
            "version": report.version,
            "validations": {}
        }
        
        for principle, validation in report.validations.items():
            report_dict["validations"][principle.value] = {
                "status": validation.status.value,
                "violations": validation.violations,
                "evidence": validation.evidence,
                "recommendations": validation.recommendations,
                "timestamp": validation.timestamp
            }
        
        return yaml.dump(report_dict, default_flow_style=False)


def create_constitutional_validator() -> ConstitutionalValidator:
    """Factory function to create a constitutional validator."""
    return ConstitutionalValidator()


def create_compliance_monitor() -> ComplianceMonitor:
    """Factory function to create a compliance monitor."""
    return ComplianceMonitor()