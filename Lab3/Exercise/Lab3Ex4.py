# **Assignment 4: Defining Functions in Python**
# Define and use functions in Python to perform specific tasks.
# **Instructions:**
# 1. Create a new Python file named `calculator.py`.
# 2. Define a function named `add` that takes two arguments and returns their sum.
# 3. Define a function named `subtract` that takes two arguments and returns their difference.
# 4. Define a function named `multiply` that takes two arguments and returns their product.
# 5. Define a function named `divide` that takes two arguments and returns their quotient.
# 6. Write a main block that calls each function with sample inputs and prints the results.

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Error: Denominator is Zero"
if __name__ == "__main__":
    print(add(2,3), subtract(2,3), multiply(2,3), divide(2,3))

