arr = list(map(int,input().split()))
reverse = []
for i in range(len(arr)-1,-1,-1):
    reverse.append(arr[i])
print(reverse)