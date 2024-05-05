from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class SmartContract(ABC):
    def __init__(self, contract_id, parties):
        self.contract_id = contract_id
        self.parties = parties
        self.is_active = True

    @abstractmethod
    def execute(self):
        pass

    def deactivate(self):
        self.is_active = False

class PaymentContract(SmartContract):
    def __init__(self, contract_id, parties, amount):
        super().__init__(contract_id, parties)
        self.amount = amount

    def execute(self):
        if self.is_active:
            print(f"Payment of ${self.amount} executed between {self.parties[0]} and {self.parties[1]}")
            self.deactivate()
        else:
            print("Contract is not active.")

class SubscriptionContract(SmartContract):
    def __init__(self, contract_id, parties, start_date, duration_months):
        super().__init__(contract_id, parties)
        self.start_date = start_date
        self.duration_months = duration_months

    def execute(self):
        if self.is_active:
            end_date = self.start_date + timedelta(days=30 * self.duration_months)
            print(f"Subscription started on {self.start_date}, will end on {end_date} for {self.parties[0]}")
            self.deactivate()
        else:
            print("Contract is not active.")


payment_contract = PaymentContract(contract_id=1, parties=["Alice", "Bob"], amount=100)
payment_contract.execute()

subscription_contract = SubscriptionContract(contract_id=2, parties=["Charlie", "David"], start_date=datetime.now(), duration_months=6)
subscription_contract.execute()
