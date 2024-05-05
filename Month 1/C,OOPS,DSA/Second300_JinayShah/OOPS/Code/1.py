from abc import ABC, abstractmethod

# Component interface
class Employee(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf class
class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"{self.position}: {self.name}")

# Composite class
class Manager(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        self.subordinates.remove(subordinate)

    def display(self):
        print(f"{self.position}: {self.name}")
        for subordinate in self.subordinates:
            subordinate.display()


dev1 = Developer("John Doe", "Developer")
dev2 = Developer("Jane Smith", "Developer")

manager = Manager("Bob Johnson", "Project Manager")
manager.add_subordinate(dev1)
manager.add_subordinate(dev2)

manager.display()
