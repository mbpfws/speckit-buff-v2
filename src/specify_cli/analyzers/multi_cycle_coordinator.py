"""
Multi-cycle Analysis Coordinator

Orchestrates multiple analysis cycles for comprehensive project understanding
with iterative refinement and knowledge accumulation across cycles.
"""

import asyncio
import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Set, Callable
from dataclasses import dataclass, asdict
from enum import Enum
import logging
from datetime import datetime, timedelta
import traceback

from .project_classifier import ProjectClassifier, ClassificationResult
from .architecture_detector import ArchitectureDetector, ArchitectureDetection
from .dependency_mapper import DependencyMapper
from .context_analyzer import ContextAnalyzer, HistoricalContext


class AnalysisCycle(Enum):
    """Analysis cycle phases"""
    INITIAL_SCAN = "initial_scan"
    DEEP_ANALYSIS = "deep_analysis"
    CONTEXT_AWARE = "context_aware"
    OPTIMIZATION = "optimization"
    VALIDATION = "validation"


class AnalysisStrategy(Enum):
    """Analysis execution strategies"""
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"
    ADAPTIVE = "adaptive"
    ITERATIVE_DEEPENING = "iterative_deepening"


@dataclass
class AnalysisCycleResult:
    """Results from a single analysis cycle"""
    cycle_number: int
    cycle_type: AnalysisCycle
    start_time: datetime
    end_time: datetime
    duration: float
    results: Dict[str, Any]
    confidence_scores: Dict[str, float]
    insights_discovered: List[str]
    uncertainty_areas: List[str]
    next_cycle_recommendations: List[str]


@dataclass
class MultiCycleAnalysisConfig:
    """Configuration for multi-cycle analysis"""
    max_cycles: int = 5
    min_confidence_threshold: float = 0.85
    time_limit_seconds: int = 300
    enable_adaptive_strategy: bool = True
    enable_mcp_integration: bool = True
    cache_results: bool = True
    verbose_logging: bool = False
    analysis_depth_per_cycle: str = "increasing"


@dataclass
class AnalysisInsight:
    """Insight discovered during analysis"""
    insight_type: str
    description: str
    confidence: float
    evidence: List[str]
    cycle_discovered: int
    impact_level: str  # low, medium, high, critical


