"""
Test cases for Constitutional Compliance Monitoring System.

These tests validate the constitutional compliance monitoring functionality
and ensure all 7 principles are properly validated.
"""

import pytest
import sys
from pathlib import Path
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

from specify_cli.governance import (
    ConstitutionalValidator,
    ComplianceMonitor,
    PrincipleType,
    ComplianceStatus,
    create_constitutional_validator,
    create_compliance_monitor
)


class TestConstitutionalValidator:
    """Test cases for ConstitutionalValidator class."""
    
    def test_validator_initialization(self):
        """Test that validator initializes correctly."""
        validator = ConstitutionalValidator()
        assert validator is not None
        assert hasattr(validator, 'supported_platforms')
        assert hasattr(validator, 'installation_methods')
        assert len(validator.supported_platforms) == 10
        assert len(validator.installation_methods) == 2
    
    def test_validate_all_principles(self):
        """Test comprehensive principle validation."""
        validator = ConstitutionalValidator()
        report = validator.validate_all_principles()
        
        assert report is not None
        assert hasattr(report, 'validations')
        assert hasattr(report, 'overall_status')
        assert hasattr(report, 'summary')
        assert hasattr(report, 'timestamp')
        
        # Should validate all 7 principles
        assert len(report.validations) == 7
        assert all(isinstance(key, PrincipleType) for key in report.validations.keys())
    
    def test_validate_cross_platform_compatibility(self):
        """Test Principle I validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_cross_platform_compatibility()
        
        assert validation.principle == PrincipleType.CROSS_PLATFORM_COMPATIBILITY
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
        assert isinstance(validation.timestamp, str)
    
    def test_validate_multi_installation_support(self):
        """Test Principle II validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_multi_installation_support()
        
        assert validation.principle == PrincipleType.MULTI_INSTALLATION_SUPPORT
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
    
    def test_validate_architecture_first_development(self):
        """Test Principle III validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_architecture_first_development()
        
        assert validation.principle == PrincipleType.ARCHITECTURE_FIRST_DEVELOPMENT
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
    
    def test_validate_template_driven_consistency(self):
        """Test Principle IV validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_template_driven_consistency()
        
        assert validation.principle == PrincipleType.TEMPLATE_DRIVEN_CONSISTENCY
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
    
    def test_validate_synchronicity_enforcement(self):
        """Test Principle V validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_synchronicity_enforcement()
        
        assert validation.principle == PrincipleType.SYNCHRONICITY_ENFORCEMENT
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
    
    def test_validate_agent_native_execution(self):
        """Test Principle VI validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_agent_native_execution()
        
        assert validation.principle == PrincipleType.AGENT_NATIVE_EXECUTION
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
    
    def test_validate_hierarchical_governance(self):
        """Test Principle VII validation."""
        validator = ConstitutionalValidator()
        validation = validator.validate_hierarchical_governance()
        
        assert validation.principle == PrincipleType.HIERARCHICAL_GOVERNANCE
        assert validation.status in [ComplianceStatus.COMPLIANT, ComplianceStatus.NON_COMPLIANT]
        assert isinstance(validation.violations, list)
        assert isinstance(validation.evidence, list)
        assert isinstance(validation.recommendations, list)
    
    def test_determine_overall_status_all_compliant(self):
        """Test overall status determination when all principles are compliant."""
        validator = ConstitutionalValidator()
        
        # Create mock validations with all compliant
        validations = {}
        for principle in PrincipleType:
            validations[principle] = type('MockValidation', (), {
                'status': ComplianceStatus.COMPLIANT
            })()
        
        status = validator._determine_overall_status(validations)
        assert status == ComplianceStatus.COMPLIANT
    
    def test_determine_overall_status_some_non_compliant(self):
        """Test overall status determination with some non-compliant principles."""
        validator = ConstitutionalValidator()
        
        # Create mock validations with some non-compliant
        validations = {}
        for i, principle in enumerate(PrincipleType):
            if i % 2 == 0:  # Every other principle is non-compliant
                validations[principle] = type('MockValidation', (), {
                    'status': ComplianceStatus.NON_COMPLIANT
                })()
            else:
                validations[principle] = type('MockValidation', (), {
                    'status': ComplianceStatus.COMPLIANT
                })()
        
        status = validator._determine_overall_status(validations)
        assert status == ComplianceStatus.NON_COMPLIANT
    
    def test_generate_summary(self):
        """Test summary generation."""
        validator = ConstitutionalValidator()
        
        # Create mock validations
        validations = {}
        for principle in PrincipleType:
            validations[principle] = type('MockValidation', (), {
                'status': ComplianceStatus.COMPLIANT,
                'violations': [],
                'evidence': ['test evidence']
            })()
        
        overall_status = ComplianceStatus.COMPLIANT
        summary = validator._generate_summary(validations, overall_status)
        
        assert isinstance(summary, str)
        assert "Constitutional Compliance Summary" in summary
        assert "Overall Status" in summary
    
    def test_get_timestamp(self):
        """Test timestamp generation."""
        validator = ConstitutionalValidator()
        timestamp = validator._get_timestamp()
        
        assert isinstance(timestamp, str)
        # Should be ISO format
        try:
            datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            assert True
        except ValueError:
            assert False, "Timestamp is not valid ISO format"


