from typing import Dict

class CommandHandler:
    def __init__(self):
        self.data_store = {}

    def handle_create_command(self, data: Dict):
        entity_id = data.get('id')
        if entity_id not in self.data_store:
            self.data_store[entity_id] = data
            print(f"Entity with ID {entity_id} created successfully.")
        else:
            print(f"Entity with ID {entity_id} already exists.")

    def handle_update_command(self, data: Dict):
        entity_id = data.get('id')
        if entity_id in self.data_store:
            self.data_store[entity_id].update(data)
            print(f"Entity with ID {entity_id} updated successfully.")
        else:
            print(f"Entity with ID {entity_id} does not exist.")

class QueryHandler:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def handle_get_query(self, entity_id: int):
        if entity_id in self.command_handler.data_store:
            return self.command_handler.data_store[entity_id]
        else:
            return f"Entity with ID {entity_id} not found."

command_handler = CommandHandler()
query_handler = QueryHandler(command_handler)

command_handler.handle_create_command({'id': 1, 'name': 'Entity1', 'value': 100})
command_handler.handle_create_command({'id': 2, 'name': 'Entity2', 'value': 200})

command_handler.handle_update_command({'id': 1, 'value': 150})

result = query_handler.handle_get_query(1)
print(result)

result = query_handler.handle_get_query(3)
print(result)
