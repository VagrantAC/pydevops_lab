#!/usr/bin/env python3
"""
Simple fire example
"""

import fire  # type: ignore


def greet(greeting: str = "Hiya", name: str = "Tammy") -> None:
    print(f"{greeting}, {name}")


def goodbye(goodbye: str = "Bye", name: str = "Tammy") -> None:
    print(f"{goodbye}, {name}")


if __name__ == "__main__":
    fire.Fire()
