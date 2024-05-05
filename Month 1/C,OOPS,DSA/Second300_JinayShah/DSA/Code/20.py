def is_valid_move(i, j, rows, cols, matrix):
    return 0 <= i < rows and 0 <= j < cols and matrix[i][j] != -1

def longest_route(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                dp[i][j] = -1  
            else:
                up = dp[i - 1][j] if is_valid_move(i - 1, j, rows, cols, matrix) else 0
                left = dp[i][j - 1] if is_valid_move(i, j - 1, rows, cols, matrix) else 0

                if up == -1 and left == -1:
                    dp[i][j] = -1
                else:
                    dp[i][j] = max(up, left) + 1

    return dp[rows - 1][cols - 1]


matrix1 = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

matrix2 = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

result1 = longest_route(matrix1)
print(f"The longest possible route in matrix1 is: {result1}")

result2 = longest_route(matrix2)
print(f"The longest possible route in matrix2 is: {result2}")
