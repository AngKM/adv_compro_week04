# 1. Create a package named `shapes`.
# 2. Inside the `shapes` package, create a module `geometry.py` and define the following classes:
#     - `Shape` (abstract class with an abstract method `area`).
#     - `Circle` (inherits from `Shape` and implements the `area` method).
#     - `Rectangle` (inherits from `Shape` and implements the `area` method).
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    @staticmethod
    def area(r):
        return 22/7*(r*r)
class Rectangle(Shape):
    @staticmethod
    def area(w,l):
        return w*l


