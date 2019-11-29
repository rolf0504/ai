import numpy as np
# from py6 import grad # 引入梯度函數
# 使用梯度下降法尋找函數最低點
def gradientDescendent(f, p0, step=0.001):
	p = p0.copy()
	while (True):
		gp = grad(f, p) # 計算梯度 gp
		norm = np.norm(gp) # norm = 梯度的長度 (步伐大小)
		print('p=', p, 'f(p)=', f(p), 'norm=', norm)
		if norm < 0.00001:  # 如果步伐已經很小了，那麼就停止吧！
			break
		gstep = np.mul(gp, -1 * step) # gstep = 逆梯度方向的一小步
		p = np.add(p, gstep) # 向 gstep 方向走一小步
	return p # 傳回最低點！
