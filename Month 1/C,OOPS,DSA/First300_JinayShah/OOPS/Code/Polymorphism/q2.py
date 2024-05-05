import zope.interface

class Shape(zope.interface.Interface):
    def calculateArea(self):
        pass

@zope.interface.implementer(Shape)
class Circle:
    def __init__(self,r):
        self.r = r

    def calculateArea(self):
        return 3.14*self.r*self.r
    
@zope.interface.implementer(Shape)
class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculateArea(self):
        return self.l*self.b
    
r = int(input("Enter radius:"))
circle = Circle(r)
print(circle.calculateArea())

l = int(input("Enter length of rectangle:"))
b = int(input("Enter bredth of rectangle:"))
rectangle = Rectangle(l,b)
print(rectangle.calculateArea())