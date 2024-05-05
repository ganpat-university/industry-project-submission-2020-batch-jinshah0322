class ConstraintError(Exception):
    pass

def constraint(constraint_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not constraint_func(*args, **kwargs):
                raise ConstraintError("Constraint violation")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def positive_number_constraint(value):
    return isinstance(value, (int, float)) and value > 0

def even_number_constraint(value):
    return isinstance(value, int) and value % 2 == 0

@constraint(positive_number_constraint)
def square_root(x):
    return x ** 0.5

@constraint(even_number_constraint)
def double(x):
    return x * 2

try:
    result1 = square_root(25)
    print("Square Root:", result1)
except ConstraintError as e:
    print(f"Error: {e}")

try:
    result2 = double(10)
    print("Double:", result2)
except ConstraintError as e:
    print(f"Error: {e}")