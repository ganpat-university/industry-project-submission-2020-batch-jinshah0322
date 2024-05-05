class TypeErasedContainer:
    def __init__(self):
        self.data = []

    def store(self, item):
        self.data.append(item)

    def retrieve(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

container = TypeErasedContainer()

container.store(42)
container.store("Hello, world!")
container.store([1, 2, 3])

item1 = container.retrieve(0)
item2 = container.retrieve(1)
item3 = container.retrieve(2)

print(f"Item 1: {item1}")
print(f"Item 2: {item2}")
print(f"Item 3: {item3}")
