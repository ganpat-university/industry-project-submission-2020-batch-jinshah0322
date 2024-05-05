arr = list(map(int,input().split()))
n = len(arr)
for i in range(n-1):
    minpos = i
    for j in range(i,n):
        if(arr[j]<arr[minpos]):
            minpos=j
    arr[i],arr[minpos] = arr[minpos],arr[i]

print(arr)