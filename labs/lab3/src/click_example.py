#!/usr/bin/env python3
"""
Command-line tool using click
"""
import click


@click.group()
def cli() -> None:
    pass


@click.group(help="Ship related commands")
def ships() -> None:
    pass


cli.add_command(ships)


@ships.command(help="Sail a ship")
def sail() -> None:
    ship_name = "Your Ship"
    print(f"{ship_name} is setting sail")


@ships.command(help="List all of the ships")
def list_ships() -> None:
    ships = ["John B", "Yankee Clipper", "Pequod"]
    print(f"Ships: {', '.join(ships)}")


@cli.command(help="Talk to a sailor")
@click.option("--greeting", default="Ahoy there", help="How do you want to be greeted?")
@click.argument("name")
def sailors(greeting: str, name: str) -> None:
    message = f"{greeting}, {name}"
    print(message)


if __name__ == "__main__":
    cli()
