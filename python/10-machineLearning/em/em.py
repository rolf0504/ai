import numpy as np
import math
# 參考文獻：Numerical example to understand Expectation-Maximization -- http://ai.stanford.edu/~chuongdo/papers/em_tutorial.pdf
# What is the expectation maximization algorithm? (PDF) -- http://stats.stackexchange.com/questions/72774/numerical-example-to-understand-expectation-maximization

def logp(n):
    pi = 1.0/n
    return math.log(pi)

def xplog(x, p): # 計算條件熵 cross entropy H(x;p)
  n = np.sum(x)
  r = logp(n)
  for xi in x:
      r -= logp(xi)
  return r + np.dot(x, np.log(p))

def EM():
# 1st:  Coin B, {HTTTHHTHTH}, 5H,5T
# 2nd:  Coin A, {HHHHTHHHHH}, 9H,1T
# 3rd:  Coin A, {HTHHHHHTHH}, 8H,2T
# 4th:  Coin B, {HTHTTTHHTT}, 4H,6T
# 5th:  Coin A, {THHHTHHHTH}, 7H,3T
# so, from MLE: pA(heads) = 0.80 and pB(heads)=0.45
    e = [ [5,5], [9,1], [8,2], [4,6], [7,3] ]
    pA = [0.6, 0.4]
    pB = [0.5, 0.5]
    delta = 9.9999
    for _ in range(1000):
        print("pA={} pB={} delta={}".format(pA, pB, delta))
        sumA=[0,0]
        sumB=[0,0]
        for ei in e:
            lA = xplog(ei, pA)
            lB = xplog(ei, pB)
            a = np.exp(lA)
            b = np.exp(lB)
            wA = a/(a+b)
            wB = b/(a+b)
            eA = np.multiply(wA, ei)
            eB = np.multiply(wB, ei)
            sumA = np.add(sumA, eA)
            sumB = np.add(sumB, eB)

        npA = np.multiply(sumA, 1.0/np.sum(sumA))
        npB = np.multiply(sumB, 1.0/np.sum(sumB))
        dA  = np.subtract(npA, pA)
        dB  = np.subtract(npB, pB)
        delta = np.max([dA, dB])
        if delta < 0.001: break
        pA = npA
        pB = npB

EM()
