class mathOperations:
    @staticmethod
    def squareRoot(n):
        if(n>0):
            return n**0.5
        else:
            return "Square root of negative number is not possible"
        
n = int(input("Enter a number:"))
print(mathOperations.squareRoot(n))