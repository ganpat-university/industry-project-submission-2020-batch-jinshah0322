def findFirstAndLast(arr, n, x):
	first = -1
	last = -1
	for i in range(0, n):
		if(arr[i]==x):
			first = i
			last = i
			break
	for i in range(last,n):
		if(arr[i]==x):
			last = i
	print(first)
	print(last)
	


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
findFirstAndLast(arr, n, x)