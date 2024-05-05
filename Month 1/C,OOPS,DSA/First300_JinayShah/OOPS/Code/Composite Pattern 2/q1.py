import zope.interface
class Component(zope.interface.Interface):
    def display(self):
        pass

    def add(self,component):
        pass

    def remove(self,component):
        pass

@zope.interface.implementer(Component)
class Composite:
    def __init__(self) -> None:
        self.children = []

    def add(self,Component):
        self.children.append(Component)

    def remove(self,component):
        self.children.remove(component)

    def display(self):
        print("This is composite operaton")
        for child in self.children:
            child.display()

@zope.interface.implementer(Component)
class Leaf:
    def display(self):
        print("This is leaf component")

    def add(self,component):
        print("Cannot add to leaf")

    def remove(self,component):
        print("Cannot remove from leaf")

leaf1 = Leaf()
leaf2 = Leaf()

composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

composite.display()

leaf1.add(leaf2)