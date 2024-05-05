from collections import defaultdict

def evaluate_fractions(fractions, values, queries):
    graph = defaultdict(dict)

    
    for (numerator, denominator), value in zip(fractions, values):
        graph[numerator][denominator] = value
        graph[denominator][numerator] = 1.0 / value

    def dfs(start, end, visited):
        if start == end:
            return 1.0

        visited.add(start)
        for neighbor, value in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return value * result

        return -1.0

    results = []

    for query in queries:
        start, end = query
        if start not in graph or end not in graph:
            results.append(-1.0)
        elif start == end:
            results.append(1.0)
        else:
            visited = set()
            result = dfs(start, end, visited)
            results.append(result)

    return results


fractions = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

results = evaluate_fractions(fractions, values, queries)
print("Results:", results)
