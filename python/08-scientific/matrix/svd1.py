import numpy as np
# from scipy import linalg

a = [[1,2,3], [4,5,6]]

u,s,vh = np.linalg.svd(a, full_matrices=True)

print('u=', u, '\ns=', s, '\nvh=', vh)