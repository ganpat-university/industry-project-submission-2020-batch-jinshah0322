class Item:
   def __init__(self, name, initial_bid):
       self.name = name
       self.current_bid = initial_bid
       self.highest_bidder = None

class Auction:
   def __init__(self):
       self.items = []
       self.bidders = []

   def add_item(self, item):
       self.items.append(item)

   def add_bidder(self, bidder):
       self.bidders.append(bidder)

   def place_bid(self, bidder, item, bid_amount):
       if bid_amount > item.current_bid:
           item.current_bid = bid_amount
           item.highest_bidder = bidder
       else:
           print("Your bid is lower than the current bid.")

class Bidder:
   def __init__(self, name):
       self.name = name
       self.bids = {}

   def place_bid(self, item, bid_amount):
       self.bids[item] = bid_amount


# Create an auction
auction = Auction()

# Create items
item1 = Item('Item1', 100)
item2 = Item('Item2', 200)

# Add items to the auction
auction.add_item(item1)
auction.add_item(item2)

# Create a bidder
bidder1 = Bidder('John')

# Add the bidder to the auction
auction.add_bidder(bidder1)

# Place a bid
auction.place_bid(bidder1, item1, 150)
auction.place_bid(bidder1, item2, 250)

for item in auction.items:
    print("Item:", item.name, "Highest bidder:", item.highest_bidder.name)
