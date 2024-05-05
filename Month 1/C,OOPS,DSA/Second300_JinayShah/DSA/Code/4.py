import heapq

def find_the_city(n, edges, distance_threshold):
    graph = {i: {} for i in range(n)}

    for edge in edges:
        u, v, w = edge
        graph[u][v] = graph[v][u] = w

    def dijkstra(src):
        min_distances = {i: float('inf') for i in range(n)}
        min_distances[src] = 0

        heap = [(0, src)]

        while heap:
            dist_u, u = heapq.heappop(heap)

            if dist_u > min_distances[u]:
                continue

            for v, weight in graph[u].items():
                dist_v = dist_u + weight
                if dist_v < min_distances[v]:
                    min_distances[v] = dist_v
                    heapq.heappush(heap, (dist_v, v))

        return min_distances

    min_neighbors = float('inf')
    result_city = -1

    for city in range(n):
        distances = dijkstra(city)
        neighbors_within_threshold = sum(1 for dist in distances.values() if 0 < dist <= distance_threshold)

        if neighbors_within_threshold < min_neighbors:
            min_neighbors = neighbors_within_threshold
            result_city = city

    return result_city

n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distance_threshold = 4

result = find_the_city(n, edges, distance_threshold)
print("City with the smallest number of neighbors at a threshold distance:", result)
