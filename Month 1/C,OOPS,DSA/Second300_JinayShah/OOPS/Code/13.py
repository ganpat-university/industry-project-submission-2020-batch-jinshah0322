import zope.interface

class PaymentStrategy(zope.interface.Interface):
    def pay(self):
        pass

@zope.interface.implementer(PaymentStrategy)
class CreditCardPayment:
    def __init__(self,cardNumber,cvv,expiryDate):
        self.cardNumber = cardNumber
        self.cvv = cvv
        self.expiryDate = expiryDate

    def pay(self,amount):
        print(f"Card payment with card number {self.cardNumber}, cvv {self.cvv} ,expiry date {self.expiryDate} and amount {amount}")

@zope.interface.implementer(PaymentStrategy)
class PayPalPayment:
    def __init__(self,pin):
        self.pin = pin
    
    def pay(self,amount):
        print(f"PaypalPayment payment done with amount {amount}")

class shoppingCart:
    def __init__(self,payment_method,amount,cardNumber=None,cvv=None,expiryDate=None,pin=None):
        self.payment_method = payment_method
        self.amount = amount
        self.cardNumber = cardNumber
        self.cvv = cvv
        self.expiryDate = expiryDate
        self.pin = pin

    def checkout(self):
        if(self.payment_method=="card"):
            CreditCardPayment(self.cardNumber,self.cvv,self.expiryDate).pay(self.amount)
        elif(self.payment_method=="paypal"):
            PayPalPayment(self.pin).pay(self.amount)
        else:
            print("Invalid payment method")

payment_method = input("Enter payment method \n1)Card \n2)Paypal:").lower()
amount = int(input("Enter total amount:"))
if(payment_method == "card"):
    cardNumber = input("Enter card number:")
    cvv = input("Enter cvv:")
    expiryDate = input("Enter expiry date:")
    sc = shoppingCart(payment_method=payment_method,cardNumber=cardNumber,cvv=cvv,expiryDate=expiryDate,amount=amount).checkout()
else:
    pin = input("Enter pin:")
    sc = shoppingCart(payment_method=payment_method,amount=amount).checkout()