# 計算 3 的平方根之迭代程式
# https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E6%BC%94%E7%AE%97%E6%B3%95/04-iterative
def f1(x):
    return 3 / x
def f2(x):
    return x - 1 / 4 * (x * x - 3)
def f3(x):
    return 1 / 2 * (x + 3 / x)

x1 = x2 = x3 = 1
for i in range(20):
    x1 = f1(x1)
    x2 = f2(x2)
    x3 = f3(x3)
    print('x1:', x1, 'x2:', x2, 'x3:', x3)
