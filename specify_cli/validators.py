"""
Validators module for executing validation scripts and parsing results.
Target: ~60 LOC
"""
import platform
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class ValidationMessage:
    """Individual validation message."""
    level: str  # INFO, WARN, ERROR
    message: str
    file: str = ""
    line: int = 0


@dataclass
class ValidationResult:
    """Result from validation script execution."""
    script_name: str
    target: str
    exit_code: int
    messages: List[ValidationMessage]


def detect_platform() -> str:
    """Detect current platform for script selection."""
    return "windows" if platform.system() == "Windows" else "unix"


def run_validation_script(script_name: str, target_path: str, platform_type: str = "auto") -> ValidationResult:
    """
    Execute a validation script and return structured results.
    
    Args:
        script_name: Name of validation script (e.g., "validate-structure")
        target_path: Path to validate
        platform_type: Platform type ('unix', 'windows', or 'auto')
        
    Returns:
        ValidationResult with parsed messages
    """
    if platform_type == "auto":
        platform_type = detect_platform()
    
    # Construct script path
    specify_dir = Path(".specify")
    if platform_type == "windows":
        script_path = specify_dir / "scripts" / "powershell" / f"{script_name}.ps1"
        cmd = ["powershell", "-File", str(script_path), target_path]
    else:
        script_path = specify_dir / "scripts" / "bash" / f"{script_name}.sh"
        cmd = ["bash", str(script_path), target_path]
    
    # Execute script
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        messages = parse_validation_output(result.stdout)
        
        return ValidationResult(
            script_name=script_name,
            target=target_path,
            exit_code=result.returncode,
            messages=messages
        )
    except subprocess.TimeoutExpired:
        return ValidationResult(
            script_name=script_name,
            target=target_path,
            exit_code=1,
            messages=[ValidationMessage("ERROR", f"Validation script {script_name} timed out")]
        )
    except FileNotFoundError:
        return ValidationResult(
            script_name=script_name,
            target=target_path,
            exit_code=1,
            messages=[ValidationMessage("ERROR", f"Validation script not found: {script_path}")]
        )


def parse_validation_output(output: str) -> List[ValidationMessage]:
    """Parse validation script output into structured messages."""
    import re
    
    messages = []
    pattern = r'\[(INFO|WARN|ERROR)\]\s+(.+)'
    
    for line in output.splitlines():
        match = re.match(pattern, line)
        if match:
            messages.append(ValidationMessage(
                level=match.group(1),
                message=match.group(2).strip()
            ))
    
    return messages
