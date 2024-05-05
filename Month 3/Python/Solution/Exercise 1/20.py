class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.result = None

    def method1(self, param):
        self.result = self.var1 + self.var2 + param

    def method2(self):
        print("Result:", self.result)

obj = MyClass(10, 20)

obj.method1(30)

obj.method2()