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
from specify_cli.commands.init import init
from specify_cli.commands.check import check

main.add_command(init)
main.add_command(check)


if __name__ == "__main__":
    main()
