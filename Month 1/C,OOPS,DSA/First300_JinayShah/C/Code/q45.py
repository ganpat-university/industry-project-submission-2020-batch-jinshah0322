def lowerTaningularMatrixChecker(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if(j>i):
                if(x[i][j]==0):
                    pass
                else:
                    return "It is not lower triangular matrx"
    return "It is a lower triangular matrix"

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1,0,0],[1,4,0],[5,5,6]]
print(lowerTaningularMatrixChecker(x))
print(lowerTaningularMatrixChecker(y))