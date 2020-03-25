# Tensor: 


## torch and numpy

```
mac020:numpy mac020$ python3
Python 3.7.6 (default, Feb 12 2020, 10:56:16) 
[Clang 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> z = torch.Tensor(3,4)
>>> print(z)
tensor([[9.8091e-45, 1.3873e-43, 1.4574e-43, 4.4842e-44],
        [1.4293e-43, 1.4714e-43, 1.5134e-43, 1.4153e-43],
        [4.4842e-44, 1.5554e-43, 1.5975e-43, 4.4842e-44]])
>>> y = torch.rand(4,5)
>>> y = torch.rand(3,4)
>>> print(y)
tensor([[0.3160, 0.9217, 0.5557, 0.3974],
        [0.2133, 0.2687, 0.1911, 0.6648],
        [0.3894, 0.6999, 0.3097, 0.3955]])
>>> print(x+y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> print(z+y)
tensor([[0.3160, 0.9217, 0.5557, 0.3974],
        [0.2133, 0.2687, 0.1911, 0.6648],
        [0.3894, 0.6999, 0.3097, 0.3955]])
>>> b = z.numpy()
>>> print(b)
[[9.81e-45 1.39e-43 1.46e-43 4.48e-44]
 [1.43e-43 1.47e-43 1.51e-43 1.42e-43]
 [4.48e-44 1.56e-43 1.60e-43 4.48e-44]]
>>> import numpy as np
>>> a = np.ones(5)
>>> b = torch.from_numpy(a)
>>> np.add(a, 1, out=a)
array([2., 2., 2., 2., 2.])
>>> a
array([2., 2., 2., 2., 2.])
>>> b
tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
>>> a = np.ones(5)
>>> a
array([1., 1., 1., 1., 1.])
>>> b = torch.from_numpy(a)
>>> b
tensor([1., 1., 1., 1., 1.], dtype=torch.float64)
>>> np.add(a,1, out=a)
array([2., 2., 2., 2., 2.])
>>> a
array([2., 2., 2., 2., 2.])
>>> b
tensor([2., 2., 2., 2., 2.], dtype=torch.float64)
>>> x = torch.zeros(2,1,2,1,2)
>>> x.size()
torch.Size([2, 1, 2, 1, 2])
>>> y = torch.squeeze(x)
>>> y.size()
torch.Size([2, 2, 2])
>>> y = torch.squeeze(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: squeeze(): argument 'input' (position 1) must be Tensor, not int
>>> y = torch.squeeze(x, 1)
>>> y
tensor([[[[0., 0.]],

         [[0., 0.]]],


        [[[0., 0.]],

         [[0., 0.]]]])
>>> y.size()
torch.Size([2, 2, 1, 2])
```

## math

```
>>> torch.abs(torch.FloatTensor([-1,-2,3]))
tensor([1., 2., 3.])
>>> a = torch.randn(4)
>>> b = torch.add(a, 20)
>>> b
tensor([20.0828, 20.8518, 20.6350, 19.3439])
>>> a
tensor([ 0.0828,  0.8518,  0.6350, -0.6561])
```

## statistics
