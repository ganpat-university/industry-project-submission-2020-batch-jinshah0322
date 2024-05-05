class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

name = input("Enter name:")
age = int(input("Enter age:"))
p = Person(name,age)
p.display()