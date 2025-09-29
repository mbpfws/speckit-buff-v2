"""
Check command implementation.
Target: ~80 LOC
"""
import json
from pathlib import Path

import click
import yaml

from specify_cli.validators import run_validation_script, ValidationMessage


@click.command()
@click.argument("target_path", default=".", type=click.Path(exists=True))
@click.option("--quality", is_flag=True, help="Run quality tool checks")
@click.option("--validation", default="all", help="Which validations to run: all, structure, naming, frontmatter, none")
@click.option("--update-templates", is_flag=True, help="Check for template updates")
@click.option("--fix", is_flag=True, help="Attempt automatic fixes")
@click.option("--format", "output_format", default="text", type=click.Choice(["text", "json", "yaml"]), help="Output format")
@click.option("--verbose", is_flag=True, help="Show detailed output")
def check(target_path, quality, validation, update_templates, fix, output_format, verbose):
    """
    Verify project structure, run validation scripts, and optionally check quality tools.
    
    Performance target: <1 second.
    """
    cwd = Path.cwd()
    specify_dir = cwd / ".specify"
    
    # Check if .specify/ exists
    if not specify_dir.exists():
        click.secho("Error: .specify/ directory not found", fg="red", err=True)
        click.echo("Run 'specify init' to initialize project", err=True)
        raise click.Abort()
    
    # Collect validation results
    results = []
    
    # Run validation scripts
    if validation != "none":
        scripts_to_run = []
        
        if validation == "all":
            scripts_to_run = ["validate-structure", "validate-naming", "validate-frontmatter"]
        else:
            script_map = {
                "structure": "validate-structure",
                "naming": "validate-naming",
                "frontmatter": "validate-frontmatter"
            }
            if validation in script_map:
                scripts_to_run = [script_map[validation]]
        
        for script in scripts_to_run:
            result = run_validation_script(script, target_path)
            results.append(result)
    
    # Check for template updates
    if update_templates:
        from specify_cli.template_loader import check_for_updates, get_cached_version
        current = get_cached_version()
        latest = check_for_updates()
        if latest and current and latest != current:
            click.echo(f"\nTemplate update available: {current} → {latest}")
    
    # Output results
    if output_format == "json":
        _output_json(results)
    elif output_format == "yaml":
        _output_yaml(results)
    else:
        _output_text(results, verbose)
    
    # Exit code is always 0 (non-blocking philosophy)
    return 0


def _output_text(results, verbose):
    """Output results in human-readable text format."""
    total_info = total_warn = total_error = 0
    
    for result in results:
        # Count messages by level
        info = sum(1 for m in result.messages if m.level == "INFO")
        warn = sum(1 for m in result.messages if m.level == "WARN")
        error = sum(1 for m in result.messages if m.level == "ERROR")
        
        total_info += info
        total_warn += warn
        total_error += error
        
        # Show status
        if error > 0:
            click.secho("✗", fg="red", nl=False)
            status = "FAIL"
        elif warn > 0:
            click.secho("⚠", fg="yellow", nl=False)
            status = "WARNINGS"
        else:
            click.secho("✓", fg="green", nl=False)
            status = "PASS"
        
        click.echo(f" {result.script_name}: {status}")
        
        # Show messages if verbose or if there are errors/warnings
        if verbose or warn > 0 or error > 0:
            for msg in result.messages:
                if msg.level == "ERROR":
                    click.secho(f"  [ERROR] {msg.message}", fg="red")
                elif msg.level == "WARN":
                    click.secho(f"  [WARN] {msg.message}", fg="yellow")
                elif verbose:
                    click.echo(f"  [INFO] {msg.message}")
    
    # Summary
    click.echo()
    click.echo("Summary:")
    click.echo(f"  Checks run: {len(results)}")
    click.echo(f"  Errors: {total_error}")
    click.echo(f"  Warnings: {total_warn}")
    click.echo(f"  Info: {total_info}")


def _output_json(results):
    """Output results in JSON format."""
    data = {
        "status": "pass" if all(r.exit_code == 0 for r in results) else "fail",
        "checks_run": len(results),
        "results": [
            {
                "script": r.script_name,
                "target": r.target,
                "exit_code": r.exit_code,
                "messages": [{"level": m.level, "message": m.message} for m in r.messages]
            }
            for r in results
        ]
    }
    click.echo(json.dumps(data, indent=2))


def _output_yaml(results):
    """Output results in YAML format."""
    data = {
        "status": "pass" if all(r.exit_code == 0 for r in results) else "fail",
        "checks_run": len(results),
        "results": [
            {
                "script": r.script_name,
                "target": r.target,
                "exit_code": r.exit_code,
                "messages": [{"level": m.level, "message": m.message} for m in r.messages]
            }
            for r in results
        ]
    }
    click.echo(yaml.dump(data, default_flow_style=False))
