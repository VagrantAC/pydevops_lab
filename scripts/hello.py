#!/usr/bin/env python3
"""Hello script for Python DevOps Lab."""

import click


@click.command()
@click.option("--name", default="World", help="Name to greet")
def hello(name: str) -> None:
    """Greet the user."""
    click.echo(f"Hello, {name}! Welcome to Python DevOps Lab!")


if __name__ == "__main__":
    hello()
