import zope.interface

class Target(zope.interface.Interface):
    def request(self):
        pass

class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request"
    
@zope.interface.implementer(Target)
class Adapter:
    def __init__(self,adaptee) -> None:
        self.adaptee = adaptee

    def request(self):
        return f"Adaptee:{self.adaptee.specific_request()}"
    
def clientCode(target):
    print(target.request())

adaptee = Adaptee()
adapter = Adapter(adaptee)
clientCode(adapter)