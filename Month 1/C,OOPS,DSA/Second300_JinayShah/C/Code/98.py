import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class GraphGeneticAlgorithm:
    def __init__(self, population_size, num_nodes):
        self.population_size = population_size
        self.num_nodes = num_nodes
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            graph = np.random.randint(2, size=(self.num_nodes, self.num_nodes))
            np.fill_diagonal(graph, 0)  # No self-loops
            population.append(graph)
        return population

    def crossover(self, parent1, parent2):
        crossover_point = np.random.randint(1, self.num_nodes - 1)
        child = np.vstack((parent1[:crossover_point, :], parent2[crossover_point:, :]))
        return child

    def mutate(self, individual, mutation_rate):
        mutation_mask = np.random.rand(self.num_nodes, self.num_nodes) < mutation_rate
        individual = np.logical_xor(individual, mutation_mask)
        np.fill_diagonal(individual, 0)  # No self-loops
        return individual

    def select_parents(self, fitness_scores):
        probabilities = fitness_scores / np.sum(fitness_scores)
        selected_indices = np.random.choice(np.arange(self.population_size), size=2, p=probabilities)
        return selected_indices

    def evaluate_fitness(self, graph):
        return np.sum(graph) / 2

    def evolve(self, num_generations, mutation_rate):
        for generation in range(num_generations):
            fitness_scores = [self.evaluate_fitness(individual) for individual in self.population]

            new_population = []
            for _ in range(self.population_size // 2):
                parent1_idx, parent2_idx = self.select_parents(fitness_scores)
                parent1 = self.population[parent1_idx]
                parent2 = self.population[parent2_idx]

                child1 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1, mutation_rate)

                child2 = self.crossover(parent2, parent1)
                child2 = self.mutate(child2, mutation_rate)

                new_population.extend([child1, child2])

            self.population = new_population

        best_individual_idx = np.argmax(fitness_scores)
        return self.population[best_individual_idx]

population_size = 10
num_nodes = 5
num_generations = 50
mutation_rate = 0.1

ga = GraphGeneticAlgorithm(population_size, num_nodes)
best_graph = ga.evolve(num_generations, mutation_rate)

G_best = nx.from_numpy_array(best_graph)
nx.draw(G_best, with_labels=True, font_weight='bold')
plt.show()