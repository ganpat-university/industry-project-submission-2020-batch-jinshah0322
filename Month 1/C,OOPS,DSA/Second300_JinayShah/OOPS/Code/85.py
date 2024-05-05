class Aircraft:
   def __init__(self, model, capacity):
       self.model = model
       self.capacity = capacity

class Airport:
   def __init__(self, name):
       self.name = name
       self.aircrafts = []

   def add_aircraft(self, aircraft):
       self.aircrafts.append(aircraft)

   def remove_aircraft(self, aircraft):
       self.aircrafts.remove(aircraft)

class Flight:
   def __init__(self, flight_number, departure_airport, arrival_airport, aircraft):
       self.flight_number = flight_number
       self.departure_airport = departure_airport
       self.arrival_airport = arrival_airport
       self.aircraft = aircraft

   def simulate_flight(self):
       print(f"Flight {self.flight_number} departing from {self.departure_airport.name} in {self.aircraft.model}")
       print(f"Arriving at {self.arrival_airport.name}")


airport1 = Airport('Airport1')
airport2 = Airport('Airport2')

aircraft1 = Aircraft('Boeing747', 416)
aircraft2 = Aircraft('AirbusA380', 853)

airport1.add_aircraft(aircraft1)
airport2.add_aircraft(aircraft2)

flight1 = Flight('Aerogoods', airport1, airport2, aircraft1)
flight2 = Flight('Bigindia', airport2, airport1, aircraft2)

flight1.simulate_flight()
flight2.simulate_flight()

airport1.remove_aircraft(aircraft1)
airport2.remove_aircraft(aircraft2)
