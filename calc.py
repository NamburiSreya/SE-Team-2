import math

# calculator.py

def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def sqrt(x):
    """Square Root"""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number!")
    return math.sqrt(x)

def factorial(x):
    """Factorial"""
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers!")
    return math.factorial(x)

# User input functionality
def calculator():
    print("Select operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Factorial")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"Result: {divide(num1, num2)}")
            except ValueError as e:
                print(e)

    elif choice == '5':
        num = float(input("Enter a number: "))
        try:
            print(f"Result: {sqrt(num)}")
        except ValueError as e:
            print(e)

    elif choice == '6':
        num = int(input("Enter a number (non-negative integer): "))
        try:
            print(f"Result: {factorial(num)}")
        except ValueError as e:
            print(e)

    else:
        print("Invalid input")

# Run the calculator
calculator()
