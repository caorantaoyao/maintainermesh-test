def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b


def divide(a, b):
    """Return a divided by b."""
    if b is None or b == 0:
        raise ValueError("Cannot divide by zero or None")
    if a is None:
        raise ValueError("Cannot divide None")
    return a / b


def multiply(a, numbers=[]):
    """Multiply a by each number in numbers and return the list of products."""
    numbers.append(a)
    return numbers
