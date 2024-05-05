def gcd(a, b):
	if (a == 0):
		return b
	return gcd(b % a, a)

def LcmOfArray(arr, index):
	if (index == len(arr)-1):
		return arr[index]
	a = arr[index]
	b = LcmOfArray(arr, index+1)
	return int(a*b/gcd(a,b))

arr = list(map(int,input().split()))
print(LcmOfArray(arr, 0))