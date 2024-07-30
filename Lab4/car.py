class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def display(self):
        print(f"Name: {self.name}, Speed: {self.speed}")
Tesla = Car("Tesla", "150")
print(Tesla.display())