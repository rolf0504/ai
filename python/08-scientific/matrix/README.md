# 矩陣運算

## eigen1.py

注意：以下 eigen vector X 的排列是 [x1, x2, ..., xn] ，所以 X*L 才是 [l1*x1, l2*x2, ..., ln*xn]

這樣的排列，確實得用 X*L 才會得到所要 A*X 結果。

```
A X = X L

         l1
            l2
A X= X        ...         
                  ln


mac020:matrix mac020$ python3 eigen1.py
eA=
 (array([1.13027756+0.j, 0.76972244+0.j]), array([[ 0.91724574,  0.79325185],
       [-0.3983218 ,  0.60889368]]))
L=
 [[1.13027756+0.j 0.        +0.j]
 [0.        +0.j 0.76972244+0.j]]
X=
 [[ 0.91724574  0.79325185]
 [-0.3983218   0.60889368]]
XL=
 [[ 1.03674228+0.j  0.61058374+0.j]
 [-0.45021419+0.j  0.46867912+0.j]]
AX=
 [[ 1.03674228  0.61058374]
 [-0.45021419  0.46867912]]
is XL==AX ? True
```

## solve1.py

* [solve1.py](solve1.py) 


```
A X = B

3 2   a  = 5
1 1   b    2

3a+2b = 5
1a+1b = 2

inv(A) A  X = inv(A) B

I X = inv(A) B

X = inv(A) B
```

## 轉置

M = 

a b c
d e f

M.transpose()

a d
b e
c f