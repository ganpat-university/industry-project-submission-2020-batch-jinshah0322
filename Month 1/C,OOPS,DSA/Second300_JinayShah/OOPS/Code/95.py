class Pet:
   def __init__(self, name):
       self.name = name
       self.health = 100
       self.happiness = 100

   def feed(self, food):
       self.health += food.nutrition
       if self.health > 100:
           self.health = 100

   def play(self):
       self.happiness += 10
       if self.happiness > 100:
           self.happiness = 100

   def update_status(self):
       print(f"{self.name}'s Health: {self.health}, Happiness: {self.happiness}")

class Food:
   def __init__(self, name, nutrition):
       self.name = name
       self.nutrition = nutrition

class Owner:
   def __init__(self, name):
       self.name = name
       self.pet = None

   def adopt_pet(self, pet):
       self.pet = pet

   def feed_pet(self, food):
       self.pet.feed(food)

   def play_with_pet(self):
       self.pet.play()

   def check_pet_status(self):
       self.pet.update_status()


owner = Owner('Karan')
pet = Pet('Kukoo')
owner.adopt_pet(pet)

food = Food('Apple', 10)
owner.feed_pet(food)

owner.play_with_pet()
owner.check_pet_status()
