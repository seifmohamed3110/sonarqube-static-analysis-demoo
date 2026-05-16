# BAD VERSION

from calculator import calculate, print_result

print_result(10, 5, "add")
print_result(10, 0, "divide")   # Will crash
print_result(10, 5, "unknown")  # No error handling