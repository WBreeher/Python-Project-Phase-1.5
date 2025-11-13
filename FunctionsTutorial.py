# A function is named chunk of code that you can call again later.

# Think of it like a machine
    # You give it inputs (called parameters or arguments).
    # It does something inside.
    # It may give back an output (with return).

# Anatomy
def greet(name):    # "def" starts a function definition.
    print(f"Hello, {name}")     # code block indented under it.

greet("Cloud")  # prints: Hello, Cloud.

# Functions that return something
def add(a, b):
    return a + b 

result = add(2, 3)
print(result) # 5

# return sends data back to the caller.
# Without it, the function just runs code and returns None.

# Parameters vs Arguments.
    # Parameters = the name in the definition (a, b).
    # Argument = the actual value you pass (2, 3).

# Why use them.
    # They make code:
        # Reusable - you write once, use everywhere.
        # Organized - each part has its own job.
        # Easier to debug - small testable pieces.
    
# Example: wrapping your own logic

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")

else:
    print("Odd")

# Turn it into a function:

def is_even(num):
    return num % 2 == 0

num = int(input("Enter number: "))
if is_even(num):
    print("Even")

else:
    print("Odd")

# You can have multiple returns:

def compare(a, b):
    if a > b:
        return "A is bigger"
    
    elif b > a:
        return "B is bigger"
    
    else:
        return "Equal"
    
# Functions can call other functions:

def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

# Default parameters

def greet(name="Traveler"):
    print(f"Hello, {name}")

greet()
greet("Cloud")

# Keyword Arguments

def power(base, exponent):
    return base ** exponent

print(power(2, 3))                  # normal
print(power(exponent=3, base=2))    # keyword order doesn't matter

# Keyword arguments make code easier to read when a function has many parameters

# Variable number of arguments (*args, **kwargs)

# *args lets you take any number of positional arguments:

def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4, 5)) # 15

# **kwargs lets you take any number of keyword arguments:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Cloud", job="Programming", level=1.5)

# Scope (Local vs Global)
    # variables inside a funciton only exist inside it.

def test():
    x = 5   # this is a different 'x'
    print(x)

test()  # prints 5
print(x)    # still 10

# Functions can return multiple things.

def stats(a, b):
    return a + b, a * b

s, p = stats(2, 3)
print(s, p)    # 5 6

# Lambda functions (one-liners)

square = lambda x: x * x
print(square(5))    # 25

def apply_twice(func, x):
    return func(func(x))

def double(n):
    return n * 2

print(apply_twice(double, 5))

# Docstrings (built-in documentation)

def add(a, b):
    """Return the sum of a and b."""
    return a + b

help(add)

# Return ends the function immediately

def test():
    return "done"
    print("you'll never see this")

# Best practices
    # One job per function
        # Don't make "do everything" monsters
    # Use descriptive names
        # calculate_total() is better than calc()
    # Keep I/O seperate.
        # Logic inside; input/output outside. That's how you make code reusable.