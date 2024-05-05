from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # If no path is found

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_node = 'A'
end_node = 'H'

shortest_path = bfs_shortest_path(graph, start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {end_node}")