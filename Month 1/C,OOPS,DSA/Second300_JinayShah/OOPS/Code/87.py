class Ingredient:
   def __init__(self, name):
       self.name = name

class Recipe:
   def __init__(self, name, ingredients):
       self.name = name
       self.ingredients = ingredients

class User:
   def __init__(self, name, dietary_restrictions=None):
       self.name = name
       self.dietary_restrictions = dietary_restrictions if dietary_restrictions else []

   def suggest_recipe(self, recipe):
       for ingredient in recipe.ingredients:
           if ingredient.name in self.dietary_restrictions:
               return False
       return True


ingredient1 = Ingredient('Namkeen')
ingredient2 = Ingredient('Salted')

recipe1 = Recipe('Namkeen Soup', [ingredient1])

user1 = User('Kiara', ['Salted'])

if user1.suggest_recipe(recipe1):
   print(f"{user1.name}, we suggest you try {recipe1.name}.")
else:
   print(f"{user1.name}, we don't have a suitable recipe for you.")
