# BAD VERSION - has quality problems intentionally

password = "admin123"  # Hardcoded password (security issue)

def calculate(a, b, operation):
    result = 0

    if operation == "add":
        result = a + b

    if operation == "subtract":
        result = a - b

    if operation == "multiply":
        result = a * b

    if operation == "divide":
        result = a / b  # No zero check (reliability issue)

    return result


def print_result(a, b, operation):
    result = calculate(a, b, operation)
    print("The result is: " + str(result))


# Duplicated function (code smell)
def calculate_again(a, b, operation):
    result = 0

    if operation == "add":
        result = a + b

    if operation == "subtract":
        result = a - b

    if operation == "multiply":
        result = a * b

    if operation == "divide":
        result = a / b

    return result