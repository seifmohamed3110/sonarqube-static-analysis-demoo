# FIXED VERSION

from calculator import calculate, get_result

try:
    print(get_result(10, 5, "add"))
    print(get_result(10, 0, "divide"))    # Now handled safely
    print(get_result(10, 5, "unknown"))   # Now handled safely
except ValueError as e:
    print("Error:", e)