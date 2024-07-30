# #### Assignment 9: Polymorphism
# Required Knowledge: Polymorphism
# 1. Define a function `introduce` that takes a `Person` object and calls its `greet` method.
# 2. Instantiate both `Person` and `Student` objects and pass them to the `introduce` function.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, My name is {self.name} and I am {self.age} years old."
Ang = Person("Ang", 19)
def introduce(human):
    print(human.greet())
introduce(Ang)

