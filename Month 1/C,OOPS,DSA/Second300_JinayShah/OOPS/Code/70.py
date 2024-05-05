class Vehicle:
  def __init__(self, license_plate, size):
      self.license_plate = license_plate
      self.size = size

class Ticket:
  def __init__(self, vehicle, ticket_number):
      self.vehicle = vehicle
      self.ticket_number = ticket_number

class ParkingLot:
  def __init__(self, size):
      self.size = size
      self.spots = [None]*size
      self.tickets = []

  def park_vehicle(self, vehicle):
      for i in range(self.size):
          if self.spots[i] is None:
              self.spots[i] = vehicle
              ticket = Ticket(vehicle, i+1)
              self.tickets.append(ticket)
              return f"Vehicle parked with ticket #{ticket.ticket_number}"
      return "Parking lot is full."

  def retrieve_vehicle(self, ticket_number):
      for i in range(self.size):
          if self.spots[i] is not None and self.tickets[i].ticket_number == ticket_number:
              vehicle = self.spots[i]
              self.spots[i] = None
              del self.tickets[i]
              return f"Vehicle with license plate {vehicle.license_plate} retrieved."
      return "Invalid ticket number."

  def calculate_fee(self, ticket_number):
      for ticket in self.tickets:
          if ticket.ticket_number == ticket_number:
              return ticket.vehicle.size * 10 # Assuming $10 fee per hour
      return "Invalid ticket number."

car1 = Vehicle("ABC123", 1)
car2 = Vehicle("XYZ789", 1)

parking_lot = ParkingLot(2)
print(parking_lot.park_vehicle(car1))
print(parking_lot.park_vehicle(car2))

print(parking_lot.retrieve_vehicle(1))

print(parking_lot.calculate_fee(2))