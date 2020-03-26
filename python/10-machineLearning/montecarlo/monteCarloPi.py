from random import random

def monteCarloPi(n):
    hits = 0
    for _ in range(n):
        x = random()
        y = random()
        if (x*x+y*y <= 1):
            hits += 1
    return 4*(hits/n)

print('MonteCarloPi(100000)=', monteCarloPi(100000))