def is_valid_position(board, row, col):
  # Check for existing queens in the same row, column, or diagonals.
  for i in range(len(board)):
    if board[i][col] == 1 or abs(i - row) == abs(col - board[i][col]):
      return False
  return True

def solve_n_queens(n):
  solutions = []
  board = [[0 for _ in range(n)] for _ in range(n)]

  def backtrack(row):
    if row == n:
      solutions.append([i for i, col in enumerate(board) if col[0] == 1])
      return
    for col in range(n):
      if is_valid_position(board, row, col):
        board[row][col] = 1
        backtrack(row + 1)
        board[row][col] = 0

  backtrack(0)
  return solutions

n = 4
solutions = solve_n_queens(n)
print(f"Found {len(solutions)} solutions for {n}-queens problem:")
for solution in solutions:
  print(solution)