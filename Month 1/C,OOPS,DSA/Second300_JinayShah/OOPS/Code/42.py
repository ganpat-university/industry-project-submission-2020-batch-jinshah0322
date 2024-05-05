def memoize(f):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")