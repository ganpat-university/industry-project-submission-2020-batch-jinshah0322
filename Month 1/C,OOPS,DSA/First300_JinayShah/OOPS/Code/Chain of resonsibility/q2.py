from abc import ABC,abstractmethod

class Handler:
    @abstractmethod
    def setSuccessor(self,successor):
        pass
    
    @abstractmethod
    def handleRequest(self,request):
        pass

class concreteHandler1(Handler):
    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        if(request=="handler1"):
            print("ConcreteHandler1 is handling the request")
        elif self.successor:
            self.successor.handleRequest(request)
        else:
            return

class concreteHandler2(Handler):
    def setSuccessor(self, successor):
        self.successor = successor
    
    def handleRequest(self, request):
        if(request=="handler2"):
            print("ConcreteHandler2 is handling the request")
        elif self.successor:
            self.successor.handleRequest(request)
        else:
            return

handler1 = concreteHandler1()
handler2 = concreteHandler2()
handler1.setSuccessor(handler2)
handler1.handleRequest("handler1")
handler1.handleRequest("handler2")