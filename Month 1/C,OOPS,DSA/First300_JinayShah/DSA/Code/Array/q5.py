arr = list(map(int,input().split()))
cp = []
k = int(input())
for i in range(k,len(arr)):
    cp.append(arr[i])

for i in range(0,k):
    cp.append(arr[i])

print(cp)