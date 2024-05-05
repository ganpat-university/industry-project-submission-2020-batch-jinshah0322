import zope.interface

class observer(zope.interface.Interface):
    def update(self,msg):
        pass

class subject(zope.interface.Interface):
    def registerObserver(self,observer):
        pass
    def unregisterObserver(self,observer):
        pass
    def notifyObserver(self,msg):
        pass

@zope.interface.implementer(observer)
class user1:
    def update(self,msg):
        print("user 1",msg)

@zope.interface.implementer(observer)
class user2:
    def update(self,msg):
        print("user 2",msg)

@zope.interface.implementer(subject)
class channel1:
    def __init__(self):
        self.observers = []
    def registerObserver(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
    def unregisterObserver(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)
    def notifyObserver(self,msg):
        for i in self.observers:
            i.update(msg)
    def newVideoAdded(self,msg):
        self.notifyObserver(msg)


@zope.interface.implementer(subject)
class channel2:
    def __init__(self):
        self.observers = []
    def registerObserver(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
    def unregisterObserver(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)
    def notifyObserver(self,msg):
        for i in self.observers:
            i.update(msg)
    def newVideoAdded(self,msg):
        self.notifyObserver(msg)

c1 = channel1()
c2 = channel2()

u1 = user1()
u2 = user2()

c1.registerObserver(u1)
c1.registerObserver(u2)

c2.registerObserver(u1)

c1.newVideoAdded("New video for observer pattern is added")
c2.newVideoAdded("New video for abstract factory patter is added")