class MultiCycleAnalysisCoordinator:
    """
    Coordinates multiple analysis cycles for comprehensive understanding.

    Features:
    - Multi-phase analysis with increasing depth
    - Adaptive strategy selection
    - Confidence-based cycle termination
    - Knowledge accumulation across cycles
    - MCP server integration for enhanced analysis
    - Uncertainty identification and resolution
    - Performance optimization with caching
    """

    def __init__(self, config: Optional[MultiCycleAnalysisConfig] = None):
        self.config = config or MultiCycleAnalysisConfig()
        self.logger = self._setup_logger()

        # Initialize analyzers
        self.project_classifier = ProjectClassifier()
        self.architecture_detector = ArchitectureDetector()
        self.dependency_mapper = DependencyMapper()
        self.context_analyzer = ContextAnalyzer()

        # Analysis state
        self.analysis_history: List[AnalysisCycleResult] = []
        self.accumulated_knowledge: Dict[str, Any] = {}
        self.insights: List[AnalysisInsight] = []
        self.uncertainty_areas: Set[str] = set()
        self.confidence_trajectory: List[Dict[str, float]] = []

        # MCP integration (if enabled)
        self.mcp_integrations = {}
        if self.config.enable_mcp_integration:
            self._initialize_mcp_integrations()

        # Performance metrics
        self.performance_metrics = {
            "total_cycles": 0,
            "total_time": 0.0,
            "avg_cycle_time": 0.0,
            "confidence_improvement": 0.0,
            "insights_per_cycle": 0.0
        }

    def _setup_logger(self) -> logging.Logger:
        """Setup logger for analysis coordination."""
        logger = logging.getLogger("MultiCycleAnalysis")
        logger.setLevel(logging.DEBUG if self.config.verbose_logging else logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    def _initialize_mcp_integrations(self):
        """Initialize MCP server integrations."""
        # Placeholder for MCP server initialization
        # In practice, you would connect to:
        # - Tavily Expert for web search
        # - Context7 for documentation lookup
        # - DeepWiki for repository analysis
        # - Fetch for content retrieval
        self.mcp_integrations = {
            "tavily": {"available": False, "endpoint": None},
            "context7": {"available": False, "endpoint": None},
            "deepwiki": {"available": False, "endpoint": None},
            "fetch": {"available": False, "endpoint": None}
        }

    async def coordinate_multi_cycle_analysis(
        self,
        project_path: str,
        analysis_strategy: AnalysisStrategy = AnalysisStrategy.ADAPTIVE
    ) -> Dict[str, Any]:
        """
        Coordinate multiple analysis cycles for comprehensive project understanding.

        Args:
            project_path: Path to the project to analyze
            analysis_strategy: Strategy for executing analysis cycles

        Returns:
            Complete multi-cycle analysis results
        """
        self.logger.info(f"Starting multi-cycle analysis for {project_path}")
        start_time = time.time()

        # Initialize analysis state
        project_path = Path(project_path)
        self.accumulated_knowledge = {
            "project_path": str(project_path),
            "analysis_start": datetime.now().isoformat(),
            "project_structure": self._get_project_structure(project_path)
        }

        try:
            # Execute analysis cycles
            cycle_results = await self._execute_analysis_cycles(
                project_path, analysis_strategy
            )

            # Consolidate results
            consolidated_results = await self._consolidate_results(cycle_results)

            # Generate final insights
            final_insights = self._generate_final_insights()

            # Update performance metrics
            total_time = time.time() - start_time
            self.performance_metrics.update({
                "total_cycles": len(cycle_results),
                "total_time": total_time,
                "avg_cycle_time": total_time / len(cycle_results) if cycle_results else 0,
                "confidence_improvement": self._calculate_confidence_improvement(),
                "insights_per_cycle": len(self.insights) / len(cycle_results) if cycle_results else 0
            })

            # Prepare final result
            result = {
                "project_summary": consolidated_results,
                "analysis_cycles": [asdict(cycle) for cycle in cycle_results],
                "insights": [asdict(insight) for insight in final_insights],
                "performance_metrics": self.performance_metrics,
                "uncertainty_areas": list(self.uncertainty_areas),
                "recommendations": self._generate_final_recommendations(),
                "analysis_metadata": {
                    "strategy_used": analysis_strategy.value,
                    "completion_time": datetime.now().isoformat(),
                    "total_duration_seconds": total_time,
                    "max_cycles_reached": len(cycle_results) >= self.config.max_cycles,
                    "confidence_threshold_met": self._is_confidence_threshold_met()
                }
            }

            self.logger.info(f"Multi-cycle analysis completed in {total_time:.2f} seconds")
            return result

        except Exception as e:
            self.logger.error(f"Error during multi-cycle analysis: {e}")
            self.logger.debug(traceback.format_exc())
            raise

    async def _execute_analysis_cycles(
        self,
        project_path: Path,
        strategy: AnalysisStrategy
    ) -> List[AnalysisCycleResult]:
        """Execute analysis cycles according to strategy."""
        cycle_results = []
        current_cycle = 0
        should_continue = True

        while should_continue and current_cycle < self.config.max_cycles:
            current_cycle += 1
            cycle_type = self._determine_cycle_type(current_cycle)

            self.logger.info(f"Starting cycle {current_cycle}: {cycle_type.value}")

            # Execute cycle
            cycle_result = await self._execute_single_cycle(
                project_path, current_cycle, cycle_type, strategy
            )

            cycle_results.append(cycle_result)

            # Update accumulated knowledge
            self._update_accumulated_knowledge(cycle_result)

            # Check continuation criteria
            should_continue = self._should_continue_analysis(cycle_result)

            # Update uncertainty areas
            self._update_uncertainty_areas(cycle_result)

            # Log progress
            self.logger.info(
                f"Cycle {current_cycle} completed in {cycle_result.duration:.2f}s "
                f"with avg confidence: {self._calculate_avg_confidence(cycle_result.confidence_scores):.2f}"
            )

        return cycle_results

    def _determine_cycle_type(self, cycle_number: int) -> AnalysisCycle:
        """Determine the type of analysis cycle based on number."""
        cycle_sequence = [
            AnalysisCycle.INITIAL_SCAN,
            AnalysisCycle.DEEP_ANALYSIS,
            AnalysisCycle.CONTEXT_AWARE,
            AnalysisCycle.OPTIMIZATION,
            AnalysisCycle.VALIDATION
        ]

        if cycle_number <= len(cycle_sequence):
            return cycle_sequence[cycle_number - 1]
        else:
            return AnalysisCycle.OPTIMIZATION  # Default to optimization for extra cycles

    async def _execute_single_cycle(
        self,
        project_path: Path,
        cycle_number: int,
        cycle_type: AnalysisCycle,
        strategy: AnalysisStrategy
    ) -> AnalysisCycleResult:
        """Execute a single analysis cycle."""
        start_time = time.time()

        # Determine analysis depth for this cycle
        if self.config.analysis_depth_per_cycle == "increasing":
            depth = "quick" if cycle_number == 1 else "deep" if cycle_number >= 3 else "standard"
        else:
            depth = self.config.analysis_depth_per_cycle

        # Prepare cycle-specific parameters
        cycle_params = self._prepare_cycle_parameters(
            cycle_number, cycle_type, depth
        )

        # Execute analysis tasks
        if strategy == AnalysisStrategy.SEQUENTIAL:
            results = await self._execute_sequential_analysis(
                project_path, cycle_params
            )
        elif strategy == AnalysisStrategy.PARALLEL:
            results = await self._execute_parallel_analysis(
                project_path, cycle_params
            )
        elif strategy == AnalysisStrategy.ADAPTIVE:
            results = await self._execute_adaptive_analysis(
                project_path, cycle_params, cycle_number
            )
        else:  # ITERATIVE_DEEPENING
            results = await self._execute_iterative_deepening(
                project_path, cycle_params
            )

        # Calculate confidence scores
        confidence_scores = self._calculate_confidence_scores(results)

        # Extract insights
        insights = self._extract_cycle_insights(results, cycle_number)

        # Identify uncertainty areas
        uncertainties = self._identify_cycle_uncertainties(results)

        # Generate recommendations for next cycle
        next_recommendations = self._generate_cycle_recommendations(
            results, confidence_scores, uncertainties
        )

        end_time = time.time()
        duration = end_time - start_time

        # Create cycle result
        cycle_result = AnalysisCycleResult(
            cycle_number=cycle_number,
            cycle_type=cycle_type,
            start_time=datetime.fromtimestamp(start_time),
            end_time=datetime.fromtimestamp(end_time),
            duration=duration,
            results=results,
            confidence_scores=confidence_scores,
            insights_discovered=[insight.description for insight in insights],
            uncertainty_areas=uncertainties,
            next_cycle_recommendations=next_recommendations
        )

        # Add insights to global list
        self.insights.extend(insights)

        return cycle_result

    def _prepare_cycle_parameters(
        self,
        cycle_number: int,
        cycle_type: AnalysisCycle,
        depth: str
    ) -> Dict[str, Any]:
        """Prepare parameters for analysis cycle."""
        params = {
            "cycle_number": cycle_number,
            "cycle_type": cycle_type,
            "analysis_depth": depth,
            "use_cached_results": self.config.cache_results and cycle_number > 1,
            "previous_knowledge": self.accumulated_knowledge if cycle_number > 1 else None
        }

        # Add cycle-specific parameters
        if cycle_type == AnalysisCycle.INITIAL_SCAN:
            params.update({
                "include_dependencies": False,
                "include_history": False,
                "quick_mode": True
            })
        elif cycle_type == AnalysisCycle.DEEP_ANALYSIS:
            params.update({
                "include_dependencies": True,
                "include_history": True,
                "include_transitive": True
            })
        elif cycle_type == AnalysisCycle.CONTEXT_AWARE:
            params.update({
                "include_developer_profiles": True,
                "framework_specific": True,
                "check_patterns": True
            })
        elif cycle_type == AnalysisCycle.OPTIMIZATION:
            params.update({
                "check_vulnerabilities": True,
                "check_licenses": True,
                "optimization_focus": True
            })
        elif cycle_type == AnalysisCycle.VALIDATION:
            params.update({
                "validation_mode": True,
                "cross_check_results": True,
                "consistency_check": True
            })

        return params

    async def _execute_sequential_analysis(
        self,
        project_path: Path,
        params: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute analysis tasks sequentially."""
        results = {}

        # Project classification
        try:
            classification = await self.project_classifier.classify_project(
                str(project_path),
                analysis_depth=params["analysis_depth"],
                include_dependencies=params.get("include_dependencies", False),
                detect_frameworks=True
            )
            results["classification"] = asdict(classification)
        except Exception as e:
            self.logger.warning(f"Project classification failed: {e}")
            results["classification"] = {"error": str(e)}

        # Architecture detection
        try:
            architecture = await self.architecture_detector.detect_architecture(
                str(project_path),
                project_analysis=results.get("classification"),
                framework_specific=params.get("framework_specific", True)
            )
            results["architecture"] = asdict(architecture)
        except Exception as e:
            self.logger.warning(f"Architecture detection failed: {e}")
            results["architecture"] = {"error": str(e)}

        # Dependency mapping
        if params.get("include_dependencies", False):
            try:
                dependencies = await self.dependency_mapper.map_dependencies(
                    str(project_path),
                    include_transitive=params.get("include_transitive", False),
                    check_vulnerabilities=params.get("check_vulnerabilities", False)
                )
                results["dependencies"] = dependencies
            except Exception as e:
                self.logger.warning(f"Dependency mapping failed: {e}")
                results["dependencies"] = {"error": str(e)}

        # Context analysis
        if params.get("include_history", False):
            try:
                context = await self.context_analyzer.analyze_context(
                    str(project_path),
                    analysis_depth=params["analysis_depth"],
                    include_developer_profiles=params.get("include_developer_profiles", False)
                )
                results["context"] = asdict(context)
            except Exception as e:
                self.logger.warning(f"Context analysis failed: {e}")
                results["context"] = {"error": str(e)}

        return results

    async def _execute_parallel_analysis(
        self,
        project_path: Path,
        params: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute analysis tasks in parallel."""
        results = {}

        # Create tasks for parallel execution
        tasks = []

        # Project classification task
        tasks.append(self.project_classifier.classify_project(
            str(project_path),
            analysis_depth=params["analysis_depth"],
            include_dependencies=params.get("include_dependencies", False),
            detect_frameworks=True
        ))

        # Architecture detection task
        tasks.append(self.architecture_detector.detect_architecture(
            str(project_path),
            project_analysis=None,  # Will be filled in consolidation
            framework_specific=params.get("framework_specific", True)
        ))

        # Dependency mapping task (if enabled)
        if params.get("include_dependencies", False):
            tasks.append(self.dependency_mapper.map_dependencies(
                str(project_path),
                include_transitive=params.get("include_transitive", False),
                check_vulnerabilities=params.get("check_vulnerabilities", False)
            ))

        # Context analysis task (if enabled)
        if params.get("include_history", False):
            tasks.append(self.context_analyzer.analyze_context(
                str(project_path),
                analysis_depth=params["analysis_depth"],
                include_developer_profiles=params.get("include_developer_profiles", False)
            ))

        # Execute tasks in parallel
        try:
            task_results = await asyncio.gather(*tasks, return_exceptions=True)

            # Process results
            result_keys = ["classification", "architecture", "dependencies", "context"]
            for i, result in enumerate(task_results):
                if i < len(result_keys):
                    key = result_keys[i]
                    if isinstance(result, Exception):
                        results[key] = {"error": str(result)}
                    else:
                        results[key] = asdict(result) if hasattr(result, '__dict__') else result

        except Exception as e:
            self.logger.error(f"Parallel execution failed: {e}")

        return results

    async def _execute_adaptive_analysis(
        self,
        project_path: Path,
        params: Dict[str, Any],
        cycle_number: int
    ) -> Dict[str, Any]:
        """Execute analysis with adaptive strategy based on previous results."""
        results = {}

        # Use previous knowledge to adapt analysis
        if params.get("previous_knowledge"):
            previous_results = params["previous_knowledge"].get("cycle_results", {})

            # Skip certain analyses if high confidence already achieved
            skip_classification = previous_results.get("classification", {}).get("confidence", 0) > 0.9
            skip_architecture = previous_results.get("architecture", {}).get("confidence", 0) > 0.9

            if skip_classification and cycle_number > 1:
                results["classification"] = previous_results["classification"]
                results["classification"]["from_cache"] = True

            if skip_architecture and cycle_number > 1:
                results["architecture"] = previous_results["architecture"]
                results["architecture"]["from_cache"] = True

        # Execute remaining analyses
        if "classification" not in results:
            try:
                classification = await self.project_classifier.classify_project(
                    str(project_path),
                    analysis_depth=params["analysis_depth"],
                    include_dependencies=params.get("include_dependencies", False),
                    detect_frameworks=True
                )
                results["classification"] = asdict(classification)
            except Exception as e:
                self.logger.warning(f"Project classification failed: {e}")
                results["classification"] = {"error": str(e)}

        if "architecture" not in results:
            try:
                architecture = await self.architecture_detector.detect_architecture(
                    str(project_path),
                    project_analysis=results.get("classification"),
                    framework_specific=params.get("framework_specific", True)
                )
                results["architecture"] = asdict(architecture)
            except Exception as e:
                self.logger.warning(f"Architecture detection failed: {e}")
                results["architecture"] = {"error": str(e)}

        # Continue with other analyses...
        return results

    async def _execute_iterative_deepening(
        self,
        project_path: Path,
        params: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute analysis with iterative deepening approach."""
        results = {}

        # Start with quick analysis
        quick_results = await self._execute_sequential_analysis(
            project_path, {**params, "analysis_depth": "quick"}
        )

        # Identify areas needing deeper analysis
        uncertainty_areas = self._identify_cycle_uncertainties(quick_results)

        # Execute deep analysis only on uncertain areas
        if uncertainty_areas:
            deep_params = {
                **params,
                "analysis_depth": "deep",
                "focus_areas": uncertainty_areas
            }
            deep_results = await self._execute_sequential_analysis(project_path, deep_params)

            # Merge results
            for key in quick_results:
                if key in deep_results and deep_results[key].get("confidence", 0) > quick_results[key].get("confidence", 0):
                    results[key] = deep_results[key]
                else:
                    results[key] = quick_results[key]
        else:
            results = quick_results

        return results

    def _calculate_confidence_scores(self, results: Dict[str, Any]) -> Dict[str, float]:
        """Calculate confidence scores for each analysis type."""
        scores = {}

        for analysis_type, result in results.items():
            if isinstance(result, dict):
                # Extract confidence from result
                if "confidence" in result:
                    scores[analysis_type] = result["confidence"]
                elif "project_type" in result:  # Classification result
                    scores[analysis_type] = result.get("confidence_score", 0.5)
                elif "primary_pattern" in result:  # Architecture result
                    scores[analysis_type] = result.get("confidence", 0.5)
                elif "summary" in result:  # Dependencies result
                    # Calculate confidence based on completeness
                    summary = result["summary"]
                    completeness = (
                        summary.get("total_direct_dependencies", 0) > 0 and
                        summary.get("total_transitive_dependencies", 0) > 0
                    )
                    scores[analysis_type] = 0.8 if completeness else 0.3
                elif "total_commits" in result:  # Context result
                    # Confidence based on data richness
                    scores[analysis_type] = 0.7 if result["total_commits"] > 10 else 0.4
                else:
                    scores[analysis_type] = 0.5  # Default confidence
            else:
                scores[analysis_type] = 0.0  # Error case

        return scores

    def _extract_cycle_insights(
        self,
        results: Dict[str, Any],
        cycle_number: int
    ) -> List[AnalysisInsight]:
        """Extract insights from analysis results."""
        insights = []

        # Extract from classification
        if "classification" in results and isinstance(results["classification"], dict):
            classification = results["classification"]
            project_type = classification.get("project_type")
            complexity = classification.get("complexity_score", 0)

            if complexity > 7:
                insights.append(AnalysisInsight(
                    insight_type="complexity",
                    description=f"High complexity project ({complexity}/10) requires careful architecture",
                    confidence=0.8,
                    evidence=[f"Complexity score: {complexity}"],
                    cycle_discovered=cycle_number,
                    impact_level="high"
                ))

        # Extract from architecture
        if "architecture" in results and isinstance(results["architecture"], dict):
            architecture = results["architecture"]
            patterns = architecture.get("secondary_patterns", [])

            if len(patterns) > 2:
                insights.append(AnalysisInsight(
                    insight_type="architecture",
                    description=f"Multiple architectural patterns detected: {', '.join(patterns)}",
                    confidence=0.7,
                    evidence=patterns,
                    cycle_discovered=cycle_number,
                    impact_level="medium"
                ))

        # Extract from dependencies
        if "dependencies" in results and isinstance(results["dependencies"], dict):
            deps = results["dependencies"]
            vuln_count = deps.get("summary", {}).get("vulnerability_count", 0)

            if vuln_count > 0:
                insights.append(AnalysisInsight(
                    insight_type="security",
                    description=f"Found {vuln_count} potential security vulnerabilities",
                    confidence=0.9,
                    evidence=[f"Vulnerability count: {vuln_count}"],
                    cycle_discovered=cycle_number,
                    impact_level="critical"
                ))

        # Extract from context
        if "context" in results and isinstance(results["context"], dict):
            context = results["context"]
            bus_factor = context.get("bus_factor", 1)

            if bus_factor <= 1:
                insights.append(AnalysisInsight(
                    insight_type="risk",
                    description="Low bus factor - project knowledge concentrated in few developers",
                    confidence=0.8,
                    evidence=[f"Bus factor: {bus_factor}"],
                    cycle_discovered=cycle_number,
                    impact_level="high"
                ))

        return insights

    def _identify_cycle_uncertainties(self, results: Dict[str, Any]) -> List[str]:
        """Identify areas of uncertainty in analysis results."""
        uncertainties = []

        for analysis_type, result in results.items():
            if isinstance(result, dict):
                confidence = result.get("confidence", 0.5)
                if confidence < 0.7:
                    uncertainties.append(f"Low confidence in {analysis_type} analysis")

                # Check for error conditions
                if "error" in result:
                    uncertainties.append(f"Error in {analysis_type}: {result['error']}")

                # Check for missing data
                if analysis_type == "dependencies" and isinstance(result, dict):
                    summary = result.get("summary", {})
                    if summary.get("total_direct_dependencies", 0) == 0:
                        uncertainties.append("No dependencies detected")

                if analysis_type == "context" and isinstance(result, dict):
                    if result.get("total_commits", 0) == 0:
                        uncertainties.append("No git history available")

        return uncertainties

    def _generate_cycle_recommendations(
        self,
        results: Dict[str, Any],
        confidence_scores: Dict[str, float],
        uncertainties: List[str]
    ) -> List[str]:
        """Generate recommendations for next analysis cycle."""
        recommendations = []

        # Recommend based on low confidence areas
        low_confidence_areas = [
            area for area, confidence in confidence_scores.items()
            if confidence < 0.7
        ]

        if low_confidence_areas:
            recommendations.append(f"Focus on improving {', '.join(low_confidence_areas)} analysis")

        # Recommend based on uncertainties
        if uncertainties:
            recommendations.append(f"Address uncertainties: {', '.join(uncertainties[:3])}")

        # Recommend deeper analysis
        if any(score > 0.7 for score in confidence_scores.values()):
            recommendations.append("Consider enabling MCP integrations for enhanced analysis")

        # Recommend validation
        if len(confidence_scores) >= 3:
            recommendations.append("Perform cross-analysis validation between components")

        return recommendations

    def _update_accumulated_knowledge(self, cycle_result: AnalysisCycleResult):
        """Update accumulated knowledge with new cycle results."""
        self.accumulated_knowledge[f"cycle_{cycle_result.cycle_number}"] = {
            "results": cycle_result.results,
            "confidence_scores": cycle_result.confidence_scores,
            "insights": cycle_result.insights_discovered,
            "timestamp": cycle_result.end_time.isoformat()
        }

        # Track confidence trajectory
        self.confidence_trajectory.append(cycle_result.confidence_scores)

    def _should_continue_analysis(self, cycle_result: AnalysisCycleResult) -> bool:
        """Determine if another analysis cycle should be executed."""
        # Check time limit
        if cycle_result.duration > self.config.time_limit_seconds:
            self.logger.info("Time limit reached, stopping analysis")
            return False

        # Check confidence threshold
        if self._is_confidence_threshold_met():
            self.logger.info("Confidence threshold met, stopping analysis")
            return False

        # Check if max cycles reached
        if cycle_result.cycle_number >= self.config.max_cycles:
            self.logger.info("Maximum cycles reached")
            return False

        # Check if there are significant new insights
        if len(cycle_result.insights_discovered) == 0 and cycle_result.cycle_number > 2:
            self.logger.info("No new insights discovered, stopping analysis")
            return False

        return True

    def _is_confidence_threshold_met(self) -> bool:
        """Check if confidence threshold is met across all analyses."""
        if not self.confidence_trajectory:
            return False

        # Check latest confidence scores
        latest_scores = self.confidence_trajectory[-1]
        avg_confidence = sum(latest_scores.values()) / len(latest_scores)

        return avg_confidence >= self.config.min_confidence_threshold

    def _update_uncertainty_areas(self, cycle_result: AnalysisCycleResult):
        """Update set of uncertainty areas."""
        for uncertainty in cycle_result.uncertainty_areas:
            self.uncertainty_areas.add(uncertainty)

    async def _consolidate_results(
        self,
        cycle_results: List[AnalysisCycleResult]
    ) -> Dict[str, Any]:
        """Consolidate results from all analysis cycles."""
        consolidated = {
            "project_type": None,
            "architecture": None,
            "complexity_score": 0,
            "risk_level": "low",
            "recommendations": [],
            "analysis_quality": {
                "overall_confidence": 0.0,
                "completeness_score": 0.0,
                "consistency_score": 0.0
            }
        }

        # Extract best results from all cycles
        best_results = {}

        for cycle in cycle_results:
            for analysis_type, result in cycle.results.items():
                if analysis_type not in best_results or self._is_better_result(
                    result, best_results[analysis_type]
                ):
                    best_results[analysis_type] = result

        # Build consolidated view
        if "classification" in best_results:
            classification = best_results["classification"]
            consolidated["project_type"] = classification.get("project_type")
            consolidated["complexity_score"] = classification.get("complexity_score", 0)

        if "architecture" in best_results:
            architecture = best_results["architecture"]
            consolidated["architecture"] = {
                "primary_pattern": architecture.get("primary_pattern"),
                "framework": architecture.get("framework"),
                "confidence": architecture.get("confidence")
            }

        if "dependencies" in best_results:
            deps = best_results["dependencies"]
            if deps.get("summary", {}).get("vulnerability_count", 0) > 0:
                consolidated["risk_level"] = "high"

        # Calculate analysis quality metrics
        consolidated["analysis_quality"] = self._calculate_analysis_quality(
            best_results, cycle_results
        )

        return consolidated

    def _is_better_result(
        self,
        new_result: Dict[str, Any],
        existing_result: Dict[str, Any]
    ) -> bool:
        """Determine if new result is better than existing one."""
        new_confidence = new_result.get("confidence", 0)
        existing_confidence = existing_result.get("confidence", 0)

        return new_confidence > existing_confidence

    def _calculate_analysis_quality(
        self,
        best_results: Dict[str, Any],
        cycle_results: List[AnalysisCycleResult]
    ) -> Dict[str, float]:
        """Calculate overall analysis quality metrics."""
        quality = {
            "overall_confidence": 0.0,
            "completeness_score": 0.0,
            "consistency_score": 0.0
        }

        # Overall confidence
        if best_results:
            confidences = [
                result.get("confidence", 0.5)
                for result in best_results.values()
                if isinstance(result, dict)
            ]
            if confidences:
                quality["overall_confidence"] = sum(confidences) / len(confidences)

        # Completeness score
        expected_analyses = ["classification", "architecture", "dependencies", "context"]
        completed_analyses = [
            analysis for analysis in expected_analyses
            if analysis in best_results and "error" not in best_results[analysis]
        ]
        quality["completeness_score"] = len(completed_analyses) / len(expected_analyses)

        # Consistency score (based on confidence trajectory stability)
        if len(self.confidence_trajectory) > 1:
            # Calculate variance in confidence scores
            all_scores = []
            for scores in self.confidence_trajectory:
                all_scores.extend(scores.values())

            if all_scores:
                mean_score = sum(all_scores) / len(all_scores)
                variance = sum((x - mean_score) ** 2 for x in all_scores) / len(all_scores)
                # Convert variance to consistency score (lower variance = higher consistency)
                quality["consistency_score"] = max(0, 1 - variance)

        return quality

    def _generate_final_insights(self) -> List[AnalysisInsight]:
        """Generate final insights from all analysis cycles."""
        # Group insights by type
        insight_groups = defaultdict(list)
        for insight in self.insights:
            insight_groups[insight.insight_type].append(insight)

        # Generate summary insights
        final_insights = []

        # High-level summary
        if len(self.insights) > 0:
            high_impact_insights = [
                insight for insight in self.insights
                if insight.impact_level in ["high", "critical"]
            ]

            if high_impact_insights:
                final_insights.append(AnalysisInsight(
                    insight_type="summary",
                    description=f"Found {len(high_impact_insights)} high-impact insights requiring attention",
                    confidence=1.0,
                    evidence=[f"High impact insights: {len(high_impact_insights)}"],
                    cycle_discovered=max(cycle_results.cycle_number for cycle_results in self.analysis_history),
                    impact_level="high"
                ))

        # Add most critical insights from each type
        for insight_type, type_insights in insight_groups.items():
            if type_insights:
                # Get highest confidence insight of this type
                best_insight = max(type_insights, key=lambda x: x.confidence)
                final_insights.append(best_insight)

        return final_insights

    def _generate_final_recommendations(self) -> List[str]:
        """Generate final recommendations based on complete analysis."""
        recommendations = []

        # Recommend based on overall confidence
        overall_confidence = self.performance_metrics.get("confidence_improvement", 0)
        if overall_confidence < 0.7:
            recommendations.append("Consider additional manual analysis due to low confidence results")

        # Recommend based on uncertainty areas
        if self.uncertainty_areas:
            recommendations.append(f"Address these uncertainty areas: {', '.join(list(self.uncertainty_areas)[:3])}")

        # Recommend based on insights
        critical_insights = [
            insight for insight in self.insights
            if insight.impact_level == "critical"
        ]

        if critical_insights:
            recommendations.append("Immediately address critical insights for project health")

        # Recommend based on analysis strategy
        if self.performance_metrics.get("total_cycles", 0) == self.config.max_cycles:
            recommendations.append("Consider increasing max cycles for more complex projects")

        return recommendations

    def _calculate_confidence_improvement(self) -> float:
        """Calculate overall confidence improvement across cycles."""
        if len(self.confidence_trajectory) < 2:
            return 0.0

        initial_avg = sum(self.confidence_trajectory[0].values()) / len(self.confidence_trajectory[0])
        final_avg = sum(self.confidence_trajectory[-1].values()) / len(self.confidence_trajectory[-1])

        return final_avg - initial_avg

    def _calculate_avg_confidence(self, confidence_scores: Dict[str, float]) -> float:
        """Calculate average confidence score."""
        if not confidence_scores:
            return 0.0
        return sum(confidence_scores.values()) / len(confidence_scores)

    def _get_project_structure(self, project_path: Path) -> Dict[str, Any]:
        """Get basic project structure information."""
        structure = {
            "root_files": [],
            "directories": [],
            "total_files": 0,
            "total_dirs": 0
        }

        try:
            for item in project_path.iterdir():
                if item.is_file():
                    structure["root_files"].append(item.name)
                elif item.is_dir() and not item.name.startswith('.'):
                    structure["directories"].append(item.name)

            # Count total files and directories
            for root, dirs, files in os.walk(project_path):
                structure["total_files"] += len(files)
                structure["total_dirs"] += len(dirs)
        except Exception as e:
            self.logger.warning(f"Error scanning project structure: {e}")

        return structure

    def get_analysis_summary(self) -> Dict[str, Any]:
        """Get a summary of the analysis coordination."""
        return {
            "total_cycles_executed": len(self.analysis_history),
            "total_insights_discovered": len(self.insights),
            "uncertainty_areas_count": len(self.uncertainty_areas),
            "performance_metrics": self.performance_metrics,
            "mcp_integrations_available": sum(1 for mcp in self.mcp_integrations.values() if mcp["available"])
        }

    async def export_analysis_report(
        self,
        results: Dict[str, Any],
        output_path: str,
        format: str = "json"
    ) -> None:
        """Export analysis results to file."""
        output_path = Path(output_path)

        if format == "json":
            with open(output_path, 'w') as f:
                json.dump(results, f, indent=2, default=str)
        elif format == "markdown":
            # Generate markdown report
            report = self._generate_markdown_report(results)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report)
        else:
            raise ValueError(f"Unsupported format: {format}")

        self.logger.info(f"Analysis report exported to {output_path}")

    def _generate_markdown_report(self, results: Dict[str, Any]) -> str:
        """Generate markdown report from analysis results."""
        # Placeholder for markdown generation
        # In practice, you would generate a comprehensive report
        return "# Multi-Cycle Analysis Report\n\nAnalysis results not yet formatted for markdown."