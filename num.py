import numpy as np
#coefficient matrix
A = np.matrix([2 , 3], [1 , -2])
# Right hand vector
B = np. array ((10, 5))
#Solve the system of linear equations
solution = np. linalg.solve(A , B)
#print the solution
print( "Numerical solution:", solution)