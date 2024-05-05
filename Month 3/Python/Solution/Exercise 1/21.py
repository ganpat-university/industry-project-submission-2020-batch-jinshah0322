class parent:
    def method1(self):
        print("This is method1 of parent class")

    def method2(self):
        print("This is method2 of parent class")

class child(parent):
    def method3(self):
        print("This is method3 of child class")

pobj = parent()
pobj.method1()
pobj.method2() 

cobj = child()
cobj.method3()
cobj.method1()
cobj.method2()