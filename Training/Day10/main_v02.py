from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, operation, b):
    if operation in operations:
        return operations[operation](a, b)
    else:
        return "Invalid operation"


print(logo)

try:
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    result = calculate(num1, operation, num2)
    print(f"The result is: {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
