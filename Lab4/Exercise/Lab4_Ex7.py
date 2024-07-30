# <!-- #### Assignment 7: Private Attributes and Methods
# Required Knowledge: Encapsulation, Private Attributes
# 1. Add a private attribute `__salary` to the `Person` class and a method to set its value.
# 2. Add a method to retrieve the value of the `__salary` attribute.
# 3. Instantiate an object, set the salary, and print it using the retrieval method. -->

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_salary(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
Ang = Person("Ang", 19)
Ang.set_salary(69)
print(Ang.get_salary())
