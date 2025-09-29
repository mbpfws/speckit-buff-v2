"""
Test helper utilities for spec-kit tests.
"""
from pathlib import Path
from typing import Dict, List


def create_artifact(path: Path, frontmatter: Dict[str, any], content: str = "") -> None:
    """
    Create an artifact file with YAML frontmatter.
    
    Args:
        path: Path to artifact file
        frontmatter: Dictionary of frontmatter fields
        content: Markdown content after frontmatter
    """
    import yaml
    
    yaml_str = yaml.dump(frontmatter, default_flow_style=False)
    full_content = f"---\n{yaml_str}---\n\n{content}"
    path.write_text(full_content)


def parse_validation_output(output: str) -> Dict[str, List[str]]:
    """
    Parse validation script output into structured format.
    
    Args:
        output: Raw output from validation script
        
    Returns:
        Dictionary with 'info', 'warn', 'error' lists
    """
    import re
    
    result = {'info': [], 'warn': [], 'error': []}
    pattern = r'\[(INFO|WARN|ERROR)\]\s+(.+)'
    
    for line in output.splitlines():
        match = re.match(pattern, line)
        if match:
            level = match.group(1).lower()
            message = match.group(2)
            result[level].append(message)
    
    return result


def count_loc(file_path: Path, exclude_comments: bool = True, exclude_blank: bool = True) -> int:
    """
    Count lines of code in a Python file.
    
    Args:
        file_path: Path to Python file
        exclude_comments: Whether to exclude comment lines
        exclude_blank: Whether to exclude blank lines
        
    Returns:
        Line count
    """
    if not file_path.exists():
        return 0
    
    count = 0
    in_multiline_string = False
    
    for line in file_path.read_text().splitlines():
        stripped = line.strip()
        
        # Track multiline strings/comments
        if '"""' in line or "'''" in line:
            in_multiline_string = not in_multiline_string
            continue
        
        # Skip based on options
        if in_multiline_string:
            continue
        if exclude_blank and not stripped:
            continue
        if exclude_comments and stripped.startswith('#'):
            continue
        
        count += 1
    
    return count
