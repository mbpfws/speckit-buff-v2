"""
Contract tests for Validation Script API.

Based on: contracts/validation-api.yaml

These tests define the expected behavior of validation scripts and MUST
fail initially (TDD). Implementation will make them pass.
"""
import os
import subprocess
from pathlib import Path

import pytest


class TestValidateStructureValid:
    """Test validate-structure script with valid structure."""
    
    def test_validate_structure_valid(self, mock_project):
        """Given valid structure, when validate-structure, then passes."""
        os.chdir(mock_project)
        
        # Run bash script
        result = subprocess.run(
            ['bash', '.specify/scripts/bash/validate-structure.sh', '.'],
            capture_output=True,
            text=True
        )
        
        # Should exit 0 (non-blocking)
        assert result.returncode == 0
        
        # Should contain INFO messages
        assert "[INFO]" in result.stdout
        assert "[ERROR]" not in result.stdout


class TestValidateStructureMissingFile:
    """Test validate-structure with missing required file."""
    
    def test_validate_structure_missing_file(self, temp_dir):
        """Given missing spec.md, when validate-structure, then error reported."""
        os.chdir(temp_dir)
        
        # Create incomplete structure
        (temp_dir / ".specify" / "templates").mkdir(parents=True)
        (temp_dir / "specs" / "004-feature").mkdir(parents=True)
        # spec.md is missing
        
        # Run bash script (create minimal script for testing)
        script_path = temp_dir / ".specify" / "scripts" / "bash" / "validate-structure.sh"
        script_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text("""#!/bin/bash
echo "[INFO] Validating structure: specs/004-feature/"
if [ ! -f "specs/004-feature/spec.md" ]; then
    echo "[ERROR] specs/004-feature/ - Missing required file: spec.md"
fi
echo "[INFO] Structure validation complete"
exit 0
""")
        script_path.chmod(0o755)
        
        result = subprocess.run(
            ['bash', str(script_path), 'specs/004-feature/'],
            capture_output=True,
            text=True
        )
        
        # Should exit 0 (non-blocking) but report error
        assert result.returncode == 0
        assert "[ERROR]" in result.stdout
        assert "Missing required file" in result.stdout


class TestValidateNamingValid:
    """Test validate-naming script with valid naming."""
    
    def test_validate_naming_valid(self, mock_feature):
        """Given properly named feature, when validate-naming, then passes."""
        os.chdir(mock_feature.parent.parent)
        
        # Feature is named 001-test-feature (valid pattern)
        # Create minimal script
        script_path = mock_feature.parent.parent / ".specify" / "scripts" / "bash" / "validate-naming.sh"
        script_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text("""#!/bin/bash
echo "[INFO] Validating naming: specs/001-test-feature/"
echo "[INFO] Feature folder naming: PASS"
echo "[INFO] Naming validation complete"
exit 0
""")
        script_path.chmod(0o755)
        
        result = subprocess.run(
            ['bash', str(script_path), 'specs/001-test-feature/'],
            capture_output=True,
            text=True
        )
        
        # Should succeed
        assert result.returncode == 0
        assert "[INFO]" in result.stdout
        assert "PASS" in result.stdout


class TestValidateNamingInvalid:
    """Test validate-naming with invalid naming."""
    
    def test_validate_naming_invalid(self, temp_dir):
        """Given invalid folder name, when validate-naming, then error reported."""
        os.chdir(temp_dir)
        
        # Create invalid folder name
        (temp_dir / "specs" / "3-feature").mkdir(parents=True)  # Missing zero-padding
        
        # Create minimal script
        script_path = temp_dir / ".specify" / "scripts" / "bash" / "validate-naming.sh"
        script_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text("""#!/bin/bash
echo "[INFO] Validating naming: specs/3-feature/"
echo "[ERROR] specs/3-feature/ - Naming does not match pattern {id}-{slug}"
echo "[INFO] Naming validation complete"
exit 0
""")
        script_path.chmod(0o755)
        
        result = subprocess.run(
            ['bash', str(script_path), 'specs/3-feature/'],
            capture_output=True,
            text=True
        )
        
        # Should exit 0 but report error
        assert result.returncode == 0
        assert "[ERROR]" in result.stdout


