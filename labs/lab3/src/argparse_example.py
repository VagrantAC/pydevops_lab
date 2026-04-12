#!/usr/bin/env python3
"""
Command-line tool using argparse
"""

import argparse


def sail() -> None:
    ship_nane = "Your ship"
    print(f"{ship_nane} is setting sail")


def list_ships() -> None:
    ships = ["John B", "Yankee Clipper", "Requod"]
    print(f"Ships: {', '.join(ships)}")


def greet(greeting: str, name: str) -> None:
    message = f"{greeting}, {name}"
    print(message)


# ./argparse_example.py --help
### usage: argparse_example.py [-h] [--twice] {ship,sailor} ...
##
### Maritime control
##
### positional arguments:
###   {ship,sailor}
###     ship         Ship related commands
###     sailor       Talk to a sailor
##
### options:
###   -h, --help     show this help message and exit
###   --twice, -t    Do it twice

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maritime control")

    # Global arguments
    parser.add_argument("--twice", "-t", help="Do it twice", action="store_true")

    subparsers = parser.add_subparsers(dest="func")

    # Ship subparser
    ship_parser = subparsers.add_parser("ship", help="Ship related commands")
    # Ship subparser arguments
    ship_parser.add_argument("command", choices=["sail", "list"])

    # Sailor subparser
    sailor_parser = subparsers.add_parser("sailor", help="Talk to a sailor")
    # Sailor subparser arguments
    sailor_parser.add_argument("name", help="Sailors name")
    sailor_parser.add_argument(
        "--greeting", "-g", help="Greeting", default="Ahoy there"
    )

    args = parser.parse_args()
    if args.func == "sailor":
        greet(args.greeting, args.name)
    elif args.command == "list":
        list_ships()
    else:
        sail()
