"""
Historical Context Analyzer

Analyzes development history, patterns, and context to provide insights
into project evolution, team dynamics, and development practices.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime, timedelta
import subprocess
import csv
from collections import defaultdict, Counter
import statistics


class ActivityLevel(Enum):
    """Development activity levels"""
    VERY_LOW = "very_low"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"


class DevelopmentPhase(Enum):
    """Project development phases"""
    INITIALIZATION = "initialization"
    RAPID_DEVELOPMENT = "rapid_development"
    STABLE_DEVELOPMENT = "stable_development"
    MAINTENANCE = "maintenance"
    DECLINE = "decline"
    REFACTORING = "refactoring"


class TeamSize(Enum):
    """Team size categories"""
    SOLO = "solo"
    SMALL = "small"  # 2-5
    MEDIUM = "medium"  # 6-15
    LARGE = "large"  # 16-50
    ENTERPRISE = "enterprise"  # 50+


@dataclass
class CommitInfo:
    """Individual commit information"""
    hash: str
    author: str
    email: str
    timestamp: datetime
    message: str
    files_changed: int
    insertions: int
    deletions: int
    is_merge: bool
    branches: List[str]


@dataclass
class DeveloperProfile:
    """Developer activity profile"""
    name: str
    email: str
    commit_count: int
    first_commit: datetime
    last_commit: datetime
    avg_commits_per_month: float
    preferred_hours: List[int]
    file_types: Dict[str, int]
    avg_changes_per_commit: float
    is_active: bool


@dataclass
class DevelopmentPattern:
    """Detected development patterns"""
    pattern_type: str
    confidence: float
    description: str
    evidence: List[str]
    timeframe: Tuple[datetime, datetime]


@dataclass
class HistoricalContext:
    """Complete historical context analysis"""
    project_age: timedelta
    total_commits: int
    active_contributors: int
    total_contributors: int
    development_phase: DevelopmentPhase
    activity_level: ActivityLevel
    team_size: TeamSize
    development_patterns: List[DevelopmentPattern]
    developer_profiles: Dict[str, DeveloperProfile]
    commit_frequency: Dict[str, int]
    bus_factor: int
    risk_indicators: List[str]
    recommendations: List[str]
    analysis_metadata: Dict[str, Any]


class ContextAnalyzer:
    """
    Analyzes project history and development context.

    Features:
    - Git history analysis with commit patterns
    - Developer activity profiling
    - Development phase detection
    - Team dynamics analysis
    - Risk assessment
    - Historical pattern recognition
    - Bus factor calculation
    """

    def __init__(self):
        self.development_patterns = {
            "spike_activity": {
                "description": "Sudden burst of commits, often before deadlines",
                "indicators": ["high_commit_density", "deadline_proximity"]
            },
            "weekend_warrior": {
                "description": "Significant development activity on weekends",
                "indicators": ["weekend_commits", "high_weekend_ratio"]
            },
            "night_owl": {
                "description": "Development primarily during night hours",
                "indicators": ["night_commits", "high_night_ratio"]
            },
            "refactoring_burst": {
                "description": "Concentrated refactoring activity",
                "indicators": ["refactor_keywords", "structural_changes"]
            },
            "documentation_focus": {
                "description": "Periods focused on documentation",
                "indicators": ["doc_commits", "readme_changes"]
            },
            "testing_spree": {
                "description": "Intensive test writing periods",
                "indicators": ["test_commits", "test_file_creation"]
            },
            "feature_sprint": {
                "description": "Focused feature development",
                "indicators": ["feature_branches", "focused_commits"]
            },
            "bug_fix_cycle": {
                "description": "Repetitive bug fixing patterns",
                "indicators": ["fix_commits", "recurring_issues"]
            }
        }

        self.refactor_keywords = [
            "refactor", "restructure", "cleanup", "reorganize",
            "extract", "consolidate", "simplify", "modularize"
        ]

        self.test_keywords = [
            "test", "spec", "fixture", "mock", "assert",
            "coverage", "unit test", "integration test"
        ]

        self.doc_keywords = [
            "doc", "readme", "documentation", "comment",
            "guide", "tutorial", "explain"
        ]

        self.fix_keywords = [
            "fix", "bug", "issue", "error", "correct",
            "patch", "resolve", "repair"
        ]

    async def analyze_context(
        self,
        project_path: str,
        analysis_depth: str = "standard",
        include_developer_profiles: bool = True,
        max_commits: int = 1000
    ) -> HistoricalContext:
        """
        Analyze historical context of the project.

        Args:
            project_path: Path to the project root
            analysis_depth: Analysis depth (quick, standard, deep)
            include_developer_profiles: Whether to analyze individual developers
            max_commits: Maximum number of commits to analyze

        Returns:
            Complete historical context analysis
        """
        project_path = Path(project_path)

        # Check if it's a git repository
        if not (project_path / ".git").exists():
            raise ValueError("Not a git repository")

        # Get commit history
        commits = await self._get_commit_history(project_path, max_commits)

        if not commits:
            raise ValueError("No commit history found")

        # Basic statistics
        project_age = commits[-1].timestamp - commits[0].timestamp
        total_commits = len(commits)

        # Analyze contributors
        contributors = self._analyze_contributors(commits)
        total_contributors = len(contributors)
        active_contributors = len([
            c for c in contributors.values()
            if self._is_active_developer(c)
        ])

        # Determine development phase
        development_phase = self._determine_development_phase(commits)

        # Calculate activity level
        activity_level = self._calculate_activity_level(commits)

        # Estimate team size
        team_size = self._estimate_team_size(contributors, project_age)

        # Detect development patterns
        patterns = self._detect_development_patterns(commits)

        # Create developer profiles
        developer_profiles = {}
        if include_developer_profiles:
            developer_profiles = await self._create_developer_profiles(commits)

        # Calculate commit frequency
        commit_frequency = self._calculate_commit_frequency(commits)

        # Calculate bus factor
        bus_factor = self._calculate_bus_factor(commits, contributors)

        # Identify risk indicators
        risk_indicators = self._identify_risk_indicators(
            commits, contributors, patterns
        )

        # Generate recommendations
        recommendations = self._generate_context_recommendations(
            development_phase, activity_level, team_size, risk_indicators
        )

        # Prepare metadata
        analysis_metadata = {
            "analysis_depth": analysis_depth,
            "commits_analyzed": total_commits,
            "time_span_days": project_age.days,
            "analysis_timestamp": datetime.now().isoformat(),
            "git_version": self._get_git_version()
        }

        return HistoricalContext(
            project_age=project_age,
            total_commits=total_commits,
            active_contributors=active_contributors,
            total_contributors=total_contributors,
            development_phase=development_phase,
            activity_level=activity_level,
            team_size=team_size,
            development_patterns=patterns,
            developer_profiles=developer_profiles,
            commit_frequency=commit_frequency,
            bus_factor=bus_factor,
            risk_indicators=risk_indicators,
            recommendations=recommendations,
            analysis_metadata=analysis_metadata
        )

    async def _get_commit_history(
        self,
        project_path: Path,
        max_commits: int
    ) -> List[CommitInfo]:
        """Retrieve commit history from git."""
        commits = []

        try:
            # Get commit log with detailed information
            cmd = [
                "git", "-C", str(project_path), "log",
                f"--max-count={max_commits}",
                "--pretty=format:%H|%an|%ae|%at|%s|%P",
                "--shortstat",
                "--no-merges"  # Exclude merge commits by default
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )

            # Parse output
            lines = result.stdout.strip().split('\n')
            i = 0
            while i < len(lines):
                if not lines[i]:
                    i += 1
                    continue

                # Parse commit header
                parts = lines[i].split('|')
                if len(parts) >= 5:
                    commit_hash = parts[0]
                    author = parts[1]
                    email = parts[2]
                    timestamp = datetime.fromtimestamp(int(parts[3]))
                    message = parts[4]
                    parents = parts[5].split() if len(parts) > 5 else []

                    is_merge = len(parents) > 1

                    # Parse file changes (next line)
                    files_changed = 0
                    insertions = 0
                    deletions = 0

                    if i + 1 < len(lines) and lines[i + 1]:
                        stat_line = lines[i + 1]
                        if "files changed" in stat_line:
                            match = re.search(r'(\d+) files? changed(?:, (\d+) insertions?\(\+\))?(?:, (\d+) deletions?\(-\))?', stat_line)
                            if match:
                                files_changed = int(match.group(1))
                                insertions = int(match.group(2) or 0)
                                deletions = int(match.group(3) or 0)
                            i += 1  # Skip stat line

                    # Get branches
                    branches = self._get_commit_branches(project_path, commit_hash)

                    commit = CommitInfo(
                        hash=commit_hash,
                        author=author,
                        email=email,
                        timestamp=timestamp,
                        message=message,
                        files_changed=files_changed,
                        insertions=insertions,
                        deletions=deletions,
                        is_merge=is_merge,
                        branches=branches
                    )
                    commits.append(commit)

                i += 1

            # Sort by timestamp
            commits.sort(key=lambda x: x.timestamp)

        except subprocess.CalledProcessError as e:
            print(f"Error getting git history: {e}")

        return commits

    def _get_commit_branches(self, project_path: Path, commit_hash: str) -> List[str]:
        """Get branches that contain the commit."""
        try:
            cmd = ["git", "-C", str(project_path), "branch", "--contains", commit_hash]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )

            branches = []
            for line in result.stdout.strip().split('\n'):
                branch = line.strip().replace('*', '').strip()
                if branch and not branch.startswith("(no branch"):
                    branches.append(branch)

            return branches

        except subprocess.CalledProcessError:
            return []

    def _analyze_contributors(
        self,
        commits: List[CommitInfo]
    ) -> Dict[str, Dict[str, Any]]:
        """Analyze contributor statistics."""
        contributors = defaultdict(lambda: {
            "commit_count": 0,
            "first_commit": None,
            "last_commit": None,
            "total_changes": 0,
            "file_types": defaultdict(int),
            "commit_hours": [],
            "merge_commits": 0
        })

        for commit in commits:
            email = commit.email
            contributor = contributors[email]

            contributor["commit_count"] += 1

            if not contributor["first_commit"] or commit.timestamp < contributor["first_commit"]:
                contributor["first_commit"] = commit.timestamp

            if not contributor["last_commit"] or commit.timestamp > contributor["last_commit"]:
                contributor["last_commit"] = commit.timestamp

            contributor["total_changes"] += commit.insertions + commit.deletions
            contributor["commit_hours"].append(commit.timestamp.hour)

            # Count file types from commit message (simplified)
            if any(ext in commit.message.lower() for ext in [".py", ".js", ".ts", ".java", ".go"]):
                for ext in [".py", ".js", ".ts", ".java", ".go"]:
                    if ext in commit.message.lower():
                        contributor["file_types"][ext] += 1

            if commit.is_merge:
                contributor["merge_commits"] += 1

        return dict(contributors)

    def _is_active_developer(self, contributor: Dict[str, Any]) -> bool:
        """Check if a developer is still active."""
        if not contributor["last_commit"]:
            return False

        # Consider active if committed in the last 90 days
        days_since_last = (datetime.now() - contributor["last_commit"]).days
        return days_since_last <= 90

    def _determine_development_phase(
        self,
        commits: List[CommitInfo]
    ) -> DevelopmentPhase:
        """Determine the current development phase."""
        if not commits:
            return DevelopmentPhase.INITIALIZATION

        # Get recent activity (last 30 days)
        now = datetime.now()
        recent_cutoff = now - timedelta(days=30)
        recent_commits = [c for c in commits if c.timestamp > recent_cutoff]

        # Get total project age
        project_start = commits[0].timestamp
        project_age_days = (now - project_start).days

        # Analyze commit patterns
        monthly_commits = self._group_commits_by_month(commits)

        # Phase determination logic
        if project_age_days < 30:
            return DevelopmentPhase.INITIALIZATION
        elif len(recent_commits) == 0:
            return DevelopmentPhase.DECLINE
        elif len(recent_commits) < 5:
            return DevelopmentPhase.MAINTENANCE
        else:
            # Check for refactoring patterns
            recent_messages = [c.message.lower() for c in recent_commits]
            refactor_count = sum(1 for msg in recent_messages if any(keyword in msg for keyword in self.refactor_keywords))

            if refactor_count > len(recent_commits) * 0.3:
                return DevelopmentPhase.REFACTORING

            # Check activity level
            avg_recent_commits = len(recent_commits) / 30
            if avg_recent_commits > 2:
                return DevelopmentPhase.RAPID_DEVELOPMENT
            else:
                return DevelopmentPhase.STABLE_DEVELOPMENT

    def _calculate_activity_level(
        self,
        commits: List[CommitInfo]
    ) -> ActivityLevel:
        """Calculate current activity level."""
        if not commits:
            return ActivityLevel.VERY_LOW

        # Get commits from last 30 days
        now = datetime.now()
        recent_commits = [c for c in commits if c.timestamp > now - timedelta(days=30)]

        commits_per_day = len(recent_commits) / 30

        if commits_per_day < 0.1:
            return ActivityLevel.VERY_LOW
        elif commits_per_day < 0.5:
            return ActivityLevel.LOW
        elif commits_per_day < 2:
            return ActivityLevel.MODERATE
        elif commits_per_day < 5:
            return ActivityLevel.HIGH
        else:
            return ActivityLevel.VERY_HIGH

    def _estimate_team_size(
        self,
        contributors: Dict[str, Dict[str, Any]],
        project_age: timedelta
    ) -> TeamSize:
        """Estimate team size based on contributor patterns."""
        active_count = len([
            c for c in contributors.values()
            if self._is_active_developer(c)
        ])

        # Consider historical maximum
        max_concurrent = self._estimate_max_concurrent_contributors(contributors)

        # Use the larger of current active or historical max
        estimated_size = max(active_count, max_concurrent)

        if estimated_size <= 1:
            return TeamSize.SOLO
        elif estimated_size <= 5:
            return TeamSize.SMALL
        elif estimated_size <= 15:
            return TeamSize.MEDIUM
        elif estimated_size <= 50:
            return TeamSize.LARGE
        else:
            return TeamSize.ENTERPRISE

    def _estimate_max_concurrent_contributors(
        self,
        contributors: Dict[str, Dict[str, Any]]
    ) -> int:
        """Estimate maximum number of concurrent contributors."""
        # Group contributors by month
        monthly_contributors = defaultdict(set)

        for email, data in contributors.items():
            if data["first_commit"] and data["last_commit"]:
                # Generate all months this contributor was active
                current = data["first_commit"].replace(day=1)
                end = data["last_commit"].replace(day=1)

                while current <= end:
                    monthly_contributors[current].add(email)
                    # Move to next month
                    if current.month == 12:
                        current = current.replace(year=current.year + 1, month=1)
                    else:
                        current = current.replace(month=current.month + 1)

        # Find month with most contributors
        if monthly_contributors:
            max_month = max(monthly_contributors.values(), key=len)
            return len(max_month)

        return 0

    def _detect_development_patterns(
        self,
        commits: List[CommitInfo]
    ) -> List[DevelopmentPattern]:
        """Detect development patterns in commit history."""
        patterns = []

        # Group commits by month for pattern analysis
        monthly_commits = self._group_commits_by_month(commits)

        for month, month_commits in monthly_commits.items():
            # Analyze each pattern type
            for pattern_name, pattern_info in self.development_patterns.items():
                if self._matches_pattern(month_commits, pattern_info["indicators"]):
                    pattern = DevelopmentPattern(
                        pattern_type=pattern_name,
                        confidence=self._calculate_pattern_confidence(month_commits, pattern_name),
                        description=pattern_info["description"],
                        evidence=self._gather_pattern_evidence(month_commits, pattern_name),
                        timeframe=(month, month.replace(day=28))  # Approximate month end
                    )
                    patterns.append(pattern)

        return patterns

    def _group_commits_by_month(
        self,
        commits: List[CommitInfo]
    ) -> Dict[datetime, List[CommitInfo]]:
        """Group commits by month."""
        monthly = defaultdict(list)

        for commit in commits:
            month_key = commit.timestamp.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            monthly[month_key].append(commit)

        return dict(monthly)

    def _matches_pattern(
        self,
        commits: List[CommitInfo],
        indicators: List[str]
    ) -> bool:
        """Check if commits match a pattern based on indicators."""
        # This is a simplified pattern matching
        # In practice, you would implement specific logic for each pattern

        for indicator in indicators:
            if indicator == "high_commit_density":
                if len(commits) > 50:  # More than 50 commits in a month
                    return True
            elif indicator == "deadline_proximity":
                # Check for commits near month-end
                month_end_commits = [c for c in commits if c.timestamp.day > 25]
                if len(month_end_commits) > len(commits) * 0.4:
                    return True
            elif indicator == "weekend_commits":
                weekend_commits = [c for c in commits if c.timestamp.weekday() >= 5]
                if len(weekend_commits) > len(commits) * 0.3:
                    return True
            elif indicator == "night_commits":
                night_commits = [c for c in commits if c.timestamp.hour < 6 or c.timestamp.hour > 22]
                if len(night_commits) > len(commits) * 0.4:
                    return True
            elif indicator == "refactor_keywords":
                refactor_count = sum(1 for c in commits if any(keyword in c.message.lower() for keyword in self.refactor_keywords))
                if refactor_count > len(commits) * 0.2:
                    return True
            elif indicator == "doc_commits":
                doc_count = sum(1 for c in commits if any(keyword in c.message.lower() for keyword in self.doc_keywords))
                if doc_count > len(commits) * 0.3:
                    return True
            elif indicator == "test_commits":
                test_count = sum(1 for c in commits if any(keyword in c.message.lower() for keyword in self.test_keywords))
                if test_count > len(commits) * 0.4:
                    return True
            elif indicator == "fix_commits":
                fix_count = sum(1 for c in commits if any(keyword in c.message.lower() for keyword in self.fix_keywords))
                if fix_count > len(commits) * 0.5:
                    return True

        return False

    def _calculate_pattern_confidence(
        self,
        commits: List[CommitInfo],
        pattern_name: str
    ) -> float:
        """Calculate confidence score for a pattern."""
        # This is a simplified confidence calculation
        # In practice, you would use more sophisticated metrics

        if pattern_name == "spike_activity":
            commit_density = len(commits) / 30  # Commits per day
            return min(commit_density / 3, 1.0)  # Normalize to 0-1
        elif pattern_name == "weekend_warrior":
            weekend_ratio = len([c for c in commits if c.timestamp.weekday() >= 5]) / len(commits)
            return weekend_ratio
        elif pattern_name == "night_owl":
            night_ratio = len([c for c in commits if c.timestamp.hour < 6 or c.timestamp.hour > 22]) / len(commits)
            return night_ratio
        elif pattern_name in ["refactoring_burst", "documentation_focus", "testing_spree", "bug_fix_cycle"]:
            # Count keyword matches
            keywords = {
                "refactoring_burst": self.refactor_keywords,
                "documentation_focus": self.doc_keywords,
                "testing_spree": self.test_keywords,
                "bug_fix_cycle": self.fix_keywords
            }
            keyword_count = sum(1 for c in commits if any(keyword in c.message.lower() for keyword in keywords[pattern_name]))
            return min(keyword_count / len(commits), 1.0)

        return 0.5

    def _gather_pattern_evidence(
        self,
        commits: List[CommitInfo],
        pattern_name: str
    ) -> List[str]:
        """Gather evidence for a detected pattern."""
        evidence = []

        if pattern_name == "spike_activity":
            evidence.append(f"{len(commits)} commits in single month")
        elif pattern_name == "weekend_warrior":
            weekend_count = len([c for c in commits if c.timestamp.weekday() >= 5])
            evidence.append(f"{weekend_count} commits on weekends")
        elif pattern_name == "night_owl":
            night_count = len([c for c in commits if c.timestamp.hour < 6 or c.timestamp.hour > 22])
            evidence.append(f"{night_count} commits during night hours")
        elif pattern_name == "refactoring_burst":
            refactors = [c.message for c in commits if any(keyword in c.message.lower() for keyword in self.refactor_keywords)]
            evidence.append(f"Refactoring commits: {', '.join(refactors[:3])}")
        elif pattern_name == "documentation_focus":
            docs = [c.message for c in commits if any(keyword in c.message.lower() for keyword in self.doc_keywords)]
            evidence.append(f"Documentation commits: {', '.join(docs[:3])}")
        elif pattern_name == "testing_spree":
            tests = [c.message for c in commits if any(keyword in c.message.lower() for keyword in self.test_keywords)]
            evidence.append(f"Test commits: {', '.join(tests[:3])}")
        elif pattern_name == "bug_fix_cycle":
            fixes = [c.message for c in commits if any(keyword in c.message.lower() for keyword in self.fix_keywords)]
            evidence.append(f"Bug fix commits: {', '.join(fixes[:3])}")

        return evidence

    async def _create_developer_profiles(
        self,
        commits: List[CommitInfo]
    ) -> Dict[str, DeveloperProfile]:
        """Create detailed developer profiles."""
        profiles = {}

        # Group commits by developer
        developer_commits = defaultdict(list)
        for commit in commits:
            developer_commits[commit.email].append(commit)

        for email, dev_commits in developer_commits.items():
            if not dev_commits:
                continue

            # Calculate statistics
            commit_count = len(dev_commits)
            first_commit = min(c.timestamp for c in dev_commits)
            last_commit = max(c.timestamp for c in dev_commits)

            # Calculate average commits per month
            active_months = self._calculate_active_months(dev_commits)
            avg_commits_per_month = commit_count / max(active_months, 1)

            # Preferred working hours
            hour_counts = Counter(c.timestamp.hour for c in dev_commits)
            preferred_hours = [hour for hour, count in hour_counts.most_common(3)]

            # File types worked on
            file_types = defaultdict(int)
            for commit in dev_commits:
                # Extract file types from commit message (simplified)
                for ext in [".py", ".js", ".ts", ".java", ".go", ".cpp", ".h", ".md", ".yml", ".json"]:
                    if ext in commit.message.lower() or any(
                        commit.message.lower().endswith(ext)
                        for ext in [".py", ".js", ".ts", ".java", ".go"]
                    ):
                        file_types[ext] += 1

            # Average changes per commit
            total_changes = sum(c.insertions + c.deletions for c in dev_commits)
            avg_changes = total_changes / commit_count if commit_count > 0 else 0

            # Check if active
            is_active = self._is_active_developer({
                "last_commit": last_commit,
                "commit_count": commit_count
            })

            profile = DeveloperProfile(
                name=dev_commits[0].author,
                email=email,
                commit_count=commit_count,
                first_commit=first_commit,
                last_commit=last_commit,
                avg_commits_per_month=avg_commits_per_month,
                preferred_hours=preferred_hours,
                file_types=dict(file_types),
                avg_changes_per_commit=avg_changes,
                is_active=is_active
            )
            profiles[email] = profile

        return profiles

    def _calculate_active_months(self, commits: List[CommitInfo]) -> int:
        """Calculate number of months with commits."""
        months = set()
        for commit in commits:
            month_key = commit.timestamp.replace(day=1)
            months.add(month_key)
        return len(months)

    def _calculate_commit_frequency(
        self,
        commits: List[CommitInfo]
    ) -> Dict[str, int]:
        """Calculate commit frequency by time period."""
        frequency = {
            "daily": 0,
            "weekly": 0,
            "monthly": 0,
            "yearly": 0
        }

        if not commits:
            return frequency

        # Get project timespan
        project_start = commits[0].timestamp
        project_end = commits[-1].timestamp
        project_duration = project_end - project_start

        # Calculate frequencies
        frequency["daily"] = len(commits) / max(project_duration.days, 1)
        frequency["weekly"] = len(commits) / max(project_duration.days / 7, 1)
        frequency["monthly"] = len(commits) / max(project_duration.days / 30, 1)
        frequency["yearly"] = len(commits) / max(project_duration.days / 365, 1)

        # Round to integers
        return {k: round(v) for k, v in frequency.items()}

    def _calculate_bus_factor(
        self,
        commits: List[CommitInfo],
        contributors: Dict[str, Dict[str, Any]]
    ) -> int:
        """Calculate bus factor (number of developers who know >50% of codebase)."""
        if not commits:
            return 0

        # Calculate contribution percentages
        total_changes = sum(
            sum(c.insertions + c.deletions for c in commits if c.email == email)
            for email in contributors
        )

        if total_changes == 0:
            return 0

        contributor_percentages = []
        for email in contributors:
            changes = sum(
                c.insertions + c.deletions
                for c in commits
                if c.email == email
            )
            percentage = changes / total_changes
            contributor_percentages.append((email, percentage))

        # Sort by contribution percentage
        contributor_percentages.sort(key=lambda x: x[1], reverse=True)

        # Calculate bus factor
        cumulative = 0
        bus_factor = 0

        for email, percentage in contributor_percentages:
            cumulative += percentage
            bus_factor += 1
            if cumulative >= 0.5:
                break

        return bus_factor

    def _identify_risk_indicators(
        self,
        commits: List[CommitInfo],
        contributors: Dict[str, Dict[str, Any]],
        patterns: List[DevelopmentPattern]
    ) -> List[str]:
        """Identify project risk indicators."""
        risks = []

        # Contributor concentration risk
        if len(contributors) <= 1:
            risks.append("Single point of failure - only one contributor")

        # Activity risk
        recent_commits = [c for c in commits if c.timestamp > datetime.now() - timedelta(days=30)]
        if len(recent_commits) == 0:
            risks.append("Project appears abandoned - no recent commits")

        # Bus factor risk
        bus_factor = self._calculate_bus_factor(commits, contributors)
        if bus_factor <= 1:
            risks.append("Low bus factor - knowledge concentrated in few developers")

        # Pattern-based risks
        pattern_types = [p.pattern_type for p in patterns]
        if "bug_fix_cycle" in pattern_types:
            risks.append("Recurring bug fixing patterns detected")

        if "decline" in pattern_types:
            risks.append("Declining development activity")

        # Large commits risk
        large_commits = [c for c in commits if c.insertions + c.deletions > 1000]
        if len(large_commits) > len(commits) * 0.1:
            risks.append("Large commits detected - potential code quality issues")

        # Merge frequency risk
        merge_commits = [c for c in commits if c.is_merge]
        if len(merge_commits) > len(commits) * 0.3:
            risks.append("High merge frequency - potential branching issues")

        return risks

    def _generate_context_recommendations(
        self,
        development_phase: DevelopmentPhase,
        activity_level: ActivityLevel,
        team_size: TeamSize,
        risk_indicators: List[str]
    ) -> List[str]:
        """Generate recommendations based on context analysis."""
        recommendations = []

        # Phase-based recommendations
        if development_phase == DevelopmentPhase.INITIALIZATION:
            recommendations.append("Establish project structure and coding standards")
            recommendations.append("Set up CI/CD pipeline early")
        elif development_phase == DevelopmentPhase.RAPID_DEVELOPMENT:
            recommendations.append("Focus on maintaining code quality during rapid growth")
            recommendations.append("Consider code reviews for all changes")
        elif development_phase == DevelopmentPhase.MAINTENANCE:
            recommendations.append("Plan for feature updates or project retirement")
            recommendations.append("Document maintenance procedures")
        elif development_phase == DevelopmentPhase.DECLINE:
            recommendations.append("Assess project viability and user needs")
            recommendations.append("Consider sunsetting or archiving the project")

        # Activity-based recommendations
        if activity_level in [ActivityLevel.VERY_LOW, ActivityLevel.LOW]:
            recommendations.append("Increase development activity to maintain project health")

        # Team size recommendations
        if team_size == TeamSize.SOLO:
            recommendations.append("Document code extensively for future maintainers")
            recommendations.append("Consider onboarding additional contributors")

        # Risk-based recommendations
        if "Single point of failure" in risk_indicators:
            recommendations.append("Immediately onboard additional contributors")

        if "Low bus factor" in risk_indicators:
            recommendations.append("Implement knowledge sharing practices")
            recommendations.append("Cross-train team members on critical components")

        if "Project appears abandoned" in risk_indicators:
            recommendations.append("Communicate project status to stakeholders")
            recommendations.append("Consider transferring ownership or archiving")

        return recommendations

    def _get_git_version(self) -> str:
        """Get git version."""
        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return "Unknown"

    def get_contributor_heatmap(
        self,
        commits: List[CommitInfo],
        granularity: str = "month"
    ) -> Dict[str, Any]:
        """Generate contributor activity heatmap."""
        heatmap = defaultdict(lambda: defaultdict(int))

        for commit in commits:
            if granularity == "month":
                time_key = commit.timestamp.strftime("%Y-%m")
            elif granularity == "week":
                # Week number
                time_key = f"{commit.timestamp.year}-W{commit.timestamp.isocalendar()[1]:02d}"
            else:  # day
                time_key = commit.timestamp.strftime("%Y-%m-%d")

            heatmap[commit.email][time_key] += 1

        return dict(heatmap)

    def get_project_velocity(
        self,
        commits: List[CommitInfo],
        window_days: int = 30
    ) -> Dict[str, Any]:
        """Calculate project velocity metrics."""
        if not commits:
            return {"velocity": 0, "trend": "stable"}

        # Group commits by time windows
        windows = []
        now = datetime.now()

        for i in range(6):  # Last 6 windows
            window_end = now - timedelta(days=i * window_days)
            window_start = now - timedelta(days=(i + 1) * window_days)

            window_commits = [
                c for c in commits
                if window_start <= c.timestamp < window_end
            ]
            windows.append(len(window_commits))

        # Calculate velocity (commits per window)
        current_velocity = windows[0] if windows else 0
        avg_velocity = statistics.mean(windows) if windows else 0

        # Determine trend
        if len(windows) >= 3:
            if windows[0] > windows[1] > windows[2]:
                trend = "increasing"
            elif windows[0] < windows[1] < windows[2]:
                trend = "decreasing"
            else:
                trend = "stable"
        else:
            trend = "stable"

        return {
            "current_velocity": current_velocity,
            "average_velocity": avg_velocity,
            "trend": trend,
            "windows": windows
        }

    def get_code_churn_analysis(
        self,
        commits: List[CommitInfo]
    ) -> Dict[str, Any]:
        """Analyze code churn (additions/deletions)."""
        if not commits:
            return {"total_churn": 0, "churn_rate": 0}

        total_churn = sum(c.insertions + c.deletions for c in commits)

        # Calculate churn rate (changes per day)
        project_span = commits[-1].timestamp - commits[0].timestamp
        churn_rate = total_churn / max(project_span.days, 1)

        # Analyze churn by time
        monthly_churn = self._calculate_monthly_churn(commits)

        return {
            "total_churn": total_churn,
            "churn_rate": round(churn_rate, 2),
            "monthly_churn": monthly_churn,
            "avg_commit_size": statistics.mean([c.insertions + c.deletions for c in commits])
        }

    def _calculate_monthly_churn(
        self,
        commits: List[CommitInfo]
    ) -> Dict[str, int]:
        """Calculate code churn by month."""
        monthly_churn = defaultdict(int)

        for commit in commits:
            month_key = commit.timestamp.strftime("%Y-%m")
            monthly_churn[month_key] += commit.insertions + commit.deletions

        return dict(monthly_churn)