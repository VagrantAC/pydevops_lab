from typing import Iterator


def print_all_args(**kwargs: str) -> None:
    for arg in kwargs:
        print(arg)


def is_uppercase(text: str) -> bool:
    for char in text:
        if not char.isupper():
            return False
    return True


def yield_event_or_odd() -> Iterator[str]:
    while True:
        yield "Even"
        yield "Odd"


print_all_args(a="1", b="2", c="3")

process = yield_event_or_odd()

for i in range(10):
    print(next(process))
