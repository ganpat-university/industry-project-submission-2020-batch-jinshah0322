from abc import ABC, abstractmethod

class Shape(ABC):
   @abstractmethod
   def draw(self):
       pass

class Circle(Shape):
   def __init__(self, radius):
       self.radius = radius

   def draw(self):
       print(f"Drawing a circle with radius {self.radius}")

class Rectangle(Shape):
   def __init__(self, width, height):
       self.width = width
       self.height = height

   def draw(self):
       print(f"Drawing a rectangle with width {self.width} and height {self.height}")

class Triangle(Shape):
   def __init__(self, side1, side2, side3):
       self.side1 = side1
       self.side2 = side2
       self.side3 = side3

   def draw(self):
       print(f"Drawing a triangle with sides {self.side1}, {self.side2}, {self.side3}")

class Drawing:
   def __init__(self):
       self.shapes = []

   def add_shape(self, shape):
       self.shapes.append(shape)

   def draw_all(self):
       for shape in self.shapes:
           shape.draw()

circle = Circle(5)
rectangle = Rectangle(10, 20)
triangle = Triangle(3, 4, 5)

drawing = Drawing()
drawing.add_shape(circle)
drawing.add_shape(rectangle)
drawing.add_shape(triangle)

drawing.draw_all()