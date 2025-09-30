"""Check command - validation and diagnostics."""
import typer
import subprocess
import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

app = typer.Typer(help="Run validation checks on your Specify project")


@app.command()
def check(
    tags: bool = typer.Option(False, "--tags", help="Validate code tags (TODO/FIXME/TASK-XXX)"),
    dependencies: bool = typer.Option(False, "--dependencies", help="Check dependencies for vulnerabilities"),
    tasks: bool = typer.Option(False, "--tasks", help="Sync task tracking (YAML ↔ code ↔ git)"),
    all: bool = typer.Option(False, "--all", help="Run all checks"),
):
    """
    Run validation checks on your Specify project.
    
    Examples:
        specify check --tags
        specify check --dependencies
        specify check --tasks
        specify check --all
    """
    if not any([tags, dependencies, tasks, all]):
        console.print("[yellow]No checks specified. Use --help to see available options.[/yellow]")
        console.print("[dim]Hint: Use --all to run all checks[/dim]")
        raise typer.Exit(0)
    
    if all:
        tags = dependencies = tasks = True
    
    # Check if we're in a Specify project
    specify_dir = Path(".specify")
    if not specify_dir.exists():
        console.print("[red]Error:[/red] Not in a Specify project directory")
        console.print("[dim]Run 'specify init' to initialize a project[/dim]")
        raise typer.Exit(1)
    
    results = {}
    
    # Run tag validation
    if tags:
        console.print("\n[cyan]Validating code tags...[/cyan]")
        try:
            result = subprocess.run(
                ["bash", ".specify/scripts/bash/validate-tags.sh", "--json"],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0 and result.stdout:
                results['tags'] = json.loads(result.stdout)
                display_tag_results(results['tags'])
            else:
                console.print("[yellow]Tag validation script not available or returned no data[/yellow]")
        except Exception as e:
            console.print(f"[red]Error running tag validation:[/red] {e}")
    
    # Run dependency check
    if dependencies:
        console.print("\n[cyan]Checking dependencies...[/cyan]")
        try:
            result = subprocess.run(
                ["bash", ".specify/scripts/bash/check-dependencies.sh", "--json"],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0 and result.stdout:
                results['dependencies'] = json.loads(result.stdout)
                display_dependency_results(results['dependencies'])
            else:
                console.print("[yellow]Dependency check script not available or returned no data[/yellow]")
        except Exception as e:
            console.print(f"[red]Error running dependency check:[/red] {e}")
    
    # Run task sync
    if tasks:
        console.print("\n[cyan]Synchronizing task tracking...[/cyan]")
        try:
            result = subprocess.run(
                ["bash", ".specify/scripts/bash/sync-tasks.sh", "--validate", "--json"],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0 and result.stdout:
                results['tasks'] = json.loads(result.stdout)
                display_task_results(results['tasks'])
            else:
                console.print("[yellow]Task sync script not available or returned no data[/yellow]")
        except Exception as e:
            console.print(f"[red]Error running task sync:[/red] {e}")
    
    # Summary
    console.print("\n[bold]Check Summary:[/bold]")
    if results:
        for check_type, data in results.items():
            status = data.get('status', 'unknown')
            if status == 'ok' or status == 'stub':
                console.print(f"  ✓ {check_type}: [green]{status}[/green]")
            else:
                console.print(f"  ⚠ {check_type}: [yellow]{status}[/yellow]")
    else:
        console.print("  [dim]No checks completed[/dim]")


def display_tag_results(data: dict):
    """Display tag validation results."""
    orphaned = data.get('orphaned_todos', [])
    metadata_issues = data.get('metadata_issues', [])
    
    if not orphaned and not metadata_issues:
        console.print("[green]✓[/green] No tag issues found")
        return
    
    if orphaned:
        console.print(f"\n[yellow]⚠ Found {len(orphaned)} orphaned TODOs (missing TASK-XXX):[/yellow]")
        for item in orphaned[:5]:  # Show first 5
            console.print(f"  - {item}")
        if len(orphaned) > 5:
            console.print(f"  [dim]... and {len(orphaned) - 5} more[/dim]")
    
    if metadata_issues:
        console.print(f"\n[yellow]⚠ Found {len(metadata_issues)} metadata issues:[/yellow]")
        for item in metadata_issues[:5]:
            console.print(f"  - {item}")
        if len(metadata_issues) > 5:
            console.print(f"  [dim]... and {len(metadata_issues) - 5} more[/dim]")


def display_dependency_results(data: dict):
    """Display dependency check results."""
    vulnerabilities = data.get('vulnerabilities', [])
    outdated = data.get('outdated', [])
    
    if not vulnerabilities and not outdated:
        console.print("[green]✓[/green] No dependency issues found")
        return
    
    if vulnerabilities:
        console.print(f"\n[red]⚠ Found {len(vulnerabilities)} vulnerabilities:[/red]")
        table = Table(show_header=True)
        table.add_column("Package")
        table.add_column("Severity")
        table.add_column("Fix")
        
        for vuln in vulnerabilities[:5]:
            table.add_row(
                vuln.get('package', 'unknown'),
                vuln.get('severity', 'unknown'),
                vuln.get('fix_available', 'none')
            )
        console.print(table)
        if len(vulnerabilities) > 5:
            console.print(f"[dim]... and {len(vulnerabilities) - 5} more[/dim]")
    
    if outdated:
        console.print(f"\n[yellow]ℹ {len(outdated)} outdated packages[/yellow]")


def display_task_results(data: dict):
    """Display task sync results."""
    status = data.get('status', 'unknown')
    misalignments = data.get('misalignments', [])
    warnings = data.get('warnings', [])
    
    if status == 'ok' and not misalignments and not warnings:
        console.print("[green]✓[/green] Tasks are synchronized")
        return
    
    if misalignments:
        console.print(f"\n[red]⚠ Found {len(misalignments)} misalignments:[/red]")
        for item in misalignments[:5]:
            console.print(f"  - {item}")
        if len(misalignments) > 5:
            console.print(f"  [dim]... and {len(misalignments) - 5} more[/dim]")
    
    if warnings:
        console.print(f"\n[yellow]⚠ {len(warnings)} warnings:[/yellow]")
        for item in warnings[:3]:
            console.print(f"  - {item}")
        if len(warnings) > 3:
            console.print(f"  [dim]... and {len(warnings) - 3} more[/dim]")


if __name__ == "__main__":
    app()
