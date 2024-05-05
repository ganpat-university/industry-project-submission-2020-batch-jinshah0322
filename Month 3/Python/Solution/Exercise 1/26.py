class my_parent_class:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, a=0, b=0):
        self.res1 = self.x + a
        self.res2 = self.y + b
        self.print_result()

    def sub(self, a=0, b=0):
        self.res1 = self.x - a
        self.res2 = self.y - b
        self.print_result()

    def print_result(self):
        print("Result 1:", self.res1)
        print("Result 2:", self.res2)

    def __del__(self):
        print("Destructor of my_parent_class called")

class my_child_class(my_parent_class):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def add(self, a=0, b=0):
        result = self.x + self.y + self.z
        print("Result of addition:", result)

    def sub(self, a=0, b=0):
        result = self.x * self.y * self.z
        print("Result of multiplication:", result)

    def __del__(self):
        print("Destructor of my_child_class called")

print("Object 1 - No values passed:")
obj1 = my_parent_class()
obj1.add()
del obj1

print("Object 2 - Single value passed:")
obj2 = my_parent_class(10)
obj2.add(5, 3)
del obj2

print("Object 3 - Two values passed:")
obj3 = my_parent_class(20, 30)
obj3.sub(10, 5)
del obj3

print("Child Object - With values passed:")
child_obj = my_child_class(10, 20, 30)
child_obj.add()
child_obj.sub()
del child_obj