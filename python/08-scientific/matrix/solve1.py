import numpy as np
from scipy import linalg

m,n=500,50

A = np.random.rand(m, m)
B = np.random.rand(m, n)
print('A=', A)
print('B=', B)
X1 = linalg.solve(A,B)
X2 = np.dot(linalg.inv(A), B)
print('X1=', X1)
print('X2=', X2)
print(np.allclose(X1,X2))

# %timeit linalg.solve(A,B)
# %timeit np.dot(linalg.inv(A), B)
