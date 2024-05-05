import random

POPULATION_SIZE = 10
TARGET_STRING = "1010101010"
MUTATION_RATE = 0.1
GENERATIONS = 100

def generate_individual(length):
    return ''.join(random.choice("01") for _ in range(length))

def initialize_population(population_size, target_string):
    return [generate_individual(len(target_string)) for _ in range(population_size)]

def fitness(individual, target_string):
    return sum(1 for a, b in zip(individual, target_string) if a == b)

def mutate(individual, mutation_rate):
    mutated_individual = ''
    for bit in individual:
        if random.random() < mutation_rate:
            mutated_individual += '1' if bit == '0' else '0'
        else:
            mutated_individual += bit
    return mutated_individual

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    probabilities = [fitness / total_fitness for fitness in fitness_scores]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents[0], parents[1]

def genetic_algorithm(population_size, target_string, mutation_rate, generations):
    population = initialize_population(population_size, target_string)

    for generation in range(generations):
        fitness_scores = [fitness(individual, target_string) for individual in population]
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        
        if best_individual == target_string:
            print(f"Target string '{target_string}' achieved in generation {generation}")
            break

        new_population = [best_individual]

        for _ in range(population_size - 1):
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    print(f"Best individual: {best_individual}")

genetic_algorithm(POPULATION_SIZE, TARGET_STRING, MUTATION_RATE, GENERATIONS)