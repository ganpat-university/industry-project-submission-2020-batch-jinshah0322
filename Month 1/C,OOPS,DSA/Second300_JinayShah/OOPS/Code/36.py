import functools
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def log_entry_exit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Entering {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Exiting {func.__name__} with result {result}")
        return result
    return wrapper

@log_entry_exit
def example_function(x, y):
    return x + y

class ExampleClass:
    @log_entry_exit
    def example_method(self, x, y):
        return x * y

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

result1 = example_function(3, 4)
print(f"Result 1: {result1}")

example_instance = ExampleClass()
result2 = example_instance.example_method(5, 6)
print(f"Result 2: {result2}")
