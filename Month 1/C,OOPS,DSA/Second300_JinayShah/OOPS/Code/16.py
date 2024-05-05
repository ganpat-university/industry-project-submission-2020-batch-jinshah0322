from typing import Dict

class Event:
    def __init__(self, entity_id: int):
        self.entity_id = entity_id


class EntityCreated(Event):
    def __init__(self, entity_id: int, name: str, value: int):
        super().__init__(entity_id)
        self.name = name
        self.value = value


class EntityUpdated(Event):
    def __init__(self, entity_id: int, value: int):
        super().__init__(entity_id)
        self.value = value


class Entity:
    def __init__(self, entity_id: int):
        self.entity_id = entity_id
        self.name = ""
        self.value = 0
        self.changes = []

    def create(self, name: str, value: int):
        event = EntityCreated(self.entity_id, name, value)
        self.apply_change(event)

    def update(self, value: int):
        event = EntityUpdated(self.entity_id, value)
        self.apply_change(event)

    def apply_change(self, event: Event):
        self.changes.append(event)
        self.apply(event)

    def apply(self, event: Event):
        if isinstance(event, EntityCreated):
            self.name = event.name
            self.value = event.value
        elif isinstance(event, EntityUpdated):
            self.value = event.value


class EventStore:
    def __init__(self):
        self.events = []

    def save_event(self, event: Event):
        self.events.append(event)

    def get_events_for_entity(self, entity_id: int):
        return [event for event in self.events if event.entity_id == entity_id]


event_store = EventStore()

entity = Entity(entity_id=1)
entity.create(name="Entity1", value=100)
event_store.save_event(entity.changes[0])

entity.update(value=150)
event_store.save_event(entity.changes[1])

events_for_entity = event_store.get_events_for_entity(entity_id=1)

reconstructed_entity = Entity(entity_id=1)

for event in events_for_entity:
    reconstructed_entity.apply(event)

print(f"Final State - Entity ID: {reconstructed_entity.entity_id}, Name: {reconstructed_entity.name}, Value: {reconstructed_entity.value}")