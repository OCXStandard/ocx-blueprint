#  Copyright (c) {{cookiecutter.year }}. OCX Consortium https://3docx.org. See the LICENSE
""" CLI script tests."""
import pytest
from typer.testing import CliRunner

from {{ cookiecutter.package_slug }} import __version__
from {{ cookiecutter.package_slug }}.cli import {{ cookiecutter.app_name }}


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke({{ cookiecutter.app_name }}, ['version'])
    assert result.exit_code == 0
    assert __version__ in result.output

def test_cli_greet():
    runner = CliRunner()
    name = 'John'
    surname = 'Doe'
    result = runner.invoke({{ cookiecutter.app_name }}, ['greet', name, '--surname', surname])
    assert result.exit_code == 0
    assert surname in result.stdout
