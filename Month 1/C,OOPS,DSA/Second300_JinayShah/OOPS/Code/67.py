class Flight:
  def __init__(self, flight_number, capacity):
      self.flight_number = flight_number
      self.capacity = capacity
      self.seats = [None]*capacity

  def book_seat(self, passenger):
      for i in range(len(self.seats)):
          if self.seats[i] is None:
              self.seats[i] = passenger
              return True
      return False

  def cancel_reservation(self, passenger):
      for i in range(len(self.seats)):
          if self.seats[i] == passenger:
              self.seats[i] = None
              return True
      return False

  def check_availability(self):
      return sum([1 for seat in self.seats if seat is None])

class Passenger:
  def __init__(self, name):
      self.name = name

class Reservation:
  def __init__(self):
      self.flights = {}

  def add_flight(self, flight):
      self.flights[flight.flight_number] = flight

  def book_seat(self, flight_number, passenger):
      if flight_number in self.flights:
          return self.flights[flight_number].book_seat(passenger)
      return False

  def cancel_reservation(self, flight_number, passenger):
      if flight_number in self.flights:
          return self.flights[flight_number].cancel_reservation(passenger)
      return False

  def check_availability(self, flight_number):
      if flight_number in self.flights:
          return self.flights[flight_number].check_availability()
      return -1

flight1 = Flight('FL101', 10)
passenger1 = Passenger('John Doe')

reservation = Reservation()
reservation.add_flight(flight1)

print(reservation.book_seat('FL101', passenger1))

print(reservation.cancel_reservation('FL101', passenger1))

print(reservation.check_availability('FL101'))
