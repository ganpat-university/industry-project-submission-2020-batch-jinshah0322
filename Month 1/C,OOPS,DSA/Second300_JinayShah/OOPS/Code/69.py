class Event:
    def __init__(self, event_id, name, date, location, organizer):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.organizer = organizer
        self.attendees = set()

    def register_attendee(self, attendee):
        self.attendees.add(attendee)
        print(f"{attendee.name} has registered for the event '{self.name}'.")

    def notify_attendees(self, message):
        print(f"Sending notification to attendees of '{self.name}': {message}")
        for attendee in self.attendees:
            attendee.receive_notification(message)


class Attendee:
    def __init__(self, attendee_id, name, email):
        self.attendee_id = attendee_id
        self.name = name
        self.email = email

    def receive_notification(self, message):
        print(f"Notification for {self.name}: {message}")


class Organizer:
    def __init__(self, organizer_id, name, email):
        self.organizer_id = organizer_id
        self.name = name
        self.email = email

    def create_event(self, event_id, name, date, location):
        event = Event(event_id, name, date, location, self)
        print(f"Event '{name}' created by {self.name}.")
        return event


organizer = Organizer(1, "Event Organizer", "organizer@example.com")
attendee1 = Attendee(2, "Alice", "alice@example.com")
attendee2 = Attendee(3, "Bob", "bob@example.com")

event = organizer.create_event(1, "Tech Conference", "2024-01-31", "Convention Center")

event.register_attendee(attendee1)
event.register_attendee(attendee2)

event.notify_attendees("Tech Conference details have been updated.")