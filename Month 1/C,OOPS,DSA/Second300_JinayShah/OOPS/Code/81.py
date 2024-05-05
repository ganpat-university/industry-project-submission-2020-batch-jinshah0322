class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_availability(self, room_type):
        available_rooms = [room for room in self.rooms if room.is_available and room.room_type == room_type]
        return available_rooms

    def check_in(self, room, guest):
        if room.is_available:
            room.is_available = False
            room.guest = guest
        else:
            print("Room is not available")

    def check_out(self, room):
        if not room.is_available:
            room.is_available = True
            room.guest = None
        else:
            print("Guest is not checked in")


class Room:
    def __init__(self, room_type, price):
        self.room_type = room_type
        self.price = price
        self.is_available = True
        self.guest = None

    def get_price(self):
        return self.price


class Guest:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Booking:
    def __init__(self, hotel, room, guest, check_in_date, check_out_date):
        self.hotel = hotel
        self.room = room
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def check_in(self):
        self.hotel.check_in(self.room, self.guest)

    def check_out(self):
        self.hotel.check_out(self.room)

hotel = Hotel("Plaza")

room1 = Room("single", 100)
room2 = Room("double", 200)

hotel.add_room(room1)
hotel.add_room(room2)

guest1 = Guest("John Doe", "123 Street, City")

booking1 = Booking(hotel, room1, guest1, "2022-01-01", "2022-01-05")
booking1.check_in()

print(hotel.check_availability("single"))


booking1.check_out()

print("Is single room available:", hotel.check_availability("single")[0].is_available)