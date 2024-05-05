class Person:
    def __init__(self,name=None,age=None):
        self.name = name
        self.age = age

person = Person()
print(person.name,person.age)

person1 = Person(name="jinay")
print(person1.name,person1.age)

person2 = Person(age=20)
print(person2.name,person2.age)

person3 = Person(name="Jinay",age=20)
print(person3.name,person3.age)