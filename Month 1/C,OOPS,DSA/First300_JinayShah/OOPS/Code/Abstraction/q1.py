from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self,eat,sound):
        self.eat = eat
        self.sound = sound

    def eat(self):
        return self.eat
    
    def sound(self):
        return self.sound
    
class Cat(Animal):
    def __init__(self,eat,sound):
        self.eat = eat
        self.sound = sound

    def eat(self):
        return self.eat
    
    def sound(self):
        return self.sound
    
eat = input("Enter what dog eats:")
sound = input("Enter what dog sounds:")
dog = Dog(eat,sound)
print(dog.eat,dog.sound)

eat = input("Enter what cat eats:")
sound = input("Enter what cat sounds:")
cat = Cat(eat,sound)
print(cat.eat,cat.sound)