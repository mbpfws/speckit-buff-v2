"""
Validation tests for multi-cycle agent analysis functionality
Tests MUST fail before implementation (TDD approach)
"""

import pytest
import json
import asyncio
from httpx import AsyncClient


@pytest.mark.integration
class TestMultiCycleAnalysis:
    """Validation tests for multi-cycle agent analysis workflows"""

    @pytest.mark.asyncio
    async def test_multi_cycle_analysis_workflow(self):
        """Test complete multi-cycle analysis workflow"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Initialize multi-cycle analysis
            init_request = {
                "action": "initialize_multi_cycle",
                "project_context": {
                    "project_type": "brownfield",
                    "technologies": ["python", "django", "react"],
                    "complexity": "high"
                },
                "analysis_goals": [
                    "identify_technical_debt",
                    "suggest_improvements",
                    "create_migration_plan"
                ],
                "max_cycles": 3,
                "convergence_threshold": 0.9
            }

            init_response = await client.post("/analysis/multi_cycle/init", json=init_request)
            assert init_response.status_code == 200

            init_data = init_response.json()
            assert "analysis_session_id" in init_data
            assert "cycle_plan" in init_data

            session_id = init_data["analysis_session_id"]

            # Execute first analysis cycle
            cycle1_request = {
                "session_id": session_id,
                "cycle_number": 1,
                "focus_areas": ["code_quality", "architecture"],
                "mcp_servers": ["tavily", "context7"]
            }

            cycle1_response = await client.post("/analysis/multi_cycle/execute", json=cycle1_request)
            assert cycle1_response.status_code == 200

            cycle1_data = cycle1_response.json()
            assert "findings" in cycle1_data
            assert "insights" in cycle1_data
            assert "next_actions" in cycle1_data

            # Execute second cycle based on first cycle results
            cycle2_request = {
                "session_id": session_id,
                "cycle_number": 2,
                "previous_findings": cycle1_data["findings"],
                "refinement_questions": cycle1_data["next_actions"]["questions"],
                "mcp_servers": ["deepwiki", "fetch"]
            }

            cycle2_response = await client.post("/analysis/multi_cycle/execute", json=cycle2_request)
            assert cycle2_response.status_code == 200

            cycle2_data = cycle2_response.json()
            assert "refined_insights" in cycle2_data
            assert "convergence_metrics" in cycle2_data

            # Check for convergence
            if cycle2_data["convergence_metrics"]["convergence_score"] < init_request["convergence_threshold"]:
                # Execute third cycle if needed
                cycle3_request = {
                    "session_id": session_id,
                    "cycle_number": 3,
                    "focus_areas": cycle2_data["convergence_metrics"]["areas_needing_improvement"]
                }

                cycle3_response = await client.post("/analysis/multi_cycle/execute", json=cycle3_request)
                assert cycle3_response.status_code == 200

            # Finalize analysis
            finalize_request = {
                "session_id": session_id,
                "compile_final_report": True,
                "include_recommendations": True
            }

            finalize_response = await client.post("/analysis/multi_cycle/finalize", json=finalize_request)
            assert finalize_response.status_code == 200

            final_data = finalize_response.json()
            assert "final_analysis" in final_data
            assert "executive_summary" in final_data
            assert "implementation_plan" in final_data

    @pytest.mark.asyncio
    async def test_self_correction_mechanism(self):
        """Test agent self-correction during multi-cycle analysis"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Start analysis with known issues
            request = {
                "action": "self_correcting_analysis",
                "initial_analysis": {
                    "project_type": "monolithic",
                    "technologies": ["legacy_system"],
                    "identified_issues": ["scalability", "maintainability"]
                },
                "correction_triggers": [
                    "incomplete_dependency_analysis",
                    "missing_performance_considerations",
                    "inadequate_security_review"
                ]
            }

            response = await client.post("/analysis/self_correction/start", json=request)
            assert response.status_code == 200

            data = response.json()
            assert "correction_session_id" in data
            assert "initial_confidence" in data

            # Simulate detection of correction need
            correction_request = {
                "session_id": data["correction_session_id"],
                "detected_issue": "incomplete_dependency_analysis",
                "context": {
                    "missing_dependencies": ["database_connections", "external_apis"],
                    "impact_analysis": "high"
                }
            }

            correction_response = await client.post("/analysis/self_correction/correct", json=correction_request)
            assert correction_response.status_code == 200

            correction_data = correction_response.json()
            assert "corrected_analysis" in correction_data
            assert "improvements_made" in correction_data
            assert "confidence_improvement" in correction_data

    @pytest.mark.asyncio
    async def test_iterative_refinement_loop(self):
        """Test iterative refinement of analysis results"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Initial analysis
            initial_request = {
                "project_path": "/test/project",
                "analysis_type": "architecture",
                "initial_questions": [
                    "What is the current architecture pattern?",
                    "Are there any anti-patterns present?"
                ]
            }

            initial_response = await client.post("/analysis/iterative/start", json=initial_request)
            assert initial_response.status_code == 200

            initial_data = initial_response.json()
            session_id = initial_data["session_id"]

            # Multiple refinement iterations
            refinements = [
                {
                    "iteration": 1,
                    "focus": "performance_implications",
                    "new_insights": "Database queries need optimization"
                },
                {
                    "iteration": 2,
                    "focus": "scalability_concerns",
                    "new_insights": "Current architecture won't scale beyond 1000 users"
                },
                {
                    "iteration": 3,
                    "focus": "migration_path",
                    "new_insights": "Microservices migration recommended in phases"
                }
            ]

            for refinement in refinements:
                refine_request = {
                    "session_id": session_id,
                    "iteration": refinement["iteration"],
                    "focus_area": refinement["focus"],
                    "insight": refinement["new_insights"]
                }

                refine_response = await client.post("/analysis/iterative/refine", json=refine_request)
                assert refine_response.status_code == 200

                refine_data = refine_response.json()
                assert "updated_analysis" in refine_data
                assert "new_questions_generated" in refine_data

            # Final refined analysis
            final_request = {
                "session_id": session_id,
                "compile_comprehensive_report": True
            }

            final_response = await client.post("/analysis/iterative/finalize", json=final_request)
            assert final_response.status_code == 200

            final_data = final_response.json()
            assert "refined_analysis" in final_data
            assert "iteration_history" in final_data
            assert "confidence_evolution" in final_data

    @pytest.mark.asyncio
    async def test_cross_cycle_learning(self):
        """Test knowledge transfer between analysis cycles"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Start learning-enabled analysis
            learning_request = {
                "action": "learning_analysis",
                "project_domain": "e-commerce",
                "enable_cross_cycle_learning": True,
                "knowledge_base": {
                    "previous_analyses": [],
                    "learned_patterns": [],
                    "domain_expertise": {}
                }
            }

            learning_response = await client.post("/analysis/learning/start", json=learning_request)
            assert learning_response.status_code == 200

            learning_data = learning_response.json()
            learning_session_id = learning_data["session_id"]

            # Execute multiple analysis cycles
            cycles = [
                {
                    "cycle": 1,
                    "analysis_type": "technical_debt",
                    "findings": ["high coupling", "lack of tests"]
                },
                {
                    "cycle": 2,
                    "analysis_type": "architecture",
                    "findings": ["monolithic structure", "scaling issues"]
                },
                {
                    "cycle": 3,
                    "analysis_type": "performance",
                    "findings": ["slow queries", "memory leaks"]
                }
            ]

            learned_patterns = []

            for cycle in cycles:
                cycle_request = {
                    "session_id": learning_session_id,
                    "cycle": cycle["cycle"],
                    "analysis_type": cycle["analysis_type"],
                    "findings": cycle["findings"],
                    "extract_patterns": True
                }

                cycle_response = await client.post("/analysis/learning/cycle", json=cycle_request)
                assert cycle_response.status_code == 200

                cycle_data = cycle_response.json()
                if "learned_patterns" in cycle_data:
                    learned_patterns.extend(cycle_data["learned_patterns"])

            # Verify knowledge accumulation
            knowledge_request = {
                "session_id": learning_session_id,
                "action": "extract_knowledge"
            }

            knowledge_response = await client.post("/analysis/learning/knowledge", json=knowledge_request)
            assert knowledge_response.status_code == 200

            knowledge_data = knowledge_response.json()
            assert "accumulated_knowledge" in knowledge_data
            assert "pattern_recognition" in knowledge_data
            assert len(knowledge_data["learned_insights"]) > 0

    @pytest.mark.asyncio
    async def test_convergence_detection(self):
        """Test automatic detection of analysis convergence"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Start convergence-monitored analysis
            convergence_request = {
                "action": "convergence_analysis",
                "initial_hypothesis": "Project needs microservices migration",
                "convergence_criteria": {
                    "confidence_threshold": 0.85,
                    "stability_cycles": 2,
                    "max_iterations": 5
                }
            }

            convergence_response = await client.post("/analysis/convergence/start", json=convergence_request)
            assert convergence_response.status_code == 200

            convergence_data = convergence_response.json()
            session_id = convergence_data["session_id"]

            # Simulate analysis iterations
            iterations = [
                {
                    "iteration": 1,
                    "confidence": 0.6,
                    "insights": ["Initial assessment suggests migration benefits"]
                },
                {
                    "iteration": 2,
                    "confidence": 0.75,
                    "insights": ["Migration complexity identified", "ROI calculated"]
                },
                {
                    "iteration": 3,
                    "confidence": 0.88,
                    "insights": ["Detailed migration plan created", "Risks assessed"]
                }
            ]

            converged = False

            for iteration in iterations:
                iter_request = {
                    "session_id": session_id,
                    "iteration": iteration["iteration"],
                    "confidence_score": iteration["confidence"],
                    "new_insights": iteration["insights"]
                }

                iter_response = await client.post("/analysis/convergence/iterate", json=iter_request)
                assert iter_response.status_code == 200

                iter_data = iter_response.json()
                if iter_data.get("converged", False):
                    converged = True
                    break

            # Check final convergence status
            final_request = {
                "session_id": session_id,
                "action": "check_convergence"
            }

            final_response = await client.post("/analysis/convergence/check", json=final_request)
            assert final_response.status_code == 200

            final_data = final_response.json()
            assert "converged" in final_data
            assert "final_confidence" in final_data
            assert "convergence_path" in final_data

    @pytest.mark.asyncio
    async def test_multi_agent_coordination(self):
        """Test coordination between multiple specialized analysis agents"""
        async with AsyncClient(base_url="http://localhost:8000/api/v1") as client:
            # Initialize multi-agent analysis
            coord_request = {
                "action": "multi_agent_analysis",
                "agents": [
                    {"type": "architecture_expert", "focus": "system_design"},
                    {"type": "security_analyst", "focus": "vulnerabilities"},
                    {"type": "performance_engineer", "focus": "optimization"},
                    {"type": "domain_expert", "focus": "business_requirements"}
                ],
                "coordination_strategy": "sequential_with_feedback"
            }

            coord_response = await client.post("/analysis/multi_agent/start", json=coord_request)
            assert coord_response.status_code == 200

            coord_data = coord_response.json()
            session_id = coord_data["session_id"]

            # Execute agent analyses
            agent_results = {}

            agents = ["architecture_expert", "security_analyst", "performance_engineer", "domain_expert"]

            for i, agent in enumerate(agents):
                agent_request = {
                    "session_id": session_id,
                    "agent_type": agent,
                    "previous_agent_results": agent_results if i > 0 else None,
                    "analysis_context": {
                        "project_phase": "analysis",
                        "current_focus": agent
                    }
                }

                agent_response = await client.post("/analysis/multi_agent/execute", json=agent_request)
                assert agent_response.status_code == 200

                agent_data = agent_response.json()
                agent_results[agent] = agent_data

                # Check for agent coordination
                if "coordination_messages" in agent_data:
                    assert isinstance(agent_data["coordination_messages"], list)

            # Synthesize results
            synthesize_request = {
                "session_id": session_id,
                "agent_results": agent_results,
                "synthesis_strategy": "prioritize_by_impact"
            }

            synthesize_response = await client.post("/analysis/multi_agent/synthesize", json=synthesize_request)
            assert synthesize_response.status_code == 200

            synthesize_data = synthesize_response.json()
            assert "synthesized_analysis" in synthesize_data
            assert "conflict_resolution" in synthesize_data
            assert "prioritized_recommendations" in synthesize_data