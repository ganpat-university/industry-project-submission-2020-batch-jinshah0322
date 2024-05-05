from abc import ABC,abstractmethod

class abstractFactory(ABC):
    @abstractmethod
    def createProductA(self):
        pass

    @abstractmethod
    def createProductB(self):
        pass

class concreteFactory1(abstractFactory):
    def createProductA(self):
        return concreteProductA1()
    
    def createProductB(self):
        return concreteProductB1()
    
class concreteFactory2:
    def createProductA(self):
        return concreteProductA2()
    
    def createProductB(self):
        return concreteProductB2()
    
class abstractProductA(ABC):
    @abstractmethod
    def usefulFunctionA(self):
        pass

class concreteProductA1(abstractProductA):
    def usefulFunctionA(self):
        return "This is product A1"
    
class concreteProductA2(abstractProductA):
    def usefulFunctionA(self):
        return "This is product A2"
    
class abstractProductB(ABC):
    @abstractmethod
    def usefulFunctionB(self):
        pass

class concreteProductB1(abstractProductB):
    def usefulFunctionB(self):
        return "This is product B1"
    
class concreteProductB2(abstractProductB):
    def usefulFunctionB(self):
        return "This is product B2"
    
def clientCode(factory):
    productA = factory.createProductA()
    productB = factory.createProductB()
    print(f"{productA.usefulFunctionA()}")
    print(f"{productB.usefulFunctionB()}")

factory = input("selct factory 1 or 2:")
if(factory == "1"):
    clientCode(concreteFactory1())
elif(factory == "2"):
    clientCode(concreteFactory2())