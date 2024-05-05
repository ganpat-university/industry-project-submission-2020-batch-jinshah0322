import numpy as np

def differential_evolution(cost_function, bounds, population_size=50, generations=200, crossover_prob=0.8, scaling_factor=0.5):
    dimension = len(bounds)
    population = np.random.rand(population_size, dimension)
    population = bounds[:, 0] + population * (bounds[:, 1] - bounds[:, 0])

    for generation in range(generations):
        for i in range(population_size):
            target_index = i
            while target_index == i:
                target_index = np.random.randint(population_size)

            mutant = population[np.random.choice(population_size, 1)[0]] + scaling_factor * (population[target_index] - population[i])
            mutant = np.clip(mutant, bounds[:, 0], bounds[:, 1])

            if np.random.rand() < crossover_prob:
                trial_vector = np.copy(population[i])
                crossover_points = np.random.rand(dimension) < 0.5
                trial_vector[crossover_points] = mutant[crossover_points]

                if cost_function(trial_vector) < cost_function(population[i]):
                    population[i] = trial_vector

    best_index = np.argmin([cost_function(ind) for ind in population])
    return population[best_index]

def sphere_function(x):
    return np.sum(x**2)

bounds = np.array([[-5.12, 5.12]] * 3)  # Adjust based on the problem

result = differential_evolution(sphere_function, bounds)
print("Optimal Solution:", result)
print("Optimal Value:", sphere_function(result))
