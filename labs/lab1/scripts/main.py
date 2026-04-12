#!/usr/bin/env python3
"""Lab 1 Main Script: Python Basics and Environment Configuration"""

import os
import sys


def check_python_version():
    """Check Python version"""
    print(f"Python版本: {sys.version}")
    print(f"Python路径: {sys.executable}")
    return True


def check_environment():
    """Check environment configuration"""
    print("\n环境配置检查:")
    print(f"当前目录: {os.getcwd()}")
    print(f"用户目录: {os.path.expanduser('~')}")
    print(f"环境变量: {dict(os.environ)}")
    return True


def basic_operations():
    """Demonstrate basic operations"""
    print("\nBasic Operations Demo:")

    # String operations
    text = "Hello, DevOps!"
    print(f"String: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")

    # List operations
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers)}")

    # Dictionary operations
    config = {"name": "Lab 1", "version": "1.0"}
    print(f"Dictionary: {config}")

    return True


def main():
    """Main function"""
    print("=" * 50)
    print("Lab 1: Python Basics and Environment Configuration")
    print("=" * 50)

    try:
        check_python_version()
        check_environment()
        basic_operations()

        print("\n" + "=" * 50)
        print("Experiment completed!")
        print("=" * 50)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
