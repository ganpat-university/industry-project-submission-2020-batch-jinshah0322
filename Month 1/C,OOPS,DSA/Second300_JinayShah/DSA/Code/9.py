def bipartite_color(v, g, colr, paint):
	global one, zero, flag

	
	if colr[v] != -1:
		
		
		
		if colr[v] != paint:
			flag = False
		return

	
	colr[v] = paint

	
	if paint:
		one += 1
	
	else:
		zero += 1

	
	for child in g[v]:
		
		
		
		bipartite_color(child, g, colr, not paint)


def maximum_soldier(N, arr):
	global one, zero, flag

	
	g = [[] for _ in range(20001)]

	
	st = set()
	
	for i in range(N):
		
		u, v = arr[i][0], arr[i][1]

		
		g[u].append(v)
		g[v].append(u)

		
		st.add(u)
		st.add(v)

	
	soldiers = list(st)

	
	ans = 0

	
	colr = [-1] * 20001

	
	for e in soldiers:
		
		if colr[e] != -1:
			continue

		
		one = 0
		zero = 0

		
		bipartite_color(e, g, colr, 0)

		
		ans += max(one, zero)

	if flag:
		print(ans)
	else:
		print(-1)

if __name__ == "__main__":
	
	N = 4
	arr = [[1, 2], [2, 3], [2, 4], [2, 5]]
	flag = True

	
	maximum_soldier(N, arr)
	

