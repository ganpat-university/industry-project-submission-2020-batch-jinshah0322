def gcdfinder(n1,n2):
    greater = max(n1,n2)
    for i in range(1,greater+1):
        if(n1%i==0 and n2%i==0):
            ans = i
    return ans

arr = list(map(int,input().split()))
n1 = arr[0]
n2= arr[1]
gcd = gcdfinder(n1,n2)
for i in range(2,len(arr)):
    gcd = gcdfinder(gcd,arr[i])
print(gcd)