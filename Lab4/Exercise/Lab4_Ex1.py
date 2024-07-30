# <!-- #### Assignment 1: Creating a Class
# Required Knowledge: Class Definition, Object Instantiation
# 1. Define a class named `Person`.
# 2. Add two attributes: `name` and `age`.
# 3. Instantiate an object of the `Person` class with your name and age.
# 4. Print the object's attributes. -->

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
Person1 = Person("Ang", "19")
print(Person1.name, Person1.age)

