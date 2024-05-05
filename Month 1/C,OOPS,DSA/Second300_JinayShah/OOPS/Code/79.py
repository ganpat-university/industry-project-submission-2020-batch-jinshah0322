from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_availability(self, start_date, end_date):
        available_rooms = [room for room in self.rooms if not room.is_booked]
        return available_rooms

class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Reservation:
    def __init__(self, guest, room, start_date, end_date):
        self.guest = guest
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = (end_date - start_date).days * room.price_per_night

        room.is_booked = True

hotel = Hotel("Luxury Inn")

room1 = Room(101, 2, 150)
room2 = Room(102, 3, 200)

hotel.add_room(room1)
hotel.add_room(room2)

guest = Guest("Alice", "alice@example.com")

start_date = datetime(2024, 2, 1)
end_date = datetime(2024, 2, 5)

available_rooms = hotel.check_availability(start_date, end_date)
if available_rooms:
    selected_room = available_rooms[0]
    reservation = Reservation(guest, selected_room, start_date, end_date)
    print(f"Reservation made for {guest.name} in Room {selected_room.room_number}. Total cost: ${reservation.total_cost}")
else:
    print("No available rooms for the selected dates.")
