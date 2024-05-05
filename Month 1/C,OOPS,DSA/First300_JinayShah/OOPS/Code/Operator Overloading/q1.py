class complexNumber:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self,other):
        newReal = self.real+other.real
        newImaginary = self.imaginary+other.imaginary
        return complexNumber(newReal,newImaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    
real = int(input("Enter real number:"))
imaginary = int(input("Enter imaginary number:"))
realadd = int(input("Enter other real number to be added:"))
imaginaryadd = int(input("Enter other imaginary number to be added:"))
cn1 = complexNumber(real,imaginary)
cn2 = complexNumber(realadd,imaginaryadd)
result = cn1+cn2
print(result)