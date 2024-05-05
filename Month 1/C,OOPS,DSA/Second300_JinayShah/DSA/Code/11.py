import heapq


def make(i, parent, sizez):
	parent[i] = i
	sizez[i] = 1


def find(v, parent):
	if v == parent[v]:
		return v
	parent[v] = find(parent[v], parent)
	return parent[v]


def union(a, b, parent, sizez):
	a = find(a, parent)
	b = find(b, parent)
	if a != b:
		if sizez[a] < sizez[b]:
			a, b = b, a
		parent[b] = a
		sizez[a] += sizez[b]


def min_cost_to_provide_water(n, wells, pipes):
	edges = []

	
	for pipe in pipes:
		u, v, wt = pipe
		edges.append((wt, u, v))

	
	for i in range(n):
		edges.append((wells[i], 0, i + 1))

	
	parent = [0] * (n + 1)
	sizez = [0] * (n + 1)
	for i in range(n + 1):
		make(i, parent, sizez)

	answer = 0

	
	edges.sort()
	for edge in edges:
		wt, u, v = edge
		if find(u, parent) != find(v, parent):
			answer += wt
			union(u, v, parent, sizez)

	return answer


if __name__ == "__main__":
	N = 3
	wells = [1, 2, 2]
	pipes = [
		(1, 2, 1),
		(2, 3, 1)
	]

	
	print(min_cost_to_provide_water(N, wells, pipes))
