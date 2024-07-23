# 3. Create a module named `calculator.py` inside `utilities` and include the functions defined in Assignment 4.
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
