import zope.interface
from copy import deepcopy

class Prototype(zope.interface.Interface):
    def clone(self):
        pass

class objectOne(zope.interface.implementer):
    def __init__(self,object):
        self.object = object

    def clone(self):
        return deepcopy(self)

class objectTwo(zope.interface.implementer):
    def __init__(self,object):
        self.object = object

    def clone(self):
        return deepcopy(self)
    
objectOneClone = objectOne("Object 1").clone()
print("This is copy of",objectOneClone.object)

objectTwoClone = objectTwo("Object 2").clone()
print("This is copy of",objectTwoClone.object)