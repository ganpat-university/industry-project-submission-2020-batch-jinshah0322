from collections import deque

def bfs(grid, start_row, start_col, target_value):
  rows = len(grid)
  cols = len(grid[0])
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
  queue = deque([(start_row, start_col)])  
  visited = [[False] * cols for _ in range(rows)]  
  while queue:
    row, col = queue.popleft()
    visited[row][col] = True
    if grid[row][col] == target_value:
      return True
    for dr, dc in directions:
      new_row = row + dr
      new_col = col + dc
      if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and grid[new_row][new_col] != '#':  # Assuming '#' represents obstacles
        queue.append((new_row, new_col))
  return False

grid = [
  ['S', '.', '.', '#'],
  ['.', '.', '.', '.'],
  ['#', '.', '.', 'T']
]
start_row, start_col = 0, 0  
target_value = 'T'  
if bfs(grid, start_row, start_col, target_value):
  print("Target found!")
else:
  print("Target not found.")
