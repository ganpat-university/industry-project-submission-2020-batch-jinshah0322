class Car:
  def __init__(self, model, availability):
      self.model = model
      self.availability = availability

class RentalAgency:
  def __init__(self):
      self.cars = []
      self.customers = []

  def add_car(self, car):
      self.cars.append(car)

  def add_customer(self, customer):
      self.customers.append(customer)

  def rent_car(self, customer, car):
      if car.availability:
          car.availability = False
          customer.rent_car(car)
      else:
          print("Sorry, this car is not available.")

  def return_car(self, customer, car):
      if car in customer.rented_cars:
          car.availability = True
          customer.return_car(car)
      else:
          print("You didn't rent this car.")

class Customer:
  def __init__(self, name):
      self.name = name
      self.rented_cars = []

  def rent_car(self, car):
      self.rented_cars.append(car)

  def return_car(self, car):
      self.rented_cars.remove(car)


agency = RentalAgency()

car1 = Car('Sedan', True)
car2 = Car('SUV', True)

agency.add_car(car1)
agency.add_car(car2)

customer1 = Customer('John')

agency.add_customer(customer1)

agency.rent_car(customer1, car1)

agency.return_car(customer1, car1)

print("Cars available with agency")
for car in agency.cars:
    if car.availability:
        print(car.model)