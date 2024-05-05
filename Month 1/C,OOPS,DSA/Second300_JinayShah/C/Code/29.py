import itertools

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    
    min_distance = float('inf')
    min_path = None

    for path in itertools.permutations(cities):
        current_distance = calculate_total_distance(path, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = path

    return min_path, min_distance

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_path, optimal_distance = traveling_salesman_bruteforce(distances)
print("Optimal Path:", optimal_path)
print("Optimal Distance:", optimal_distance)