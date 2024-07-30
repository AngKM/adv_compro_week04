# #### Assignment 10: Creating and Using a Package
# Required Knowledge: Package Creation, Module Import, Class Design
# 1. Create a package named `shapes`.
# 2. Inside the `shapes` package, create a module `geometry.py` and define the following classes:
#     - `Shape` (abstract class with an abstract method `area`).
#     - `Circle` (inherits from `Shape` and implements the `area` method).
#     - `Rectangle` (inherits from `Shape` and implements the `area` method).
# 3. Create a script outside the `shapes` package named `main.py` to:
#     - Import the `Circle` and `Rectangle` classes from the `shapes.geometry` module.
#     - Instantiate `Circle` and `Rectangle` objects with sample dimensions.
#     - Print the area of the instantiated shapes.

from Shapes.geometry import Circle, Rectangle
Circle1=(Circle.area(2))
Rectangle1=(Rectangle.area(2,3))
print(f"Circle: {Circle1}, Rectangle: {Rectangle1}")
