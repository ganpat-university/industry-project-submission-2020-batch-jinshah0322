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
class observer1:
    def update(self,msg):
        print(f"user 1 {msg}")

@zope.interface.implementer(observer)
class observer2:
    def update(self,msg):
        print(f"user 2 {msg}")

@zope.interface.implementer(subject)
class temperature:
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
    def temperatureChanged(self,msg):
        self.notifyObserver(msg)

@zope.interface.implementer(subject)
class humidity:
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
    def humidityChanged(self,msg):
        self.notifyObserver(msg)

s1 = temperature()
s2 = humidity()

o1 = observer1()
o2 = observer2()

s1.registerObserver(o1)
s1.registerObserver(o2)

s2.registerObserver(o1)

s1.temperatureChanged("today's temperature is 29 degree celcius")
s2.humidityChanged("today's humidity is very high")

s1.unregisterObserver(o1)

s1.notifyObserver("today's temperature is 35 degree celcius")