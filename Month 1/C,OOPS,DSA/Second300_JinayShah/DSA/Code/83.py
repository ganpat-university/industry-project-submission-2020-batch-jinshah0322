import matplotlib.pyplot as plt
import numpy as np
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def euclidean_distance(p1, p2):
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def yao_graph(points):
    if len(points) == 1:
        return {}

    x_median = np.median([point.x for point in points])
    left_points = [point for point in points if point.x <= x_median]
    right_points = [point for point in points if point.x > x_median]

    left_graph = yao_graph(left_points)
    right_graph = yao_graph(right_points)

    nearest_left = find_nearest_neighbor(left_points, right_points)
    nearest_right = find_nearest_neighbor(right_points, left_points)

    left_graph[nearest_left] = right_graph[nearest_right] = None

    return {**left_graph, **right_graph}

def find_nearest_neighbor(points, other_points):
    nearest_neighbor = None
    min_distance = float('inf')

    for point in points:
        for other_point in other_points:
            distance = euclidean_distance(point, other_point)
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = point

    return nearest_neighbor

def plot_yao_graph(points, graph):
    plt.scatter([point.x for point in points], [point.y for point in points], color='blue')

    for point, neighbor in graph.items():
        if neighbor:
            plt.plot([point.x, neighbor.x], [point.y, neighbor.y], color='red')

    plt.title('Yao Graph Construction')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


random.seed(42)
points = [Point(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(10)]

yao_graph_result = yao_graph(points)
plot_yao_graph(points, yao_graph_result)
