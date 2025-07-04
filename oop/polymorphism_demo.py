import math

class Shape:

    def area(self):
        raise NotImplementedError("Derived class need to override this method")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width

class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius
         self.area = math.pi* self.radius **2
         
    
    
