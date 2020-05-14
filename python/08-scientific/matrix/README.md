# 矩陣運算

## eigen1.py

```
A Xt = L Xt

      l1
         l2
L Xt=        ...       Xt = A Xt  
               ln

```

```
mac020:matrix mac020$ python3 eigen1.py
eA=
 (array([1.13027756+0.j, 0.76972244+0.j]), array([[ 0.91724574,  0.79325185],
       [-0.3983218 ,  0.60889368]]))
L= 特徵值對角矩陣
 [[1.13027756+0.j 0.        +0.j]
 [0.        +0.j 0.76972244+0.j]]
X= 特徵向量矩陣
 [[ 0.91724574  0.79325185]
 [-0.3983218   0.60889368]]
LXt= L * Xt
 [[ 1.03674228+0.j -0.45021419+0.j]
 [ 0.61058374+0.j  0.46867912+0.j]]
AXt= A * Xt
 [[ 1.03674228+0.j -0.45021419+0.j]
 [ 0.61058374+0.j  0.46867912+0.j]]
is LXt==AXt ? True  
   L*Xt == A*Xt

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