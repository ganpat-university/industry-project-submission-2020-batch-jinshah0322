import zope.interface
class Component(zope.interface.Interface):
    def display(self):
        pass

    def add(self,component):
        pass

    def remove(self,component):
        pass

@zope.interface.implementer(Component)
class Directory:
    def __init__(self) -> None:
        self.children = []

    def add(self,Component):
        self.children.append(Component)

    def remove(self,component):
        self.children.remove(component)

    def display(self):
        print("This is Directory")
        for child in self.children:
            child.display()

@zope.interface.implementer(Component)
class File:
    def display(self):
        print("This is File")

    def add(self,component):
        print("Cannot add to a File")

    def remove(self,component):
        print("Cannot remove from a File")

File1 = File()
File2 = File()

directory = Directory()
directory.add(File1)
directory.add(File2)

directory.display()

File1.add(File2)