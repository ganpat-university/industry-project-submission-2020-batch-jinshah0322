from abc import ABC,abstractmethod

class RealSubject(ABC):
    def request(self):
        pass

class ConcreteSubject(RealSubject):
    def request(self):
        print("Handling request")

class Proxy(RealSubject):
    def __init__(self,realSubject) -> None:
        self.realSubject = realSubject
    
    def request(self):
        print("Proxy:Checking access before handling request")
        self.realSubject.request()
        print("Proxy:Request complete")

realSubject = ConcreteSubject()
proxy = Proxy(realSubject)
proxy.request()