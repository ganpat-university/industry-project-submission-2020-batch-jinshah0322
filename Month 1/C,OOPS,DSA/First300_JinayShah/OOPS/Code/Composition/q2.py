class Engine:
    def __init__(self,cc):
        self.cc = cc

    def engineCC(self) :
        return self.cc

class Car:
    def __init__(self,name,cc):
        self.name = name
        self.obj_Engine = Engine(cc)

    def display(self):
        return self.obj_Engine.engineCC()

car = Car("Kia Carens",1.5)
print(f"kia carens has {car.display()}L cc")