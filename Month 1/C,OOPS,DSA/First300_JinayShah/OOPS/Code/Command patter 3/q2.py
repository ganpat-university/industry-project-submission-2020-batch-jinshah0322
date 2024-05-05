from abc import ABC,abstractmethod

class Command(ABC):
    def execute(self):
        pass

class TurnOnLightsCommand(Command):
    def __init__(self,item):
        self.item = item

    def execute(self):
        self.item.turnON()

class TurnOffACCommand(Command):
    def __init__(self,item) :
        self.item = item

    def execute(self):
        self.item.turnOFF()

class Item:
    def turnON(self):
        print("Light is turned on")

    def turnOFF(self):
        print("AC is turned off")

class RemoteControl:
    def __init__(self) -> None:
        self.command= None

    def set_command(self,command):
        self.command = command

    def press_button(self):
        self.command.execute()

item = Item()
turn_on_light = TurnOnLightsCommand(item)
turn_off_ac = TurnOffACCommand(item)
rc = RemoteControl()

rc.set_command(turn_on_light)
rc.press_button()

rc.set_command(turn_off_ac)
rc.press_button()