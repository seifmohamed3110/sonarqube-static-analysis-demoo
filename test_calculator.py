# FIXED VERSION - stronger tests with edge cases

import pytest
from calculator import calculate

def test_add():
    assert calculate(2, 3, "add") == 5

def test_subtract():
    assert calculate(5, 3, "subtract") == 2

def test_multiply():
    assert calculate(4, 3, "multiply") == 12

def test_divide():
    assert calculate(10, 2, "divide") == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(10, 0, "divide")

def test_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        calculate(10, 5, "unknown")