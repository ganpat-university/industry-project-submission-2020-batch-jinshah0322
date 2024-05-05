import zope.interface
from abc import ABC,abstractmethod

class Component(ABC):
    @abstractmethod
    def accept(self,visitor):
        pass

class ElementA(Component):
    def accept(self, visitor):
        visitor.visitElementA(self)

    def function(self):
        return "A"

class ElementB(Component):
    def accept(self, visitor):
        visitor.visitElementB(self)

    def function(self):
        return "B"

class Visitor(zope.interface.Interface):
    def visitElementA(self,elementA):
        pass

    def visitElementB(self,elementB):
        pass

@zope.interface.implementer(Visitor)
class concreteVisitor1:
    def visitElementA(self,elementA):
        print(f"{elementA.function()} - Visitor1")

    def visitElementB(self,elementB):
        print(f"{elementB.function()} - Visitor1")

@zope.interface.implementer(Visitor)
class concreteVisitor2:
    def visitElementA(self,elementA):
        print(f"{elementA.function()} - Visitor2")

    def visitElementB(self,elementB):
        print(f"{elementB.function()} - Visitor2")

visitor1 = concreteVisitor1()
visitor2 = concreteVisitor2()
elementA = ElementA()
elementB = ElementB()
elementA.accept(visitor1)
elementA.accept(visitor2)
elementB.accept(visitor1)
elementB.accept(visitor2)