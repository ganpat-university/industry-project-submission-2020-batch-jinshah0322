class Account:
 def __init__(self, account_number, account_holder):
     self.account_number = account_number
     self.account_holder = account_holder
     self.balance = 0
     self.transaction_history = []

 def deposit(self, amount):
     self.balance += amount
     self.transaction_history.append(('Deposit', amount))

 def withdraw(self, amount):
     if self.balance >= amount:
         self.balance -= amount
         self.transaction_history.append(('Withdrawal', amount))
     else:
         print("Insufficient balance.")

 def check_balance(self):
     return self.balance

class Customer:
 def __init__(self, name):
     self.name = name
     self.accounts = []

 def add_account(self, account):
     self.accounts.append(account)

class Bank:
 def __init__(self):
     self.customers = []

 def add_customer(self, customer):
     self.customers.append(customer)

 def transfer_funds(self, sender_account, receiver_account, amount):
     if sender_account.check_balance() >= amount:
         sender_account.withdraw(amount)
         receiver_account.deposit(amount)
     else:
         print("Insufficient funds.")


bank = Bank()

customer1 = Customer('John')
customer2 = Customer('Jane')

bank.add_customer(customer1)
bank.add_customer(customer2)

account1 = Account('12345', customer1)
account2 = Account('67890', customer2)

customer1.add_account(account1)
customer2.add_account(account2)

account1.deposit(1000)

bank.transfer_funds(account1, account2, 500)

print("Balance fo account1 is:", account1.check_balance()) 
print("Balance fo account2 is:",account2.check_balance())
