import random
def decorator(fx):
    def numberGenerator():
        num1,num2 = random.sample(range(1,11),2)
        return fx(num1,num2)
    return numberGenerator

@decorator
def add(n1,n2):
    print(n1+n2)

@decorator
def sub(n1,n2):
    print(n1-n2)

@decorator
def mul(n1,n2):
    print(n1*n2)

@decorator
def div(n1,n2):
    print(n1/n2)

add()
sub()
mul()
div()