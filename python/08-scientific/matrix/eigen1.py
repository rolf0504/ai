import numpy as np
from scipy import linalg

A = np.array([[1,   -0.3], 
              [-0.1, 0.9]])
eA = linalg.eig(A)
print('eA=\n', eA)

l, X = eA
L = np.diag(l) # 把 lambda 轉成對角矩陣
print('L=\n', L)
print('X=\n', X)

XL = np.dot(X, L)
AX = np.dot(A, X)

print('XL=\n', XL)
print('AX=\n', AX)
print('is XL==AX ?', np.allclose(XL,AX))
