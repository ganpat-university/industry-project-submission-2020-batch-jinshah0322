from collections import deque

def is_valid_move(i, j, rows, cols, matrix):
    return 0 <= i < rows and 0 <= j < cols and matrix[i][j] != 0

def shortest_safe_route(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    
    queue = deque([(0, 0, 0)])  
    visited[0][0] = True

    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        i, j, distance = queue.popleft()

        if i == rows - 1 and j == cols - 1:
            return distance

        for move in moves:
            new_i, new_j = i + move[0], j + move[1]

            if is_valid_move(new_i, new_j, rows, cols, matrix) and not visited[new_i][new_j]:
                queue.append((new_i, new_j, distance + 1))
                visited[new_i][new_j] = True

    return -1  


matrix = [
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

result = shortest_safe_route(matrix)
print(f"The shortest safe route distance is: {result}")
