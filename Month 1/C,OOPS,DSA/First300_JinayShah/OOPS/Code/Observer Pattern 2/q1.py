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
class stock1:
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
class stock2:
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

s1 = stock1()
s2 = stock2()

u1 = user1()
u2 = user2()

s1.registerObserver(u1)
s1.registerObserver(u2)

s2.registerObserver(u1)

s1.newVideoAdded("Stock price are decreased by 1.5 rupees")
s2.newVideoAdded("Stock price increased by 0.7 rupees")

s1.unregisterObserver(u2)

s1.notifyObserver("Stock price increased by 5 rupees")