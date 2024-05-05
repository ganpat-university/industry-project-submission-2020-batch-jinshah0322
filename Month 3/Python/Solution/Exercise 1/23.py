class Parent:
    def method(self, arg=None):
        if arg is None:
            print("This is the method from the Parent class")
        else:
            print("This is the method from the Parent class with argument:", arg)

class Child(Parent):
    def method(self, arg=None):
        if arg is None:
            print("This is the method from the Child class (Method Overriding)")
        else:
            print("This is the method from the Child class with argument:", arg)

child_obj = Child()

child_obj.method() 
child_obj.method("test") 