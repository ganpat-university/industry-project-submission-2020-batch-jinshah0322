from abc import ABC,abstractmethod

class Game(ABC):
    def templateMethod(self):
        self.initialize()
        self.startPlay()
        self.endPlay()

    def initialize(self):
        print("Game initialized")

    def startPlay(self):
        print("Game started")

    @abstractmethod
    def endPlay(self):
        pass

class Football(Game):
    def endPlay(self):
        print("Football is ended after 90 minutes ideally")

class Basketball(Game):
    def endPlay(self):
        print("Basketball is ended in 48 minutes ideally")

football = Football()
football.templateMethod()
print()

basketball = Basketball()
basketball.templateMethod()