class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

class Order:
    def __init__(self, customer_name, shopping_cart):
        self.customer_name = customer_name
        self.shopping_cart = shopping_cart

    def process_order(self):
        total_amount = self.shopping_cart.calculate_total()
        print(f"Processing order for {self.customer_name}. Total amount: ${total_amount}")

product1 = Product(1, "Laptop", 1000)
product2 = Product(2, "Smartphone", 500)

shopping_cart = ShoppingCart()
shopping_cart.add_product(product1, 2)
shopping_cart.add_product(product2, 1)

order = Order("John Doe", shopping_cart)
order.process_order()
