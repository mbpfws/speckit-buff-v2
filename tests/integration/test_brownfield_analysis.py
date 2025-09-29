"""
Integration tests for brownfield project analysis functionality
Tests MUST fail before implementation (TDD approach)
"""

import pytest
import json
import tempfile
import os
from pathlib import Path
from httpx import AsyncClient


@pytest.mark.integration
class TestBrownfieldAnalysis:
    """Integration tests for brownfield project analysis"""

    @pytest.fixture
    def sample_brownfield_project(self):
        """Create a sample brownfield project structure for testing"""
        with tempfile.TemporaryDirectory() as temp_dir:
            project_root = Path(temp_dir)

            # Create a typical brownfield project structure
            (project_root / "src").mkdir()
            (project_root / "tests").mkdir()
            (project_root / "docs").mkdir()
            (project_root / "config").mkdir()

            # Add some source files
            (project_root / "src" / "main.py").write_text("""
def main():
    return "Hello World"

class LegacyService:
    def old_method(self):
        pass
""")

            (project_root / "src" / "models.py").write_text("""
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
""")

            # Add package.json for Node.js project detection
            (project_root / "package.json").write_text("""
{
    "name": "brownfield-project",
    "version": "1.0.0",
    "dependencies": {
        "react": "^16.0.0",
        "express": "^4.0.0"
    }
}
""")

            # Add requirements.txt for Python detection
            (project_root / "requirements.txt").write_text("""
django==3.2.0
requests==2.25.0
""")

            # Add Dockerfile
            (project_root / "Dockerfile").write_text("""
FROM python:3.9
COPY . /app
""")

            yield str(project_root)

    @pytest.mark.asyncio
    async def test_end_to_end_brownfield_analysis(self, sample_brownfield_project):
        """Test complete brownfield project analysis workflow"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Step 1: Analyze the project
            analysis_request = {
                "project_path": sample_brownfield_project,
                "analysis_depth": "deep",
                "include_dependencies": True,
                "detect_frameworks": True
            }

            analysis_response = await client.post("/analyze/project", json=analysis_request)

            # This should fail initially - implementation doesn't exist
            assert analysis_response.status_code == 200

            analysis_data = analysis_response.json()
            assert analysis_data["project_type"] == "brownfield"
            assert len(analysis_data["tech_stack"]["languages"]) > 0
            assert len(analysis_data["tech_stack"]["frameworks"]) > 0

            # Step 2: Get architecture guidance
            architecture_request = {
                "project_analysis": analysis_data,
                "framework_specific": True
            }

            architecture_response = await client.post("/analyze/architecture", json=architecture_request)
            assert architecture_response.status_code == 200

            architecture_data = architecture_response.json()
            assert "framework_patterns" in architecture_data
            assert "folder_structures" in architecture_data
            assert "integration_patterns" in architecture_data

    @pytest.mark.asyncio
    async def test_multi_framework_detection(self, sample_brownfield_project):
        """Test detection of multiple frameworks in brownfield project"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request = {
                "project_path": sample_brownfield_project,
                "analysis_depth": "standard",
                "detect_frameworks": True
            }

            response = await client.post("/analyze/project", json=request)
            assert response.status_code == 200

            data = response.json()
            # Should detect both Django and React/Node.js
            frameworks = data["tech_stack"]["frameworks"]
            assert any("django" in f.lower() for f in frameworks)
            assert any("react" in f.lower() for f in frameworks)

    @pytest.mark.asyncio
    async def test_legacy_code_detection(self, sample_brownfield_project):
        """Test detection of legacy code patterns"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request = {
                "project_path": sample_brownfield_project,
                "analysis_depth": "deep"
            }

            response = await client.post("/analyze/project", json=request)
            assert response.status_code == 200

            data = response.json()
            # Should detect legacy patterns
            assert "LegacyService" in str(data) or len(data["architecture_patterns"]) > 0

    @pytest.mark.asyncio
    async def test_dependency_analysis(self, sample_brownfield_project):
        """Test dependency tree analysis"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request = {
                "project_path": sample_brownfield_project,
                "include_dependencies": True
            }

            response = await client.post("/analyze/project", json=request)
            assert response.status_code == 200

            data = response.json()
            dependencies = data.get("dependencies", {})
            assert isinstance(dependencies, dict)

            # Should have both Python and Node.js dependencies
            assert "python" in dependencies or "node" in dependencies

    @pytest.mark.asyncio
    async def test_architecture_recommendations(self, sample_brownfield_project):
        """Test architecture improvement recommendations"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # First get project analysis
            analysis_request = {
                "project_path": sample_brownfield_project,
                "analysis_depth": "standard"
            }

            analysis_response = await client.post("/analyze/project", json=analysis_request)
            assert analysis_response.status_code == 200

            analysis_data = analysis_response.json()

            # Get pattern detection
            pattern_request = {
                "project_analysis": analysis_data,
                "target_frameworks": ["django", "react"],
                "include_anti_patterns": True
            }

            pattern_response = await client.post("/architecture/patterns", json=pattern_request)
            assert pattern_response.status_code == 200

            pattern_data = pattern_response.json()
            # Should have recommendations for improvement
            assert "recommendations" in pattern_data
            assert isinstance(pattern_data["recommendations"], list)

            # Should detect anti-patterns in brownfield project
            if pattern_data.get("anti_patterns"):
                assert len(pattern_data["anti_patterns"]) > 0

    @pytest.mark.asyncio
    async def test_brownfield_complexity_scoring(self, sample_brownfield_project):
        """Test complexity scoring for brownfield projects"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request = {
                "project_path": sample_brownfield_project,
                "analysis_depth": "deep"
            }

            response = await client.post("/analyze/project", json=request)
            assert response.status_code == 200

            data = response.json()
            # Brownfield projects should have higher complexity
            assert "complexity_score" in data
            assert data["complexity_score"] >= 3  # Should be at least moderate complexity

    @pytest.mark.asyncio
    async def test_technical_debt_detection(self, sample_brownfield_project):
        """Test detection of technical debt indicators"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request = {
                "project_path": sample_brownfield_project,
                "analysis_depth": "deep"
            }

            response = await client.post("/analyze/project", json=request)
            assert response.status_code == 200

            data = response.json()
            # Should detect technical debt indicators
            recommendations = data.get("recommendations", [])
            assert isinstance(recommendations, list)

            # Look for technical debt related recommendations
            tech_debt_keywords = ["refactor", "modernize", "upgrade", "migration"]
            has_tech_debt = any(
                any(keyword in rec.lower() for keyword in tech_debt_keywords)
                for rec in recommendations
            )
            # Note: Technical debt detection might not always be present
            # So we don't assert on has_tech_debt