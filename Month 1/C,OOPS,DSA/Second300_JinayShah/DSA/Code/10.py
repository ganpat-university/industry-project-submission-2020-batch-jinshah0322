parent = [0] * 100010



sizez = [0] * 100010



freq = [0] * 100010


st = set()



def make(i):
	parent[i] = i
	sizez[i] = 1
	freq[1] += 1



def find(v):
	if v == parent[v]:
		return v
	parent[v] = find(parent[v])
	return parent[v]




def Union(a, b):
	a = find(a)
	b = find(b)
	if a != b:
		if sizez[a] < sizez[b]:
			a, b = b, a
		
		
		freq[sizez[a]] -= 1

		
		if freq[sizez[a]] == 0:
			st.remove(sizez[a])

		
		freq[sizez[b]] -= 1

		
		if freq[sizez[b]] == 0:
			st.remove(sizez[b])
		
		parent[b] = a
		sizez[a] += sizez[b]

		
		freq[sizez[a]] += 1

		
		if freq[sizez[a]] == 1:
			st.add(sizez[a])


N, Q = 4, 2
queries = [[1, 2], [2, 4]]


st.add(1)


for i in range(1, N + 1):
	make(i)

for i in range(Q):
	u, v = queries[i]
	Union(u, v)
	ans = float('inf')
	pre = float('-inf')

	
	
	for e in sorted(st):
		
		
		if freq[e] > 1:
			ans = 0
			break
		ans = min(ans, e - pre)
		pre = e
	
	if ans == float('inf'):
		ans = 0
	print(ans)

