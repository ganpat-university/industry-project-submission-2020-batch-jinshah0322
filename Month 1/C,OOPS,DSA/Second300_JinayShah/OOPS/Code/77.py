class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

class Recipe:
    def __init__(self, title, ingredients, instructions, category):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

class Cookbook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = [recipe for recipe in self.recipes if any(ingredient.name == ingredient_name for ingredient in recipe.ingredients)]
        return matching_recipes


cookbook = Cookbook()

recipe1 = Recipe("Spaghetti Bolognese", [Ingredient("Spaghetti", 200, "g"), Ingredient("Tomato Sauce", 400, "ml")], "Cook spaghetti, mix with sauce.", "Italian")
recipe2 = Recipe("Chicken Stir-Fry", [Ingredient("Manchurian", 300, "g"), Ingredient("Vegetables", 200, "g")], "Cabage.", "Asian")

cookbook.add_recipe(recipe1)
cookbook.add_recipe(recipe2)

search_result = cookbook.search_by_ingredient("Spaghetti")
for recipe in search_result:
    print(f"Matching Recipe: {recipe.title}")
