class Coffee:
    def cost(self):
        return 150
    
class Milk:
    def __init__(self,coffee) -> None:
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 50
    
class Sugar:
    def __init__(self,coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10
    
c = Coffee()
print(f"Plain coffee cost = {c.cost()}")
m = Milk(c)
print(f"Coffee with milk = {m.cost()}")
s = Sugar(c)
print(f"Coffee with sugar = {s.cost()}")