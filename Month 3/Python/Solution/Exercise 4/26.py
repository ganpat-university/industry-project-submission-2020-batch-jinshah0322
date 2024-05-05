class MyClass:
    global_attribute = "This is a global attribute"
    
    def __init__(self):
        self.local_attribute = "This is a local attribute"
        
    def method_with_access(self):
        local_var = "This is a local variable"
        print(f"Global Attribute: {MyClass.global_attribute}")
        print(f"Local Attribute: {self.local_attribute}")
        print(f"Local Variable: {local_var}")

my_instance = MyClass()

my_instance.method_with_access()