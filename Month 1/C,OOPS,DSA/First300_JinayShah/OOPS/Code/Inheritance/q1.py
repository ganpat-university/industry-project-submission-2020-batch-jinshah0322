class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b

    def perimeter(self):
        return self.l+self.b

class Circle(Shape):
    def __init__(self,r) :
        self.r = r

    def area(self):
        return 3.14*self.r*self.r

    def perimeter(self):
        return 2*3.14*self.r

rect = Rectangle(2,4)
print(f"Area of rectangle is {rect.area()}")
print(f"Perimeter of rectangle is {rect.perimeter()}")

circ = Circle(5)
print(f"Area of circle is {circ.area()}")
print(f"Perimeter of circle is {circ.perimeter()}")