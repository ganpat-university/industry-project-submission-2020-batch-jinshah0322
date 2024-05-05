class parent:
    def __init__(self):
        print("This is constructor of parent class")

    def method1(self):
        print("This is method1 of parent class")

    def method2(self):
        print("This is method2 of parent class")

    def __del__(self):
        print("This is destructor of parent class")

class child(parent):
    def __init__(self):
        print("This is constructor of child class")

    def method3(self):
        print("This is method3 of child class")

    def __del__(self):
        print("This is destructor of child class")

print("Parent class")
pobj = parent()
pobj.method1()
pobj.method2() 
del pobj

print("\nChild class")
cobj = child()
cobj.method3()
cobj.method1()
cobj.method2()
del cobj