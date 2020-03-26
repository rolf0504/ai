import torch
import random

sigmoid = torch.nn.Sigmoid()
x = torch.Tensor([[1,0,0],[1,0,1], [1,1,0], [1,1,1]])
y = torch.Tensor([0,0,0,1]) # and gate
# y = torch.Tensor([0,1,1,1]) # or gate
# y = torch.Tensor([0,1,1,0]) # xor gate
xt = x.T
w = torch.randn(1, 3, requires_grad=True)

learning_rate = 1e-3
for t in range(50000):
    y_pred = sigmoid(torch.mm(w, xt))
    loss = (y_pred - y).pow(2).sum()
    if t % 1000 == 999:
        print(t, 'loss=', loss.item(), 'y_pred=', y_pred)
    loss.backward()
    with torch.no_grad():
        w -= learning_rate * w.grad
        w.grad.zero_()