class TestComplianceMonitor:
    """Test cases for ComplianceMonitor class."""
    
    def test_monitor_initialization(self):
        """Test that monitor initializes correctly."""
        monitor = ComplianceMonitor()
        assert monitor is not None
        assert hasattr(monitor, 'validator')
        assert hasattr(monitor, 'history')
        assert isinstance(monitor.history, list)
    
    def test_run_compliance_check(self):
        """Test running a compliance check."""
        monitor = ComplianceMonitor()
        initial_history_length = len(monitor.history)
        
        report = monitor.run_compliance_check()
        
        assert report is not None
        assert len(monitor.history) == initial_history_length + 1
        assert monitor.history[-1] == report
    
    def test_generate_text_report(self):
        """Test text report generation."""
        monitor = ComplianceMonitor()
        report = monitor.run_compliance_check()
        text_report = monitor._generate_text_report(report)
        
        assert isinstance(text_report, str)
        assert "CONSTITUTIONAL COMPLIANCE REPORT" in text_report
        assert "Overall Status" in text_report
    
    def test_generate_json_report(self):
        """Test JSON report generation."""
        monitor = ComplianceMonitor()
        report = monitor.run_compliance_check()
        json_report = monitor._generate_json_report(report)
        
        assert isinstance(json_report, str)
        # Should be valid JSON
        import json
        parsed = json.loads(json_report)
        assert "timestamp" in parsed
        assert "overall_status" in parsed
        assert "validations" in parsed
    
    def test_generate_yaml_report(self):
        """Test YAML report generation."""
        monitor = ComplianceMonitor()
        report = monitor.run_compliance_check()
        yaml_report = monitor._generate_yaml_report(report)
        
        assert isinstance(yaml_report, str)
        # Should contain YAML structure indicators
        assert "timestamp:" in yaml_report
        assert "overall_status:" in yaml_report
    
    def test_generate_report_text_format(self):
        """Test report generation with text format."""
        monitor = ComplianceMonitor()
        report = monitor.generate_report(format="text")
        
        assert isinstance(report, str)
        assert "CONSTITUTIONAL COMPLIANCE REPORT" in report
    
    def test_generate_report_json_format(self):
        """Test report generation with JSON format."""
        monitor = ComplianceMonitor()
        report = monitor.generate_report(format="json")
        
        assert isinstance(report, str)
        import json
        parsed = json.loads(report)
        assert "timestamp" in parsed
    
    def test_generate_report_yaml_format(self):
        """Test report generation with YAML format."""
        monitor = ComplianceMonitor()
        report = monitor.generate_report(format="yaml")
        
        assert isinstance(report, str)
        assert "timestamp:" in report


class TestFactoryFunctions:
    """Test factory functions for creating validators and monitors."""
    
    def test_create_constitutional_validator(self):
        """Test factory function for constitutional validator."""
        validator = create_constitutional_validator()
        assert isinstance(validator, ConstitutionalValidator)
    
    def test_create_compliance_monitor(self):
        """Test factory function for compliance monitor."""
        monitor = create_compliance_monitor()
        assert isinstance(monitor, ComplianceMonitor)


class TestComplianceStatusEnum:
    """Test ComplianceStatus enum functionality."""
    
    def test_compliance_status_values(self):
        """Test that all compliance status values are defined."""
        statuses = [status.value for status in ComplianceStatus]
        expected = ["compliant", "non_compliant", "pending_validation", "partially_compliant"]
        assert all(status in statuses for status in expected)
    
    def test_principle_type_values(self):
        """Test that all principle type values are defined."""
        principles = [principle.value for principle in PrincipleType]
        expected = [
            "I. Cross-Platform Compatibility",
            "II. Multi-Installation Support", 
            "III. Architecture-First Development",
            "IV. Template-Driven Consistency",
            "V. Synchronicity Enforcement",
            "VI. Agent-Native Execution",
            "VII. Hierarchical Governance"
        ]
        assert all(principle in principles for principle in expected)


class TestIntegration:
    """Integration tests for constitutional compliance system."""
    
    def test_end_to_end_compliance_check(self):
        """Test complete end-to-end compliance checking workflow."""
        # Create monitor
        monitor = create_compliance_monitor()
        
        # Run compliance check
        report = monitor.run_compliance_check()
        
        # Verify report structure
        assert report.overall_status in [
            ComplianceStatus.COMPLIANT, 
            ComplianceStatus.NON_COMPLIANT,
            ComplianceStatus.PARTIALLY_COMPLIANT
        ]
        
        # Verify all principles are validated
        assert len(report.validations) == 7
        
        # Verify report contains meaningful information
        assert len(report.summary) > 0
        assert "Constitutional Compliance Summary" in report.summary
        
        # Verify history is maintained
        assert len(monitor.history) == 1
        assert monitor.history[0] == report
    
    def test_multiple_compliance_checks(self):
        """Test running multiple compliance checks."""
        monitor = create_compliance_monitor()
        
        # Run multiple checks
        report1 = monitor.run_compliance_check()
        report2 = monitor.run_compliance_check()
        
        # Verify history contains both reports
        assert len(monitor.history) == 2
        assert monitor.history[0] == report1
        assert monitor.history[1] == report2
        
        # Verify timestamps are different
        assert report1.timestamp != report2.timestamp


if __name__ == "__main__":
    pytest.main([__file__, "-v"])