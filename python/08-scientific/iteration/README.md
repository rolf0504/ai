# Iteration

* [陳鍾誠 : 迭代法 Iterative (JavaScript)](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E6%BC%94%E7%AE%97%E6%B3%95/04-iterative)

求 x = f(x) 的解

方法：

1. 隨便選一個 x=x0
2. x1 = f(x0)
   x2 = f(x1)
   ....
   xn = f(x[n-1])

3. 一但收斂了 (x[n] = x[n-1]), 
   就代表 xn = f(xn)
   就輸出結果。

迭代的結果有幾種可能：
1. 收斂 xn = f(xn)
2. 發散 xn ==> oo
3. 震盪 xn = f(x[n-1]), ...., x[n-1] = f(xn), 且 xn != x[n-1]
4. 混屯 既不收斂，也不發散，又不震盪，但是只在有限範圍內遊走。

## 範例

x = f(x)

x*x = 3

改成迭代式

```
1. x = 3/x

2. ...

x*x - x = 3-x
x(x-1) = 3-x
x = (3-x)/(x-1)


1. x = 3/x    => f(x) => 3 / x
2. f(x) => x - 1 / 4 * (x * x - 3)
   x = f(x) 
   x = x-1/4(x^2-3)
   0 = -1/4(x^2-3)
   0 = x^2-3
   x^2 = 3
3. f(x) => 1 / 2 * (x + 3 / x)
   x = f(x)
   x = 1/2 * (x + 3 / x)
   x = x/2 + 3/(2x)
   x/2 = 3/(2x)
   x^2 = 3
```

## 所有電腦方法大部分都可以視為迭代法

ex: 爬山演算法

x1 => f(x0) 
   if n(x0) better than x0, then return n(x0) else return x0
x2 => f(x1)

...



## 參考文獻

* [維基百科:巴拿赫不動點定理](https://zh.wikipedia.org/wiki/%E5%B7%B4%E6%8B%BF%E8%B5%AB%E4%B8%8D%E5%8A%A8%E7%82%B9%E5%AE%9A%E7%90%86)
* [維基百科:不動點定理](https://zh.wikipedia.org/wiki/%E4%B8%8D%E5%8A%A8%E7%82%B9%E5%AE%9A%E7%90%86)
* [維基百科:旋轉矩陣](https://zh.wikipedia.org/wiki/%E6%97%8B%E8%BD%AC%E7%9F%A9%E9%98%B5)

