from abc import ABC,abstractmethod

class Handler(ABC):
    @abstractmethod
    def setSuccessor(self,successor):
        pass

    @abstractmethod
    def handleRequest(self,request):
        pass

class Log1(Handler):
    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        if(request == "Log1"):
            print("Logging 1")
        elif self.successor:
            self.successor.handleRequest(request)

class Log1(Handler):
    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        if(request == "Log1"):
            print("Logging 1")
        elif self.successor:
            self.successor.handleRequest(request)

class Log2(Handler):
    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        if(request == "Log2"):
            print("Logging 2")
        elif self.successor:
            self.successor.handleRequest(request)

log1 = Log1()
log2 = Log2()
log1.setSuccessor(log2)
log1.handleRequest("Log1")
log1.handleRequest("Log2")