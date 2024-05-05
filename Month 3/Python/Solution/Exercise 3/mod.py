class MyClass:
    def __init__(self, name):
        self.name = name
        self.counter = 0

    def greet(self):
        print("Hello,", self.name)
        self.counter += 1

    def leave(self):
        print("Goodbye,", self.name)
        self.counter += 1

def outside_method():
    print("This is an outside method")