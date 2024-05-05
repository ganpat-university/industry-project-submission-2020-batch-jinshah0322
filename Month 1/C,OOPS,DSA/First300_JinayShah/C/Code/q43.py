import numpy as np

x = [[1,2,3],[4,5,6],[7,8,9]]
transposed = np.zeros([3,3])

for i in range(len(x)):
    for j in range(len(x)):
        transposed[i][j] = x[j][i]

print(transposed)