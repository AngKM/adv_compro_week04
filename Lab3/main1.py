from utilities import calculator
from utilities import string_operations

print("Using calculator.py:")
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))

sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", string_operations.reverse_string(sample_string))
print("Capitalized:", string_operations.capitalize_string(sample_string))
print("Lowercase:", string_operations.lowercase_string(sample_string))
print("Uppercase:", string_operations.uppercase_string(sample_string))
