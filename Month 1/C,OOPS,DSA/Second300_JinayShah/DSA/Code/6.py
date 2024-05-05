

parent = list(range(26))



def find(v):
	if v == parent[v]:
		return v
	parent[v] = find(parent[v])
	return parent[v]



def Union(a, b):
	a = find(a)
	b = find(b)
	if a != b:
		parent[b] = a

def satisfactoryEquation(arr):
	
	for i in range(26):
		parent[i] = i

	
	for e in arr:
		a = ord(e[0]) - ord('a')
		b = ord(e[3]) - ord('a')
		c = e[1]

		
		if c == '=':
			
			Union(a, b)

	
	for e in arr:
		
		if e[1] == '!':
			a = ord(e[0]) - ord('a')
			b = ord(e[3]) - ord('a')

			
			if find(a) == find(b):
				return "False"

	return "True"


if __name__ == "__main__":
	N = 3
	arr = ["a==b", "a==c", "b!=c"]

	
	print(satisfactoryEquation(arr))
