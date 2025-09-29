"""
Contract tests for Governance System API
Tests MUST fail before implementation (TDD approach)
"""

import pytest
import json
from httpx import AsyncClient


@pytest.mark.contract
class TestGovernanceSystemAPI:
    """Contract tests for Governance System API endpoints"""

    @pytest.mark.asyncio
    async def test_create_artifact_success(self):
        """Test successful artifact creation"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "artifact_type": "spec",
                "artifact_name": "test-spec",
                "content": "# Test Specification\nThis is a test spec.",
                "parent_artifact": None,
                "platform_specific": False,
                "metadata": {
                    "version": "1.0",
                    "author": "test-user"
                }
            }

            response = await client.post("/governance/artifact", json=request_data)

            # This should fail initially - implementation doesn't exist
            assert response.status_code == 201

            data = response.json()
            assert "artifact_id" in data
            assert "relationship_id" in data
            assert "file_path" in data
            assert "validation_results" in data
            assert isinstance(data["validation_results"], list)

    @pytest.mark.asyncio
    async def test_create_artifact_invalid_data(self):
        """Test artifact creation with invalid data"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Missing required fields
            request_data = {
                "artifact_type": "spec"
                # Missing artifact_name and content
            }

            response = await client.post("/governance/artifact", json=request_data)

            # Should return 400 for invalid request
            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_artifact_invalid_type(self):
        """Test artifact creation with invalid type"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "artifact_type": "invalid_type",
                "artifact_name": "test",
                "content": "test content"
            }

            response = await client.post("/governance/artifact", json=request_data)

            # Should return 400 for invalid artifact type
            assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_synchronize_artifacts_success(self):
        """Test successful artifact synchronization"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "source_artifact": "artifact-123",
                "target_platforms": ["claude", "copilot", "gemini"],
                "sync_strategy": "incremental"
            }

            response = await client.post("/governance/synchronize", json=request_data)

            # This should fail initially - implementation doesn't exist
            assert response.status_code == 200

            data = response.json()
            assert "synchronized_platforms" in data
            assert "failed_platforms" in data
            assert "sync_details" in data
            assert isinstance(data["synchronized_platforms"], list)
            assert isinstance(data["failed_platforms"], list)

    @pytest.mark.asyncio
    async def test_synchronize_full_sync(self):
        """Test full synchronization strategy"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "source_artifact": "artifact-456",
                "target_platforms": ["claude", "roo"],
                "sync_strategy": "full"
            }

            response = await client.post("/governance/synchronize", json=request_data)

            assert response.status_code == 200
            data = response.json()
            assert len(data["synchronized_platforms"]) <= 2  # Max 2 platforms requested

    @pytest.mark.asyncio
    async def test_validate_artifact_success(self):
        """Test successful artifact validation"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "artifact_id": "artifact-789",
                "validation_rules": ["naming", "structure", "content"],
                "strict_mode": False
            }

            response = await client.post("/governance/validate", json=request_data)

            # This should fail initially - implementation doesn't exist
            assert response.status_code == 200

            data = response.json()
            assert "is_valid" in data
            assert "violations" in data
            assert "recommendations" in data
            assert isinstance(data["violations"], list)
            assert isinstance(data["recommendations"], list)

            # Check violation structure if any exist
            if data["violations"]:
                violation = data["violations"][0]
                assert "rule" in violation
                assert "message" in violation
                assert "severity" in violation
                assert violation["severity"] in ["error", "warning", "info"]

    @pytest.mark.asyncio
    async def test_validate_artifact_strict_mode(self):
        """Test artifact validation in strict mode"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "artifact_id": "artifact-strict",
                "validation_rules": ["naming"],
                "strict_mode": True
            }

            response = await client.post("/governance/validate", json=request_data)

            assert response.status_code == 200
            data = response.json()
            assert "is_valid" in data

    @pytest.mark.asyncio
    async def test_validate_all_rules(self):
        """Test validation with all possible rules"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "artifact_id": "artifact-comprehensive",
                "validation_rules": ["naming", "structure", "content", "relationships", "platform_compatibility"]
            }

            response = await client.post("/governance/validate", json=request_data)

            assert response.status_code == 200
            data = response.json()
            assert len(data["violations"]) >= 0  # Should not fail for requesting all rules

    @pytest.mark.asyncio
    async def test_create_platform_specific_artifact(self):
        """Test creating platform-specific artifact"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            request_data = {
                "artifact_type": "task",
                "artifact_name": "claude-specific-task",
                "content": "Platform specific task",
                "platform_specific": True,
                "metadata": {
                    "platform": "claude"
                }
            }

            response = await client.post("/governance/artifact", json=request_data)

            assert response.status_code == 201
            data = response.json()
            assert data["artifact_id"] is not None