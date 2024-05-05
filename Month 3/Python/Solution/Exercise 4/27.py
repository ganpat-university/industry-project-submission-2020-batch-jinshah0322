class Parent:
    pass

class Child(Parent):
    pass

if issubclass(Child, Parent):
    print("Child is a subclass of Parent")
else:
    print("Child is not a subclass of Parent")