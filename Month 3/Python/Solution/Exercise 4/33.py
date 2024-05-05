def multiply_decorator(param1, param2):
    def decorator(func):
        def wrapper(x, y):
            multiplied_result = param1 * param2
            return func(x * multiplied_result, y * multiplied_result)
        return wrapper
    return decorator

@multiply_decorator(2, 3)
def multiply_function(a, b):
    return a * b

result = multiply_function(4, 5)
print("Result:", result) 