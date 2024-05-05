import math

def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = permutation(n, r)
print(f"{n}P{r} = {result}")
result = combination(n, r)
print(f"{n}C{r} = {result}")