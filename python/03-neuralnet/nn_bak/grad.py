# 函數 f 在點 p 上的梯度
def grad(f, p, step=0.01):
	gp = p.copy()
	for k in range(len(p)):
		gp[k] = df(f, p, k, step)
	return gp