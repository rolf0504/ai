# Gradient

## auto_diff1.py


```
mac020:gradient mac020$ python3 auto_diff1.py
tensor([[0.],
        [1.],
        [2.],
        [3.]], requires_grad=True)
tensor([[28.]], grad_fn=<MulBackward0>)
x.grad: tensor([[ 0.],
        [ 4.],
        [ 8.],
        [12.]])
x.grad_fn: None
y.grad_fn: <MulBackward0 object at 0x1293bb650>
True
tensor([[ 0.],
        [ 4.],
        [ 8.],
        [12.]])
```

## chain_rule1.py

```
mac020:gradient mac020$ python3 chain_rule1.py
tensor([[0.0000],
        [4.0000],
        [0.8000],
        [0.1200]])
```