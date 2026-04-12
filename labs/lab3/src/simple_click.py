#!/usr/bin/env python3
"""
Simple click tool
"""
import click


@click.command()
@click.option("--greeting", default="Hiya", help="How do you want to be greeted?")
@click.option("--name", default="World", help="What is your name?")
def greet(greeting: str, name: str) -> None:
    click.echo(f"{greeting}, {name}!")


if __name__ == "__main__":
    greet()
