"""
Integration tests for artifact synchronization functionality
Tests MUST fail before implementation (TDD approach)
"""

import pytest
import json
import asyncio
from datetime import datetime
from httpx import AsyncClient


@pytest.mark.integration
class TestArtifactSynchronization:
    """Integration tests for artifact synchronization across platforms"""

    @pytest.mark.asyncio
    async def test_create_and_sync_artifact_workflow(self):
        """Test complete workflow: create artifact and sync across platforms"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Step 1: Create a specification artifact
            spec_request = {
                "artifact_type": "spec",
                "artifact_name": "user-authentication-spec",
                "content": """# User Authentication Specification

## Requirements
- Users must be able to register with email/password
- Support OAuth2 integration
- Implement JWT tokens
- Password strength validation

## API Endpoints
- POST /api/auth/register
- POST /api/auth/login
- POST /api/auth/refresh
- POST /api/auth/logout

## Security Considerations
- Rate limiting on auth endpoints
- Password hashing with bcrypt
- CSRF protection
""",
                "metadata": {
                    "version": "1.0",
                    "author": "spec-kit",
                    "created": datetime.now().isoformat(),
                    "tags": ["authentication", "security", "api"]
                }
            }

            create_response = await client.post("/governance/artifact", json=spec_request)
            assert create_response.status_code == 201

            artifact_data = create_response.json()
            artifact_id = artifact_data["artifact_id"]

            # Step 2: Synchronize to multiple platforms
            sync_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["claude", "copilot", "gemini", "roo"],
                "sync_strategy": "incremental"
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200

            sync_data = sync_response.json()
            assert len(sync_data["synchronized_platforms"]) > 0
            assert isinstance(sync_data["sync_details"], dict)

    @pytest.mark.asyncio
    async def test_hierarchical_artifact_sync(self):
        """Test synchronization of hierarchical artifacts (parent-child relationships)"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create parent artifact
            parent_request = {
                "artifact_type": "spec",
                "artifact_name": "project-overview",
                "content": "# Project Overview\nHigh-level project requirements."
            }

            parent_response = await client.post("/governance/artifact", json=parent_request)
            assert parent_response.status_code == 201

            parent_data = parent_response.json()
            parent_id = parent_data["artifact_id"]

            # Create child artifacts
            child_artifacts = []
            for i in range(3):
                child_request = {
                    "artifact_type": "task",
                    "artifact_name": f"task-{i+1}",
                    "content": f"# Task {i+1}\nImplementation details for task {i+1}.",
                    "parent_artifact": parent_id
                }

                child_response = await client.post("/governance/artifact", json=child_request)
                assert child_response.status_code == 201

                child_data = child_response.json()
                child_artifacts.append(child_data["artifact_id"])

            # Sync parent and verify children are included
            sync_request = {
                "source_artifact": parent_id,
                "target_platforms": ["claude", "roo"],
                "sync_strategy": "full"
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200

            sync_data = sync_response.json()
            assert "relationship_hierarchy" in sync_data["sync_details"]

    @pytest.mark.asyncio
    async def test_cross_artifact_type_sync(self):
        """Test synchronization between different artifact types"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create related artifacts of different types
            artifacts = []

            # Specification
            spec_request = {
                "artifact_type": "spec",
                "artifact_name": "payment-gateway-spec",
                "content": "# Payment Gateway Specification\nRequirements for payment integration."
            }

            spec_response = await client.post("/governance/artifact", json=spec_request)
            artifacts.append(spec_response.json()["artifact_id"])

            # Plan
            plan_request = {
                "artifact_type": "plan",
                "artifact_name": "payment-gateway-plan",
                "content": "# Implementation Plan\nStep-by-step implementation guide.",
                "parent_artifact": artifacts[0]
            }

            plan_response = await client.post("/governance/artifact", json=plan_request)
            artifacts.append(plan_response.json()["artifact_id"])

            # Tasks
            for i, task in enumerate(["backend", "frontend", "testing"]):
                task_request = {
                    "artifact_type": "task",
                    "artifact_name": f"implement-{task}",
                    "content": f"# Implement {task}\nDetailed implementation steps.",
                    "parent_artifact": artifacts[1]
                }

                task_response = await client.post("/governance/artifact", json=task_request)
                artifacts.append(task_response.json()["artifact_id"])

            # Sync the entire hierarchy
            sync_request = {
                "source_artifact": artifacts[0],  # Sync from spec
                "target_platforms": ["claude", "copilot", "gemini", "cursor"],
                "sync_strategy": "selective"
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200

            sync_data = sync_response.json()
            # Should sync related artifacts
            assert "related_artifacts" in sync_data["sync_details"]
            assert len(sync_data["sync_details"]["related_artifacts"]) > 0

    @pytest.mark.asyncio
    async def test_sync_conflict_resolution(self):
        """Test synchronization conflict detection and resolution"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create initial artifact
            request = {
                "artifact_type": "spec",
                "artifact_name": "api-design",
                "content": "# API Design\nInitial API design document."
            }

            response = await client.post("/governance/artifact", json=request)
            assert response.status_code == 201

            artifact_data = response.json()
            artifact_id = artifact_data["artifact_id"]

            # Simulate sync conflicts by trying to sync to platforms
            # with potentially conflicting versions
            sync_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["claude", "roo"],
                "sync_strategy": "incremental"
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200

            sync_data = sync_response.json()
            # Should handle conflicts gracefully
            if "conflicts" in sync_data["sync_details"]:
                assert "resolution_strategy" in sync_data["sync_details"]

    @pytest.mark.asyncio
    async def test_real_time_sync_notification(self):
        """Test real-time synchronization notifications"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create artifact
            request = {
                "artifact_type": "research",
                "artifact_name": "tech-stack-research",
                "content": "# Tech Stack Research\nResearch findings on technology choices."
            }

            response = await client.post("/governance/artifact", json=request)
            assert response.status_code == 201

            artifact_data = response.json()
            artifact_id = artifact_data["artifact_id"]

            # Sync with notification
            sync_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["claude", "copilot"],
                "sync_strategy": "incremental",
                "notify_on_complete": True
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200

            sync_data = sync_response.json()
            # Should include notification information
            if "notifications" in sync_data:
                assert isinstance(sync_data["notifications"], list)

    @pytest.mark.asyncio
    async def test_sync_performance_metrics(self):
        """Test synchronization performance metrics collection"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create large artifact to test performance
            large_content = "# Large Specification\n" + "\n".join([f"Section {i}: Content" for i in range(100)])

            request = {
                "artifact_type": "spec",
                "artifact_name": "large-spec",
                "content": large_content
            }

            response = await client.post("/governance/artifact", json=request)
            assert response.status_code == 201

            artifact_data = response.json()
            artifact_id = artifact_data["artifact_id"]

            # Sync and measure performance
            sync_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["claude", "roo", "gemini"],
                "sync_strategy": "full",
                "collect_metrics": True
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200

            sync_data = sync_response.json()
            # Should include performance metrics
            if "performance_metrics" in sync_data:
                metrics = sync_data["performance_metrics"]
                assert "sync_duration" in metrics
                assert "data_transfer_size" in metrics
                assert isinstance(metrics["sync_duration"], (int, float))

    @pytest.mark.asyncio
    async def test_incremental_vs_full_sync(self):
        """Test difference between incremental and full synchronization"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create artifact
            request = {
                "artifact_type": "plan",
                "artifact_name": "migration-plan",
                "content": "# Migration Plan\nInitial migration strategy."
            }

            response = await client.post("/governance/artifact", json=request)
            assert response.status_code == 201

            artifact_data = response.json()
            artifact_id = artifact_data["artifact_id"]

            # Test incremental sync
            incremental_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["claude"],
                "sync_strategy": "incremental"
            }

            incremental_response = await client.post("/governance/synchronize", json=incremental_request)
            assert incremental_response.status_code == 200

            # Test full sync
            full_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["roo"],
                "sync_strategy": "full"
            }

            full_response = await client.post("/governance/synchronize", json=full_request)
            assert full_response.status_code == 200

            # Compare sync details
            incremental_data = incremental_response.json()
            full_data = full_response.json()

            assert "sync_details" in incremental_data
            assert "sync_details" in full_data

            # Full sync should include more comprehensive information
            if "sync_completeness" in full_data["sync_details"]:
                assert full_data["sync_details"]["sync_completeness"] == 1.0

    @pytest.mark.asyncio
    async def test_sync_error_recovery(self):
        """Test synchronization error handling and recovery"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Create artifact
            request = {
                "artifact_type": "data_model",
                "artifact_name": "user-model",
                "content": "# User Data Model\nDatabase schema definition."
            }

            response = await client.post("/governance/artifact", json=request)
            assert response.status_code == 201

            artifact_data = response.json()
            artifact_id = artifact_data["artifact_id"]

            # Attempt sync with invalid platform
            sync_request = {
                "source_artifact": artifact_id,
                "target_platforms": ["claude", "invalid_platform"],
                "sync_strategy": "incremental"
            }

            sync_response = await client.post("/governance/synchronize", json=sync_request)
            assert sync_response.status_code == 200  # Should partially succeed

            sync_data = sync_response.json()
            # Should report failed platforms
            assert "failed_platforms" in sync_data
            assert len(sync_data["failed_platforms"]) > 0

            # Should still succeed for valid platforms
            assert len(sync_data["synchronized_platforms"]) > 0