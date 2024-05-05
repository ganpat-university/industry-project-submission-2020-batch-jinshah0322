class Instrument:
    def __init__(self, type, price):
        self.type = type
        self.price = price

class Musician:
    def __init__(self, name):
        self.name = name
        self.instruments = []

    def buy_instrument(self, instrument):
        self.instruments.append(instrument)

class Inventory:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def remove_instrument(self, instrument):
        self.instruments.remove(instrument)

inventory = Inventory()

instrument1 = Instrument('Guitar', 2000)
instrument2 = Instrument('Piano', 5000)

inventory.add_instrument(instrument1)
inventory.add_instrument(instrument2)

musician1 = Musician('John')
musician2 = Musician('Jane')

musician1.buy_instrument(instrument1)
musician2.buy_instrument(instrument2)

for instrument in inventory.instruments:
    print(instrument.type)
