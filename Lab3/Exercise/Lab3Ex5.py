# **Assignment 5: Using Lambda Functions in Python**
# Rewrite the functions from Assignment 4 using lambda functions.
# **Instructions:**
# 1. Create a new Python file named `lambda_calculator.py`.
# 2. Define a lambda function for addition that takes two arguments and returns their sum.
# 3. Define a lambda function for subtraction that takes two arguments and returns their difference.
# 4. Define a lambda function for multiplication that takes two arguments and returns their product.
# 5. Define a lambda function for division that takes two arguments and returns their quotient.
# 6. Write a main block that calls each lambda function with sample inputs and prints the results.

add = lambda x,y: x+y
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y
divide = lambda x,y: x/y
print(add(2,3), subtract(2,3), multiply(2,3), divide(2,3))


