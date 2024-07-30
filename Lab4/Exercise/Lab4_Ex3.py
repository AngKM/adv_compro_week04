# ### Assignment 3: Adding More Attributes and Methods
# 1. **Add Attributes**: Extend the `Person` class to include `address` and `phone_number` attributes.
# 2. **Add Method**: Create a method `update_contact_info` that updates the `address` and `phone_number` attributes.
# 3. **Display Information**: Add a method `display_info` that prints all the attributes of the `Person` object.

class Person:
    def __init__(self,name,age, adress, phone_number):
        self.name = name
        self.age = age
        self.adress = adress
        self.phone_number = phone_number
    def update_contact_info(self, new_adress, new_phone_number):
        self.adress = new_adress
        self.phone_number = new_phone_number
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Adress: {self.adress}, Phone Number: {self.phone_number}")
Ang = Person("Ang", "19", "Bangkok", "191")
print(Ang.display())
Ang.update_contact_info("London", "1991")
print(Ang.display())
