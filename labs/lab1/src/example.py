"""Lab 1 Source Code Example"""


class Calculator:
    """Simple calculator class"""

    def __init__(self) -> None:
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        """Addition"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtraction"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiplication"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Division"""
        if b == 0:
            raise ValueError("Divisor cannot be zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self) -> list[str]:
        """Get calculation history"""
        return self.history


def main() -> None:
    """Main function example"""
    calc = Calculator()

    print("Calculator Example:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

    print("\nHistory:")
    for record in calc.get_history():
        print(f"  {record}")


if __name__ == "__main__":
    main()
