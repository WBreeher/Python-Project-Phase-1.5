
# This is a function-driven Calculator
import sys

print("Welcome to the function-driven Calculator, created by W. Breeher. Nov. 12th 2025.")
print("Type quit to leave the program at anytime.")

# === Functions ===
def add(a, b):
    """Return the sum of A + B"""
    return a + b

def sub(a, b):
    """Return the difference of A - B"""
    return a - b

def mul(a, b):
    """Return the product of A * B"""
    return a * b

def div(a, b):
    """Return the quotient of A / B"""
    return a / b

def leave():
    """Ends program"""
    sys.exit("Program ended. Have a good day.")

# === Program ===

while True:
    try:
        op = input("\nEnter Operator: add, sub, mul, or div: ").strip().lower()
        if op == "leave":
            leave()

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if op == "add":
            print(add(a, b))
        elif op == "sub":
            print(sub(a, b))
        elif op == "mul":
            print(mul(a, b))
        elif op == "div":
            print(div(a, b))
        else:
            print("Invalid op.")
    except ValueError:
        print("Numbers only. Try again.")