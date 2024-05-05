import zope.interface

class Mediator(zope.interface.Interface):
    def sendMessage(self,msg,user):
        pass

@zope.interface.implementer(Mediator)
class chatMediator:
    def __init__(self) -> None:
        self.users = []

    def addUser(self,user):
        self.users.append(user)

    def sendMessage(self,msg,user):
        for u in self.users:
            if(u!=user):
                u.receiveMessage(msg)

class Colleague(zope.interface.Interface):
    def sendMessage(self,msg):
        pass

    def revieveMessage(self,msg):
        pass

@zope.interface.implementer(Colleague)
class User:
    def __init__(self,mediator,name) -> None:
        self.mediator = mediator
        self.name = name

    def sendMessage(self,msg):
        self.mediator.sendMessage(msg,self)

    def receiveMessage(self,msg):
        print(f"{self.name}: {msg}")

mediator = chatMediator()
user1 = User(mediator,"Jinay")
user2 = User(mediator,"Shah")

mediator.addUser(user1)
mediator.addUser(user2)

user1.sendMessage("Hello shah")
user2.sendMessage("Hello jinay")