import pytest
from calculator import add, subtract, multiply


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(5, 0) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply_no_mutable_default():
    # First call
    result1 = multiply(2)
    assert result1 == [2]
    # Second call should not reuse the same list
    result2 = multiply(3)
    assert result2 == [3]
    # Ensure the first result is unchanged
    assert result1 == [2]
