n = int(input())
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        if(j == i or j == 0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print(end=" ")
for i in range(n+1):
    print("*",end=" ")