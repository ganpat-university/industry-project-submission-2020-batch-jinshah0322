import numpy as np

def hill_climbing(cost_function, initial_solution, step_size=0.1, max_iterations=100):
    current_solution = np.array(initial_solution)

    for _ in range(max_iterations):
        neighbors = [current_solution + step_size * (np.random.rand(len(initial_solution)) - 0.5) for _ in range(10)]
        neighbors.append(current_solution)  

        neighbor_costs = [cost_function(neighbor) for neighbor in neighbors]
        best_neighbor = neighbors[np.argmin(neighbor_costs)]

        if cost_function(best_neighbor) < cost_function(current_solution):
            current_solution = best_neighbor

    return current_solution

def square_function(x):
    return np.sum(x**2)

initial_solution = [1.0, 2.0]
result = hill_climbing(square_function, initial_solution)
print("Optimal Solution:", result)
print("Optimal Value:", square_function(result))
