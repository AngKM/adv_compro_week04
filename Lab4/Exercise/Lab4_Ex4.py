# ### Assignment 4: Implementing Age Manipulation Methods
# 1. **Add Method**: Create a method `have_birthday` that increments the `age` attribute by 1 and prints a birthday message.
# 2. **Display Age**: Modify the `display_info` method to also include a message if the age is 18 or above.

class Person:
    def __init__(self,name,age, adress, phone_number):
        self.name = name
        self.age = age
        self.adress = adress
        self.phone_number = phone_number
    def display(self):
        if self.age >=18:
            print("Congrats You're Legal Now")
        print(f"Name: {self.name}, Age: {self.age}, Adress: {self.adress}, Phone Number: {self.phone_number}")
    def have_birthday(self):
        self.age = self.age+1
Ang = Person("Ang", 16, "Bangkok", "191")
print(Ang.display())
Ang.have_birthday()
print(Ang.display())
Ang.have_birthday()
print(Ang.display())



