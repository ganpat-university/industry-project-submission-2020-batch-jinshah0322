def cache_oblivious_matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    if n <= 8:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
    else:
        half = n // 2

        A11, A12 = [row[:half] for row in A[:half]], [row[half:] for row in A[:half]]
        A21, A22 = [row[:half] for row in A[half:]], [row[half:] for row in A[half:]]

        B11, B12 = [row[:half] for row in B[:half]], [row[half:] for row in B[:half]]
        B21, B22 = [row[:half] for row in B[half:]], [row[half:] for row in B[half:]]

        C11 = [[0] * half for _ in range(half)]
        C12 = [[0] * half for _ in range(half)]
        C21 = [[0] * half for _ in range(half)]
        C22 = [[0] * half for _ in range(half)]

        cache_oblivious_matrix_multiply(A11, B11, C11)
        cache_oblivious_matrix_multiply(A12, B21, C12)
        cache_oblivious_matrix_multiply(A11, B12, C21)
        cache_oblivious_matrix_multiply(A12, B22, C22)

        for i in range(half):
            for j in range(half):
                C[i][j] = C11[i][j] + C12[i][j]
                C[i][j + half] = C21[i][j] + C22[i][j]
                C[i + half][j] = C11[i + half][j] + C12[i + half][j]
                C[i + half][j + half] = C21[i + half][j] + C22[i + half][j]

    return C

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]

result = cache_oblivious_matrix_multiply(A, B)
for row in result:
    print(row)
