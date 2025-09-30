"""
Main CLI entry point for specify-cli.
Target: ~80 LOC
"""
import click

from specify_cli import __version__


@click.group()
@click.version_option(version=__version__, prog_name="specify-cli")
@click.pass_context
def main(ctx):
    """
    Spec-Kit v2.0 - Simple, template-driven specifications for AI agents.
    
    A minimalist framework that empowers AI agents with high-quality templates
    and validation scripts—no complex analysis engines required.
    """
    ctx.ensure_object(dict)


# Import commands
# Note: init command is in __init__.py for backward compatibility
# Import check command from new modular structure
try:
    from specify_cli.commands.check import app as check_app
    main.add_command(check_app, name="check")
except ImportError:
    # Fallback if commands module not available
    pass


if __name__ == "__main__":
    main()
