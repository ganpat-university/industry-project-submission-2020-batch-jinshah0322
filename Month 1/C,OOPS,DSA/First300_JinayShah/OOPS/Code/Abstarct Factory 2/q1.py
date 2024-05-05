from abc import ABC,abstractmethod

class abstractFactory(ABC):
    @abstractmethod
    def createFurnitureChair(self):
        pass

    @abstractmethod
    def createFurnitureTable(self):
        pass

class concreteFactoryOffice(ABC):
    def createFurnitureChair(self):
        return concreteFurnitureOfficeChair()
    
    def createFurnitureTable(self):
        return concreteFurnitureOfficeTable()
    
class concreteFactoryCasual(ABC):
    def createFurnitureChair(self):
        return concreteFurnitureCasualChair()
    
    def createFurnitureTable(self):
        return concreteFurnitureCasualTable()
    
class abstractFurnitureChair(ABC):
    @abstractmethod
    def useFurnitureChair(self):
        pass

class concreteFurnitureOfficeChair(abstractFurnitureChair):
    def useFurnitureChair(self):
        return  "Office furniture includes comfortable chair"
    
class concreteFurnitureCasualChair(abstractFurnitureChair):
    def useFurnitureChair(self):
        return  "Casual furniture includes chair"
    
class abstractFurnitureTable(ABC):
    @abstractmethod
    def useFurnitureTable(self):
        pass

class concreteFurnitureOfficeTable(abstractFurnitureTable):
    def useFurnitureTable(self):
        return  "Office furniture includes amazing table"
    
class concreteFurnitureCasualTable(abstractFurnitureTable):
    def useFurnitureTable(self):
        return  "Casual furniture includes table"
    
def clientChoise(furniture):
    chair = furniture.createFurnitureChair()
    table = furniture.createFurnitureTable()

    print(chair.useFurnitureChair())
    print(table.useFurnitureTable())

furniture = input("Enter which set of chair and table do you want:\n1)Office\n2)Casual:").lower()
if(furniture == "office" or furniture == "1"):
    clientChoise(concreteFactoryOffice())
elif(furniture == "casual" or furniture == "2"):
    clientChoise(concreteFactoryCasual())