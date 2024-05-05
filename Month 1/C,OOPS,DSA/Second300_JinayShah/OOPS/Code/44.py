from functools import wraps

def enforce_type(type_constraint):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_constraint):
                    raise TypeError(f"Argument {arg} does not satisfy the type constraint {type_constraint}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@enforce_type(int)
def add_numbers(a, b):
    return a + b

@enforce_type(str)
def concatenate_strings(s1, s2):
    return s1 + s2

if __name__ == "__main__":
    try:
        result = add_numbers(3, 4)
        print("Result of add_numbers:", result)

        result = concatenate_strings("Hello", "World")
        print("Result of concatenate_strings:", result)

        # This will raise a TypeError because "Hello" is not an integer
        add_numbers("Hello", 5)
    except TypeError as e:
        print(f"TypeError: {e}")