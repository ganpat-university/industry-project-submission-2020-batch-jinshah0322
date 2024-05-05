import zope.interface
from abc import ABC,abstractmethod

class Shape(zope.interface.Interface):
    def run(self,renderEngine):
        pass

@zope.interface.implementer(Shape)
class Square:
    def run(self,renderEngine):
        print(f"Square is rendered on {renderEngine}")
    
@zope.interface.implementer(Shape)
class Circle:
    def run(self,renderEngine):
        print(f"Circle is rendered on {renderEngine}")
    
class renderEngine(ABC):
    def __init__(self,shape) -> None:
        self.shape = shape

    @abstractmethod
    def description(self):
        pass

class ObjectEngine(renderEngine):
    def __init__(self, shape,renderEngine) -> None:
        super().__init__(shape)
        self.renderEngine = renderEngine
    
    def description(self):
        self.shape.run(self.renderEngine)

square = Square()
circle = Circle()
ObjectEngine(square,"Intel").description()
ObjectEngine(circle,"Amd Ryzed").description()