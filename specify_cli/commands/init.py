"""Init command - delegates to main __init__.py for backward compatibility."""
import typer
from specify_cli import app as main_app

# Re-export the init command from main module
# This maintains backward compatibility while providing modular structure
init = main_app.registered_commands[0] if main_app.registered_commands else None

if __name__ == "__main__":
    typer.run(init)
