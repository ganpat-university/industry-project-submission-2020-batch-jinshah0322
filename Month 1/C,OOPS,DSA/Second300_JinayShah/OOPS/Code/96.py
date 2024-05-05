class Product:
   def __init__(self, id, name, category, quantity):
       self.id = id
       self.name = name
       self.category = category
       self.quantity = quantity

class Category:
   def __init__(self, name):
       self.name = name
       self.products = []

   def add_product(self, product):
       self.products.append(product)

   def remove_product(self, product):
       self.products.remove(product)

class Warehouse:
   def __init__(self):
       self.categories = []

   def add_category(self, category):
       self.categories.append(category)

   def remove_category(self, category):
       self.categories.remove(category)

   def add_product(self, category, product):
       for cat in self.categories:
           if cat.name == category:
               cat.add_product(product)
               break

   def remove_product(self, category, product):
       for cat in self.categories:
           if cat.name == category:
               cat.remove_product(product)
               break

electronics = Category('Electronics')
laptop = Product(1, 'Laptop', electronics, 100)
mobile = Product(2, 'Mobile', electronics, 50)

warehouse = Warehouse()
warehouse.add_category(electronics)
warehouse.add_product('Electronics', laptop)
warehouse.add_product('Electronics', mobile)

for category in warehouse.categories:
   print(f"Category: {category.name}")
   for product in category.products:
       print(f"Product ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}")
