import zope.interface
from abc import ABC,abstractmethod

class Component(ABC):
    @abstractmethod
    def accept(self,visitor):
        pass

class paragraph(Component):
    def accept(self, visitor):
        visitor.visitparagraph(self)

    def function(self):
        return "Paragraph visited "

class image(Component):
    def accept(self, visitor):
        visitor.visitimage(self)

    def function(self):
        return "Image visited"

class Visitor(zope.interface.Interface):
    def visitparagraph(self,paragraph):
        pass

    def visitimage(self,image):
        pass

@zope.interface.implementer(Visitor)
class concreteVisitor1:
    def visitparagraph(self,paragraph):
        print(f"{paragraph.function()} - Visitor1")

    def visitimage(self,image):
        print(f"{image.function()} - Visitor1")

@zope.interface.implementer(Visitor)
class concreteVisitor2:
    def visitparagraph(self,paragraph):
        print(f"{paragraph.function()} - Visitor2")

    def visitimage(self,image):
        print(f"{image.function()} - Visitor2")

visitor1 = concreteVisitor1()
visitor2 = concreteVisitor2()
paragraph = paragraph()
image = image()
paragraph.accept(visitor1)
paragraph.accept(visitor2)
image.accept(visitor1)
image.accept(visitor2)