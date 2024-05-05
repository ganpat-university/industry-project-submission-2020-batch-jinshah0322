import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_obj = Person(name="Alice", age=30)
serialized_data = pickle.dumps(person_obj)

deserialized_obj = pickle.loads(serialized_data)

print("Original Object:")
print(f"Name: {person_obj.name}, Age: {person_obj.age}")

print("\nDeserialized Object:")
print(f"Name: {deserialized_obj.name}, Age: {deserialized_obj.age}")