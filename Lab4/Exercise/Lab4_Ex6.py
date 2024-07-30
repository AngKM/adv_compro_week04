# #### Assignment 6: Overriding Methods
# Required Knowledge: Method Overriding
# 1. Override the `greet` method in the `Student` class to include the student ID in the greeting.
# 2. Call the `greet` method from an instantiated `Student` object.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old. My ID is {self.student_id}")
Ang = Student("Ang", 17, 66011586)
Ang.greet()

