import inspect
import functools

class DependencyInjector:
    def __init__(self):
        self.dependencies = {}

    def register_dependency(self, dependency_type, dependency_instance):
        self.dependencies[dependency_type] = dependency_instance

    def inject_dependencies(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signature = inspect.signature(func)
            parameters = signature.parameters

            for param_name, param_info in parameters.items():
                param_type = param_info.annotation

                if param_type != inspect.Parameter.empty and param_type in self.dependencies:
                    kwargs[param_name] = self.dependencies[param_type]

            return func(*args, **kwargs)

        return wrapper

# Example Usage
class Database:
    def query(self, query):
        return f"Executing query: {query}"

class Service:
    @DependencyInjector().inject_dependencies
    def __init__(self, database: Database):
        self.database = database

    @DependencyInjector().inject_dependencies
    def perform_operation(self):
        if self.database:
            result = self.database.query("SELECT * FROM table")
            print(result)
        else:
            print("Database dependency not injected.")

database_instance = Database()
service_instance = Service(database=database_instance)

# Use the Service instance
service_instance.perform_operation()
