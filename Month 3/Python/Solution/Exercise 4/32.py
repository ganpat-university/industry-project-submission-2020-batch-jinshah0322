def square_decorator(func):
    def wrapper(x):
        return func(x ** 2)
    return wrapper

def increase_by_10_decorator(func):
    def wrapper(x):
        return func(x + 10)
    return wrapper

@increase_by_10_decorator
@square_decorator
def operation(x):
    return x

result = operation(5)
print("Result:", result) 
