class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def remove_item(self, product, quantity=1):
        for item in self.items:
            if item["product"] == product:
                if quantity < item["quantity"]:
                    item["quantity"] -= quantity
                    print(f"Removed {quantity} {product.name}(s) from the cart.")
                else:
                    self.items.remove(item)
                    print(f"Removed {item['quantity']} {product.name}(s) from the cart.")
                break
        else:
            print(f"{product.name} not found in the cart.")

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

    def checkout(self):
        total = self.calculate_total()
        print(f"Total amount to pay: ${total}")
        print("Checkout completed. Thank you for shopping!")

class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

product1 = Product(1, "Laptop", 800)
product2 = Product(2, "Headphones", 50)
product3 = Product(3, "Mouse", 20)

customer = Customer("Alice")

customer.shopping_cart.add_item(product1, 2)
customer.shopping_cart.add_item(product2)
customer.shopping_cart.add_item(product3, 3)

print("Items in the cart:")
for item in customer.shopping_cart.items:
    print(f"{item['quantity']} {item['product'].name}(s) - ${item['product'].price} each")

customer.shopping_cart.remove_item(product2, 1)

total_amount = customer.shopping_cart.calculate_total()
print(f"Total amount in the cart: ${total_amount}")

customer.shopping_cart.checkout()