import zope.interface

class billingStrategy(zope.interface.Interface):
    def pay(self):
        pass

@zope.interface.implementer(billingStrategy)
class NormalBilling:
    def pay(self,amount):
        print(f"your final bill is {amount}")

@zope.interface.implementer(billingStrategy)
class DiscountBilling:
    def __init__(self):
        self.discount = 0.1
    
    def pay(self,amount):
        print(f"your final bill is {amount-amount*self.discount}")

class billing:
    def __init__(self,amount,billing_method):
        self.amount = amount
        self.billing_method = billing_method

    def checkout(self):
        if(self.billing_method=="normal"):
            NormalBilling().pay(self.amount)
        elif(self.billing_method=="discount"):
            DiscountBilling().pay(self.amount)
        else:
            print("Invalid payment method")

billing_method = input("Enter payment method \n1)normal \n2)discount:").lower()
amount = int(input("Enter total amount:"))
bill = billing(amount,billing_method)
bill.checkout()