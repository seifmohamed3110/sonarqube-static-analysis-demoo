from calculator import calculate, get_result

try:
    print(get_result(10, 5, "add"))
    print(get_result(10, 2, "divide"))
except ValueError as e:
    print("Error:", e)