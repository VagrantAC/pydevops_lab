import os
import subprocess
import sys

# import say_it


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


def use_os() -> None:
    print(f"Current directory: {os.getcwd()}")
    os.chdir("/tmp")
    print(f"Current directory: {os.getcwd()}")

    print(f"Environment variable LOGLEVEL: {os.environ.get('LOGLEVEL')}")
    os.environ["LOGLEVEL"] = "DEBUG"
    print(f"Environment variable LOGLEVEL: {os.environ.get('LOGLEVEL')}")
    print(f"get login name: {os.getlogin()}")
    return None


def use_subprocess() -> None:
    cp = subprocess.run(["ls", "-l"], capture_output=True, universal_newlines=True)
    print(f"ls -l output: {cp.stdout}")

    cp = subprocess.run(
        ["ls", "/doesnotexist"], capture_output=True, universal_newlines=True
    )
    print(f"ls -l output: {cp.stderr}")

    cp = subprocess.run(
        ["ls", "/doesnotexist"],
        capture_output=True,
        universal_newlines=True,
        check=True,
    )
    print(f"ls -l output: {cp.stderr}")


def say_it() -> None:
    greeting = "Hello"
    target = "World"
    message = f"{greeting} {target}"
    print(message)


if __name__ == "__main__":
    # print_info()
    # use_os()
    # use_subprocess()
    say_it()