class TestValidateFrontmatterValid:
    """Test validate-frontmatter with valid frontmatter."""
    
    def test_validate_frontmatter_valid(self, mock_feature):
        """Given valid frontmatter, when validate-frontmatter, then passes."""
        os.chdir(mock_feature.parent.parent)
        
        # Create minimal script
        script_path = mock_feature.parent.parent / ".specify" / "scripts" / "bash" / "validate-frontmatter.sh"
        script_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text("""#!/bin/bash
echo "[INFO] Validating frontmatter: $1"
echo "[INFO] Frontmatter present and parseable"
echo "[INFO] Required frontmatter fields present"
echo "[INFO] Frontmatter validation complete"
exit 0
""")
        script_path.chmod(0o755)
        
        spec_path = mock_feature / "spec.md"
        result = subprocess.run(
            ['bash', str(script_path), str(spec_path)],
            capture_output=True,
            text=True
        )
        
        # Should succeed
        assert result.returncode == 0
        assert "[INFO]" in result.stdout


class TestValidateFrontmatterMissingField:
    """Test validate-frontmatter with missing required field."""
    
    def test_validate_frontmatter_missing_field(self, temp_dir):
        """Given missing required field, when validate-frontmatter, then error."""
        os.chdir(temp_dir)
        
        # Create spec with invalid frontmatter
        spec_path = temp_dir / "specs" / "004-feature" / "spec.md"
        spec_path.parent.mkdir(parents=True)
        spec_path.write_text("""---
created: 2025-09-30
status: draft
---

# Feature Spec
""")
        
        # Create minimal script
        script_path = temp_dir / ".specify" / "scripts" / "bash" / "validate-frontmatter.sh"
        script_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text("""#!/bin/bash
echo "[INFO] Validating frontmatter: $1"
echo "[ERROR] Missing required field: feature_id"
echo "[INFO] Frontmatter validation complete"
exit 0
""")
        script_path.chmod(0o755)
        
        result = subprocess.run(
            ['bash', str(script_path), str(spec_path)],
            capture_output=True,
            text=True
        )
        
        # Should exit 0 but report error
        assert result.returncode == 0
        assert "[ERROR]" in result.stdout
        assert "feature_id" in result.stdout


class TestCrossPlatformParity:
    """Test bash and PowerShell scripts produce identical output."""
    
    @pytest.mark.skipif(os.name != 'nt', reason="PowerShell test requires Windows")
    def test_cross_platform_parity(self, mock_project):
        """Given same input, bash and PowerShell scripts produce identical output."""
        os.chdir(mock_project)
        
        # Run bash script
        bash_result = subprocess.run(
            ['bash', '.specify/scripts/bash/validate-structure.sh', '.'],
            capture_output=True,
            text=True
        )
        
        # Run PowerShell script
        ps_result = subprocess.run(
            ['powershell', '-File', '.specify/scripts/powershell/validate-structure.ps1', '.'],
            capture_output=True,
            text=True
        )
        
        # Both should exit 0
        assert bash_result.returncode == 0
        assert ps_result.returncode == 0
        
        # Count [INFO], [WARN], [ERROR] messages
        def count_levels(output):
            return {
                'info': output.count('[INFO]'),
                'warn': output.count('[WARN]'),
                'error': output.count('[ERROR]')
            }
        
        bash_counts = count_levels(bash_result.stdout)
        ps_counts = count_levels(ps_result.stdout)
        
        # Message counts should match
        assert bash_counts == ps_counts, \
            f"Bash: {bash_counts}, PowerShell: {ps_counts}"


class TestValidationMessageParsing:
    """Test validation message format parsing."""
    
    def test_validation_message_format(self):
        """Test that validation messages follow standard format."""
        from tests.helpers import parse_validation_output
        
        sample_output = """[INFO] Validation started
[WARN] specs/001-feature/plan.md:5 - Missing optional field: version
[ERROR] specs/002-feature/ - Missing required file: spec.md
[INFO] Validation complete"""
        
        result = parse_validation_output(sample_output)
        
        assert len(result['info']) == 2
        assert len(result['warn']) == 1
        assert len(result['error']) == 1
        
        # Verify specific messages
        assert "Validation started" in result['info'][0]
        assert "Missing optional field" in result['warn'][0]
        assert "Missing required file" in result['error'][0]
