import zope.interface
from abc import ABC,abstractmethod

class Color(zope.interface.Interface):
    def fill(self,shape):
        pass

@zope.interface.implementer(Color)
class Red:
    def fill(self,shape):
        print(f"{shape} is of red color")
    
@zope.interface.implementer(Color)
class Blue:
    def fill(self,shape):
        print(f"{shape} is of blue color")
    
class Shape(ABC):
    def __init__(self,color) -> None:
        self.color = color

    @abstractmethod
    def description(self):
        pass

class ObjectShape(Shape):
    def __init__(self, color,shape) -> None:
        super().__init__(color)
        self.shape = shape
    
    def description(self):
        self.color.fill(self.shape)

red = Red()
blue = Blue()
ObjectShape(red,"Square").description()
ObjectShape(blue,"Circle").description()