"""
Test JSON output contracts for helper scripts.
Validates that all helper scripts produce standardized JSON output.
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


def validate_json_paths(data, field_names):
    """Validate that JSON paths use forward slashes and are absolute."""
    for field in field_names:
        if field in data and data[field]:
            path = data[field]
            if isinstance(path, str):
                # Check for forward slashes (cross-platform compatibility)
                if '\\' in path:
                    pytest.fail(f"Path {field} contains backslashes: {path}")
                
                # Check for absolute path (starts with / or drive letter)
                if not (path.startswith('/') or (len(path) > 2 and path[1] == ':')):
                    pytest.fail(f"Path {field} is not absolute: {path}")


class TestCheckPrerequisitesContract:
    """Test check-prerequisites script JSON contract."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_check_prerequisites_bash_contract(self):
        """Test bash check-prerequisites.sh JSON contract."""
        result = run_bash_script("check-prerequisites.sh", ["--json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON
        data = json.loads(result.stdout)
        
        # Validate required fields
        assert "FEATURE_DIR" in data, "Missing required field: FEATURE_DIR"
        assert "AVAILABLE_DOCS" in data, "Missing required field: AVAILABLE_DOCS"
        
        # Validate field types
        assert isinstance(data["AVAILABLE_DOCS"], list), "AVAILABLE_DOCS should be a list"
        
        # Validate paths
        if data.get("FEATURE_DIR"):
            validate_json_paths(data, ["FEATURE_DIR", "FEATURE_SPEC", "IMPL_PLAN", "TASKS"])
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_check_prerequisites_powershell_contract(self):
        """Test PowerShell check-prerequisites.ps1 JSON contract."""
        result = run_powershell_script("check-prerequisites.ps1", ["-Json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON
        data = json.loads(result.stdout)
        
        # Validate required fields
        assert "FEATURE_DIR" in data, "Missing required field: FEATURE_DIR"
        assert "AVAILABLE_DOCS" in data, "Missing required field: AVAILABLE_DOCS"
        
        # Validate field types
        assert isinstance(data["AVAILABLE_DOCS"], list), "AVAILABLE_DOCS should be a list"
        
        # Validate paths use forward slashes
        if data.get("FEATURE_DIR"):
            validate_json_paths(data, ["FEATURE_DIR", "FEATURE_SPEC", "IMPL_PLAN", "TASKS"])


class TestSetupPlanContract:
    """Test setup-plan script JSON contract."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_setup_plan_bash_contract(self):
        """Test bash setup-plan.sh JSON contract."""
        result = run_bash_script("setup-plan.sh", ["--json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON
        data = json.loads(result.stdout)
        
        # Should have either success fields or error field
        if "error" not in data:
            # Validate success case fields
            expected_fields = ["FEATURE_SPEC", "IMPL_PLAN", "SPECS_DIR"]
            for field in expected_fields:
                if field in data and data[field]:
                    validate_json_paths(data, [field])
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_setup_plan_powershell_contract(self):
        """Test PowerShell setup-plan.ps1 JSON contract."""
        result = run_powershell_script("setup-plan.ps1", ["-Json"])
        
        assert result.returncode == 0, "Script should exit with code 0"
        
        # Parse JSON
        data = json.loads(result.stdout)
        
        # Should have either success fields or error field
        if "error" not in data:
            # Validate success case fields
            expected_fields = ["FEATURE_SPEC", "IMPL_PLAN", "SPECS_DIR"]
            for field in expected_fields:
                if field in data and data[field]:
                    validate_json_paths(data, [field])


class TestCreateNewFeatureContract:
    """Test create-new-feature script JSON contract."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_create_new_feature_bash_dry_run(self):
        """Test bash create-new-feature.sh JSON output (dry run)."""
        # Note: This would create a branch, so we skip actual execution
        # Just validate the script exists and is executable
        script_path = get_repo_root() / "scripts" / "bash" / "create-new-feature.sh"
        assert script_path.exists(), "create-new-feature.sh should exist"
        assert script_path.stat().st_mode & 0o111, "Script should be executable"
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_create_new_feature_powershell_exists(self):
        """Test PowerShell create-new-feature.ps1 exists."""
        script_path = get_repo_root() / "scripts" / "powershell" / "create-new-feature.ps1"
        assert script_path.exists(), "create-new-feature.ps1 should exist"


class TestJSONFormatting:
    """Test JSON formatting consistency."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_bash_json_is_valid(self):
        """Test that bash scripts output valid, parseable JSON."""
        scripts = [
            ("check-prerequisites.sh", ["--json"]),
            ("setup-plan.sh", ["--json"]),
        ]
        
        for script_name, args in scripts:
            result = run_bash_script(script_name, args)
            
            try:
                data = json.loads(result.stdout)
                assert isinstance(data, dict), f"{script_name} should output JSON object"
            except json.JSONDecodeError as e:
                pytest.fail(f"{script_name} produced invalid JSON: {e}\nOutput: {result.stdout}")
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_powershell_json_is_valid(self):
        """Test that PowerShell scripts output valid, parseable JSON."""
        scripts = [
            ("check-prerequisites.ps1", ["-Json"]),
            ("setup-plan.ps1", ["-Json"]),
        ]
        
        for script_name, args in scripts:
            result = run_powershell_script(script_name, args)
            
            try:
                data = json.loads(result.stdout)
                assert isinstance(data, dict), f"{script_name} should output JSON object"
            except json.JSONDecodeError as e:
                pytest.fail(f"{script_name} produced invalid JSON: {e}\nOutput: {result.stdout}")


class TestPathNormalization:
    """Test that all paths use forward slashes for cross-platform compatibility."""
    
    @pytest.mark.skipif(is_windows(), reason="Bash not available on Windows CI")
    def test_bash_paths_use_forward_slashes(self):
        """Test bash script paths use forward slashes."""
        result = run_bash_script("check-prerequisites.sh", ["--json"])
        data = json.loads(result.stdout)
        
        # Check all path fields
        path_fields = ["FEATURE_DIR", "FEATURE_SPEC", "IMPL_PLAN", "TASKS", "REPO_ROOT"]
        for field in path_fields:
            if field in data and data[field]:
                path = data[field]
                if isinstance(path, str):
                    assert '\\' not in path, f"{field} should use forward slashes, got: {path}"
    
    @pytest.mark.skipif(not is_windows(), reason="PowerShell not available on Unix")
    def test_powershell_paths_use_forward_slashes(self):
        """Test PowerShell script paths use forward slashes."""
        result = run_powershell_script("check-prerequisites.ps1", ["-Json"])
        data = json.loads(result.stdout)
        
        # Check all path fields
        path_fields = ["FEATURE_DIR", "FEATURE_SPEC", "IMPL_PLAN", "TASKS", "REPO_ROOT"]
        for field in path_fields:
            if field in data and data[field]:
                path = data[field]
                if isinstance(path, str):
                    assert '\\' not in path, f"{field} should use forward slashes, got: {path}"
