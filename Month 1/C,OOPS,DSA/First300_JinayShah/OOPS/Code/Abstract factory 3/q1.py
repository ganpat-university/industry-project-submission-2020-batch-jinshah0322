from abc import ABC,abstractmethod

class abstractFactory(ABC):
    @abstractmethod
    def createDesktopUI(self):
        pass

    @abstractmethod
    def createMobileUI(self):
        pass

class concreteFactoryDesktop(abstractFactory):
    def createDesktopUI(self):
        return concreteDesktopUserDashboard()
    
    def createMobileUI(self):
        return concreteDesktopAdminDashboard()
    
class concreteFactoryMobileUI:
    def createDesktopUI(self):
        return concreteMobileUserDashboard()
    
    def createMobileUI(self):
        return concreteMobileAdminDashboard()
    
class abstractDesktop(ABC):
    @abstractmethod
    def usefulFunctionUser(self):
        pass

class concreteDesktopUserDashboard(abstractDesktop):
    def usefulFunctionUser(self):
        return "User dashboard can be opened in desktop UI"
    
class concreteMobileUserDashboard(abstractDesktop):
    def usefulFunctionUser(self):
        return "User dashboard can be opened in Mobile UI"
    
class abstractMobile(ABC):
    @abstractmethod
    def usefulFunctionAdmin(self):
        pass

class concreteDesktopAdminDashboard(abstractMobile):
    def usefulFunctionAdmin(self):
        return "Admin dashboard can be opened in desktop UI"
    
class concreteMobileAdminDashboard(abstractMobile):
    def usefulFunctionAdmin(self):
        return "Admin dashboard can be opened in Mobile UI"
    
def clientCode(factory):
    productA = factory.createDesktopUI()
    productB = factory.createMobileUI()
    print(f"{productA.usefulFunctionUser()}")
    print(f"{productB.usefulFunctionAdmin()}")

factory = input("Select 1 for Desktop UI and 2 for Mobile UI:")
if(factory == "1"):
    clientCode(concreteFactoryDesktop())
elif(factory == "2"):
    clientCode(concreteFactoryMobileUI())