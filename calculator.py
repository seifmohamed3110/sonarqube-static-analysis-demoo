# FIXED VERSION - quality problems resolved

import os

# Removed hardcoded password (security fix)
password = os.environ.get("APP_PASSWORD")

def calculate(a, b, operation):
    """Perform a calculation based on the operation."""

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")  # Reliability fix
        return a / b

    else:
        raise ValueError(f"Unknown operation: {operation}")  # Invalid operation fix


def get_result(a, b, operation):
    """Return the result as a formatted string."""
    result = calculate(a, b, operation)
    return "The result is: " + str(result)

# calculate_again function removed (duplication fix)