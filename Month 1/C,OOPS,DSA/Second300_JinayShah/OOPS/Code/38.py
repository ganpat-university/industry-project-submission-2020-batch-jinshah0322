import pickle

class Serializable:
    def serialize(self):
        return pickle.dumps(self)

    @classmethod
    def deserialize(cls, data):
        return pickle.loads(data)

class MyClass(Serializable):
    def __init__(self, name, value):
        self.name = name
        self.value = value

obj = MyClass(name="Example", value=42)

serialized_data = obj.serialize()
print("Serialized data:", serialized_data)

new_obj = MyClass.deserialize(serialized_data)
print("Deserialized object:", new_obj.name, new_obj.value)