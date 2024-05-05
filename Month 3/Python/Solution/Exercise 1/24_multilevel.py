class Grandparent:
    def method1(self):
        print("Method from Grandparent")

    def method(self):
        print("Method from Grandparent")


class Parent(Grandparent):
    def method(self):
        print("Method from Parent")

class Child(Parent):
    pass

child_obj = Child()
child_obj.method1()  