class Calculator:
    def add(self,n1,n2,n3=None):
        if(n3 is None):
            return n1+n2
        else:
            return n1+n2+n3
    
calc = Calculator()
print(calc.add(1,2))
print(calc.add(1,2,3))