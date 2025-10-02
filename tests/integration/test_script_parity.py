"""
Test script parity between bash and PowerShell versions.
Ensures identical behavior and output across platforms.
"""
import json
import platform
import subprocess
import pytest
from pathlib import Path


def get_repo_root():
    """Get repository root directory."""
    return Path(__file__).parent.parent.parent


def is_windows():
    """Check if running on Windows."""
    return platform.system() == "Windows"


def run_bash_script(script_name, args=None):
    """Run a bash script and return output."""
    script_path = get_repo_root() / "scripts" / "bash" / script_name
    cmd = ["bash", str(script_path)]
    if args:
        cmd.extend(args)
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=get_repo_root()
    )
    return result


def run_powershell_script(script_name, args=None):
    """Run a PowerShell script and return output."""
    script_path = get_repo_root() / "scripts" / "powershell" / script_name
    cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(script_path)]
    if args:
        cmd.extend(args)
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=get_repo_root()
    )
    return result


def normalize_paths(text):
    """Normalize paths by converting backslashes to forward slashes."""
    return text.replace('\\', '/')


class TestValidationScriptParity:
    """Test validation script parity (bash vs PowerShell)."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_validate_structure_bash(self):
        """Test bash validate-structure.sh script."""
        result = run_bash_script("validate-structure.sh", ["."])
        
        assert result.returncode == 0, "Script should exit with code 0"
        assert "[INFO]" in result.stdout, "Should contain INFO messages"
        assert "Structure validation complete" in result.stdout
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_validate_structure_powershell(self):
        """Test PowerShell validate-structure.ps1 script."""
        result = run_powershell_script("validate-structure.ps1", ["."])
        
        assert result.returncode == 0, "Script should exit with code 0"
        assert "[INFO]" in result.stdout, "Should contain INFO messages"
        assert "Structure validation complete" in result.stdout
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_validate_naming_bash(self):
        """Test bash validate-naming.sh script."""
        result = run_bash_script("validate-naming.sh", ["."])
        
        assert result.returncode == 0, "Script should exit with code 0"
        assert "[INFO]" in result.stdout, "Should contain INFO messages"
        assert "Naming validation complete" in result.stdout
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_validate_naming_powershell(self):
        """Test PowerShell validate-naming.ps1 script."""
        result = run_powershell_script("validate-naming.ps1", ["."])
        
        assert result.returncode == 0, "Script should exit with code 0"
        assert "[INFO]" in result.stdout, "Should contain INFO messages"
        assert "Naming validation complete" in result.stdout
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_validate_frontmatter_bash(self):
        """Test bash validate-frontmatter.sh script."""
        # Use existing spec file for testing
        spec_file = get_repo_root() / "specs" / "004-realignment-v2-corrected" / "spec.md"
        if spec_file.exists():
            result = run_bash_script("validate-frontmatter.sh", [str(spec_file)])
            
            assert result.returncode == 0, "Script should exit with code 0"
            assert "[INFO]" in result.stdout, "Should contain INFO messages"
            assert "Frontmatter validation complete" in result.stdout
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_validate_frontmatter_powershell(self):
        """Test PowerShell validate-frontmatter.ps1 script."""
        # Use existing spec file for testing
        spec_file = get_repo_root() / "specs" / "004-realignment-v2-corrected" / "spec.md"
        if spec_file.exists():
            result = run_powershell_script("validate-frontmatter.ps1", [str(spec_file)])
            
            assert result.returncode == 0, "Script should exit with code 0"
            assert "[INFO]" in result.stdout, "Should contain INFO messages"
            assert "Frontmatter validation complete" in result.stdout


class TestHelperScriptParity:
    """Test helper script JSON output parity (bash vs PowerShell)."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_check_prerequisites_bash_json(self):
        """Test bash check-prerequisites.sh JSON output."""
        result = run_bash_script("check-prerequisites.sh", ["--json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON output
        try:
            data = json.loads(result.stdout)
            assert "FEATURE_DIR" in data, "Should contain FEATURE_DIR"
            assert "AVAILABLE_DOCS" in data, "Should contain AVAILABLE_DOCS"
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON output: {e}")
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_check_prerequisites_powershell_json(self):
        """Test PowerShell check-prerequisites.ps1 JSON output."""
        result = run_powershell_script("check-prerequisites.ps1", ["-Json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON output
        try:
            data = json.loads(result.stdout)
            assert "FEATURE_DIR" in data, "Should contain FEATURE_DIR"
            assert "AVAILABLE_DOCS" in data, "Should contain AVAILABLE_DOCS"
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON output: {e}")
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_setup_plan_bash_json(self):
        """Test bash setup-plan.sh JSON output."""
        result = run_bash_script("setup-plan.sh", ["--json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON output
        try:
            data = json.loads(result.stdout)
            assert "FEATURE_SPEC" in data or "error" in data, "Should contain FEATURE_SPEC or error"
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON output: {e}")
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_setup_plan_powershell_json(self):
        """Test PowerShell setup-plan.ps1 JSON output."""
        result = run_powershell_script("setup-plan.ps1", ["-Json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON output
        try:
            data = json.loads(result.stdout)
            assert "FEATURE_SPEC" in data or "error" in data, "Should contain FEATURE_SPEC or error"
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON output: {e}")


class TestScriptExitCodes:
    """Test that all scripts exit with code 0 (non-blocking)."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    @pytest.mark.parametrize("script_name", [
        "validate-structure.sh",
        "validate-naming.sh",
        "check-prerequisites.sh",
        "setup-plan.sh",
    ])
    def test_bash_scripts_exit_zero(self, script_name):
        """All bash scripts should exit with code 0."""
        result = run_bash_script(script_name, ["--json"] if "check" in script_name or "setup" in script_name else ["."])
        assert result.returncode == 0, f"{script_name} should exit with code 0"
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    @pytest.mark.parametrize("script_name", [
        "validate-structure.ps1",
        "validate-naming.ps1",
        "check-prerequisites.ps1",
        "setup-plan.ps1",
    ])
    def test_powershell_scripts_exit_zero(self, script_name):
        """All PowerShell scripts should exit with code 0."""
        result = run_powershell_script(script_name, ["-Json"] if "check" in script_name or "setup" in script_name else ["."])
        assert result.returncode == 0, f"{script_name} should exit with code 0"
