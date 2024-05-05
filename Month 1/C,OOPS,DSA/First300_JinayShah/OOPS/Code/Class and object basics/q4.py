class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Company name is {self.make} having model {self.model} and was created in year {self.year}")

make = input("Enter the company name:")
model = input("Enter the model name:")
year = input("Enter the year:")
car = Car(make,model,year)
car.display()