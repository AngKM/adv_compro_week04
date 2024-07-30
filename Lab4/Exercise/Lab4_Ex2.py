# #### Assignment 2: Instance Methods
# Required Knowledge: Instance Methods
# 1. Add a method `greet` to the `Person` class that prints "Hello, my name is [name] and I am [age] years old."
# 2. Call the `greet` method from an instantiated object.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")
Person1 = Person("Ang", "19")
print(Person1.greet())
