from abc import ABC,abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class fanOnCommand(Command):
    def __init__(self,fan):
        self.fan = fan

    def execute(self):
        self.fan.turnON("Fan")

class fanOffCommand(Command):
    def __init__(self,fan):
        self.fan = fan

    def execute(self):
        self.fan.turnOFF("Fan")

class lightOnCommand(Command):
    def __init__(self,light):
        self.light = light

    def execute(self):
        self.light.turnON("Light")

class lightOffCommand(Command):
    def __init__(self,light):
        self.light = light

    def execute(self):
        self.light.turnOFF("Light")

class Item:
    def turnON(self,item):
        print(f"{item} is turned on")

    def turnOFF(self,item):
        print(f"{item} is turned off")

class RemoteControl:
    def __init__(self):
        self.command = None

    def setCommand(self,command):
        self.command = command

    def pressButton(self):
        self.command.execute()

item =Item()
light_on = lightOnCommand(item)
light_off = lightOffCommand(item)
fan_on = fanOnCommand(item)
fan_off = fanOffCommand(item)
remote = RemoteControl()

remote.setCommand(light_on)
remote.pressButton()  

remote.setCommand(fan_on)
remote.pressButton()  

remote.setCommand(fan_off)
remote.pressButton()  

remote.setCommand(light_off)
remote.pressButton()  