class overloading:
    def __init__(self,args=None):
        if(args is not None):
            print(f"Constructor with one argument:{args}")
        else:
            print("Constructor with no arguments")

    def overload(self,args=None):
        if(args is None):
            print("This is method overloading")
        else:
            print(f"This is method overloading with one argument:{args}")

obj = overloading()
obj.overload()
obj.overload("jinay")

obj1 = overloading("jinay")