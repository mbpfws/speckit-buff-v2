"""
Contract tests for Project Analyzer API
Tests MUST fail before implementation (TDD approach)
"""

import pytest
import json
from httpx import AsyncClient


@pytest.mark.contract
class TestProjectAnalyzerAPI:
    """Contract tests for Project Analyzer API endpoints"""

    @pytest.mark.asyncio
    async def test_analyze_project_endpoint_success(self):
        """Test successful project analysis"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "project_path": "/test/project",
                "analysis_depth": "standard",
                "include_dependencies": True,
                "detect_frameworks": True
            }

            response = await client.post("/analyze/project", json=request_data)

            # This should fail initially - implementation doesn't exist
            assert response.status_code == 200

            data = response.json()
            assert "project_type" in data
            assert data["project_type"] in ["greenfield", "brownfield", "ongoing", "prototype"]
            assert "architecture_patterns" in data
            assert "tech_stack" in data
            assert "complexity_score" in data
            assert 1 <= data["complexity_score"] <= 10

    @pytest.mark.asyncio
    async def test_analyze_project_endpoint_invalid_path(self):
        """Test project analysis with invalid path"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "project_path": "",
                "analysis_depth": "standard"
            }

            response = await client.post("/analyze/project", json=request_data)

            # Should return 400 for invalid request
            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_analyze_architecture_endpoint_success(self):
        """Test successful architecture analysis"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # First get project analysis
            project_analysis = {
                "project_type": "brownfield",
                "architecture_patterns": ["mvc", "microservices"],
                "tech_stack": {
                    "languages": ["python", "javascript"],
                    "frameworks": ["django", "react"],
                    "databases": ["postgresql"]
                },
                "dependencies": {},
                "complexity_score": 7,
                "recommendations": []
            }

            request_data = {
                "project_analysis": project_analysis,
                "framework_specific": True
            }

            response = await client.post("/analyze/architecture", json=request_data)

            # This should fail initially - implementation doesn't exist
            assert response.status_code == 200

            data = response.json()
            assert "framework_patterns" in data
            assert "folder_structures" in data
            assert "code_standards" in data
            assert "integration_patterns" in data
            assert "performance_guidelines" in data

    @pytest.mark.asyncio
    async def test_analyze_project_quick_analysis(self):
        """Test quick analysis mode"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "project_path": "/test/project",
                "analysis_depth": "quick"
            }

            response = await client.post("/analyze/project", json=request_data)

            assert response.status_code == 200
            data = response.json()
            assert data["project_type"] is not None

    @pytest.mark.asyncio
    async def test_analyze_project_deep_analysis(self):
        """Test deep analysis mode"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "project_path": "/test/project",
                "analysis_depth": "deep",
                "include_dependencies": True,
                "detect_frameworks": True
            }

            response = await client.post("/analyze/project", json=request_data)

            assert response.status_code == 200
            data = response.json()
            assert "dependencies" in data
            assert len(data["architecture_patterns"]) > 0

    @pytest.mark.asyncio
    async def test_endpoint_not_found(self):
        """Test non-existent endpoint returns 404"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            response = await client.post("/analyze/nonexistent", json={})
            assert response.status_code == 404