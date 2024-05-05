from functools import wraps

def compile_time_factorial(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        n = args[0]
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    return wrapper

@compile_time_factorial
def factorial(n):
    return n

result = factorial(5)
print(result)
