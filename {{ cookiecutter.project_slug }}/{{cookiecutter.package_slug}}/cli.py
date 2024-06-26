#  Copyright (c) 2024. OCX Consortium https://3docx.org. See the LICENSE
"""Sample CLI with greeting."""
# System imports
from pathlib import Path
from typing import Any, Tuple
from rich import print

# 3rd party imports
import typer
from typing_extensions import Annotated
# Project imports
from {{cookiecutter.package_slug}} import __app_name__, __version__

{{cookiecutter.app_name}}  = typer.Typer(help="{{cookiecutter.short_project_description}}")



@{{cookiecutter.app_name}}.command()
def greet(
    name: str,
    surname: Annotated[str, typer.Option(help="The person surname")] = '',
):
    """Greet the person"""
    print(f'Hello {name} {surname}!')
@{{cookiecutter.app_name}}.command()
def version():
    print(__version__)


def cli_plugin() -> Tuple[str, Any]:
    """
    ClI plugin

    Returns the typer command object
    """
    typer_click_object = typer.main.get_command(__app_name__)
    return __app_name__, typer_click_object

if __name__ == "__main__":
    {{ cookiecutter.app_name }}()

