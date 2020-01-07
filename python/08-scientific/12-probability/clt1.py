import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt

def CLT(s, bins=100, rwidth=0.9):
    n = len(s)
    fig, axs = plt.subplots(2, 2) # 設為 2*2 的四格繪圖版
    s1 = np.array(s)
    axs[0,0].hist(s1, bins=bins, rwidth=rwidth)
    s2 = s1.reshape((2, int(n/2))).sum(axis=0)/2
    axs[0,1].hist(s2, bins=bins, rwidth=rwidth)
    s10 = s1.reshape((10, int(n/10))).sum(axis=0)/10
    axs[1,0].hist(s10, bins=bins, rwidth=rwidth)
    s20 = s1.reshape((20, int(n/20))).sum(axis=0)/20
    axs[1,1].hist(s20, bins=bins, rwidth=rwidth)
    plt.show()

n = 100000
CLT(norm.rvs(size=n))
CLT(uniform.rvs(size=n))
CLT(np.random.choice([0,1], size=n))
CLT(np.random.choice([1,2,3,4,5,6], size=n))
