import numpy as np
import math
import gd3 as gd

def sig(t):
    return 1.0/(1.0+math.exp(-t))

def andLoss(p):
    [w1,w2,b] = p
    o1 = sig(w1*0+w2*0+b)
    o2 = sig(w1*0+w2*1+b)
    o3 = sig(w1*1+w2*0+b)
    o4 = sig(w1*1+w2*1+b)
    delta = np.array([o1-0, o2-0, o3-0, o4-1]) 
    return np.linalg.norm(delta, 2)

p = [0.0, 0.0, 0.0] # [w1,w2,b] 
gd.gradientDescendent(andLoss, p)
