import numpy as np
from scipy import linalg

A = np.array([[1, -0.3], [-0.1, 0.9]])
eA = linalg.eig(A)
print(eA)

l, X = eA
L = np.diag(l)
print('L=', L)
print('X=', X)

Lx = np.dot(L, X)
Ax = np.dot(A, X)

print('Lx=', Lx)
print('Ax=', Ax)
