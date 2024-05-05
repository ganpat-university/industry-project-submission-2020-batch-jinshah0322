class ImmutablePerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

person = ImmutablePerson(name="John", age=30)

try:
    person.name = "Jane"
except AttributeError as e:
    print(f"Error: {e}")

point = ImmutablePoint(x=5, y=10)

try:
    point.x = 8
except AttributeError as e:
    print(f"Error: {e}")

print(f"Person: {person.name}, Age: {person.age}")
print(f"Point: X={point.x}, Y={point.y}")
