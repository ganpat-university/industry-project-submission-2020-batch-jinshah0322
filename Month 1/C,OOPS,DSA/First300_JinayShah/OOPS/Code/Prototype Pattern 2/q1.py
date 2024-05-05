import zope.interface
from copy import deepcopy

class Prototype(zope.interface.Interface):
    def clone(self):
        pass

class dog(zope.interface.implementer):
    def __init__(self,name):
        self.name = name

    def clone(self):
        return deepcopy(self)

class cat(zope.interface.implementer):
    def __init__(self,name):
        self.name = name

    def clone(self):
        return deepcopy(self)
    
dogClone = dog("German Shepherd").clone()
print(dogClone.name)

catClone = cat("British shorthair").clone()
print(catClone.name)