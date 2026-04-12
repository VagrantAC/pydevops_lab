import sys


def print_info() -> None:
    print(f"Byte order: {sys.byteorder}")
    print(f"Int Size: {sys.getsizeof(1)}")
    print(f"Float Size: {sys.getsizeof(1.0)}")
    print(f"Platform: {sys.platform}")

    if sys.version_info.major < 3:
        print("You need to update you Python version")
    elif sys.version_info.minor < 7:
        print("You are not running the lastest version of Python")
    else:
        print("All is good")
    return None


if __name__ == "__main__":
    print_info()
