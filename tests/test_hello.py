"""Tests for hello script."""

from click.testing import CliRunner
from scripts.hello import hello


def test_hello_default() -> None:
    """Test hello with default name."""
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.exit_code == 0
    assert "Hello, World!" in result.output


def test_hello_with_name() -> None:
    """Test hello with custom name."""
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "DevOps"])
    assert result.exit_code == 0
    assert "Hello, DevOps!" in result.output
