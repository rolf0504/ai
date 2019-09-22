import random

def hillClimbing(f, x, y, h=0.01):
	while (True):
		fxy = f(x, y)
		print('x=', x, 'y=', y, 'f(x,y)=', fxy)
		if f(x+h, y) >= fxy:
			x = x + h
		elif f(x-h, y) >= fxy:
			x = x - h
		elif f(x, y+h) >= fxy:
			y = y + h
		elif f(x, y-h) >= fxy:
			y = y - h
		else:
			break
	return (x,y,fxy)

def f(x, y):
	return -1 * ( x*x -2*x + y*y +2*y - 8 )

hillClimbing(f, 0, 0)