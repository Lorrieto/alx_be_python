import math

class Shape:

    def area(self):
        g"NotImplementedError"

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.length * self.width

class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius
         math.pi* self.radius * self.radius
    
    
