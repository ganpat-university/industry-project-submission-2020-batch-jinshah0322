import json

class SerializationError(Exception):
    pass

class EvolvableObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def serialize(obj):
    return json.dumps(obj.__dict__)

def deserialize(data, expected_class):
    try:
        loaded_data = json.loads(data)
        loaded_obj = expected_class(**loaded_data)
        return loaded_obj
    except Exception as e:
        raise SerializationError(f"Deserialization error: {str(e)}")

original_obj = EvolvableObject(name="Alice", age=25)
serialized_data = serialize(original_obj)
class EvolvableObjectV2:
    def __init__(self, name, age, new_field=None):
        self.name = name
        self.age = age
        self.new_field = new_field
deserialized_obj = deserialize(serialized_data, EvolvableObjectV2)
print(deserialized_obj.__dict__)