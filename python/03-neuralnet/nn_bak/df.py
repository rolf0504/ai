# 函數 f 對變數 k 的偏微分: df / dk
def df(f, p, k, step=0.01):
	p1 = p.copy()
	p1[k] = p[k]+step
	return (f(p1) - f(p)) / step