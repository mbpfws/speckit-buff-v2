"""
Test that `specify init` copies all scripts to .specify/scripts/.
Validates script copying functionality and executable permissions.
"""
import pytest
import tempfile
import shutil
from pathlib import Path
from click.testing import CliRunner
from specify_cli.cli import cli


@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory for testing."""
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    # Cleanup
    shutil.rmtree(temp_dir, ignore_errors=True)


def get_repo_root():
    """Get repository root directory."""
    return Path(__file__).parent.parent.parent


class TestInitCopiesScripts:
    """Test script copying during initialization."""
    
    def test_init_creates_scripts_directory(self, temp_project_dir):
        """Test that init creates .specify/scripts/ directory."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            result = runner.invoke(cli, ["init", "--offline"])
            
            assert result.exit_code == 0, f"Init failed: {result.output}"
            
            specify_dir = temp_project_dir / ".specify"
            scripts_dir = specify_dir / "scripts"
            
            assert scripts_dir.exists(), ".specify/scripts/ directory should exist"
            assert (scripts_dir / "bash").exists(), ".specify/scripts/bash/ should exist"
            assert (scripts_dir / "powershell").exists(), ".specify/scripts/powershell/ should exist"
    
    def test_init_copies_bash_scripts(self, temp_project_dir):
        """Test that init copies all bash scripts."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            result = runner.invoke(cli, ["init", "--offline"])
            
            assert result.exit_code == 0, f"Init failed: {result.output}"
            
            bash_dir = temp_project_dir / ".specify" / "scripts" / "bash"
            
            # Expected bash scripts
            expected_scripts = [
                "validate-structure.sh",
                "validate-naming.sh",
                "validate-frontmatter.sh",
                "check-prerequisites.sh",
                "setup-plan.sh",
                "create-new-feature.sh",
                "update-agent-context.sh",
            ]
            
            for script_name in expected_scripts:
                script_path = bash_dir / script_name
                assert script_path.exists(), f"Bash script {script_name} should be copied"
    
    def test_init_copies_powershell_scripts(self, temp_project_dir):
        """Test that init copies all PowerShell scripts."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            result = runner.invoke(cli, ["init", "--offline"])
            
            assert result.exit_code == 0, f"Init failed: {result.output}"
            
            ps_dir = temp_project_dir / ".specify" / "scripts" / "powershell"
            
            # Expected PowerShell scripts
            expected_scripts = [
                "validate-structure.ps1",
                "validate-naming.ps1",
                "validate-frontmatter.ps1",
                "check-prerequisites.ps1",
                "setup-plan.ps1",
                "create-new-feature.ps1",
                "update-agent-context.ps1",
            ]
            
            for script_name in expected_scripts:
                script_path = ps_dir / script_name
                assert script_path.exists(), f"PowerShell script {script_name} should be copied"
    
    def test_bash_scripts_are_executable(self, temp_project_dir):
        """Test that bash scripts have executable permissions."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            result = runner.invoke(cli, ["init", "--offline"])
            
            assert result.exit_code == 0, f"Init failed: {result.output}"
            
            bash_dir = temp_project_dir / ".specify" / "scripts" / "bash"
            
            # Check a few scripts for executable permission
            for script_name in ["validate-structure.sh", "check-prerequisites.sh"]:
                script_path = bash_dir / script_name
                if script_path.exists():
                    # Check if file is executable (Unix-like systems)
                    # On Windows, this check might not be meaningful
                    import os
                    mode = script_path.stat().st_mode
                    # Owner executable permission (0o100)
                    is_executable = bool(mode & 0o100)
                    assert is_executable or os.name == 'nt', f"{script_name} should be executable"
    
    def test_script_count_matches_source(self, temp_project_dir):
        """Test that all source scripts are copied."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            result = runner.invoke(cli, ["init", "--offline"])
            
            assert result.exit_code == 0, f"Init failed: {result.output}"
            
            repo_root = get_repo_root()
            source_bash = repo_root / "scripts" / "bash"
            source_ps = repo_root / "scripts" / "powershell"
            
            dest_bash = temp_project_dir / ".specify" / "scripts" / "bash"
            dest_ps = temp_project_dir / ".specify" / "scripts" / "powershell"
            
            # Count source scripts
            source_bash_count = len(list(source_bash.glob("*.sh")))
            source_ps_count = len(list(source_ps.glob("*.ps1")))
            
            # Count copied scripts
            dest_bash_count = len(list(dest_bash.glob("*.sh")))
            dest_ps_count = len(list(dest_ps.glob("*.ps1")))
            
            assert dest_bash_count == source_bash_count, \
                f"Should copy all bash scripts (expected {source_bash_count}, got {dest_bash_count})"
            assert dest_ps_count == source_ps_count, \
                f"Should copy all PowerShell scripts (expected {source_ps_count}, got {dest_ps_count})"
    
    def test_script_content_preserved(self, temp_project_dir):
        """Test that script content is preserved during copy."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            result = runner.invoke(cli, ["init", "--offline"])
            
            assert result.exit_code == 0, f"Init failed: {result.output}"
            
            repo_root = get_repo_root()
            source_script = repo_root / "scripts" / "bash" / "validate-structure.sh"
            dest_script = temp_project_dir / ".specify" / "scripts" / "bash" / "validate-structure.sh"
            
            if source_script.exists() and dest_script.exists():
                source_content = source_script.read_text()
                dest_content = dest_script.read_text()
                
                assert source_content == dest_content, \
                    "Script content should be identical after copying"
    
    def test_init_with_force_updates_scripts(self, temp_project_dir):
        """Test that init --force updates scripts."""
        runner = CliRunner()
        
        with runner.isolated_filesystem(temp_dir=temp_project_dir):
            # First init
            result1 = runner.invoke(cli, ["init", "--offline"])
            assert result1.exit_code == 0
            
            # Modify a script
            script_path = temp_project_dir / ".specify" / "scripts" / "bash" / "validate-structure.sh"
            script_path.write_text("# Modified")
            
            # Second init with force
            result2 = runner.invoke(cli, ["init", "--force", "--offline"])
            assert result2.exit_code == 0
            
            # Check that script was updated
            content = script_path.read_text()
            assert content != "# Modified", "Script should be updated on --force init"
