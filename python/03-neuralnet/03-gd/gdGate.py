import numpy as np
import math
import gd3 as gd

def sig(t):
    return 1.0/(1.0+math.exp(-t))

o = [0,0,0,1] # and gate outputs
# o = [0,1,1,1] # or gate outputs
# o = [0,1,1,0] # xor gate outputs
def andLoss(p):
    [w1,w2,b] = p
    o1 = sig(w1*0+w2*0+b)
    o2 = sig(w1*0+w2*1+b)
    o3 = sig(w1*1+w2*0+b)
    o4 = sig(w1*1+w2*1+b)
    delta = np.array([o1-o[0], o2-o[1], o3-o[2], o4-o[3]]) 
    print('o1={:.3f} o2={:.3f} o3={:.3f} o4={:.3f}'.format(o1,o2,o3,o4))
    return np.linalg.norm(delta, 2)

p = [0.0, 0.0, 0.0] # [w1,w2,b] 
gd.gradientDescendent(andLoss, p, max_loops=1500)
