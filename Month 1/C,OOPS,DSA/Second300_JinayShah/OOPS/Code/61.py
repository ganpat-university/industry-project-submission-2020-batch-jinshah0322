class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Balance for {self.account_holder}: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest. New balance: ${self.balance}")

account = BankAccount("Alice")
account.deposit(1000)
account.withdraw(200)
account.check_balance()

savings_account = SavingsAccount("Bob", interest_rate=0.05)
savings_account.deposit(500)
savings_account.add_interest()
savings_account.check_balance()
savings_account.withdraw(100)
savings_account.check_balance()