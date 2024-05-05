from math import factorial

n = int(input())
result = []
resultappend = []
for i in range(n):
    for j in range(i+1):
        resultappend.append(0)
    result.append(resultappend)
    resultappend = []
    
for i in range(n):
    for j in range(i+1):
        result[i][j] = factorial(i)/(factorial(j)*factorial(i-j))
print(result)