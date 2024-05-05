class Destination:
   def __init__(self, name):
       self.name = name

class Itinerary:
   def __init__(self, traveler):
       self.destinations = []
       self.traveler = traveler

   def add_destination(self, destination):
       self.destinations.append(destination)

   def remove_destination(self, destination):
       self.destinations.remove(destination)

class Traveler:
   def __init__(self, name):
       self.name = name
       self.itineraries = []

   def create_itinerary(self):
       itinerary = Itinerary(self)
       self.itineraries.append(itinerary)
       return itinerary


destination1 = Destination('Paris')
destination2 = Destination('London')

traveler1 = Traveler('John')

itinerary1 = traveler1.create_itinerary()

itinerary1.add_destination(destination1)
itinerary1.add_destination(destination2)

for itineraries in itinerary1.destinations:
    print("Destinations added to itenaries:", itineraries.name)
