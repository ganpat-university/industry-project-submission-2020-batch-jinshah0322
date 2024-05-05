import zope.interface

class Iterator(zope.interface.Interface):
    def __iter__(self):
        pass

    def __next__(self):
        pass

@zope.interface.implementer(Iterator)
class batIterator:
    def __init__(self,bats):
        self.bats = bats
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.index<len(self.bats)):
            result = self.bats[self.index]
            self.index+=1
            return result
        else:
            raise StopIteration
        
class Iterable(zope.interface.Interface):
    def __iter__(self):
        pass

@zope.interface.implementer(Iterable)
class batCollection:
    def __init__(self) :
        self.bats = []

    def addBats(self,bat):
        self.bats.append(bat)

    def __iter__(self):
        return batIterator(self.bats)
    
bat = batCollection()
bat.addBats("SG")
bat.addBats("Addidas")

batIterator = iter(bat)
for bat in batIterator:
    print(bat)