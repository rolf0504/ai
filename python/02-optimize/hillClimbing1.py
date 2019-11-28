def hillClimbing(f, x, dx=0.01):
	while (True):
		print('x=', x, 'f(x)=', f(x))
		if f(x+dx)>f(x):
			x = x + dx
		elif f(x-dx)>f(x):
			x = x - dx
		else:
			break
	return x

def f(x):
	return -1*(x*x+3*x+5)

hillClimbing(f, 0)
