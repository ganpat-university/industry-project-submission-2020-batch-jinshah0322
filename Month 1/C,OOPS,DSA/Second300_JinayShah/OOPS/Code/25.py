from typing import Protocol, TypeVar, Union, List

T = TypeVar('T', int, float)

class HasMultiplyMethod(Protocol):
    def __mul__(self, other: Union[int, float]) -> T: ...


def multiply_elements(lst: List[HasMultiplyMethod], factor: Union[int, float]) -> List[T]:
    return [item * factor for item in lst]


numbers = [1, 2, 3, 4, 5]
result = multiply_elements(numbers, 2)
print(result)
