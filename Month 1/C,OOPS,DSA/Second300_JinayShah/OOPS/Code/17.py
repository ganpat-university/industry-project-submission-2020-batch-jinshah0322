def log_method_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully with result: {result}")
        return result

    return wrapper


class SampleClass:
    @log_method_execution
    def sample_method(self, x, y):
        return x + y


sample_instance = SampleClass()

result = sample_instance.sample_method(10, 20)
print(f"Final result: {result}")
