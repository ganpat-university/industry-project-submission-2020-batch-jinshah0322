import concurrent.futures

def parallel_bfs(graph, start):
    visited = set()
    queue = [start]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while queue:
            current_node = queue.pop(0)

            if current_node not in visited:
                visited.add(current_node)

                neighbors = graph.get(current_node, [])
                futures = [executor.submit(process_node, neighbor) for neighbor in neighbors]
                concurrent.futures.wait(futures)

                queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

def process_node(node):
    print(f"Processing node: {node}")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}

# Example usage:
start_node = 'A'
parallel_bfs(graph, start_node)
