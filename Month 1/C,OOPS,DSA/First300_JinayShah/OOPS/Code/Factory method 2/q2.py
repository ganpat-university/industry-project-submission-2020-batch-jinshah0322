import zope.interface

class Vehicle(zope.interface.Interface):
    def createVehicle(self):
        pass

@zope.interface.implementer(Vehicle)
class TwoWheeler:
    def createVehicle(self):
        print("Two wheeler is created")


@zope.interface.implementer(Vehicle)
class FourWheeler:
    def createVehicle(self):
        print("Four wheeler is created")

class vehicleFactory:
    def __init__(self,wheel) :
        self.wheel = wheel
    def wheelType(self):
        if(self.wheel=="four"):
            FourWheeler().createVehicle()
        elif(self.wheel=="two"):
            TwoWheeler().createVehicle()
        else:
            print("Invalid document type")
    
wheel = input("Enter document type:").lower()
vehicleFactory = vehicleFactory(wheel)
vehicleFactory.wheelType()