import numpy as np

n = int(input("Enter number of rows for matrix:"))
matrix = np.zeros([n,n])
additionList = []
summation=0
principlediagnol=0
secondarydiagnol=0
counter=0

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())

for i in range(n):
    for j in  range(n):
        summation+=matrix[i][j]
    additionList.append(summation)
    summation=0


for i in range(n):
    for j in range(n):
        summation+=matrix[j][i]
    additionList.append(summation)
    summation=0

for i in range(0, n): 
    principlediagnol += matrix[i][i]
    secondarydiagnol += matrix[i][n - i - 1]
additionList.append(principlediagnol)
additionList.append(secondarydiagnol)

print(additionList)

for i in additionList:
    if(i==additionList[0]):
        counter+=1;
    else:
        pass


if(counter==len(additionList)):
    print("Magic square")
else:
    print("Not a magic square")