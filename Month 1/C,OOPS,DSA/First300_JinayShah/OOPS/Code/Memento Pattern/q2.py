class Memento:
    def __init__(self,state) -> None:
        self.state = state

    def getState(self):
        return self.state
    
class Originator:
    def __init__(self,state) -> None:
        self.state = state

    def createMemento(self):
        return Memento(self.state)
    
    def restore_from_memento(self,memento):
        self.state = memento.getState()

    def getState(self):
        return self.state
    
    def setState(self,state):
        self.state = state

class careTaker:
    def __init__(self) -> None:
        self.memntos = []

    def addMemento(self,memento):
        self.memntos.append(memento)

    def getMemento(self,index):
        return self.memntos[index]
    
originator = Originator("State1")
caretaker = careTaker()
memento1 = originator.createMemento()
caretaker.addMemento(memento1)
originator.setState("State2")
memento2 = originator.createMemento()
caretaker.addMemento(memento2)
originator.restore_from_memento(caretaker.getMemento(1))
print(originator.getState())