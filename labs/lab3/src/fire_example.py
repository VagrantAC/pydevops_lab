#!/usr/bin/env python3
"""
Command-line tool using fire
"""

import fire  # type: ignore


class Ships:
    def sail(self) -> None:
        ship_name = "Your Ship"
        print(f"{ship_name} is setting sail")

    def list_ships(self) -> None:
        ships = ["John B", "Yankee Clipper", "Pequod"]
        print(f"Ships: {', '.join(ships)}")


def sailors(greeting: str, name: str) -> None:
    message = f"{greeting}, {name}"
    print(message)


class Cli:
    def __init__(self) -> None:
        self.ships = Ships()
        self.sailors = sailors


if __name__ == "__main__":
    fire.Fire(Cli)
