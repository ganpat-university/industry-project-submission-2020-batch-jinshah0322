class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Transaction:
    def __init__(self, stock, quantity, price_per_share):
        self.stock = stock
        self.quantity = quantity
        self.price_per_share = price_per_share
        self.total_cost = quantity * price_per_share

    def __str__(self):
        return f"Transaction: {self.quantity} shares of {self.stock.symbol} at ${self.price_per_share} per share. Total Cost: ${self.total_cost}"

class Portfolio:
    def __init__(self):
        self.transactions = []

    def buy_stock(self, stock, quantity, price_per_share):
        transaction = Transaction(stock, quantity, price_per_share)
        self.transactions.append(transaction)

    def sell_stock(self, stock, quantity, price_per_share):
        for transaction in self.transactions:
            if transaction.stock == stock:
                transaction.quantity -= quantity
                transaction.total_cost -= quantity * price_per_share
                if transaction.quantity <= 0:
                    self.transactions.remove(transaction)

    def get_total_value(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.quantity * transaction.stock.price
        return total

    def get_transaction_history(self):
        return [str(transaction) for transaction in self.transactions]

stock1 = Stock("AAPL", 150)
stock2 = Stock("GOOGL", 2000)

portfolio = Portfolio()

portfolio.buy_stock(stock1, 10, 150)
portfolio.buy_stock(stock2, 5, 2000)

print(portfolio.get_total_value())

portfolio.sell_stock(stock1, 5, 150)

print(portfolio.get_total_value())

print(portfolio.get_transaction_history())