"""A small calculator plugin using explicit arithmetic operations."""

AUTHOR = "MURUGAN08ADS"
APP_NAME = "Simple Calculator"


def calculate(first: float, second: float, operation: str) -> float:
    """Return the result of applying an arithmetic operation to two numbers."""
    if not isinstance(first, (int, float)) or not isinstance(second, (int, float)):
        raise ValueError("operands must be numbers")

    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return first / second
    raise ValueError(f"unsupported operation: {operation}")


def run() -> str:
    """Demonstrate the calculator with a fixed addition."""
    first = 12
    second = 8
    operation = "+"
    result = calculate(first, second, operation)
    return f"{first} {operation} {second} = {result}"
