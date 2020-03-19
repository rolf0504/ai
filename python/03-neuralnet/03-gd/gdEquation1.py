"""
A X = B ，求 X 是多少？

3x+2y=1
1x+1y=2
"""
import gd1 as gd
import numpy as np

A = np.array([[3.0, 2],[1, 1]])
B = np.array([5.0, 2]) # np.array([[5.0, 2]]).transpose()

def f(p): #  能量函數:計算 ||AX-B||，也就是 ||Y-B||
    X = p.transpose()
    Y = A.dot(X)
    # return np.linalg.norm(Y-B, 2)
    print('X=', X, 'Y=', Y, 'B=', B, 'Y-B=', Y-B, 'norm1=', np.linalg.norm(Y-B, 1), 'norm2=', np.linalg.norm(Y-B, 2))
    return np.linalg.norm(Y-B, 1)

p = np.array([0.0, 0])
f(p)
p = np.array([1.0, 1])
f(p)
p = np.array([1.1, 0.83])
f(p)
p = np.array([1.14, 0.86])
f(p)
# gd.gradientDescendent(f, p, step=0.01)
