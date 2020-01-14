# https://docs.sympy.org/1.5.1/tutorial/calculus.html
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

m, n, a, b = symbols('m n a b')
expr = (a*x + b)**m
print('expr.diff((x, n))=', expr.diff((x, n)))