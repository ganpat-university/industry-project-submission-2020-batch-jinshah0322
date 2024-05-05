from abc import ABC,abstractmethod

class CostlyResource(ABC):
    @abstractmethod
    def load(self):
        pass

class concreteCostlyResource(CostlyResource):
    def load(self):
        print("Loading the consly resource")

class ProxyCostlyResource(CostlyResource):
    def __init__(self,realSubject,isAuthenticated) -> None:
        self.realSubject = realSubject
        self.isAuthenticated = isAuthenticated
    
    def load(self):
        if(self.isAuthenticated):
            print("Proxy:user is authenticated loading the resource")
            self.realSubject.load()
        else:
            print("Proxy:user is not authenticated and so access is denied")

isAuthenticated = True
realSubject = concreteCostlyResource()
ProxyCostlyResource(realSubject,isAuthenticated).load()
print()
isAuthenticated = False
ProxyCostlyResource(realSubject,isAuthenticated).load()