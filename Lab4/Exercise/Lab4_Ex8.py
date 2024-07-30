# #### Assignment 8: Static Methods
# Required Knowledge: Static Methods
# 1. Add a static method `is_adult` to the `Person` class that takes an age as an argument and returns `True` if the age is 18 or above, otherwise `False`.
# 2. Call the `is_adult` method from the class without creating an object.

class Person:
    @staticmethod
    def is_legal(age):
        if age >= 18:
            return True
        else:
            return False
print(Person.is_legal(18))  
print(Person.is_legal(17))

        