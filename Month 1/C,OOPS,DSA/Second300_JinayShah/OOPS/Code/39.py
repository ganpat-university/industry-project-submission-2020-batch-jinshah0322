import gc

class MyClass:
    def __init__(self, name):
        self.name = name

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")
obj3 = MyClass("Object 3")
obj1.next = obj2
obj2.next = obj3
obj3.next = obj1
del obj1, obj2, obj3
gc.collect()
print("Garbage collection completed.")