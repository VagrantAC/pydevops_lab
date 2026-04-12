#!/usr/bin/env python3
"""
Simple command-line tool using sys.argv
"""

import sys


def say_it(greeting: str, target: str) -> None:
    message = f"{greeting} {target}"
    print(message)


if __name__ == "__main__":
    greeting = "Hello"
    target = "Joe"

    if "--help" in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()

    if "--name" in sys.argv:
        name_index = int(sys.argv[sys.argv.index("--name") + 1])
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if "--greeting" in sys.argv:
        greeting_index = int(sys.argv[sys.argv.index("--greeting") + 1])
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)
