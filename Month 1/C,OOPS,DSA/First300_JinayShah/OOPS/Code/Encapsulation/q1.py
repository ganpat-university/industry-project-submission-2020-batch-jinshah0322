class BankAccount:
    def __init__(self,accountNumber):
        self.__accountNumber = accountNumber
        self.__balance = 0

    def depositMoney(self,deposit)  :
        self.__balance += deposit
        return f"Final balance is {self.__balance}"

    def withdrawMoney(self,withdraw):
        if(withdraw>self.__balance):
            print("You dont have enough balance")
        else:
            self.__balance -= withdraw
            return f"Final balance is {self.__balance}"

accountNumber = int(input("Enter account number:"))
deposit = int(input("Enter money to be deposited:"))
withdraw = int(input("Enter money to withdraw:"))
bank = BankAccount(accountNumber)
print(bank.depositMoney(deposit))
print(bank.withdrawMoney(withdraw))