def hungarian_algorithm(cost_matrix):
    num_rows = len(cost_matrix)
    num_cols = len(cost_matrix[0])

    row_mask = [False]*num_rows
    col_mask = [False]*num_cols
    mask = [[False]*num_cols for _ in range(num_rows)]

    if num_rows != num_cols:
        difference = abs(num_rows - num_cols)
        if num_rows < num_cols:
            cost_matrix += [[0]*difference]
        else:
            for _ in range(difference):
                cost_matrix.append([0]*num_cols)

    for _ in range(len(cost_matrix)):
        for r in range(num_rows):
            cost_matrix[r] = [x - min(cost_matrix[r]) for x in cost_matrix[r]]

        for c in range(num_cols):
            col = [row[c] for row in cost_matrix]
            min_val = min(col)
            for r in range(num_rows):
                cost_matrix[r][c] -= min_val

        for r in range(num_rows):
            for c in range(num_cols):
                if cost_matrix[r][c] == 0 and not mask[r][c]:
                    mask[r][c] = True

        if sum(row_mask) == num_rows == sum(col_mask) == num_cols == sum([sum(row) for row in mask]) == num_rows * num_cols:
            break

        min_uncovered = float('inf')
        for r in range(num_rows):
            for c in range(num_cols):
                if not mask[r][c]:
                    min_uncovered = min(min_uncovered, cost_matrix[r][c])

        for r in range(num_rows):
            for c in range(num_cols):
                if not mask[r][c]:
                    cost_matrix[r][c] -= min_uncovered
                elif mask[r][c]:
                    cost_matrix[r][c] += min_uncovered

    assignments = []
    for r in range(num_rows):
        for c in range(num_cols):
            if mask[r][c]:
                assignments.append((r, c))

    return assignments


cost_matrix = [
    [4, 2, 9],
    [3, 8, 7],
    [5, 1, 8]
]

assignments = hungarian_algorithm(cost_matrix)

for i, j in assignments:
    print(f"Assign row {i} to column {j}")
