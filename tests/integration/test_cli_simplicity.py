"""
Integration test: CLI simplicity verification (Scenario 7).

Based on: quickstart.md Scenario 7

Verifies CLI is under 400 LOC with minimal complexity.
"""
from pathlib import Path

import pytest


class TestCLISimplicity:
    """Test CLI simplicity requirements."""
    
    def test_total_loc_under_400(self):
        """Total CLI code must be <400 LOC."""
        from tests.helpers import count_loc
        
        cli_dir = Path(__file__).parent.parent.parent / "specify-cli"
        
        if not cli_dir.exists():
            pytest.skip("CLI directory not found")
        
        files_to_count = [
            cli_dir / "cli.py",
            cli_dir / "commands" / "init.py",
            cli_dir / "commands" / "check.py",
            cli_dir / "template_loader.py",
            cli_dir / "validators.py",
        ]
        
        total_loc = 0
        for file_path in files_to_count:
            if file_path.exists():
                loc = count_loc(file_path, exclude_comments=True, exclude_blank=True)
                total_loc += loc
                print(f"{file_path.name}: {loc} LOC")
        
        print(f"Total: {total_loc} LOC")
        
        assert total_loc < 400, f"CLI has {total_loc} LOC, target is <400"
    
    def test_no_analysis_engines(self):
        """Verify no complex analysis engines present."""
        cli_dir = Path(__file__).parent.parent.parent / "specify-cli"
        
        if not cli_dir.exists():
            pytest.skip("CLI directory not found")
        
        # Search for prohibited patterns
        forbidden_patterns = [
            'brownfield_analyzer',
            'pattern_detector',
            'best_practices_engine',
            'deep_scanner'
        ]
        
        for py_file in cli_dir.rglob("*.py"):
            if "__pycache__" in str(py_file):
                continue
            
            content = py_file.read_text().lower()
            for pattern in forbidden_patterns:
                assert pattern not in content, \
                    f"Found forbidden pattern '{pattern}' in {py_file.name}"
    
    def test_minimal_dependencies(self):
        """Verify only 4 dependencies: stdlib, requests, PyYAML, click."""
        import sys
        from pathlib import Path
        
        # Read pyproject.toml
        pyproject = Path(__file__).parent.parent.parent / "pyproject.toml"
        
        if not pyproject.exists():
            pytest.skip("pyproject.toml not found")
        
        content = pyproject.read_text()
        
        # Check for essential dependencies
        assert "click" in content.lower()
        assert "requests" in content.lower()
        assert "pyyaml" in content.lower() or "yaml" in content.lower()
        
        # Verify not using heavy dependencies
        heavy_deps = ['tensorflow', 'torch', 'transformers', 'langchain']
        for dep in heavy_deps:
            assert dep not in content.lower(), \
                f"Heavy dependency '{dep}' found - violates simplicity principle"
    
    def test_low_cyclomatic_complexity(self):
        """Verify low cyclomatic complexity (optional - requires radon)."""
        try:
            import radon.complexity as radon_cc
        except ImportError:
            pytest.skip("radon not installed")
        
        cli_dir = Path(__file__).parent.parent.parent / "specify-cli"
        
        if not cli_dir.exists():
            pytest.skip("CLI directory not found")
        
        for py_file in cli_dir.rglob("*.py"):
            if "__pycache__" in str(py_file) or "__init__" in str(py_file):
                continue
            
            with open(py_file) as f:
                code = f.read()
            
            results = radon_cc.cc_visit(code)
            
            for result in results:
                # Complexity should be reasonable (<10 is good, <5 is excellent)
                assert result.complexity < 10, \
                    f"High complexity ({result.complexity}) in {py_file.name}:{result.name}"
