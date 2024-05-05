arr = list(map(int,input().split()))
arr = sorted(arr)
for i in range(len(arr)-1,0,-1):
    if(arr[i]==arr[i-1]):
        del arr[i]

print(arr)