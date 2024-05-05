def upperTaningularMatrixChecker(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if(j<i):
                if(x[i][j]==0):
                    pass
                else:
                    return "It is not upper triangular matrx"
    return "It is a upper triangular matrix"

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1,2,3],[0,4,5],[0,0,6]]
print(upperTaningularMatrixChecker(x))
print(upperTaningularMatrixChecker(y))