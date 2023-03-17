from numpy import *

mat = matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
print(mat)

# printing only diagonal elements
print(diagonal(mat))

# matrix multiplication 

mat1 = matrix('1 2 3;4 5 6; 7 8 9')
mat2 = matrix('0 1 0; 1 2 3; 9 10 1')
mat3 = mat1 * mat2
print(mat3)