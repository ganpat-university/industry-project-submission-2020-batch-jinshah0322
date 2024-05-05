import zope.interface

class Drawable(zope.interface.Interface):
    def draw(self):
        pass

@zope.interface.implementer(Drawable)
class Circle:
    def draw(self):
        print("Circle is drawn")

@zope.interface.implementer(Drawable)
class Rectangle:
    def draw(self):
        print("Rectangle is drawn")

circle = Circle()
circle.draw()
rectangle= Rectangle()
rectangle.draw()