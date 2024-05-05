class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_info(self):
        print(f"MyClass instance with values x={self.x} and y={self.y}")


def inspect_object(obj):
    class_name = type(obj).__name__
    print(f"Class name: {class_name}")

    attributes = {attr: getattr(obj, attr) for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")}
    print("Attributes:")
    for attr, value in attributes.items():
        print(f"  {attr}: {value}")

    if hasattr(obj, 'print_info'):
        print("Calling print_info method:")
        obj.print_info()


my_instance = MyClass(x=10, y=20)

inspect_object(my_instance)
