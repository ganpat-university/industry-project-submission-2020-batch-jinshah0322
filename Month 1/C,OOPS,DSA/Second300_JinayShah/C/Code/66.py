import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def bitonic_tsp(points):
    n = len(points)
    
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distances[i][j] = euclidean_distance(points[i], points[j])
            distances[j][i] = distances[i][j]

    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 0

    for k in range(1, n):
        for i in range(k - 1, -1, -1):
            for j in range(i + 1):
                dp[i][k] = min(dp[i][k], dp[j][i] + distances[j][k])

    min_tour_distance = float('inf')
    for i in range(n - 1):
        min_tour_distance = min(min_tour_distance, dp[i][n - 1] + distances[i][n - 1])

    return min_tour_distance

points = [(0, 0), (1, 2), (3, 1), (5, 2), (6, 0)]
result = bitonic_tsp(points)
print(f"Minimum tour distance for Bitonic Euclidean TSP: {result}")
