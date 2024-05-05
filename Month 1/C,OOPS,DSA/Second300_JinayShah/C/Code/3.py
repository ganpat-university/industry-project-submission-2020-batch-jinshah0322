import math

matrix = [[10,2,3],
          [4,5,2],
          [2,2,1]]
 
def findTrace(matrix):
   diag_sum = 0
   for i in range(len(matrix)):
     diag_sum += matrix[i][i]
   return diag_sum

def findNormal(matrix):
   sum_of_elements = 0
   for i in range(len(matrix)):
      for j in range(len(matrix)):
         sum_of_elements += math.pow(matrix[i][j], 2)
   return math.sqrt(sum_of_elements)

print("Trace of Matrix =", findTrace(matrix))
print("Normal of Matrix =", findNormal(matrix))