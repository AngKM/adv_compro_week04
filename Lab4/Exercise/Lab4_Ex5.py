# #### Assignment 5: Inheritance
# Required Knowledge: Inheritance
# 1. Define a subclass `Student` that inherits from the `Person` class.
# 2. Add an attribute `student_id` to the `Student` class.
# 3. Instantiate an object of the `Student` class and print all its attributes.

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def display(self):
        return f"Name: {self.name} ID: {self.student_id}"
Ang = Student("Ang", 66011586)
print(Ang.display())